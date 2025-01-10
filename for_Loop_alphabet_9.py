# * * * * *
#     *
#     * 
#     *
# * * * * *

for row in range(5):
    for col in range(5):
        if row==0 or col==5 or col==2 or row==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()