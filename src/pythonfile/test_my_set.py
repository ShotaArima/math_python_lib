import my_set

def test_make_set1():
    a = [1,2,1,1,1]
    assert my_set.make_set(a) == [1,2]

def test_make_set2():
    a = [4,3,2,1]
    assert my_set.make_set(a) == [1,2,3,4]

def test_make_set3():
    a = [1,2]
    assert my_set.make_set(a) == [1,2]

def test_make_set4():
    a = []
    assert my_set.make_set(a) == []

def test_intersection_set1():
    a = [1,2,3,4]
    b = [1]
    assert my_set.intersection_set(a, b) == [1]
    assert my_set.intersection_set(b, a) == [1]

def test_intersection_set2():
    a = [1,2,3,4]
    b = []
    assert my_set.intersection_set(a, b) == []
    assert my_set.intersection_set(b, a) == []

def test_union_set1():
    a = [1,2]
    b = [3,4]
    assert my_set.union_set(a, b) == [1,2,3,4]
    assert my_set.union_set(b, a) == [1,2,3,4]

def test_union_set2():
    a = [1,2]
    b = []
    assert my_set.union_set(a, b) == [1,2]
    assert my_set.union_set(b, a) == [1,2]

def test_union_set3():
    a = []
    b = []
    assert my_set.union_set(a, b) == []
    assert my_set.union_set(b, a) == []

def test_diff_set1():
    a = [1,2,3]
    b = [1]
    assert my_set.diff_set(a,b) == [2,3]
    assert my_set.diff_set(b,a) == []

def test_diff_set2():
    a = [1,2,3]
    b = [1,2,3]
    assert my_set.diff_set(a,b) == []
    assert my_set.diff_set(b,a) == []

def test_diff_set3():
    a = []
    b = []
    assert my_set.diff_set(a,b) == []
    assert my_set.diff_set(b,a) == []