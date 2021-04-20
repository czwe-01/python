print("hello world!")
message = "hello python world!"
print(message)
print(message.title())
print(message.upper())
print(message.lower())
name= "thulasizwe"
surname= "nkambule " 
fullname= name + " " + surname
print(fullname.rstrip())

print("\n")

friends=["Sizwe","Zee","Boitumelo","Sinethemba","Oreo","Gugu","Promise"]
print(friends)
friends.sort()
print(friends)
friends[3]="Kwanele" 
print(friends)
friends.append("Promise")  #adding an item at the lastposition in the list
print(friends)
friends.insert(1,"Tha") #adding an item in certain position
print(friends)
del friends[-1] #deleting the last item in the list.
print(friends)
popped_friend= friends.pop()  #removes and displays the last item in the list. inserting a number in the parenthesis will pop the item in that position.
print(popped_friend)
print(friends)
friends.remove("Sizwe")			#Remove by value
print(friends)

print("\n")

alphabet=['A','B','C','F','J','D','Z','U','T','S']
alphabet.sort() 				#Permanently sort a list.
print(alphabet)
alphabet.sort(reverse=True)		#Permanently sort a list in reverse order
print(alphabet)
print(sorted(alphabet))			#Temporarily sort a list.
alphabets=['A','B','C','F','J','D','Z','U','T','S']
print(alphabets)
alphabets.reverse() 			#Reverses the order of the list. First item becomes the last and last item becomes the first.
print(alphabets)
print(len(alphabets))			#len finds the length of the list. Number of items in the list.

print("\n")

#WORKING WITH LISTS

for alpha in alphabet:			#for loops that will print all the items in the list
	print(alpha)

print("\n")

for friend in friends:
	print("Thank you " + friend.title() + " for being my friend")
	
print("\n")
	
#Working with list of numbers
number=list(range(1,9))
print(number)

even_nums= list(range(2,17,2))	#the range() function starts with the value 2 and then
								#adds 2 to that value.
print(even_nums)
odd_nums= list(range(1,16,2))
print(odd_nums)


squares=[]
for value in range(1,11):		#This for loop will add items to our list
	square=value**2				#Two asterisks represent exponent
	squares.append(square)
print(squares)	

Squares=[]
for value in range(10,21):		#Short way
	Squares.append(value**2)
print(Squares)


squared_num = [value**2 for value in range(1,11)]		#uses a list comprehension.
print(squares)

print("\n")
#SIMPLE STATISTICS WITH A LIST OF NUMBERS
digits=list(range(0,11))
print(digits)
print(min(digits))				#Displays the smallest number in the list
print(max(digits))				#Displays the largest number in the list
print(sum(digits))				#Displays the sum of all the numbers in the list

print("\n")
#SLICING 
print(friends)
print(friends[2:4])				#prints friends on the specified index.
print(friends[:3])				#Omiting the first number will tell the print function to start at the beginning of the list
print(friends[4:])				#Omiting the second number will tell the print to from the index given to the end of the list
print(friends[-3:])				#prints the last 3 friends in the list

print(friends)

print("\nHere are the first 3 friends in the list")
friends.append("Andile")
friends.insert(1,"Oregaugetse")
for frnd in friends[:3]:		#Using a loop to print from a list.
	print("\t"+frnd.upper())


#COPYING A LIST
best_friends= friends[:3]
print(best_friends)

print("\n")

#TUPLE:Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
#Parenthesis are used instead of square brackets in a tuple

IDs=(321,423,342,345,643,326,543,247,899)
print(IDs)
print(IDs[3])
for id in IDs:
	print(id)
	
IDs=(12,54,67,77,45)			#This won't give an error because python alolows overwriting variables 
print(IDs)	
print("\n")
#If STATEMENTS
cars=["volvo","toyota", "bmw","audi","subaru"]
for car in cars:
	if car=="bmw":
		print(car.upper())
	else:
		print(car.title())

print("\n")
#Avoiding case when checking for equality
motor="Bmw"
if motor.lower() == "bmw":
	print("true")
else:
		print("false")


print("\n")

#CHECKING WHETHER A VALUE IS NOT IN A LIST
besties=["Ore","Zee",'Sne','Gugu']
friend="Pro"
if friend not in besties:
	print(friend.title()+", is not a besties.")
	print
	
	
print("\n")
#MULTIPLE IF STATEMENTS
for buddy in besties:
	print(buddy+" is my bestie.")
print("Those are all your besties")	

print("\n")

#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")			

print("\n")

#A SIMPLE DICTIONARY
bmw_1={'brand':'bmw','model':'M5 perfomance','year':2019}
bmw_2={'brand':'bmw','model':'M8 grand coupé','year':2020}
bmw_3={'brand':'bmw','model':'M2 competition','year':2019}

print(bmw_1['brand'].upper())
print(bmw_1['model'].title())
print(bmw_2['model'].title())
print(bmw_3['brand'].title())

#ADDING TO DICTIONARY
bmw_1['color']= 'yellow'
bmw_2['color']= "vanta black"
bmw_3['color']= 'red'

print("The " + bmw_2['brand'].upper()+" " + bmw_2['model'].title()  + " was made in " + str(bmw_2['year']) + " it is " + bmw_2['color'] + " in colour")
#REMOVING KEY VALUES
del bmw_1['color']
print(bmw_1)

print("\n")
#LOOPING THROUGH ALL KEY-VALUE PAIRS
for k, v in bmw_1.items():
	print(str(k) + "\t: "+ str(v))
print("\n")	
for k, v in bmw_2.items():
	print(str(k) + "\t: "+ str(v))
print("\n")	
for k, v in bmw_3.items():
	print(str(k) + "\t: "+ str(v))
print("\n")	

#READDING THE REMOVED ATTRIBUTE
bmw_1['color']= 'yellow'
#NESTING DICTIONARIES
bmws = [bmw_1,bmw_2,bmw_3]

for bmw in bmws:
	print(bmw)

