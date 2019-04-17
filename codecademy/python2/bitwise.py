'''
print 5 >> 4  # Right Shift --> 0
print 5 << 1  # Left Shift --> 10
print 8 & 5   # Bitwise AND --> 0
print 9 | 4   # Bitwise OR --> 13
print 12 ^ 42 # Bitwise XOR --> 38
print ~88     # Bitwise NOT --> -89

https://discuss.codecademy.com/t/how-can-computers-represent-everything-as-bit-strings/340558
Do you have a 32 or 64 bit system? Does your computer have a 256GB hard drive? Computers think in binary!
'''

'''
In Python, you can write numbers in binary format by starting the number with 0b. 
When doing so, the numbers can be operated on like any other number!


bin() takes an integer as input and returns the binary
You can also represent numbers in base 8 and base 16 using the oct() and hex() functions 

'''

int("42") # ==> 42
int("110", 2) # ==> 6
int("11001001",2) # ==> 201

'''
Shift operations are similar to rounding down after dividing and multiplying by 2 (respectively) 
for every time you shift, but it’s often easier just to think of it 
as shifting all the 1s and 0s left or right by the specified number of slots.

Note that you can only do bitwise operations on an integer. 
Trying to do them on strings or floats will result in nonsensical output!
'''

shift_right = 0b1100>>2
shift_left = 0b1<<2
print( bin(shift_right) ) # 0b11
print( bin(shift_left) ) # 0b100


'''
using the & operator can only result in a number that is less than or equal to the smaller of the two values.
'''
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1


'''
| operator can only create results that are greater than or equal to the larger of the two integer inputs.
'''
0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1


'''
The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number 
where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.
'''
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0


'''
Mathematically, bitwise NOT operator (~)  is equivalent to adding one to the number and then making it negative.
'''

'''
A bit mask is just a variable that aids you with bitwise operations. 
A bit mask can help you turn specific bits on, turn others off, 
or just collect data from an integer about which bits are on or off.


In the following example, we want to see if the third bit from the right is on.

    First, we first create a variable num containing the number 12, or 0b1100.
    Next, we create a mask with the third bit on.
    Then, we use a bitwise-and operation to see if the third bit from the right of num is on.
    If desired is greater than zero, then the third bit of num must have been one.
'''
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
	print("Bit was on")

def check_bit4(input):
	mask = 0b1000
	desired = input & mask
	if desired > 0:
		return "on"
	else:
		return "off"
'''
Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.

In the following example we use a bitmask and the value a=0b10111011 in order to 
achieve a result where the third bit from the right of a is turned on.
'''
a = 0b10111011
mask = 0b100
desired = a | mask
print( bin(desired) )

'''
In the following example we use a bitmask and the value a=0b10111011 in order to 
achieve a result where the third bit from the right of a is turned on.
'''
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print( bin(desired) )


'''
Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place.


a = 0b101 
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten 
desired = a ^ mask
Let’s say that I want to turn on the 10th bit from the right of the integer a.
Instead of writing out the entire number, we slide a bit over using the << operator.
We use 9 because we only need to slide the mask nine places over from the first bit to reach the tenth bit.


Define a function called flip_bit that takes the inputs (number, n).
Flip the nth bit (with the ones bit being the first bit) and store it in result.
Use the << operator to move your mask into place and the ^ operator to flip your desired bit.
'''
def flip_bit(number, n):
	bit_to_flip = 0b1 << (n -1)
	result = number ^ bit_to_flip
	return bin(result)