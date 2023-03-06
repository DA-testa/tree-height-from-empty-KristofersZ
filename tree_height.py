#211RDB475 Kristofers Zellītis 9.grupa

import sys
import threading
import numpy


def compute_height(n, parents):
    children = {i: [] for i in range(n)}
    root = [] 

    for i, parent in enumerate(parents):
        if parent == -1:
            root.append(i)
        else: 
            children[parent].append(i)
 
    def fDepth(node, fd):
        if not children[node]:
            return fd 
        else:
            mDepth = 0 
            for child in children[node]:
                cDepth = fDepth(child, fd+1) 
                mDepth = max(mDepth, cDepth)
            return mDepth 
 
    mHight =  0 
    for r in root:
        treeheight = fDepth(r, 0)
        mHight = max(mHight, treeheight) 

    return mHight + 1

def main():
    answer = input("Enter F (for file) or I (for input): ")
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

