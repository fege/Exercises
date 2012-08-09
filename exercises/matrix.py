'''A matrix can be represented as a list of lists (rows and columns).
Use the comprehensions to describe the identity matrix 
(the one with all 0s but the 1s on the diagonal) of given size.
Use the comprehensions to describe a square matrix filled with 
the first n*n integers.
Write a function to transpose a generic matrix independently 
of the size and content.
Write a function to multiply two matrices non necessarily 
square matrix.'''

def matid(n,m):
	a=[[(0,1) [i==j] for i in range(n)] for j in range(m)]
	return a

def sqmat(n):
	return [[(j*n+i)*(j*n+i) for i in range(n)] for j in range(n)]

def trasposta(m):
	righe=len(m)
	col=len(m[1])
	print('matrice data',m)     
	mt = [[m[j][i] for j in range(righe)] for i in range(col)]
	return "Matrice trasposta {0}".format(mt)

def mult(m,m1):
	print('matrice 1',m)
	print('matrice 2', m1)
	righem1=len(m1)
	colm=len(m[1])
	righe=(len(m))
	colm1=len(m1[1])
	if righem1 != colm:
		return 'ERRORE DIMENSIONI MATRICI'
	val= [ [ [m[i][j]*m1[j][x] for j in range(colm)]for x in range(colm1)] for i in range(righe)]
	mat = [[sum(val[i][j]) for j in range(len(val[0]))] for i in range(len(val))]
	return 'prodotto tra le matrici {0}'.format(mat)

if __name__ == '__main__':
	print(matid(3,3))
	print(sqmat(3))
	mat=[[1,2,3],[4,5,6],[7,8,9]]
	mat1=[[1,1,2],[0,1,-3]]
	mat2=[[1,1,1],[2,5,1],[0,-2,1]]
	print(trasposta(mat))
	print(mult(mat1,mat2))