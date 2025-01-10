#          *
#       *     *
#     *         *
#   * * * * * * * *
#   *             * 
#   *             *
#   *             *

for row in range(7):
    for col in range(7):
        if row+col==3 or row-col==-3 or row==3 or row==7 or (col==0 and row>2) or (col==6 and row>2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
