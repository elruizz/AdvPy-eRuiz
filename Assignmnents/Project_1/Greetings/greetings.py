#! /usr/bin/env python3
import sys
def answer(data):
    count = 0
    h = 'h'
    out_E = 'e'
    for i in range(len(data)):
        if data[i] == 'e':
            count += 1
        elif data[i] == 'y':
            count = count * 2
            out_E = count * out_E
            hello = h + out_E + 'y'
    return hello
    
def solve():
    data = input()
    data.lower()
    print(answer(data))

def test():
    input1 = 'hey'
    assert answer(input1) == 'heey'
    input2 = 'heey'
    assert answer(input2) == 'heeeey'
    input3 = 'heeeeeeeeeey'
    assert answer(input3) == 'heeeeeeeeeeeeeeeeeeeey'
    print('All Cases Passed')
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
