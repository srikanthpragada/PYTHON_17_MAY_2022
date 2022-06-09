import sys

print(sys.path)
sys.path.insert(0, r'c:\classroom\may17\demo\mylib')

import str_funs

print(str_funs.count_upper("Python"))