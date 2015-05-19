def counting_sort(A, B, k):
    C = [0 for i in range(k)]
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]] - 1


A = [2,5,3,0,2,3,0,3]
B = [0 for i in range(8)]
print A
counting_sort(A, B, 6)
print B

'''
why the last step i from A.length-1 to 0?
C record the max index of every element in A,
So from big num to small num , it can set every
element in A though the index , ant then each times,
the index in C, do index = index - 1, so every element
can put into B


k is max num in A adding one
'''
