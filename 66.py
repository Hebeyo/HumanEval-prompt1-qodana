def digitSum(s):
    return sum(ord(char) if char.isupper() else 0 for char in s)
