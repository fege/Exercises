import random
import itertools

def check(a):
    sud = list(a)
    sudo=[]
    for pos,riga in enumerate(sud):
        for griglia in range(3):
            if not pos % 3: sudo.append([]) 
            sudo[griglia + pos//3*3].extend(riga[griglia*3:griglia*3+3])
    for pos in range(len(sudo)):
        if [x for x in [set(sudo[pos])] if x != set(range(1,10))]:
            return False
    return True

soluzioni = set()
def sudoku():
    global soluzioni
    while True:
        rg = range(9)
        su = [[None for i in rg] for j in rg] 
        for x in rg:
            if x in range(0,9,3): blockx = range(x, x+3)
            elif x in range(1,9,3): blockx = range(x-1, x+2)
            elif x in range(2,9,3): blockx = range(x-2, x+1)
            for y in rg:
                if y in range(0,9,3): blocky = range(y, y+3)
                elif y in range(1,9,3): blocky = range(y-1, y+2)
                elif y in range(2,9,3): blocky = range(y-2, y+1)
                block = []
                for i in blockx:
                    for j in blocky:
                        block.append(su[i][j])
                ls = list(set(range(1,10)).difference(set(su[x])).\
                          difference(set(su[j][y] for j in rg)).difference(set(block)))
                if len(ls) > 0:
                    su[x][y] = random.choice(ls)
        done = True
        for t in su:
            for v in t:
                if v == None:
                    done  = False
        if done == True:
            a=tuple((tuple(i) for i in su))
            if a not in soluzioni:
                soluzioni.add(a)   
                yield a
            for k in itertools.permutations(a):
                if check(k):
                    if k not in soluzioni:
                        soluzioni.add(k)   
                        yield k
if __name__ == "__main__":
    for i in sudoku():
        print(i,'\n')
