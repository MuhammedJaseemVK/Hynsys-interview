first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

temp=''
import re
for i in range(0,m):
    for j in range(0,n):
        # print(matrix[i][j])
        temp+=matrix[j][i]

newOutput=re.sub('(?<=\w)([^\w\d]+)(?=\w)',' ',temp)
print(newOutput)