#complex expressions
a=3+4j
b=4+5j
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
#print(a // b) #foolr division does not exist
#print(a % b) #modulas does not exist

#boolean
print(4 > 3)
print(4 >= 3)
print(4 < 3)
print(type(bool)) #printing type
print(type(False))#printing type
print(int(True))#converting boolean into integer
print(int(False))#converting boolean into integer

#list
list1=[1, 2, 10, -8, 'sandhya', True, [1,2,3]]
print(list1)
print(type(list1))
print(len(list1))#length
print(list1[1])#indexing
print(list1[-2])#indexing
print(list1[2:6])#slicing
print(list1[0:7:2])#skipping one element
list1[1]=5#reassigning number
print(list1[1])

#tuple
tup=(1, 2, 10, -8, 'sandhya', True, (1,2,3))
print(tup[3])
#tup(3)=12#immutable

#range
print(range(0,100))
print(list(range(0,100)))#print 0 to 100
print(list(range(100,0)))#empty 
print(list(range(100,0,-1)))#prints 100 to 0
print(list(range(100,0,-2)))#prints 100 to 0 and skips 1 digit





