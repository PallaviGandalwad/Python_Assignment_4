#1.Write a program which contains one lambda function which accepts one parameter and return
#power of two.
#Input : 4 Output : 16
#Input : 6 Output : 64

#print("By using lambda function")

#fp = lambda no1: 2**no1
#no1=input("num:")
#ret=fp(no1)
#print("power of {} is".format(ret))
#print(result(fp))

result = lambda x: 2 ** x;
no=input("Enter number:");

print( result(no));