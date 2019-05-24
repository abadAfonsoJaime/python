'''
.items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary:

    The .keys() method returns a list of the dictionary’s keys, and
    The .values() method returns a list of the dictionary’s values.
'''
my_dict = {
  "Name": "Jaime",
  "Age": 29,
  "BDFL": True
}

print( my_dict.keys() )
print( my_dict.values() )

for key in my_dict:
	print( key, my_dict[key] )



# Building List comprehension using the for/in and if keywords 
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)


even_squares = [i*i for i in range(1, 11) if i % 2 == 0]
print(even_squares)

cubes_by_four = [ (x**3) for x in range(1,11) if (x**3)%4==0 ]
print(cubes_by_four)




'''
List Slicing Syntax allows us to access elements of a list in a concise manner. 
[start:end:stride]
Where start describes where the slice starts (inclusive), default is 0
 end is where it ends (exclusive), default is the end of the list
  and stride describes the space between items in the sliced list, default is 1.
'''
to_one_hundred = range(101)
print( to_one_hundred[::-10] )



'''
Functional Programming
	To pass functions around just as if they were variables or values

lambda x: x % 3 == 0
----IS SIMILAR TO----
def by_three(x):
  return x % 3 == 0

lambda functions are also known as anonymous functions


When we pass the lambda to filter, filter uses the lambda to determine what to filter, 
and the second argument (my_list, which is just the numbers 0 – 15) is the list it does the filtering on.
'''
my_list = range(16)
print( filter(lambda x: x % 3 == 0, my_list) ) # Python2 --> [0, 3, 6, 9, 12, 15]

# Python 3
print( list(range(100, -1, -10)))

'''
Lambdas are useful when you need a quick function to do some work for you.

If you plan on creating a function you’ll use over and over,
 you’re better off using def and giving that function a name.
'''
cubes = [x ** 3 for x in range(1, 11)]
filter(lambda x: x % 3 == 0, cubes)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter( lambda x: x!="X", garbled )
print(message)

'''
Iterating over dictionaries
print( myDicc.items() ) 
'''

