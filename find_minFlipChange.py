# count the flips
def get_flipWithStartCh(str, expected):
	flipCount = 0
	for i in range(len( str)):
		# if current character is not expected,increase flip count
		if (str[i] != expected):
			flipCount += 1
		# flip expected character each time
		if expected == '0': expected = '1'
		else: expected = '0'	
	return flipCount

# get the minimum of flips when alternate string starts with 0 or flips when alternate string starts with 1
def minFlipChange(str):
	return min(get_flipWithStartCh(str, '0'), get_flipWithStartCh(str, '1'))


def test_flipChg1():
    coin_flips = "0001010111"
    assert minFlipChange(coin_flips)  == 2

def test_flipChg2():
    coin_flips = "1111111111"
    assert minFlipChange(coin_flips)  == 5

def test_flipChg3():
    coin_flips = "0000000000"
    assert minFlipChange(coin_flips)  == 5

def test_flipChg4():
    coin_flips = "1001010111001"
    assert minFlipChange(coin_flips)  == 5

def test_flipChg5():
    coin_flips = "1100110011100"
    assert minFlipChange(coin_flips)  == 6

def test_flipChg6():
    coin_flips = ""
    assert minFlipChange(coin_flips)  == 0		

def test_flipChg7():
    coin_flips = "101010101010101"
    assert minFlipChange(coin_flips)  == 0	