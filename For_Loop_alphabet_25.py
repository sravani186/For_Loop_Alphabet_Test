# *          *
#   *     * 
#      *
#   *
# *

for row in range(5):
    for col in range(5):
        if row+col==4 or row-col==0 and col<3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()