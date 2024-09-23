num=int(input("enter a number to check an armstrong or not"))

result=0
temp=num 
while temp!=0:
        digit=temp%10
        result=result+digit**3
        temp=temp//10
print(result)
if num==result:
        print("number is armstrong",num)
else:
        print("it is not an armstrong number",num)
