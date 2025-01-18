import hashlib
import itertools
import string


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def brute_force_crack(hash_to_crack, max_length):
    characters = string.ascii_lowercase + string.digits
    attempts = 0
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            attempts += 1
            hashed_guess = hash_password(guess_password)
            print(f"Trying: {guess_password}")
            if hashed_guess == hash_to_crack:
                print(f"\nPassword found: {guess_password} in {attempts} attempts!")
                return guess_password
    print("Password not found.")
    return None


if __name__ == "__main__":
    
    target_password = "1119"  
    target_hash = hash_password(target_password)
    print(f"Target Hash: {target_hash}")
    

    brute_force_crack(target_hash, max_length=4)

