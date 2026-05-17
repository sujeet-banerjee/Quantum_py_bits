from collections import OrderedDict

def mul(*args, **kwargs):
    prod = 1
    # print(args)
    # print(kwargs)
    for arg in args:
        # print(arg)
        prod *= arg
    return prod

def eval(fn):
    (first, second, third) = fn
    #print(f"{first} ==> {second} and {third}")
    if first == 'add':
        return sum(second, **dict(third))
    elif first == 'mul':
        # why *second sometimes, but not other times!!
        return mul(*second, **dict(third))
    elif first == 'pow':
        return second[0] ** second[1]
    elif first == 'affine':
        third = dict(third)
        return second[0] * third['scale'] + third['bias']
    return None

def immute_key(fn: tuple):
    (first, second, third) = fn
    return first, tuple(second), frozenset(third.items())

def solution(capacity, calls):
    print(f"Capacity {capacity}")
    print(f"Calls {calls}")
    lru_cache = OrderedDict()
    exec_count = 0
    res_list = []
    calls_seq = [immute_key(call) for call in calls]
    for call in calls_seq:
        if call not in lru_cache:
            # drop elements from 0 to (len(lru_cache)-capacity)
            while len(lru_cache) >= capacity:
                lru_cache.popitem(last=False)
            # Evaluate and update cache
            lru_cache[call] = eval(call)
            # count execution
            exec_count += 1
        else:
            ret = lru_cache[call]
            lru_cache.move_to_end(call)
        res_list.append(lru_cache[call])
    return res_list, exec_count

print(solution(2, [('add', [1, 2], {}), ('add', [1, 2], {})]))
print(solution(2,
               [('affine', [5], {'scale': 2, 'bias': 1}),
                ('affine', [5], {'bias': 1, 'scale': 2})]))
#print(solution(3,None))