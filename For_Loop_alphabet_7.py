# * * * * *
# *       
# *   * * *
# *   *   *
# * * *   *

for row in range(5):
    for col in range(5):
        if col==0 or row==0 or (row==4 and col<3) or (row==2 and col>1) or (col==4 and row>1) or (col==2 and row==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()