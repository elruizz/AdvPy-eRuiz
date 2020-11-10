#! /usr/bin/env python3
import sys
def answer(a, b):
	ans = ''
	if a > b:
		x = a - b
		if x == 1:
			ans = 'Dr. Chaz needs 1 more piece of chicken!'
			return ans
		else:
			ans = 'Dr. Chaz needs '+ str(x) + ' more pieces of chicken!'
			return ans
	else:
		x = b - a
		if x == 1:
			ans = 'Dr. Chaz will have 1 piece of chicken left over!'
			return ans
		else:
			ans = 'Dr. Chaz will have '+ str(x) + ' pieces of chicken left over!'
			return ans
def solve():
	a, b = map(int, input().split())
	print(answer(a, b))
	
def test():
    assert answer(20, 100) == 'Dr. Chaz will have 80 pieces of chicken left over!'
    assert answer(2, 3) == 'Dr. Chaz will have 1 piece of chicken left over!'
    assert answer(10, 1) == 'Dr. Chaz needs 9 more pieces of chicken!'
    print('All Cases Passed')
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()

