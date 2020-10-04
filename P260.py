import sys

sys.setrecursionlimit(1010)

class Node:
    def __init__(self, id, data, left = None, right = None):
        self.left = left
        self.right = right
        self.data = data
        self.id = id


# pre order traversal
def preorder(root):
    if root != 0:
        res.append(treeNodes[root].data)
        preorder(treeNodes[root].left)
        preorder(treeNodes[root].right)

while True:
    try:
        treeNodes = [0] * 1001

        nodes = [0]*1001
        child = [0]*1001
        d = {0: None}
        n = int(input())
        res = []

        for _ in range(n):
            a = list(input().split())
            a = [int(a[0]), a[1], int(a[2]), int(a[3])]
            d[a[0]] = a[1]
            id = a[0]
            ch = a[1]
            left = a[2]
            right = a[3]
            nodes[id] = 1
            child[left] = child[right] = 1
            treeNodes[id] = Node(id, ch, left, right)

            if _ == n-1:
                for i in range(1001):
                    if nodes[i] !=0 and child[i] == 0:
                        break
                preorder(i)

        print("".join(res))

    except:
        break