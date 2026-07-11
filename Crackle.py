import itertools
import string
import time

def crackle(time_limit_seconds=10):
    chars = string.ascii_letters + string.digits
    start = time.time()
    attempts = 0

    for length in range(1, 999999):
        if time.time() - start >= time_limit_seconds:
            return attempts, None # timed out
        for guess in itertools.product(chars, repeat=length):
            if time.time() - start >= time_limit_seconds:
                return attempts, guess
            attempts += 1

    return attempts, "done"


password = input("Input the Password you want to Crackle: ")
attempts, guess = crackle(time_limit_seconds=10)
if attempts == crackle:
    print(f"The Password Crackled in {attempts} attempts. The password is {guess}")
else:
    print(f"The Password was not Crackled after {attempts} attempts.")
