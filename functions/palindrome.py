def palindrome(txt):
    if len(txt) <= 1:
        return "It is palindrome!"  # base case
    elif txt[0] != txt[-1]:
        return "It is not a palindrome"
    else:
        return palindrome(txt[1:-1])  # recursive case

print(palindrome("madeam"))

