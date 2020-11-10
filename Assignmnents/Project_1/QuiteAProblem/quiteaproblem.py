import sys
def answer(data):
	ans = ''
	for line in data:
         line = line.lower()
         if 'problem' in line:
             ans = 'yes'
             return ans
         else:
             ans = 'no'
             return ans
def solve():
     data = sys.stdin.readlines()
     print(answer(data))
        

def test():
    input1 = 'probably we will figure out when to solve the equation'
    assert answer(input1) == 'no'
    input2 = 'the issue will consist of when we find the error in the system'
    assert answer(input2) == 'no'
    input3 = 'probably I will think of a way to solve the question I have'
    assert answer(input3) == 'no'
    input4 = 'hearing about problims make me think about other solutions'
    assert answer(input4) == 'no'
    print('All Cases Passed')
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()

