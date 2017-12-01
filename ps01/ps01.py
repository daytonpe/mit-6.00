from math import *

# Generate the 1000th prime number: 7919
# Note: in current iteration, n>=4

def nthPrime(number):

	n = 0; #n is incremented each time we find a prime number (know 1 and 2)

	for x in range(0,10000):
		
		if number == 1:
			print(2)
			break

		i = (x*2) + 1
		# print('**'+str(i)+'**');

		yMax = int((i/2)+1) #only really need to go up to the halfway point for checking
		primeMarker = True #default the prime marker to true

		for y in range(2, yMax):
			# print(' '+str(y)+' '+str(i%y))
			remain = i%y
			if remain == 0: #i.e. i is NOT prime
				# print(str(i)+' is NOT prime')
				primeMarker = False #if we find a devisor, it can't be prime
				break

		#If i IS prime
		if primeMarker == True :
			n = n+1
			if n==number :
				print(i)
			

def primeLogs(number):
	n = 1; #n is incremented each time we find a prime number (know 1 and 2)

	primeArray = [2]

	highPrime = 0;

	for x in range(1,10000):

		i = (x*2) + 1
		# print('**'+str(i)+'**');

		yMax = int((i/2)+1) #only really need to go up to the halfway point for checking
		primeMarker = True #default the prime marker to true

		for y in range(2, yMax):
			# print(' '+str(y)+' '+str(i%y))
			remain = i%y
			if remain == 0: #i.e. i is NOT prime
				# print(str(i)+' is NOT prime')
				primeMarker = False #if we find a devisor, it can't be prime
				break

		#If i IS prime
		if primeMarker == True :
			n = n+1
			primeArray.append(i)
			if n==number :
				highPrime = i
				break

	logSum = 0
	for j in primeArray :
		# print(str(log(j)) + '!')
		logSum = logSum + log(j)

	print('Sum of logs of primes: ' + str(logSum));
	print('Highest prime: ' + str(highPrime));
	print('Ratio: ' + str(logSum/highPrime));
	print('')
	# print(primeArray)


primeLogs(10)
primeLogs(100)
primeLogs(1000)

##RETURNS:
# Sum of logs of primes: 22.59039453011566
# Highest prime: 29
# Ratio: 0.7789791217281262

# Sum of logs of primes: 505.8162331260092
# Highest prime: 541
# Ratio: 0.9349653107689634

# Sum of logs of primes: 7812.283540732839
# Highest prime: 7919
# Ratio: 0.9865239980720848

# nthPrime(4)
# nthPrime(125)
# nthPrime(999)
# nthPrime(1000)