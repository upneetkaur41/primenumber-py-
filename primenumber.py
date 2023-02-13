

number=int(input("Enter a Number:\n"))
if number==1:
    print("Number Entered is a not Prime Number!")
elif number >1:
    for x in range(2,number):
        if number% x==0:
            print("Number Entered is not a Prime Number!")
            
        else:
            print("Number Entered is a Prime Number!")   
        break     
else:
     print("Number Entered is a Prime Number!")            
