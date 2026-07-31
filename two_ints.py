from math import sqrt
from typing import Union

def is_prime(n: int) -> bool:
    """Determine if number `n` is prime or not."""
    if not isinstance(n, int) or n < 2:
        return False
    primes = [2, 3, 5, 7]
    while n > primes[-1]:
        prev_last = primes[-1]
        nxt = primes[-1]
        while primes[-1] == prev_last:
            nxt += 1
            for p in primes:
                if nxt%p == 0:
                    break
            else: # didn't break; found next prime
                primes.append(nxt)
    return n in primes
    
def assess_1(ab_sum: int) -> Union[None, list[int, int]]:
    """Assess Statement 1.
    Return a list containing all partitions of `ab_sum` that FAIL Statement 1."""
    found_partitions = []
    for A in range(2, ab_sum//2+1):
        if is_prime(A) and (is_prime(ab_sum-A) or A*A==ab_sum-A):
            found_partitions.append([A, ab_sum-A])
    return found_partitions

def assess_2(ab_prod: int) -> Union[list[list[int, int]], list[list[int, int], list[int, int]]]:
    """Assess Statement 2.
    Return a list containing all factor-pairs of `ab_prod` that PASS Statement 1 when summed."""
    found_factor_pairs = []
    for A in range(2, int(sqrt(ab_prod))+1):
        if ab_prod%A == 0:
            B = ab_prod//A
            if len(assess_1(A+B)) == 0:
                found_factor_pairs.append([A, B])
    return found_factor_pairs

def assess_3(ab_sum: int) -> Union[list[list[int, int]], list[list[int, int], list[int, int]]]:
    """Assess Statement 3.
    Assumes this `ab_sum` already passed Statement 1.
    Return a list containing all partitions of `ab_sum` that PASS Statement 2 when multiplied."""
    found_partitions = []
    for A in range(2, ab_sum//2+1):
        B = ab_sum - A
        result2 = assess_2(A*B)
        if len(result2) == 1: # anything length != 1 is a failure
            found_partitions.append(result2[0]) # flatten it
            if len(found_partitions) > 1:
                return found_partitions
    return found_partitions

RED   = f"\x1b[38;2;{200};{0};{0}m"
GREEN = f"\x1b[38;2;{0};{180};{0}m"
RESET = "\x1b[0m"
tab = "   "
for s in range(4, 101): # smallest conceivable sum is 4 (when A=2 and B=2)
    if len(result1 := assess_1(s)) == 0: # if statement 1 succeeded
        if len(result3 := assess_3(s)) == 1: # if statement 3 succeeded
            print(f"{GREEN}✓{RESET} Sum={s} passes Statement 3. Integers A and B are {' and '.join(map(str, result3[0]))}.")
        else: # statement 3 failed (number of possible factor-pairs != 1)
            status = ", ".join(str(AB) for AB in result3) if len(result3)>0 else "(none)"
            print(f"{tab}{RED}×{RESET} Sum={s} fails Statement 3 because these factor-pairs pass Statement 2: {status}.")
    else: # statement 1 failed
        print(f"{tab}{tab}{RED}×{RESET} Sum={s} fails Statement 1 because of these partitions: {', '.join(map(str, result1))}.")