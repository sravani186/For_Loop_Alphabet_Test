#    *    *
#    *   *
#    * *
#    *  *
#    *    *                           

for row in range(5):
    for col in range(5):
        if col==0 or row==5 or row+col==3 or row-col==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()