import sys

def Recursive(n, list_res):
    k = n
    list_res_ongoing = list_res
    while(True):
        list_res_ongoing.append(Solve(k))
        if k <= 2:
            list_res_ongoing.append(Solve(k))
            return list_res_ongoing

    return Recursive(k-2, list_res_ongoing)

def Solve(n):
    s = '('*(n//2)+')'*(n//2)
    return s

def main(lines):
    for i ,v in enumerate(lines):
        if i ==0:
            N = v
    N = int(N)
    list_res = []
    if N%2 != 0:
        return print('')
    else:
        list_s = Recursive(N, list_res)
        list_s.sort()
        for s in list_s:
            print(s)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
        if 'exit'== l.rstrip('\r\n'):
            break
    main(lines)
