class Prime:
    _primes = {2: None, 3: None, 5: None, 7: None} # store primes in increasing order
    _largest_checked = 7 # invariant: ALWAYS leave this at 6n+1 (whether prime or not)

    @classmethod
    def is_prime(cls, n: int) -> bool:
        """Determine if natural number `n` is prime."""
        if n > cls._largest_checked:
            cls._generate_primes_up_through(n)
        if n in cls._primes:
            return True
        return False

    @classmethod
    def _generate_primes_up_through(cls, at_least: int) -> None:
        """All primes greater than 3 conform to either 6n-1 or 6n+1 (but not
        necessarily vice versa). Leverage that fact for generating primes."""
        if at_least <= cls._largest_checked:
            return
        at_least = 6*((at_least+4)//6) + 1 # adjust to smallest 6n+1 >= at_least
        for n in range(cls._largest_checked + 5, at_least, 6):
            for pp in (n-1, n+1):
                for lo in cls._primes:
                    if pp % lo == 0:
                        break
                    if lo*lo > pp:
                        cls._primes[pp] = None
                        break
        cls._largest_checked = at_least
