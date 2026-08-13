from collections import deque

def palindrome(str1):
    l1 = []
    v = deque()

    for ch in str1:
        if ch.isalnum():
            l1.append(ch.lower())
            v.append(ch.lower())

    while len(v) > 1:
        if l1.pop() != v.popleft():
            return False

    return True

str1 = input("Enter a string: ")

if palindrome(str1):
    print(str1, "is a palindrome")
else:
    print(str1, "is not a palindrome")
