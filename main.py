import hashlib
import random
import string
import time

#config
STRING_LENGTH = 16
MAX_ATTEMPTS = 100_000_000
TRUNCATE_HEX = 12

def generate_random_string(length=STRING_LENGTH):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def get_truncated_hash(hash_func, input_str, hex_length=TRUNCATE_HEX):
    full_digest = hash_func(input_str.encode()).hexdigest()
    return full_digest[:hex_length]

def simulate_collision(hash_func, hash_name, truncate_to=TRUNCATE_HEX, max_attempts=MAX_ATTEMPTS):
    seen_digests = set()
    start_time = time.time()

    for attempt in range(1, max_attempts + 1):
        random_input = generate_random_string()
        digest = get_truncated_hash(hash_func, random_input, truncate_to)

        if digest in seen_digests:
            elapsed = time.time() - start_time
            print(f"[{hash_name}] Collision found after {attempt:,} attempts in {elapsed:.2f} seconds.")
            print(f"Truncated Digest: {digest}")
            print(f"Input Length: {STRING_LENGTH} characters")
            return attempt, elapsed, digest

        seen_digests.add(digest)

    elapsed = time.time() - start_time
    print(f"[{hash_name}] No collision found after {max_attempts:,} attempts. Time: {elapsed:.2f} seconds.")
    return None, elapsed, None

def run_simulation():
    print("=== Hash Collision Simulation ===")
    print(f"Truncating hash output to {TRUNCATE_HEX * 4} bits ({TRUNCATE_HEX} hexadecimal characters)\n")

    md5_result = simulate_collision(hashlib.md5, "MD5")
    print()
    sha1_result = simulate_collision(hashlib.sha1, "SHA-1")
    print()
    print("=== Summary ===")
    if md5_result[0]:
        print(f"MD5: Collision at {md5_result[0]:,} attempts, Time: {md5_result[1]:.2f}s, Digest: {md5_result[2]}")
    if sha1_result[0]:
        print(f"SHA-1: Collision at {sha1_result[0]:,} attempts, Time: {sha1_result[1]:.2f}s, Digest: {sha1_result[2]}")

if __name__ == "__main__":
    run_simulation()
