"""A compact, exactly decodable exponential family of earliest outside exits.

The general odd-p pair decoder recognizes all singleton words from equal
exceptions. The p=5 endpoint decoder covers all length-L singleton-then-E0
exits from singleton_source(L), including the older two-step subfamily.
It does not recognize all first exits or decide subsequent consensus.
Values are exact unscaled integer physical states, modulo permutation only.
"""
from collections import Counter
from math import gcd


def singleton_source(length):
    """A positive seven-position cluster with depth length >= 1."""
    if not isinstance(length, int) or length < 1:
        raise ValueError('length must be a positive integer')
    a = 3 if length % 2 else 2
    n = 5 ** length
    return (a,) * 5 + (a + n, a + n, -7 * a - 2 * n)


def encode_singleton_pair(word, p=5):
    if not isinstance(p, int) or p < 3 or p % 2 == 0:
        raise ValueError('p must be an odd integer at least 3')
    u, v = 1, 1
    for letter in word:
        if letter == 1:
            u, v = -u, p * v - u
        elif letter == 2:
            u, v = p * u - v, -v
        else:
            raise ValueError('letters must be 1 or 2')
    return u, v


def decode_singleton_pair(u, v, p=5):
    """Decode the entire T1/T2 orbit of (1,1), using a unique mod-p**2 inverse.

    This is an ordered pair language. Returning a word certifies membership
    in this language only, not subsequent global averaging success.
    """
    if not isinstance(p, int) or p < 3 or p % 2 == 0:
        raise ValueError('p must be an odd integer at least 3')
    if not isinstance(u, int) or not isinstance(v, int):
        return None
    reversed_runs = []
    while (u, v) != (1, 1):
        if gcd(u, p) != 1 or (u - v) % p:
            return None
        d1, d2 = (p + 1) * v - u, (p + 1) * u - v
        if d1 % (p * p) == 0:
            letter, d = 1, d1
        elif d2 % (p * p) == 0:
            letter, d = 2, d2
        else:
            return None
        # Eigenlines with eigenvalue -1 cycle under the same inverse and
        # cannot contain a descendant of (1,1).
        if d == 0:
            return None
        exponent = 0
        while d % p == 0:
            d //= p
            exponent += 1
        count = exponent - 1
        assert count >= 1
        divided = (d1 if letter == 1 else d2) // (p ** count)
        sign = -1 if count % 2 else 1
        if letter == 1:
            u = sign * u
            v, rem = divmod(divided + u, p + 1)
        else:
            v = sign * v
            u, rem = divmod(divided + v, p + 1)
        assert rem == 0
        reversed_runs.append((letter, count))
    return tuple(letter for letter, count in reversed(reversed_runs) for _ in range(count))


def encode_singletons(word):
    """An E0 exit after an arbitrary singleton word of positive length."""
    word = tuple(word)
    initial = singleton_source(len(word))
    u, v = encode_singleton_pair(word)
    d = initial[-1]
    a, rem = divmod(-d - u - v, 7)
    assert rem == 0
    z, rem = divmod(4 * a + d, 5)
    assert rem == 0
    return tuple(sorted((z,) * 5 + (a, a + u, a + v)))


def decode_singletons(values, length):
    """Recognize all singleton-then-E0 exits from singleton_source(length).

    Unlabelled endpoints identify a word with its exchange 1 <-> 2. Return
    the lexicographically smaller representative, which begins with 1.
    """
    if not isinstance(length, int) or length < 1:
        raise ValueError('length must be a positive integer')
    values = tuple(values)
    if len(values) != 8 or any(not isinstance(v, int) for v in values) or sum(values):
        return None
    counts = Counter(values)
    repeated = [v for v, count in counts.items() if count == 5]
    if len(counts) != 4 or len(repeated) != 1 or repeated[0] >= 0:
        return None
    rest = sorted(v for v in counts if v != repeated[0])
    if min(rest) <= 0:
        return None
    answers = []
    # Avoid computing 5**length before verifying a decoded word of that length.
    # Thus a huge binary-encoded length cannot force huge work on a small input.
    for a in rest:
        b, c = (v for v in rest if v != a)
        for first, second in ((b, c), (c, b)):
            word = decode_singleton_pair(first - a, second - a)
            if word is not None and len(word) == length and encode_singletons(word) == tuple(sorted(values)):
                answers.append(word)
    return min(answers) if answers else None


def source(k):
    if not isinstance(k, int) or k < 0:
        raise ValueError('k must be a nonnegative integer')
    n = 5 ** (2 * k + 1)
    return (3,) * 5 + (3 + n, 3 + n, -21 - 2 * n)


def encode_pair(word):
    x, y = 1, 4
    for letter in word:
        if letter == 1:
            x, y = x, 4 * x + 25 * y
        elif letter == 2:
            x, y = 25 * x + 4 * y, y
        else:
            raise ValueError('letters must be 1 or 2')
    return x, y


def decode_pair(x, y):
    """Return the unique word or None; O(log(max(x,y))) stripping steps."""
    if not isinstance(x, int) or not isinstance(y, int) or min(x, y) <= 0:
        return None
    reversed_word = []
    while (x, y) != (1, 4):
        if y > 4 * x:
            q, r = divmod(y - 4 * x, 25)
            if r:
                return None
            y = q
            reversed_word.append(1)
        elif x > 4 * y:
            q, r = divmod(x - 4 * y, 25)
            if r:
                return None
            x = q
            reversed_word.append(2)
        else:
            return None
    return tuple(reversed(reversed_word))


def encode(word):
    """Construct one earliest first-exit endpoint without enumerating its peers."""
    word = tuple(word)
    x, y = encode_pair(word)
    n = 5 ** (2 * len(word) + 1)
    d = -21 - 2 * n
    a, rem = divmod(21 + 2 * n + x - y, 7)
    assert not rem
    z, rem = divmod(4 * a + d, 5)
    assert not rem
    return tuple(sorted((z,) * 5 + (a - x, a, a + y)))


def decode(values, k=None):
    """Exact physical-state membership, not consensus reachability.

    An optional k restricts to exits from source(k). Scaling is deliberately
    not normalized: every genuine endpoint is already primitive with G=1.
    """
    values = tuple(values)
    if len(values) != 8 or any(not isinstance(v, int) for v in values):
        return None
    if k is not None and (not isinstance(k, int) or k < 0):
        raise ValueError('k must be a nonnegative integer or None')
    counts = Counter(values)
    repeated = [v for v, count in counts.items() if count == 5]
    if len(counts) != 4 or len(repeated) != 1 or repeated[0] >= 0:
        return None
    z = repeated[0]
    b, a, c = sorted(v for v in counts if v != z)
    if b <= 0 or sum(values):
        return None
    word = decode_pair(a - b, c - a)
    if word is None or (k is not None and len(word) != k):
        return None
    return word if encode(word) == tuple(sorted(values)) else None


def physical_word(word):
    """Letters in the existing distinguished-outside core convention."""
    word = tuple(word)
    encode_pair(word)  # Validate letters, including generators supplied by callers.
    return ('S1',) + tuple('S' + str(b) for b in word for _ in range(2)) + ('E0',)
