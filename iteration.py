# Make a local change

# iteration pattern

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	for i in range(0, len(list)):
		list[i] += 1

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]

	return list

# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"


#accumlation pattern - a type of iteration 
#keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total	

def max(numbers):
	current_max = numbers[0]

	for n in numbers:
		if n > current_max:
			current_max = n

	
	return current_max			

