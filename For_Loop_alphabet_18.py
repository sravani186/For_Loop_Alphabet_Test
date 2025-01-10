#   * * * * * 
#   *      *  
#   *    *
#   *   *
#   * *   
#   *  *
#   *    *
#   *      *

for row in range(8):
    for col in range(5):
        if col==0 or row==8 or row==0 or col==5 or row+col==5 or row-col==3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()