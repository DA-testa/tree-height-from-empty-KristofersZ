#211RDB475 Kristofers Zellītis 9.grupa

import sys
import threading


def compute_height(n, parents):
    children = {i: [] for i in range(n)}
    root = [] 

    for i, parent in enumerate(parents):
        if parent == -1:
            root.append(i)
        else: 
            children[parent].append(i)
 
            
    def find_max_depth(node, d):
        if not children[node]:
            return d 
        else:
            max_D = 0 
            for child in children[node]:
                child_D = find_max_depth(child, d+1) 
                max_D = max(max_D, child_D)
            return max_D 
 
    max_H =  0 
    for r in root:
        treeheight = find_max_depth(r, 0)
        max_H = max(max_H, treeheight) 

    return max_H  + 1

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

