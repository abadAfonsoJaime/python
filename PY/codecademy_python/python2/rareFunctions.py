#from math import sqrt

def is_int(x):
    absoluteCount = abs(x)
    typeCount =type(x)
    roundCount = round(absoluteCount)
    if typeCount and absoluteCount - roundCount == 0:
        return True
    else:
        return False

def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
        #print(x)
    return total

def sumaDig(x):
	text = str(x)
	total = 0
	for d in text:
		total += int(d)
	return total

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
        print(x)
    return total


def is_prime( x ):
	if x < 2:
		return False
	elif x < 4:
		return True
	else:
		for n in range(2, x-1, 1):
			if x % n == 0:
				return False
			else:
				continue
	# Fuera del bucle
	return True

def reverse(text):
	length = len(text)
	array = []
		
	while length > 0:
		array.append( text[length-1] )
		length = length - 1
	
	result = "".join( map(str, array) )
	
	return result
	
'''
print(reverse("Jaime") )

foo = "example text"
print(foo[::-1])
'''

def anti_vowel(text):
	result=""
	vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
	for char in text:
		if char in vowels:
			continue
		else:
			result += char
	return result

# print( anti_vowel("Hello Matrix") )



def scrabble_score(word):
	score = {
		"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4,
		"i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1,
		"n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1,
		"w": 4, "v": 4, "y": 4, "x": 8, "z": 10
	}
	totalPoints = 0
	palabra = word.lower()
	for char in palabra:
		totalPoints += score[char]
	return totalPoints


#print( scrabble_score("python") )



def censor(text, word):

	asterisk = ""

	for x in word:
		asterisk += "*"

	result = text.replace(word, asterisk)
	
	return result
# print( censor("Hola Matrix, qué tal?", "Matrix") )

def count(sequence, item):
	result = 0
	for i in sequence:
		if i == item:
			result +=1
	return result

#print( count([1, 2, 1, 1], 1) )



def purify(lista):
	result = []
	for i in lista:
		if i % 2 == 0:
			result.append(i)
	return result

#print( purify([1, 2, 1, 1]) )



def product(listOfNumbers):
	result = 1
	for x in listOfNumbers:
		result *= x
	return result

#print( product([5,4]) )


def remove_duplicates(lista):
	result = []
	for x in lista:
		if result.count(x) == 0:
			result.append(x)

	return result

# print(remove_duplicates([1, 1, 2, 2]))



def middle(listOfNumbers):
	creciente = sorted(listOfNumbers)
	longitud = len(listOfNumbers)
	return listOfNumbers[longitud // 2]

#print( middle([7, 12, 3, 1, 6]) )

def media(listOfNumbers):
	longitud = len(listOfNumbers)
	total = 0
	for i in listOfNumbers:
		total += i
	return total/longitud

#print( media([4, 5, 5, 4]) )


def mierda(listOfNumbers):
	total = 0
	creciente = sorted(listOfNumbers)
	middle = len(listOfNumbers)//2
	if len(listOfNumbers) == 1:
		return listOfNumbers[0]
	elif len(listOfNumbers) % 2 == 0:
		for i in listOfNumbers:			
			total += i
		return total/len(listOfNumbers)
	else:
		return (listOfNumbers[middle+1] + listOfNumbers[middle-1] )/ 2

#print(mierda([4, 5, 5, 4]))

def mierdaCodeCademy(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean


#########################################################################
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for e in scores:
    total += e
  return total

#print(grades_sum(grades))

def grades_average(grades_input):
  total = grades_sum(grades_input)
  average = total/(len(grades_input))
  return average

#print(grades_average(grades))


def grades_variance(scores):
	average = grades_average(scores)
	variance = 0
	for i in scores:
		variance += (average - i)**2

	return variance/len(scores)

'''
The standard deviation is the square root of the variance.
You can calculate the square root by raising the number to the one-half power.
'''
def grades_std_deviation(variance):
	return grades_variance(variance) ** 0.5

print( grades_std_deviation(grades) )