import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(root):
    if root != ".":
        print(root, end='')
        preorder(tree[root][0]) #왼쪽
        preorder(tree[root][1]) #오른쪽

def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
