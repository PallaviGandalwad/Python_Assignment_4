#arr=[8,9,5,16,2,4,21,30,11]

#filter

#evenArr=list(filter(lambda no:(no%2==0),arr))

#map

#modArray=list(map(lambda no:no+2,evenArr))

#reduce

#sum=reduce(lambda a,b: a+b ,modArray)

print("Filter map reduce")

def EvenChk(no):
	return(no%2==0)

def Increase(no):
	return no+2

def Add(a,b):
	return a+b

arr=[8,9,5,16,2,4,21,30,11]

evenArr=list(filter(EvenChk,arr))

print("data after filter",evenArr)

modArray=list(map(Increase,evenArr))

print("Data after map",modArray)

#sum1 =reduce(Add,modArray)

print("Data after addition of even number",sum1)

# Demonstration of Filter, Map reduce using lambda functions
evenArr = list(filter(lambda no : (no%2==0), arr))
print("Data after filter using lambda",evenArr)
ModArray = list(map(lambda no : no+2,evenArr))
print("Data after map using lambda", ModArray)
sum1 = reduce(lambda a,b : a+b,ModArray)
print("Addition of even numbers using lambda",sum1)


