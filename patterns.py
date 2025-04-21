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


def pattern13(n:int):
    for b in range(1, n + 1):
        col = "* "
        if b == 1:
            spaces = " " * (n-b)
            print(spaces + col)
        elif 1 < b < n:
            spaces1 = " " * (n-b)
            spaces = "  " * (b - 2)
            print(spaces1 + col + spaces + col)
        elif b == n:
            spaces = " " * (n-b)
            col = "*" * ((2*n) - 1)
            print(spaces + col)


def pattern14(n:int):
    for b in range(1, n+1):
        star = "* "
        if b == 1:
            space = " " * (b - 1)
            col = "*" * ((2*n) - 1)
            print(space + col)
        elif 1 < b < n:
            spaces1 = " " * (b - 1)
            spaces2 = "  " * (n-b-1)
            print(spaces1 + star + spaces2 + star)
        elif b == n:
            space = " " * (n - 1)
            print(space + star)
    

def pattern15(n:int):
    for b in range(1, 2*n):
        col = "* "
        if b <= n:
            if b == 1:
                space = " " * (n - b)
                col = col * b
                print(space + col)
            elif 1 < b <= n:
                space = " " * (n - b)
                space2 = "  " * (b - 2)
                print(space + col + space2 + col)
        else:
            if n < b < 2*n - 1:
                space = " " * (b - n)
                space2 = "  " * ((2*n) - b -2)
                print(space + col + space2 + col)
            elif b == 2*n - 1:
                space = " " * (b - n)
                print(space + col)

def pattern16(n:int):
    pass

def pattern17(n:int):
    num = ''
    for b in range(1, n+1):
        space = " " * (n - b)
        num += str(b)
        sort_num = "".join(sorted(num, reverse=True))
        rev = num[1:]

        output = (space + sort_num + rev)
        print(output)

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



            
        







if __name__ == '__main__':
    pattern18(5)