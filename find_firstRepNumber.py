
def  firstRepeatedNumber(arr1, arr2):
    compare = 1
    if len(arr1) <= len(arr2):
        x = arr1
        y = arr2
    elif len(arr1) > len(arr2):
        x = arr2
        y = arr1
    for i in range(len(x)):
        for j in range (len(y)):
            compare = x[i] ^ y[j]
            if (compare == 0):
                return x[i]    
    return False    
    
def test_compare1():
    vector1 = [3, 5, 2, 5, 2]
    vector2 = [2, 3, 5, 5, 2]
    assert firstRepeatedNumber(vector1, vector2)  == 3

def test_compare2():
    vector1 = [3, 5, 2, 5, 2]
    vector2 = [2, 4, 5, 0, 2]
    assert firstRepeatedNumber(vector1, vector2)  == 5

def test_compare3():
    vector1 = [3, 5, 6, 5, 2]
    vector2 = [4, 7, 9, 8, 2]
    assert firstRepeatedNumber(vector1, vector2)  == 2

def test_compare4():
    vector1 = [3, 5, 6, 5, 0]
    vector2 = [4, 7, 9, 8, 2]
    assert firstRepeatedNumber(vector1, vector2)  == False

def test_compare5():
    vector1 = [3, 5, 6, 5, -2]
    vector2 = [4, 7, 2, 8, -2]
    assert firstRepeatedNumber(vector1, vector2)  == -2

def test_compare6():
    vector1 = []
    vector2 = []
    assert firstRepeatedNumber(vector1, vector2)  == False

def test_compare7():
    vector1 = [4, 7, 9, 8, 77]
    vector2 = [3, 792, 5, 32198, 6, 55, 77, 199, 2020, 1027]
    assert firstRepeatedNumber(vector1, vector2)  == 77

def test_compare8():
    vector1 = [3, 792, 5, 32198, 6, 55, 77, 199, 2020, 1027]
    vector2 = [4, 7, 9, 8, 2020]
    assert firstRepeatedNumber(vector1, vector2)  == 2020
