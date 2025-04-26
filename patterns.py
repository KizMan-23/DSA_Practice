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
        

def pattern22(n:int):
    # digits = cycle([1, 0])
    for b in range(1, n+1):
        start = 1 if b % 2 == 1 else 0
        row = [str((start + i) % 2)  for i in range(b)]
        print(" ".join(row))
 

def pattern23(n:int):
    for b in range(1, n+1):
        row = ""
        for c in range(1, 3*n + 1):
            if  c == 3*n - (n-b) or c == 3*n - (n + b - 1):
                row += "* "
            else:
                row = ""
        print(row)


def pattern24(n:int):
    for b in range(1, 2*n +1):
        pass


def pattern25(n:int):
    for b in range(1,n+1):
        space = " " *(n -b)
        if b == 1 or b == n:
            row = "*" * (n)
            print(space + row)
        else:
            sp1 = " " * (n - 2)
            row = "*" 
            print(space + row + sp1 + row)

def pattern26(n:int):
    num = 1
    for b in range(1, n+1):
        row = str(num) * (n - (b - 1))
        num += 1
        print(" ".join(row))

def pattern27(n: int):
    num = 1
    total = n * (n + 1)
    right_start = total - n + 1
    for b in range(1, n + 1):
        spaces = "  " * (b - 1)
        count = n - b + 1

        left = [str(num + i) for i in range(count)]
        num += count

        right = [str(right_start + i) for i in range(count)]
        right_start = right_start - count + 1
        
        print(spaces + " ".join(left) + "  " + " ".join(right))

def pattern28(n:int):
    for b in range(1, 2*n + 1):     
        spaces = " " * abs(n - b)
        col = "* " * (n - abs(n-b))
        print(spaces + col)


def pattern29(n:int):
    pass # Already Solved in Pattern 19

def pattern30(n:int):
    num = 1
    row = ""
    for b in range(1, n+1):
        space = "  " * (n - b)
        row += str(num)

        rev_row = " ".join(sorted(row, reverse=True))
        new_row = " ".join(row[1:])
        num += 1
        print(space + rev_row + new_row) #tab space wasn't added for this

def pattern30a(n:int):
    num = 1
    row = ""
    for b in range(1, n+1):
        col_num = 2*n
        space = "  " * (n -b)
        row += str(f"{num}")
        rev_row = " ".join(sorted(row, reverse=True))
        for c in range(col_num):
            if c == n - (b-1):
                c = row[1:]
                c = " ".join(c)
                num += 1
                print(space + rev_row + " " + c) #the space here is funny cos i can't find how to incoporate it equally into the numbers
                 

def pattern31(n: int):
    size = 2 * n - 1
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            # Distances to edges
            top = i - 1
            bottom = size - i
            left = j - 1
            right = size - j
            value = n - min(top, bottom, left, right)
            row.append(str(value))
        print(" ".join(row))


def pattern32(n:int):
    alpha = ["A", "B", "C", "D", "E"]
    for b in range(n+1):
        val = alpha[(n - b):n+1]
        rev_alpha = " ".join(sorted(val))
        print(rev_alpha) 


def pattern33(n:int):
    import string
    letters = string.ascii_lowercase
    num = 0
    for b in range(1, n+1):
        row = ""
        for c in range(b):
            num += 1
            letter = letters[(num -1) % 26]
            if num % 2 == 0:
                letter  = letter.upper()
            row += f"{letter} "
        print(row)

def pattern33a(n:int):
    import string
    letters = string.ascii_lowercase
    num = 0
    for b in range(1, n+1):
        num += 1
        letter = [letters[(num - c -1) % 26].upper() if num % 2 == 0 else letters[(num-c -1) % 26] for c in range(b)]
        
        print(" ".join(letter))


def pattern34(n:int):
    alpha = ["A", "B", "C", "D", "E"]
    for b in range(n+1):
        val = alpha[ : (n-b) +1]
        rev_alpha = " ".join(sorted(val, reverse=True))
        print(rev_alpha)    

def pattern35(n:int):
    row = ""
    for b in range(1, n+1):
        row += str(b)
        space = " " * (2*n - (2*b))
        rev_row = "".join(sorted(row, reverse=True))
        print(row + space + rev_row)
       
        




if __name__ == '__main__':
    pattern31(4)