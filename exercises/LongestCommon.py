'''
Created on 30/mag/2012

@author: fede

Longest Common Subsequence of 3 Strings
'''
def make_table(x,y):
    m, n = len(x), len(y)
    C1 = [0] * (1+n)
    for i in range(m):
        C0 = list(C1)
        for j in range(n):
            if x[i] == y[j]:
                C1[j+1] = C0[j]+1
            else:
                C1[j+1] = max(C1[j], C0[j+1])
    return C1

def lcs(x,y):
    m, n = len(x), len(y)
    if m == 0:
        return ''
    elif m == 1:
        return x[0] if x[0] in y else ''
    else:
        i = m // 2
        x1, x2 = x[:i], x[i:]
        C1 = make_table(x1, y)
        C2 = make_table(x2[::-1], y[::-1])
        M,k = max((C1[j] + C2[n-j], j) for j in range(n+1))
        y1, y2 = y[:k], y[k:]
        return lcs(x1, y1) + lcs(x2, y2)

if __name__ == "__main__":
    import functools
    a=['a','c','b','d','e']
    b=['b','q','c','z','k','e']
    print(lcs(a,b))
    print(functools.reduce(lcs, (a, b, 'pippo')))