# *    *     *
# *   * *    *
# *  *    *  *
# * *      * *
# *          *

for row in range(5):
    for col in range(9):
        if col==0 or row==8 or col==8 or row==5 or row+col==4 or col-row==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()