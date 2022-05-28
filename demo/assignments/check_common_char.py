s1 = "abcdefg"
s2 = "pqrstd"

for c in s1:
    if c in s2:
        print("Yes")
        break
else:
    print('No')
