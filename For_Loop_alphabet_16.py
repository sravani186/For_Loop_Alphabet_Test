#    * * * * *
#    *       *
#    * * * * *
#    *
#    * 

for row in range(5):
    for col in range(5):
        if col==0 or row==5 or row==0 or col==5 or row==2 or col==-4 or col-row==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()