# 3章 配列を集合にする

# 重複削除、昇順ソート
def make_set(arrs):
    results = []
    if arrs == []:
        return results
    results.append(arrs[0])
    for arr in arrs:
        ans = True
        for result in results:
            if arr == result:
                ans = False
        if ans :
            results.append(arr)
    results = sorted(results)
    return results

def intersection_set(arrs1, arrs2):
    new_arrs1 = make_set(arrs1)
    new_arrs2 = make_set(arrs2)
    results = []
    for new_arr1 in new_arrs1:
        for new_arr2 in new_arrs2:
            if new_arr1 == new_arr2:
                results.append(new_arr2)
    return results

def union_set(arrs1, arrs2):
    results = arrs1 + arrs2
    results = make_set(results)
    return results

def diff_set(arrs1, arrs2):
    intersections = intersection_set(arrs1, arrs2)
    new_arrs1 = make_set(arrs1)
    results = []
    for new_arr1 in new_arrs1:
        ans = True
        for inteersection in intersections:
            if new_arr1 == inteersection:
                ans = False
        if ans:
            results.append(new_arr1)
    return results
