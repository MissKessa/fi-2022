#Python VI. Problem 20

def element_product(row,column):
    """Creates and returns a matrix of a given size and initialize each
element aij = i * j"""
    p=[]
    for i in range (0,row,1):
        for j in range(0,column,1):
            p.append(i*j)
    return p


def element_sum(row,column):
    """Creates and returns a matrix of a given size and initialize each
element aij = i + j"""
    p=[]
    for i in range (0,row,1):
        for j in range(0,column,1):
            p.append(i+j)
    return p


def write_list_by_columns(p,columns):
    """Given a vector of real numbers, prints the values in m
columns."""
    for i in range (0,len(p)):
        if (i)%columns==0:
            print()
        print(p[i], end=" ")


def sum_matrices(p,q,columns_p,columns_q):
    """Receives two matrices (of the same size) and returns the sum of
the two of them (matrix addition)"""
    sum=[]
    rows_p=len(p)//columns_p
    rows_q=len(q)//columns_q
    if rows_p == rows_q and columns_p==columns_q:
        for i in range(0,len(p),1):
            sum.append(p[i]+q[i])
        return sum
    return None


def product_matrices(p,q,columns_p,columns_q):
    product=[]
    rows_p=len(p)//columns_p
    rows_q=len(q)//columns_q
    if columns_p == rows_q:
        for i in range(0,rows_p,1):
            for j in range (0,columns_q,1):
                sum_line=0
                for k in range (0,columns_p,1):
                    sum_line+=p[i*columns_p+k]+q[k*columns_q+j]
                product.append(sum_line)
        return product
    return None


matrix1=element_product(2,3)
write_list_by_columns(matrix1,3)
print()
matrix2=element_sum(2,3)
write_list_by_columns(matrix2,3)
print()
matrix3=element_product(3,3)
write_list_by_columns(matrix3,3)

print()
a1=sum_matrices(matrix1,matrix2,3,3)
write_list_by_columns(a1,3)
print()
a2=sum_matrices(matrix1,matrix3,3,3)
print(a2)
print()
b1=product_matrices(matrix1,matrix2,3,3)
print(b1)
print()
b2=product_matrices(matrix1,matrix3,3,3)
write_list_by_columns(b2,3)