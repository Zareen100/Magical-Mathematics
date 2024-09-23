#activity2 find factors of a number
def factor(num):
    print("the factors of number are")
    for i in range(1,num+1):
        if num%i==0:
            print(i)
#taking input from the user
number=int(input("enter a number to find it's factors"))
factor(number)