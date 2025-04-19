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
    pass
        






if __name__ == '__main__':
    pattern12(5)