
#Using 6, 9, and 20 as possibilities for buying.
#Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets

#Greedy Algorithm DOESN'T work!
def problem1greedy(number):
	
	total = 0

	arr = [20,9,6] #must be in order

	for i in arr :
		j = 0
		while (total+i) < number :
			total = total + i
			j=j+1
		print(str(j)+' x '+str(i))

	print('Closest Greedy Total: '+str(total))

# problem1greedy(50)

#Exhaustive Algorithm works!
def exhaustiveSearch(number):
	for a in range(0,40):
		for b in range(0,40):
			for c in range(0,40):
				n = (6*a)+(9*b)+(c*20)
				if n == number:
					print(str(number)+' = '+'6*'+str(a)+' + 9*'+str(b)+' + 20*'+str(c))
					return
	print(str(number)+' cannot be made.')
	return

# for i in range(1,100):
# 	exhaustiveSearch(i)	

#Problem 4: Choose the sizes of your possible nugget orders (tup)
#tuple must be 3 in length
def tupleChoice(tup, number):
	for a in range(0,25):
		for b in range(0,25):
			for c in range(0,25):
				n = (tup[0]*a)+(tup[1]*b)+(tup[2]*c)
				if n == number:
					print(str(number)+' = '+'6*'+str(a)+' + 9*'+str(b)+' + 20*'+str(c))
					return
	print(str(number)+' cannot be made.')
	return

for i in range(1,100):
 	tupleChoice([8,2,17], i)




# ###
# ### template of code for Problem 4 of Problem Set 2, Fall 2008
# ###

# bestSoFar = 0     # variable that keeps track of largest number
#                   # of McNuggets that cannot be bought in exact quantity
# packages = (6,9,20)   # variable that contains package sizes

# for n in range(1, 150):   # only search for solutions up to size 150
#     ## complete code here to find largest size that cannot be bought
#     ## when done, your answer should be bound to bestSoFar
