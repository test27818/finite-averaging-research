"""Search symbolic return macros from the sixfold four-parameter family."""

from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations


Coeff = tuple[F, F, F, F]


def add(values):
    values = tuple(values)
    return tuple(sum((value[index] for value in values), F(0)) for index in range(4))


def mean(values):
    total = add(values)
    return tuple(value / 3 for value in total)


def step(state, selected):
    average = mean(state[index] for index in selected)
    result = list(state)
    for index in selected:
        result[index] = average
    return tuple(sorted(result))


def choices(state):
    seen = set()
    for selected in combinations(range(10), 3):
        signature = tuple(sorted(state[index] for index in selected))
        if signature in seen or len(set(signature)) == 1:
            continue
        seen.add(signature)
        yield selected, signature


def initial_state():
    u = (F(1), F(0), F(0), F(0))
    a = (F(0), F(1), F(0), F(0))
    b = (F(0), F(0), F(1), F(0))
    c = (F(0), F(0), F(0), F(1))
    d = (F(-6), F(-1), F(-1), F(-1))
    return tuple(sorted([u] * 6 + [a, b, c, d]))


def terminal_parameters(state):
    counts = Counter(state)
    if sorted(counts.values()) != [1, 3, 6]:
        return None
    background = next(value for value, count in counts.items() if count == 6)
    triple = next(value for value, count in counts.items() if count == 3)
    singleton = next(value for value, count in counts.items() if count == 1)
    assert all(singleton[index] == -6 * background[index] - 3 * triple[index]
               for index in range(4)), (background, triple, singleton, state)
    difference = tuple(background[index] - triple[index] for index in range(4))
    return background, triple, difference


def primitive_form(form):
    denominator = 1
    for value in form:
        denominator = denominator * value.denominator // __import__("math").gcd(
            denominator, value.denominator)
    integers = [int(value * denominator) for value in form]
    divisor = 0
    for value in integers:
        divisor = __import__("math").gcd(divisor, abs(value))
    integers = tuple(value // divisor for value in integers)
    first = next(value for value in integers if value)
    return tuple(-value for value in integers) if first < 0 else integers


def coefficient_mod(value, prime):
    return value.numerator * pow(value.denominator, -1, prime) % prime


def form_value_mod(form, vector, prime):
    return sum(coefficient_mod(coefficient, prime) * value
               for coefficient, value in zip(form, vector)) % prime


def locally_legal_input(vector, prime):
    u, a, b, c = vector
    d = -6 * u - a - b - c
    return len({u % prime, a % prime, b % prime, c % prime, d % prime}) > 1


def local_cover(return_macros):
    inputs = [
        (u, a, b, c)
        for u in range(10)
        for a in range(10)
        for b in range(10)
        for c in range(10)
        if locally_legal_input((u, a, b, c), 2)
        and locally_legal_input((u, a, b, c), 5)
    ]
    full = (1 << len(inputs)) - 1
    covers = {}
    for key, (_, _, difference, path) in return_macros.items():
        bits = 0
        for index, vector in enumerate(inputs):
            if (form_value_mod(difference, vector, 2)
                    and form_value_mod(difference, vector, 5)):
                bits |= 1 << index
        if bits:
            covers[key] = bits

    selected = []
    covered = 0
    while covered != full:
        key = max(covers, key=lambda candidate: (covers[candidate] & ~covered).bit_count())
        gain = covers[key] & ~covered
        if not gain:
            break
        selected.append(key)
        covered |= gain

    changed = True
    while changed:
        changed = False
        for key in selected[:]:
            union = 0
            for other in selected:
                if other != key:
                    union |= covers[other]
            if union == full:
                selected.remove(key)
                changed = True
                break

    print("local inputs", len(inputs), "selected macros", len(selected),
          "uncovered", (full & ~covered).bit_count())
    for key in selected:
        background, triple, difference, path = return_macros[key]
        print(" cover difference", primitive_form(difference), "depth", len(path))
        print("  background", background)
        print("  triple", triple)
        print("  path", path)
    if covered != full:
        misses = [inputs[index] for index in range(len(inputs))
                  if not (covered >> index) & 1]
        print("first misses", misses[:40])
    return selected, inputs, covered == full


def search(max_depth=4):
    start = initial_state()
    queue = deque([(start, ())])
    seen = {start}
    found = {}
    return_macros = {}
    levels = Counter({0: 1})
    while queue:
        state, path = queue.popleft()
        if path and (parameters := terminal_parameters(state)) is not None:
            form = primitive_form(parameters[2])
            found.setdefault(form, path)
            background, triple, difference = parameters
            key = (background, triple)
            return_macros.setdefault(key, (background, triple, difference, path))
        if len(path) == max_depth:
            continue
        for selected, signature in choices(state):
            nxt = step(state, selected)
            if nxt in seen:
                continue
            seen.add(nxt)
            levels[len(path) + 1] += 1
            queue.append((nxt, path + (signature,)))
    print("levels", dict(levels), "states", len(seen), "difference forms", len(found))
    for form, path in sorted(found.items(), key=lambda item: (len(item[1]), item[0])):
        print(" form", form, "depth", len(path), "path", path)
    print("return parameter maps", len(return_macros))
    local_cover(return_macros)
    return found, return_macros


if __name__ == "__main__":
    search()
