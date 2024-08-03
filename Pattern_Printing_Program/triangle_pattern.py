def print_triangle(rows):
       for i in range(1,rows+1):
                    print(""*(rows-i)+"*"*(2*i-1))
       for i in range(rows-1,0,-1):
                    print(""*(rows-i)+"*"*(2*i-1))
print_triangle(5)
