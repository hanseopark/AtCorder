import sys

def Score(model, tot_n, k, mid, l):
    tmp_val = 0
    cut_cnt = 0
    for i in range(tot_n):
        l_left = model[i]-tmp_val
        l_right = l -model[i]
        if l_left >= mid and l_right >= mid:
            cut_cnt +=1
            tmp_val = model[i]
    if cut_cnt >= k:
        return True
    else:
        False

def main(lines):
    A = []
    for i ,v in enumerate(lines):
        if i == 0:
            N, L = map(int, v.split())
        if i == 1:
            K = int(v)
        if i == 2:
            A = v.split()

    for i in range(len(A)):
        A[i] = int(A[i])
    right= L
    left = 0
    while right - left >1:
        mid = (right+left) // 2
        if Score(A, N, K, mid, L):
            left = mid
        else:
            right = mid

    return print(left)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
#        if 'exit'== l.rstrip('\r\n'):
#            break
    main(lines)
