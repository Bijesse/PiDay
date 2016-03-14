
#Archimedes Method for Approximating Pi
# reference: http://m.youtube.com/watch?v=_rJdkhlWZVQ


#import a Python library to do some math
import math

#set the number of sides of the inner polygon
#must be a multiple of 6
numsides = 30

sidelength = 1
pi = 0
count = 6

while count <= numsides: 

	a_length = math.sqrt(1-math.pow(sidelength/2.0, 2))
	b_length = 1-a_length

	new_sidelength = math.sqrt(math.pow(b_length,2) + math.pow(sidelength/2.0, 2))

	#calculate the perimeter of the polygon
	perimeter = numsides * sidelength

	#update the sidelength and our counter
	sidelength = new_sidelength
	count = count * 2

	#calculate pi by dividing the perimeter of the polygon by 2
	pi = perimeter / 2.0

print pi
