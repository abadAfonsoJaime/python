'''
The program should do the following:

    Prompt the user for the type of conversion they want
    Ask the user to input the RGB or Hex value
    Use Bitwise operators and shifting in order to convert the value
    Print the converted value to the user

'''

def rgb_hex():

	invalid_msg = "Invalid RGB value"

	red = int( input("Enter red (R) value: ") )
	if (red < 0 or red > 255):
		print(invalid_msg)
		return
	
	green = int( input("Enter green (G) value: ") )
	if (green < 0 or green > 255):
		print(invalid_msg)
		return

	blue = int( input("Enter blue (B) value: ") )
	if (blue < 0 or blue > 255):
		print(invalid_msg)
		return

	# the sum of shifting red to left by 16 bits, shifting green to left by 8 bits, and blue.
	val = (red << 16) + (green << 8) + blue
	'''
	A hexadecimal number can be represented with 3 bytes, a byte for each part of R, G, and B. 
	A byte is composed of two nibbles (4 bit numbers). 
	Hexadecimal numbers have 6 characters and each nibble represents a hex character.
	Shifting red to the left by 16 bits will insert 16 bits that will hold the place of green 
	(shifted 8 bits to the left) and blue (no shift).
	'''
	print( "%s" % (hex(val)[2:]).upper() )
	# This method will convert an RGB value to a hex value.


def hex_rgb():

	hex_val = input("Enter the color (six hexadecimal digits): ")
	if len(hex_val) != 6:
		print("Invalid hexidecimal value. Try again.")
		return
	else:
		hex_val = int(hex_val, 16)

	two_hex_digits = 2**8

	blue = hex_val % two_hex_digits
	hex_val = hex_val >> 8
	# shift hex_val to the right by 8 bits.
	green = hex_val % two_hex_digits
	hex_val = hex_val >> 8

	red = hex_val % two_hex_digits
	hex_val = hex_val >> 8

	print("Red: %s Green: %s Blue: %s" % (red, green, blue) )


def convert():
	while True:
		option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")

		if option == "1":
			print("RGB to Hex..")
			rgb_hex()
		elif option == "2":
			print("Hex to RGB..")
			hex_rgb()
		elif (option == "X" or option == "x"):
			break
		else:
			print("Error")


convert()