def pattern1(n:int):
        for b in range(n):
            col = '*' * n
            print(col)
        print("")

def pattern2(n:int): 
    for b in range(1,n + 1):
        col = '*' * b
        print(col)
    print("")
      
def pattern3(n:int): 
    for b in range(n + 1):
        col = '*' * (n - b)
        print(col)
    print("")

def pattern4(n:int): 
    col = " "
    for b in range(1, n + 1):
        col += f"{b} "
        print(col)
    print("")

def pattern5(n:int): 
    for b in range(1, (2* n) + 1):
        if b <= n:
            col = '*' * b
            print(col)
        else:
            col = '*' * ((2*n) -b)
            print(col)



if __name__ == '__main__':
    pattern5(5)