#211RDB475 Kristofers Zellītis 9.grupa

import sys
import threading


def compute_height(n, parents):
    child = {i:[] for i in range(n)}
    root = None
    for i in range(n):
        parents = parents[i]
        if parents==-1:
            root=i
        else:
            child[parents].append(i)

    def max_height(mh):
        height = 1
        if not child[mh]:
            return height
        else:
            for child in child[mh]:
                height = max(height, max_height(child))
            return height + 1
    return max_height(root)

def main():
    answer = input("Enter F (for file) or I (for input)")
    if "I" in answer:
        n = int(input())
        parents = list(map(int,input().split()))
    elif "F" in answer:
        fileName = input("Enter file name: ")
        file = "./test/" + fileName
        if "a" not in fileName:
            try:
                with open(file) as testFile:
                    n = int(testFile.readline())
                    parents = list(map(int, testFile.readline().split()))
            except Exception as error:
                print("Error:", str(error))
                return
    else:
        print("Error. Try again")
        return
    
    print(compute_height(n, parents))


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

