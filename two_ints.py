from math import sqrt, ceil, prod
from itertools import product
from functools import reduce
import operator
from typing import Union
from Prime import Prime

def assess_1(sm: int) -> Union[None, list[int, int]]:
    """Return None if all valid partitions succeed,
    or [A, B] for first partition found that fails."""
    for pt in range(2, sm//2+1):
        if Prime.is_prime(pt) and (Prime.is_prime(sm-pt) or pt*pt==sm-pt):
            return [pt, sm-pt]
    return None

def assess_2(pd: int) -> Union[list[list[int, int]], list[list[int, int], list[int, int]]]:
    """Return
    (success)   [A, B] if only one factor-pair succeeds, or
    (failure)   [] if none do, or
    (failure)   [[A0, B0], [A1, B1]] if multiple do (the first pair of factor-pairs found)."""

    # ensure the generated primes-pool is large enough
    Prime.is_prime(ceil(sqrt(pd)))

    # determine powers-of-primes factors
    factor_opts = []
    p = pd
    for f in Prime._primes:
        opts = [1]
        pf = f
        while p > 0 and p % f == 0:
            opts.append(pf)
            pf *= f
            p //= f
        if len(opts) > 1:
            factor_opts.append(opts)
        if p == 0:
            break

    # build all factors from the powers-of-primes options
    lo_factors = set()
    half_pd = pd // 2
    for combo in product(*factor_opts):
        if 1 < (f := reduce(operator.mul, combo, 1)) <= half_pd:
            lo_factors.add(f)

    # count factor-pair sums that pass statement 1 (w/early exit at #sums>1)
    found_sums = set()
    for f in lo_factors:
        A, B = sorted([f, pd//f])
        if assess_1(A+B) is None:
            found_sums.add( (A, B) )
            if len(found_sums) > 1:
                return list(found_sums)

    return list(found_sums)

def assess_3(sm: int) -> Union[list[list[int, int]], list[list[int, int], list[int, int]]]:
    """Assume Statement 1 was already assessed successfully for this `sm`."""
    found_prods = []
    for A in range(2, sm//2+1):
        B = sm - A
        res2 = assess_2(A*B)
        if len(res2) == 1: # else fails (which we mostly need)
            found_prods.append(res2[0])
            if len(found_prods) > 1:
                return found_prods
    return found_prods

RED   = f"\x1b[38;2;{200};{0};{0}m"
GREEN = f"\x1b[38;2;{0};{180};{0}m"
RESET = "\x1b[0m"
tab = "   "
for s in range(4, 501):
    if (res1 := assess_1(s)) is None:
        if len(res3 := assess_3(s)) == 1:
            print(f"{GREEN}✓{RESET} {s}: Statement 3. Integers A and B are {' and '.join(map(str, res3[0]))}.") # ✅
        else:
            prod_str = ' and '.join(map(str, map(prod, res3)))
            prod_str = ("products " + prod_str) if len(prod_str) > 0 else "no products"
            print(f"{tab}{RED}×{RESET} {s}: Statement 3, {prod_str} work.") # ❌
    else:
        print(f"{tab}{tab}{RED}×{RESET} {s}: Statement 1, partition {' + '.join(map(str, res1))}.") # ❌
