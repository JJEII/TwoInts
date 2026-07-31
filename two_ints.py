def is_prime(n: int) -> bool:
    """Determine if number `n` is prime or not."""
    if not isinstance(n, int) or n < 2:
        return False
    primes = [2]
    while n > primes[-1]: # generate primes as needed
        prev_last = primes[-1]
        nxt = primes[-1]
        while primes[-1] == prev_last:
            nxt += 1
            for p in primes:
                if nxt%p == 0:
                    break
            else: # found the next prime (didn't break out of loop)
                primes.append(nxt)
    return n in primes

def assess_1(ab_sum: int) -> list[tuple[int, int]]:
    """Assess Statement 1.
    Return list of all `ab_sum` bipartitions that FAIL Statement 1. (If empty, passes.)"""
    bipartitions = []
    A = 2
    while A + A <= ab_sum:
        B = ab_sum - A
        if is_prime(A) and (is_prime(B) or A*A==B):
            bipartitions.append( (A, B) ) # fail 1
        A += 1
    return bipartitions

def assess_2(ab_prod: int) -> list[tuple[int, int]]:
    """Assess Statement 2.
    Return list of all `ab_prod` factor-pairs that PASS Statement 1 when summed."""
    factor_pairs = []
    A = 2
    while A * A <= ab_prod:
        B = ab_prod // A
        if A*B==ab_prod and len(assess_1(A+B)) == 0:
            factor_pairs.append( (A, B) ) # pass 1
        A += 1
    return factor_pairs

def assess_3(ab_sum: int) -> list[tuple[int, int]]:
    """Assess Statement 3. (Assumes this `ab_sum` already passed Statement 1.)
    Return list of all `ab_sum` bipartitions that PASS Statement 2 when multiplied."""
    bipartitions = []
    A = 2
    while A + A <= ab_sum:
        B = ab_sum - A
        if len(result2:=assess_2(A*B)) == 1: # anything length != 1 fails 2
            bipartitions.append(result2[0]) # pass 2; flatten it (only one factor-pair in there)
        A += 1
    return bipartitions

PASS, FAIL = [f"\x1b[38;2;{r};{g};{b}m{sym}\x1b[0m" for sym, r, g, b in [["✓", 0, 180, 0], ["×", 200, 0, 0]]]
for s in range(4, 101): # smallest conceivable sum is 4 (when A=2 and B=2)
    if len(result1 := assess_1(s)) == 0: # if statement 1 passed (no bipartitions failed)
        if len(result3 := assess_3(s)) == 1: # if statement 3 passed (exactly one multiplied bipartition passed 2)
            details = " and ".join(map(str, result3[0]))
            print(f"{PASS} Sum={s} passes Statement 3. Integers A and B are {details}.")
        else: # statement 3 failed (number of multiplied bipartitions != 1)
            details = ", ".join(str(AB) for AB in result3) if len(result3)>0 else "(none)"
            print(f"   {FAIL} Sum={s} fails Statement 3 because these factor-pairs pass Statement 2: {details}.")
    else: # statement 1 failed (>0 failed bipartitions)
        details = ", ".join(map(str, result1))
        print(f"      {FAIL} Sum={s} fails Statement 1 because of these bipartitions: {details}.")