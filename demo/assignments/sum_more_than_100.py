def is_more_than_100(lst):
    return sum(lst) > 100


nums = [[1, 2, 34], [12, 56, 78], [32, 45, 67], [34, 1, 2]]

for lst in filter(is_more_than_100, nums):
    print(lst)
