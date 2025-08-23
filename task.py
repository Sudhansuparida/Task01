
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def is_anagram(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())

# -------------------------------

if __name__ == "__main__":
    # Prime
    print("Prime Check: 7 ->", is_prime(7))
    print("Prime Check: 10 ->", is_prime(10))

    # Palindrome
    print("Palindrome Check: 'madam' ->", is_palindrome("madam"))
    print("Palindrome Check: 'hello' ->", is_palindrome("hello"))

    # Anagram
    print("Anagram Check: 'listen' & 'silent' ->", is_anagram("listen", "silent"))
    print("Anagram Check: 'hello' & 'world' ->", is_anagram("hello", "world"))
