```python
def is_palindrome(s):
    return s == s[::-1]

def main():
    test_string = "racecar"
    if is_palindrome(test_string):
        print(f"{test_string} is a palindrome.")
    else:
        print(f"{test_string} is not a palindrome.")

if __name__ == "__main__":
    main()
```