"""passtool - tiny password strength checker and generator."""
import math
import secrets
import string
import sys

COMMON = {"password", "123456", "12345678", "qwerty", "abc123", "letmein", "admin", "welcome"}


def entropy_bits(pw):
    pool = 0
    if any(c.islower() for c in pw):
        pool += 26
    if any(c.isupper() for c in pw):
        pool += 26
    if any(c.isdigit() for c in pw):
        pool += 10
    if any(c in string.punctuation for c in pw):
        pool += len(string.punctuation)
    return len(pw) * math.log2(pool) if pool else 0.0


def rate(pw):
    if pw.lower() in COMMON:
        return "weak"
    bits = entropy_bits(pw)
    if bits < 40:
        return "weak"
    if bits < 60:
        return "okay"
    return "strong"


def generate(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*-_"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "check":
        pw = sys.argv[2]
        print(f"{rate(pw)} ({entropy_bits(pw):.1f} bits)")
    elif len(sys.argv) >= 2 and sys.argv[1] == "gen":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 16
        print(generate(n))
    else:
        print("usage: python passtool.py check <password> | gen [length]")


if __name__ == "__main__":
    main()
