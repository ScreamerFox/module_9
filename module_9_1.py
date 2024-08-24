
def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result

def max_(args):
    return max(args)

def min_(args):
    return min(args)

def len_(args):
    return len(args)
def sum_(args):
    return sum(args)
def sorted_(args):
    return sorted(args)

print(apply_all_func([6, 20, 15, 9], max_, min_))
print(apply_all_func([6, 20, 15, 9], len_, sum_, sorted_))
