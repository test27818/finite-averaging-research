#!/usr/bin/env python3
"""Projective-integer search and construction, ported from 2-average-solver.html.

Exact arithmetic; sorting and primitive scaling remove symmetries, NOT value bounds.
Numbers can grow with search depth. No denominator cutoff is used.
Construction is heuristic outside power-of-two tails; failure means budget exhausted,
not impossibility. Search returns 'proved' only after exhausting a bounded-depth tree.
All exported position sequences are independently checked by solver.verify_sequence.

Deadlines use time.time() (absolute Unix seconds, for compatibility with old callers).
Memory: bounded failed-state table in DFS; bounded frontier in escape/beam search.
No process-global per-instance state or heuristic caches are retained.
"""
from __future__ import annotations

import heapq
import sys
import time
from collections import Counter
from math import gcd

# ------------------------------------------------------------------ state primitives
def gcd_all(vec):
    g = 0
    for v in vec:
        g = gcd(g, v)
    return g


def reduce_prim(vec):
    """Primitive scaling, order preserved (labelled vector)."""
    g = gcd_all(vec)
    return tuple(vec) if g == 0 else tuple(x // g for x in vec)


def prim_sorted(vec):
    """Canonical search state = divide by gcd, then sort ascending.  Sum stays 0."""
    g = 0
    for v in vec:
        g = gcd(g, v)
        if g == 1:
            break
    if g > 1:
        vec = [x // g for x in vec]
    return tuple(sorted(vec))


def deviations(a):
    n, S = len(a), sum(a)
    return [n * x - S for x in a]


def state_of(a):
    """Instance -> canonical projective integer deviation state."""
    return prim_sorted(deviations(a))


def key_of(vec):
    """Sign-canonical key; suitable for unlabelled reachability/cost, not path labels."""
    pos = prim_sorted(vec)
    neg = tuple(-x for x in reversed(pos))
    return min(pos, neg)


def nz_count(vec):
    return sum(1 for v in vec if v)


def energy(vec):
    s = 0
    for v in vec:
        s += v * v
    return s


def floor_pow2(n):
    return 1 << (n.bit_length() - 1) if n else 0


# --------------------------------------------------------------- bounds (admissible)



def h_cancel(vec):
    """Each move zeroes at most two non-zero positions, and only by cancelling opposites."""
    return (nz_count(vec) + 1) // 2


def h_pairs(vec):
    """Admissible bound C + ceil(max(0, C-c)/2).

    m = nonzero count, c = disjoint opposite-pair count, C = ceil(m/2).
    If q cancellations and t other useful operations are used, q >= C.
    A cancellation reduces c by exactly one; any other operation raises it by at
    most two. Final c=0 implies q <= c_initial + 2*t, hence q+t >= this bound.
    This includes operations that turn a zero back into a nonzero value.
    """
    cnt = Counter(vec)
    m = sum(k for x, k in cnt.items() if x)
    c = sum(min(k, cnt.get(-x, 0)) for x, k in cnt.items() if x > 0)
    C = (m + 1) // 2
    return C + max(0, (C - c + 1) // 2)


def h_distinct(vec):
    return (len({abs(v) for v in vec if v}) + 1) // 2


def h_setup(vec):
    z = nz_count(vec)
    if z < 2:
        return z
    s = {v for v in vec if v}
    return (z + 1) // 2 if any(-v in s for v in s) else (z + 1) // 2 + 1


def heuristic(vec):
    # h_pairs dominates both h_setup and h_distinct, so don't recompute those.
    return h_pairs(vec)


def possible(state):
    """The mixability criterion applied to a primitive deviation state (sum 0).

    n<=2 always; n=3 <=> some deviation is 0 (i.e. an arithmetic progression);
    n>=4 <=> G = gcd of pairwise differences is a power of two.
    """
    if not any(state):
        return True
    n = len(state)
    if n <= 2:
        return True
    if n == 3:
        return 0 in state
    G = 0
    a0 = state[0]
    for x in state[1:]:
        G = gcd(G, x - a0)
        if G == 1:
            return True
    return G > 0 and (G & (G - 1)) == 0


# ------------------------------------------------------------------------- successors
def children(state, prune=False):
    """Successors, one per unordered value pair.  `state` must be sorted & primitive.

    prune=True also drops successors failing `possible()`.  That cut is *complete* (a
    non-mixable state has no solution) but measured to be worth 1 node in 35,529 on the
    certificate ladder, so it is OFF there and ON during construction, where it steers
    the descent towards solvable regions.
    """
    n = len(state)
    out = []
    for i in range(n):
        if i and state[i] == state[i - 1]:
            continue
        si = state[i]
        for j in range(i + 1, n):
            sj = state[j]
            if sj == si or (j > i + 1 and sj == state[j - 1]):
                continue
            s = si + sj
            w = [s if (k == i or k == j) else 2 * state[k] for k in range(n)]
            cw = prim_sorted(w)
            if prune and not possible(cw):
                continue
            out.append((cw, (si, sj)))
    return out


def ordered_children(state, prune=False):
    """Children sorted by (admissible bound, energy): find incumbents fast, prune early."""
    ch = children(state, prune)
    if len(ch) > 1:
        ch.sort(key=lambda t: (heuristic(t[0]), energy(t[0])))
    return ch


def mix(state, x, y):
    """Apply a value-pair move to a sorted primitive state (first occurrences; equal
    values are interchangeable so the resulting multiset is well defined)."""
    n = len(state)
    try:
        i = state.index(x)
    except ValueError:
        return None
    j = -1
    for k in range(n):
        if k != i and state[k] == y:
            j = k
            break
    if j < 0:
        return None
    s = x + y
    return prim_sorted([s if (k == i or k == j) else 2 * state[k] for k in range(n)])


def value_pairs_from_positions(labelled, seq):
    """Inverse of replay_value_pairs: a 1-based position schedule -> value-pair schedule.

    Needed because an incumbent may arrive as positions (e.g. concatenated per-block
    sequences from the partition DP) while the search works on values.
    """
    cur = list(reduce_prim(labelled))
    out = []
    for (i, j) in seq:
        a, b = cur[i - 1], cur[j - 1]
        if a == b:
            return None
        s = a + b
        cur = [s if (k == i - 1 or k == j - 1) else 2 * x for k, x in enumerate(cur)]
        g = gcd_all(cur)
        if g:
            cur = [x // g for x in cur]
        out.append((a, b))
    if any(cur):
        return None
    return out


def replay_value_pairs(labelled, moves):
    """Value-pair schedule -> 1-based position schedule on the original labelling."""
    cur = list(reduce_prim(labelled))
    seq = []
    for (u, v) in moves:
        try:
            i = cur.index(u)
        except ValueError:
            return None
        j = next((k for k in range(len(cur)) if k != i and cur[k] == v), None)
        if j is None:
            return None
        s = u + v
        cur = [s if (k == i or k == j) else 2 * x for k, x in enumerate(cur)]
        g = gcd_all(cur)
        if g:
            cur = [x // g for x in cur]
        seq.append((i + 1, j + 1))
    return None if any(cur) else seq


# ----------------------------------------------------- decision search + IDA* ladder
class _Abort(Exception):
    pass


def decision(state, K, deadline=None, node_budget=1_000_000, memo_cap=200_000,
             prune=False):
    """Search <=K operations. (found, value_moves, visited, memo_size, reason).

    Failed-state dominance: memo[state] is the largest FULLY EXHAUSTED remaining
    budget. Sign symmetry is used only as a failed-state key. Paths keep real signs.
    'time'/'cap'/'depth' are inconclusive, never a no-solution certificate.
    """
    if not isinstance(K, int) or K < 0:
        raise ValueError('K must be a nonnegative integer')
    state = prim_sorted(state)
    if sum(state):
        raise ValueError('decision expects zero-sum deviations')
    memo = {}
    nodes = 0
    found_path = None
    path = []

    def dfs(v, remain, h):
        nonlocal nodes, found_path
        if h == 0:
            found_path = path.copy()
            return True
        if h > remain:
            return False
        if nodes >= node_budget:
            raise _Abort('cap')
        if nodes % 128 == 0 and deadline is not None and time.time() >= deadline:
            raise _Abort('time')
        nodes += 1
        # v is already sorted/primitive; avoid another gcd for the memo key.
        k = min(v, tuple(-x for x in reversed(v)))
        if memo.get(k, -1) >= remain:
            return False
        cc = [(heuristic(w), energy(w), w, mv) for w, mv in children(v, prune)]
        cc.sort(key=lambda item: (item[0], item[1]))
        for hh, _en, w, mv in cc:
            if hh > remain - 1:
                continue
            path.append(mv)
            if dfs(w, remain - 1, hh):
                return True
            path.pop()
        if k not in memo and len(memo) >= memo_cap:
            raise _Abort('cap')
        memo[k] = max(memo.get(k, -1), remain)
        return False

    # Do not raise the process-wide recursion limit or risk a native stack overflow.
    if K > sys.getrecursionlimit() - 100:
        return False, None, 0, 0, 'depth'
    try:
        found = dfs(state, K, heuristic(state))
    except _Abort as e:
        return False, None, nodes, len(memo), str(e)
    return found, found_path, nodes, len(memo), 'found' if found else 'proved'


def ida_ladder(state, incumbent=None, lower=None, deadline=None,
               node_budget=1_000_000, memo_cap=200_000, max_depth=80, prune=False):
    """IDA* ladder with a TOTAL node budget shared by all iterations.

    `lower`, if supplied, must already be proved. `incumbent`, if supplied, must be
    a valid value-pair schedule for `state`. Public solve() validates both endpoints.
    The incumbent depth need not be searched: exhausting all smaller depths suffices.
    """
    t0 = time.time()
    state = prim_sorted(state)
    best = list(incumbent) if incumbent is not None else None
    ub = len(best) if best is not None else None
    lb = max(heuristic(state), 0 if lower is None else int(lower))
    if ub is not None and lb > ub:
        raise ValueError('lower bound exceeds incumbent: inconsistent certificate')
    expanded, notes = 0, []

    def result(certified, reason):
        return dict(steps=ub, moves=best, certified=certified, lower=lb,
                    expanded=expanded, reason=reason, notes=notes, time=time.time()-t0)

    if not any(state):
        best, ub, lb = [], 0, 0
        return result(True, 'already equal')
    while True:
        if ub is not None and lb == ub:
            return result(True, 'all shorter depths excluded')
        if lb > max_depth:
            return result(False, 'depth')
        if deadline is not None and time.time() >= deadline:
            return result(False, 'time')
        if expanded >= node_budget:
            return result(False, 'cap')
        found, moves, nodes, memo, reason = decision(
            state, lb, deadline=deadline, node_budget=node_budget-expanded,
            memo_cap=memo_cap, prune=prune)
        expanded += nodes
        notes.append((lb, reason, nodes, memo))
        if found:
            if len(moves) != lb:
                raise AssertionError('solution shorter than proved lower bound')
            best, ub = moves, len(moves)
            return result(True, 'IDA* first feasible depth')
        if reason != 'proved':
            return result(False, reason)
        lb += 1


# =========================================== construction waterfall (Task 2 core)
def opposite(state):
    """A value pair (x, -x), x != 0, if one exists (two-pointer over the sorted state)."""
    v = list(state)
    l, r = 0, len(v) - 1
    while l < r:
        s = v[l] + v[r]
        if s == 0:
            return (v[l], v[r]) if v[l] else None
        if s < 0:
            l += 1
        else:
            r -= 1
    return None


def quartet(state):
    """Positions of a zero-sum 4-subset {i,j,k,l} with x_i+x_j = -(x_k+x_l), else None."""
    v = list(state)
    n = len(v)
    pairs = {}
    for i in range(n):
        if not v[i]:
            continue
        for j in range(i + 1, n):
            if not v[j]:
                continue
            s = v[i] + v[j]
            other = pairs.get(-s)
            if other:
                for (u, w) in other:
                    if u not in (i, j) and w not in (i, j):
                        return [u, w, i, j]
            lst = pairs.get(s)
            if lst is None:
                pairs[s] = lst = []
            if len(lst) < 8:
                lst.append((i, j))
    return None


def _pow2_at_least(m):
    N = 1
    while N < m:
        N *= 2
    return N


def butterfly(state, ids=None, mode=0):
    """Power-of-two butterfly completion of one zero-sum block; value-pair moves or None.

    The non-zero positions `ids` are padded with *existing* zero positions up to a power
    of two N <= n; groups are then merged level by level, averaging element-wise.
    Invariant: after each level every group is internally equal; the block has size 2^t
    and sum 0, so its common value is 0.  Equal-valued pairs are skipped, which is what
    makes this cheaper than the textbook (N/2)log2(N) tree.

    mode = 0/2 prefer opposite pairs, 1 prefers equal pairs, 3 prefers equal then
    extremes, 4 pairs the two smallest remaining groups after checking equal groups.  Returns None instead of raising when the invariant
    cannot be established (the browser original threw here).
    """
    b = list(state)
    whole = ids is None
    ids = [i for i, x in enumerate(b) if x] if whole else list(ids)
    if not ids:
        return []
    N = _pow2_at_least(len(ids))
    if N > len(b):
        return None
    chosen = set(ids)
    p = 0
    while len(ids) < N and p < len(b):
        if b[p] == 0 and p not in chosen:
            ids.append(p)
            chosen.add(p)
        p += 1
    if len(ids) < N or sum(b[i] for i in ids) != 0:
        return None

    moves = []
    groups = [[i] for i in ids]
    while len(groups) > 1:
        unused = list(groups)
        pairs = []
        while len(unused) > 1:
            found = None
            if mode < 3:
                want_equal = (mode == 1)
                for ai in range(len(unused)):
                    for bj in range(ai + 1, len(unused)):
                        x, y = b[unused[ai][0]], b[unused[bj][0]]
                        if ((x == y) if want_equal else (x + y == 0)):
                            found = (ai, bj)
                            break
                    if found:
                        break
            if found is None and mode != 2:
                for ai in range(len(unused)):
                    for bj in range(ai + 1, len(unused)):
                        if b[unused[ai][0]] == b[unused[bj][0]]:
                            found = (ai, bj)
                            break
                    if found:
                        break
            if found is None:
                unused.sort(key=lambda g: b[g[0]])
                found = (0, 1) if mode == 4 else (0, len(unused) - 1)
            ai, bj = found
            pairs.append((unused[ai], unused[bj]))
            del unused[bj]
            del unused[ai]
        nxt = []
        for G, H in pairs:
            if len(G) != len(H):
                return None
            for k in range(len(G)):
                i, j = G[k], H[k]
                x, y = b[i], b[j]
                if x == y:
                    continue
                moves.append((x, y))
                s = x + y
                b = [s if (t == i or t == j) else 2 * b[t] for t in range(len(b))]
                g = gcd_all(b)
                if g:
                    b = [t // g for t in b]
            nxt.append(G + H)
        groups = nxt
    if any(b[i] for i in set(ids)):
        return None
    if whole and any(b):
        return None
    return moves


def best_butterfly(state, ids=None, modes=(0, 1, 2, 3, 4)):
    best = None
    for mode in modes:
        t = butterfly(state, ids, mode)
        if t is not None and (best is None or len(t) < len(best)):
            best = t
    return best


def descent_choice(state, e_cur=None, prune=True):
    """A successor with strictly smaller energy Psi = sum x^2 (and still mixable).

    n <= 16: all value pairs are examined.  n > 16: scan the extreme values of each
    parity class first (same-parity distinct values lower Psi by >= 2, paper Lemma 6) and
    fall back to the full scan, so the heuristic is only a *speed* choice, never a
    completeness one.
    """
    if e_cur is None:
        e_cur = energy(state)
    if len(state) <= 16:
        return _descent_full(state, e_cur, prune)
    buckets = [[], []]
    for x in state:
        g = buckets[x % 2]
        if not g or g[-1] != x:
            g.append(x)
    seen = set()
    best = None
    for values in buckets:
        if len(values) < 2:
            continue
        cands = values[:4] + values[-4:]
        for a in range(len(cands)):
            for bj in range(a + 1, len(cands)):
                x, y = cands[a], cands[bj]
                if x == y:
                    continue
                key = (x, y) if x <= y else (y, x)
                if key in seen:
                    continue
                seen.add(key)
                w = mix(state, x, y)
                if w is None or (prune and not possible(w)):
                    continue
                en = energy(w)
                if en < e_cur and (best is None or en < best[0]):
                    best = (en, key, w)
    if best:
        return {"move": best[1], "state": best[2], "en": best[0]}
    return _descent_full(state, e_cur, prune)


def _descent_full(state, e_cur, prune):
    best = None
    for w, mv in children(state, prune):
        en = energy(w)
        if en < e_cur and (best is None or en < best[0]):
            best = (en, mv, w)
    return None if best is None else {"move": best[1], "state": best[2], "en": best[0]}


def _path(node):
    out = []
    while node[1] is not None:
        out.append(node[2])
        node = node[1]
    return out[::-1]


def escape(state, limit=20000, deadline=None, prune=True, state_cap=100_000):
    """Bounded best-first escape; immutable parent nodes preserve replay labels."""
    e0, P = energy(state), floor_pow2(len(state))
    root = (tuple(state), None, None, 0)  # state, immutable parent, move, depth
    heap = [(0, 0, root)]
    seen = {tuple(state): 0}
    count, serial = 0, 0
    while heap and count < limit:
        if deadline is not None and time.time() >= deadline:
            break
        _score, _serial, node = heapq.heappop(heap)
        v, _parent, _move, d = node
        if seen.get(v) != d:
            continue
        count += 1
        for w, mv in children(v, prune):
            nd = d + 1
            if seen.get(w, float('inf')) <= nd:
                continue
            if w not in seen and len(seen) >= state_cap:
                return dict(moves=None, count=count)
            seen[w] = nd
            child = (w, node, mv, nd)
            en, m = energy(w), nz_count(w)
            if m <= P or en < e0:
                return dict(moves=_path(child), count=count)
            serial += 1
            heapq.heappush(heap, (en.bit_length() + 2*m + 2*nd, serial, child))
    return dict(moves=None, count=count)


def construct_moves(state, deadline=None, max_steps=19000, escape_limit=60000,
                    partition=True):
    """Verified-sequence construction: five routes, tried in this order at each step.

      1. opposite         cancel an existing (x,-x) pair - two positions reach 0 at once
      2. quartet + butterfly  a zero-sum 4-subset is finished on its own
      3. butterfly        pad the whole support with existing zeros to 2^t and finish
      4. descent_choice   any move that strictly lowers Psi and stays mixable
      5. escape           bounded best-first hunt for a state route 3 or 4 accepts

    Returns a list of value-pair moves (empty list = already solved) or None on failure.
    Invalid internal invariants are not converted into success.
    """
    v = prim_sorted(state)
    if not any(v):
        return []
    moves = []
    esc = 0
    expanded = 0
    while len(moves) < max_steps:
        if not any(v):
            return moves
        if deadline is not None and time.time() > deadline:
            break
        mv = opposite(v)
        if mv is not None:
            w = mix(v, *mv)
            if w is None:
                return None
            moves.append(mv)
            v = w
            continue
        if partition and nz_count(v) > 4:
            ids = quartet(v)
            if ids is not None:
                t = best_butterfly(v, ids)
                if t:
                    if len(moves) + len(t) > max_steps:
                        return None
                    for mv in t:
                        w = mix(v, *mv)
                        if w is None:
                            return None
                        moves.append(mv)
                        v = w
                    continue
        t = best_butterfly(v)
        if t is not None:
            if len(moves) + len(t) > max_steps:
                return None
            for mv in t:
                w = mix(v, *mv)
                if w is None:
                    return None
                moves.append(mv)
                v = w
            if not any(v):
                return moves
            continue
        best = descent_choice(v)
        if best is not None:
            moves.append(best["move"])
            v = best["state"]
            continue
        r = escape(v, limit=escape_limit, deadline=deadline)
        expanded += r["count"]
        esc += 1
        if not r["moves"] or len(moves) + len(r["moves"]) > max_steps:
            return None
        for mv in r["moves"]:
            w = mix(v, *mv)
            if w is None:
                return None
            moves.append(mv)
            v = w
    return None if any(v) else moves


# ------------------------------------------------------------- A* (kept for cross-check)
def astar(state, node_budget=1_000_000, deadline=None, limit=None, memo=True):
    """Optional best-first reference: (steps, VALUE moves, pops, status).

    solver_v2.astar wraps this to retain the old POSITION-sequence API.
    `memo` is accepted for compatibility; no cross-call result cache is used.
    """
    state = prim_sorted(state)
    root = (state, None, None, 0)
    heap = [(heuristic(state), 0, root)]
    seen = {state: 0}
    pops = serial = 0
    while heap:
        f, _serial, node = heapq.heappop(heap)
        v, _parent, _mv, d = node
        if seen.get(v) != d:
            continue
        if limit is not None and f > limit:
            return None, None, pops, 'proved'
        if not any(v):
            return d, _path(node), pops, 'solved'
        if pops >= node_budget or len(seen) >= 200_000:
            return None, None, pops, 'budget'
        if deadline is not None and time.time() >= deadline:
            return None, None, pops, 'budget'
        pops += 1
        for w, mv in children(v):
            nd = d + 1
            if seen.get(w, float('inf')) <= nd:
                continue
            h = heuristic(w)
            if limit is not None and nd + h > limit:
                continue
            seen[w] = nd
            serial += 1
            heapq.heappush(heap, (nd+h, serial, (w, node, mv, nd)))
    return None, None, pops, 'proved'


def beam_improve(state, best, deadline=None, width=24, max_states=40000):
    """Find a shorter upper bound; never certifies optimality (beam is incomplete)."""
    state = prim_sorted(state)
    root = (state, None, None, 0)
    beam, seen = [root], {state: 0}
    expanded = 0
    best = list(best)
    for depth in range(min(len(best)-1, 96)):
        nxt = []
        for node in beam:
            if deadline is not None and time.time() >= deadline:
                return best, expanded
            for w, mv in children(node[0], prune=True):
                expanded += 1
                d, h = depth+1, heuristic(w)
                if d+h >= len(best) or seen.get(w, float('inf')) <= d:
                    continue
                seen[w] = d
                child = (w, node, mv, d)
                if not any(w):
                    best = _path(child)
                else:
                    en = energy(w)
                    nxt.append((4*h+en.bit_length(), en, child))
        nxt.sort(key=lambda row: (row[0], row[1]))
        beam = [row[2] for row in nxt[:width]]
        if not beam:
            break
        for node in beam:
            if deadline is not None and time.time() >= deadline:
                return best, expanded
            if nz_count(node[0]) <= floor_pow2(len(state)):
                tail = best_butterfly(node[0])
                if tail is not None and node[3]+len(tail) < len(best):
                    best = _path(node)+tail
        if len(seen) >= max_states:
            seen = {node[0]: node[3] for node in beam}
    return best, expanded
