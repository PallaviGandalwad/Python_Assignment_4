
#2.Write a program which contains one lambda function which accepts two parameters and return
#its multiplication.
#Input : 4 3 Output : 12
#Input : 6 3 Output : 18



#print("By using lambda function")

#fp = lambda no1,no2: no1*no2
#no1=input("num1:")
#no2=input("num2:")
#ret=fp(no1,no2)
#print("power of {} is".format(ret))
#print(result(fp))


result = lambda a,b: a*b;
no1=input("Enter first number:");
no2=input("Enter second number:");

print( result(no1,no2));


