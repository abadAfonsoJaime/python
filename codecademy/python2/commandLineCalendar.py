from time import sleep, strftime, gmtime, localtime
'''
The user should be able to choose to:

    View the calendar
    Add an event to the calendar
    Update an existing event
    Delete an existing event

The program should behave in the following way:

    Print a welcome message to the user
    Prompt the user to view, add, update, or delete an event on the calendar
    Depending on the user’s input: view, add, update, or delete an event on the calendar
    The program should never terminate unless the user decides to exit

'''

USER_FIRST_NAME = "Jaime"

# Our calendar will store the dates as keys and the events as values.
calendar = {}

def welcome():
	print("Welcome " + USER_FIRST_NAME + ".")
	print( "Calendar starting..." )

# welcome()

sleep(1)

# https://docs.python.org/2/library/time.html#time.strftime
print(
	"Today is " + strftime("%A, %B %d %Y %H:%M:%S", localtime())
)

print( "What would you like to do?")


def start_calendar():
	welcome()
	start = True
	
	while start:
		user_choice = input("Please enter A to Add, U to Update, V to View, D to Delete, X to Exit: ").upper()

		if user_choice == "V":
			if len( calendar.keys() ) == 0:
				print( "The calendar is empty" )
			else:
				print(calendar)

		elif user_choice == "U":
			date = input("What date? ")
			update = input("Enter the update: ")
			calendar[date] = update
			'''
			This a very powerful (and possibly dangerous) line of code. 
			It blindly adds the update to the calendar, 
			without checking if the date is valid or if it already exists
			 (which could override things)'''
			print("Update successfully made")
			print(calendar)

		elif user_choice == "A":
			event = input("Enter event: ")
			date = input("Enter date (MM/DD/YYYY): ")
			# A date in the format MM/DD/YYYY contains 10 characters if you include the forward slashes.
			if (len(date) > 10 or int(date[6:]) < int( strftime("%Y") ) ):
				# Both years retrieved will be in the form of string,
				# but we need to compare integers, so convert both using int().
				print("Invalid date entered")
				try_again = input("Try Again? Y for Yes, N for No: ").upper()
				if try_again == "Y":
					continue
				else:
					start = False
			else:
				calendar[date] = event
				print("Event successfully added")
				print(calendar)

		elif user_choice == "D":
			if len( calendar.keys() ) == 0:
				print( "The calendar is empty" )
			else:
				event = input("What event? ")
				for date in calendar.keys():
					if event == calendar[date]:
						del calendar[date]
						#del(calendar[date])
						print("Event successfully deleted")
						print(calendar)
					else:
						print("Invalid Event entered")

		elif user_choice == "X":
			start = False

		else:
			print("Invalid command")
			start = False

start_calendar()

# $ python commandLineCalendar.py
