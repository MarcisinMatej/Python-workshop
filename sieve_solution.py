"""
In this excercise we will create very important tool for every hacker
and IT security person in the world. A script for finding prime numbers.
For this we will use so called sieve of Erasthotenes. 
"""

# Firstly create limit for our numbers
prime_limit = 1123

# we will need two arrays
# list of prime candidates 
# +1 becasue range exludes the last elements
prime_candidates = range(1,prime_limit + 1)

# flags where we will remember if the number is prime

prime_flags = [True]*prime_limit

# 1 is not considered prime by default
prime_flags[0] = False
# now compute max divisor
import math
max_divisor = math.ceil(math.sqrt(prime_limit))

# iterate over all candidate divisor 
for divisor in range(2, max_divisor + 1):
# iterate over all candidates and flag if the candidate is prime or not
	for candidate in prime_candidates:
			# check is our candite is still aviable
			# -1 becasue arrays are indexed from 0 not from 1
			# and our numbers are starting from 1
			if prime_flags[candidate-1]:
				# flag out candidate is it is divisible by divisor
				if candidate % divisor == 0 and candidate != divisor:
					prime_flags[candidate-1] = False

# print only candidates which are prime
pp = []
for candidate in prime_candidates:
	if prime_flags[candidate-1]:
		print(candidate)
		pp.append(candidate)

real_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123]

print(pp==real_primes)
