def isValid(s: str) -> bool:
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return s == ''

# Test the function
s = input()
print(isValid(s))
