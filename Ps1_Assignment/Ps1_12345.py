# 作业1
def Print_values(a,b,c):
    if a > b:
        if b > c:
            print(a,b,c)
        else:
            if a > c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b > c:
            print(c,b,a)
        else:
            print(b,c,a)
a = float(input("请输入第一个数："))
b = float(input("请输入第二个数："))
c = float(input("请输入第三个数："))
Print_values(a,b,c)







# 作业2
import random
M1 = []
for i in range(5):
    row = [random.randint(0,50) for _ in range(10)]
    M1.append(row)
print(M1)
M2 = []
for i in range(10):
    row = [random.randint(0,50) for _ in range(5)]
    M2.append(row)
print(M2)

def Matrix_multip(mat1, mat2):
    m = len(mat1)
    n = len(mat2)
    p = len(mat2[0])
    result = [[0]*p for _ in range(m)]
    
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += mat1[i][k] * mat2[k][j]
            result[i][j] = total
    return result

res = Matrix_multip(M1,M2)
print(res)








# 作业3
import math
def Pascal_triangle(k):
    row = []
    for i in range(k+1):
        comb = math.comb(k,i)
        row.append(comb)
    print(row)
    return row
Pascal_triangle(100)
Pascal_triangle(200)







# 作业4
def Least_moves(x):
    count = 0
    cur = x
    while cur > 1:
        if cur % 2 == 1:
            cur -= 1
        else:
            cur = cur // 2
        count +=1
    print(count)
    return count
num = int(input("请输入一个正整数："))
Least_moves(num)











# 作业5
def Find_expression(target):
    digits = "123456789"
    solutions = []
    def dfs(pos, current_expr, current_val, prev):
        if pos == len(digits):
            if current_val == target:
                solutions.append(current_expr)
            return
        for i in range(pos, len(digits)):
            num_str = digits[pos:i+1]
            num = int(num_str)
            if pos == 0:
                dfs(i+1, num_str, num, num)
            else:
                dfs(i+1, current_expr + "+"+num_str, current_val + num, num)
                dfs(i+1, current_expr + "-"+num_str, current_val - num, -num)
    dfs(0,"",0,0)
    for s in solutions:
        print(f"{s} = {target}")
    return solutions
t = int(input("请输入目标值："))
Find_expression(t)