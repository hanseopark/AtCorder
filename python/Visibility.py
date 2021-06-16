H, W, X, Y = map(int, input().split())
S = []
for i in range (H):
    S.append(input())

X = X-1
Y=  Y-1
count = -3

for i in range (X,H):
    if(S[i][Y]!= '#'):
        count +=1
for i in range (X,0-1,-1):
    if(S[i][Y] != '#'):
        count +=1
for j in range (Y,W):
    if(S[X][j]!= '#'):
        count +=1
for j in range (Y,0-1,-1):
    if(S[X][j] != '#'):
        count +=1

print(count)
