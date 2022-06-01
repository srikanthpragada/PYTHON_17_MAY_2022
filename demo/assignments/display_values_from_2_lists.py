l1 = [1, 2, 3, 5]
l2 = [10, 40, 50]

fl = len(l1)
sl = len(l2)
ml = fl if fl > sl else sl

for i in range(ml):
    fv = l1[i] if i < fl else 'Unknown'
    sv = l2[i] if i < sl else 'Unknown'
    print(f"{str(fv):10}  {str(sv):10}")