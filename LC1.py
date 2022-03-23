x=[i for i in range(10)]
print(x)

#Adding an expression - square of each number

squares=[i**2 for i in range(10)]
print(squares)


#Multiply each element by 3
list1=[3,4,5]
multiplied=[item*3 for item in list1]
print(multiplied)



#Word Manipulation

listOfWords=["this",'is','a','list','of','words']

#The output should be ['t','i','a','l','o','w']
items=[word[0] for word in listOfWords]
print(items)


list2=['A','B','C']
list3=[x.lower() for x in list2]
print(list3)

list4=[x.upper() for x in list3]
print(list4)

#Adding an if condition, all even numbers from 0-4(square)
new_range=[i*i for i in range(5) if i%2==0]
print(new_range)



string="Hello 12345 World"
letters=[x for x in string if x.isalpha()]
numbers=[x for x in string if x.isdigit()]
print(numbers)
print(letters)


#OLD WAY 
numbers=[]
for x in string: 
    if x.isdigit():
        numbers.append(x)

#using a file
myfile=open('test.txt','r')
results=[i.rstrip() for i in myfile if "line3" in i]
print(results)


#using functions
def double(x):
    return x*2

print(double(10))

mynumbers=[double(x) for x in range(10)]
print(mynumbers)

mynumbers=[double(x) for x in range(10) if x%2==0]
print(mynumbers)

#You can add more than one argument
result=[x+y for x in [10,30,50] for y in [20,40,60]]
print(result)