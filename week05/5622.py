import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

alpha = str(input())
ans = 0
for i in alpha:
    if i =='A' or i =='B' or i =='C':
        ans+= 3
    elif i =='D' or i =='E' or i =='F':
        ans +=4
    elif i =='G' or i =='H' or i =='I':
        ans +=5
    elif i =='J' or i =='K' or i =='L':
        ans +=6
    elif i =='M' or i =='N' or i =='O':
        ans +=7
    elif i =='P' or i =='Q' or i =='R' or i =='S':
        ans +=8
    elif i =='T' or i =='U' or i =='V':
        ans +=9
    elif i =='W' or i =='X' or i =='Y' or i =='Z':
        ans +=10
     
print(ans)