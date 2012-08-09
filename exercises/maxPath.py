'''
Created on 02/giu/2012

@author: fede
'''
def maxpath(l):
    i = len(l)-1
    return liv(l,i)

def liv(l,i):
    if i == 0:
        return l.pop(0)

    l[i-1]=[(l[i-1][k]+l[i][k+1],l[i-1][k]+l[i][k])[l[i][k]>l[i][k+1]] for k in range(len(l[i])-1)]
    return liv(l,i-1)
    

if __name__ == "__main__":
    l0 = [[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]
    l1 = [[11], [7,32], [14,14,14], [0,1,2,3], [5,99,1,2,7], [0,25,9,45, 54,1], [99,88,77,66,55,44,33]]
    l2 = [[-3],[-7,1], [-14,-2,-10], [7,0,0, -7], [-1,1,0,1,-1], [5,-5,25,-25,-7,7]]
    l3 = [[1.2], [-1.2,3.14], [1,-1,0], [-3.14,5.7,-1,.23], [.1,-.2,.3,-.4,.5]]
    print(l0, ":-",end = '')
    print(maxpath(l0))
    print(l1, ":-",end='')
    print(maxpath(l1))
    print(l2, ":-",end='')
    print(maxpath(l2))
    print(l3, ":-",end='')
    print(maxpath(l3))
