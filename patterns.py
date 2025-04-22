def pattern1(n:int):
        for _ in range(n):
            col = '*' * n
            print(col)

def pattern2(n:int): 
    for b in range(1,n + 1):
        col = '*' * b
        print(col)
      
def pattern3(n:int): 
    for b in range(n + 1):
        col = '*' * (n - b)
        print(col)

def pattern4(n:int): 
    col = " "
    for b in range(1, n + 1):
        col += f"{b} "
        print(col)    

def pattern5(n:int): 
    for b in range(1, (2* n) + 1):
        if b <= n:
            col = '*' * b
            print(col)
        else:
            col = '*' * ((2*n) -b)
            print(col)

def pattern6(n:int):
    for s in range(1, n+1):
        spaces = n - s
        output = (" " * spaces + '*' * s)
        print(output)


def pattern7(n:int): 
    for b in range(n + 1):
        spaces = n - (n - b)
        col = '*' * (n-b)
        output = (" "*spaces + col)
        print(output)
   

def pattern8(n:int):
    for b in range(1, n+1):
        spaces = " " * (n - b)
        col = "*" * ((2 * b) - 1)
        print(spaces + col)
    

def pattern9(n:int): 
    for b in range(n + 1):
        spaces = " " * (n - (n - b))
        col = "*" * (2*n - (2 * b) - 1)
        print(spaces + col)


def pattern10(n:int):
    for b in range(1, n+1):
        spaces = " " * (n-b)
        col = "* " * b
        print(spaces + col)
    

def pattern11(n:int):
    for b in range(n+1):
        spaces = " " * (n - (n-b))
        col = "* " * (n - b)
        print(spaces + col)
 

def pattern12(n:int):
    for b in range(2*n + 1):
        if b <= n:
            spaces = " " * b
            col = "* " * (n - b)
            print(spaces + col, end='')
        spaces = " " * (2*n - b)
        col = "* " * (b - n)
        print(spaces + col.rstrip())


# def pattern13(n:int):
#     for b in range(1, n + 1):
#         col = "* "
#         if b == 1:
#             spaces = " " * (n-b)
#             print(spaces + col)
#         elif 1 < b < n:
#             spaces1 = " " * (n-b)
#             spaces = "  " * (b - 2)
#             print(spaces1 + col + spaces + col)
#         elif b == n:
#             spaces = " " * (n-b)
#             col = "*" * ((2*n) - 1)
#             print(spaces + col)
def pattern13(n: int):
    for b in range(1, n + 1):
        row = ""
        for p in range(1, 2 * n):
            if b == n or p == n - b + 1 or p == n + b - 1:
                row += "*"
            else:
                row += " "
        print(row)


# def pattern14(n:int):
#     for b in range(1, n+1):
#         star = "* "
#         if b == 1:
#             space = " " * (b - 1)
#             col = "*" * ((2*n) - 1)
#             print(space + col)
#         elif 1 < b < n:
#             spaces1 = " " * (b - 1)
#             spaces2 = "  " * (n-b-1)
#             print(spaces1 + star + spaces2 + star)
#         elif b == n:
#             space = " " * (n - 1)
#             print(space + star)
def pattern14(n: int):
    for b in range(1, n + 1):
        row = ""
        for p in range(1, 2 * n):
            if b == 1 or p == b or p == 2 * n - b:
                row += "*"
            else:
                row += " "
        print(row)
    

# def pattern15(n:int):
#     for b in range(1, 2*n):
#         col = "* "
#         if b <= n:
#             if b == 1:
#                 space = " " * (n - b)
#                 col = col * b
#                 print(space + col)
#             elif 1 < b <= n:
#                 space = " " * (n - b)
#                 space2 = "  " * (b - 2)
#                 print(space + col + space2 + col)
#         else:
#             if n < b < 2*n - 1:
#                 space = " " * (b - n)
#                 space2 = "  " * ((2*n) - b -2)
#                 print(space + col + space2 + col)
#             elif b == 2*n - 1:
#                 space = " " * (b - n)
#                 print(space + col)

def pattern15(n: int):
    for b in range(1, 2*n):
        leading_spaces = abs(b - n)
        if b == 1 or b == 2*n - 1:
            print(" " * leading_spaces + "*")
        else:
            spaces_between = 2 * min(b, 2*n - b) - 3
            print(" " * leading_spaces + "*" + " " * spaces_between + "*")

def pattern16(n: int):
    prev_row = [1]
    for i in range(n):
        leading_spaces = " " * (n - i - 1)
        print(leading_spaces + " ".join(map(str, prev_row)))
        if i < n - 1:
            next_row = [1]
            for k in range(1, i + 1):
                next_row.append(prev_row[k - 1] + prev_row[k])
            next_row.append(1)
            prev_row = next_row


def pattern17(n:int):
    for b in range(1, 2*n):
        space = " " * abs(b - n)
        k = min(b, 2*n - b) #row range
        num = [str(i) for i in range(k,0, -1)] + [str(j) for j in range(2, k+1)]
        print(space + "".join(num))



def pattern18(n:int):
    for b in range(2*n + 1):
        if b < n:
            space = " " * (2*b)
            col = "*" * (n - b)
            print(col + space + col)
        else:
            col = "*" * (b -n)
            space = " "  * ((2*n) - 2*(b-n))
            print(col + space + col)


def pattern19(n:int):
    for b in range(1, 2*n):
        if b <= n:
            spaces = " " * (2*(n-b))
            col = "*" * b
            print(col + spaces + col)
        else:
            space = " " * (2 *(b - n))
            col = "*" * ((2*n) - b)
            print(col + space + col)

def pattern20(n:int):
    for b in range(1, n+1):
        if b == 1 or b == n:
            col = "*" * (n-1)
            print(col)
        else:
            space = " " * (n-3)
            col = "*"
            print(col + space + col)

def pattern21(n:int):
    num = 1
    for b in range(1, n+1):
        row = [str(num + i) for i in range(b)]
        num += b
        print(" ".join(row))
        

            
        




if __name__ == '__main__':
    pattern21(5)