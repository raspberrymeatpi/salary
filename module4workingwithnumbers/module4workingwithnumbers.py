area = 0
height = 10
width = 20

#calculate the area of a triangle
area = width*height /2

#printing formatted float value with 2 decimal places
print ("The area of the triangle would be %.2f" % area)

#printing the formatted number with right justified to take up 6 spaces
#with leading zeros
print("My favourite number is %06d !" % 42)

#do the same thing with the .format syntax to include numbers our output
print("the area of the triangle would be {0:f} ".format(area))
print("my favourite number is {0:d} ".format (42))

#this is an example with multiple numbers
#I have added a \ to indicate the command continues onto the following line
print("Here are three numbers! " + \
    "The first is {0:d} The second is {1:4d} and {2:d}".format(7,8,9))








#print("I have %d cats" %6) #I have 6 cats
#print("I have %3d cats" %6) #I have 6 cats
#print("I have %03d cats" %6) #I have 006 cats
#print("I have %f cats" %6) #I have 6.000000 cats
#print("I have %.2f cats" %6) #I have 6.00 cats


#print("I have {0:d} cats".format (6)) #I have 6 cats
#print("I have {0:3d} cats".format (6)) #I have 6 cats
#print("I have {0:03d} cats".format (6)) #I have 006 cats
#print("I have {0:f} cats".format (6)) #I have 6.000000 cats
#print("I have {0:.2f} cats".format (6)) #I have 6.00 cats

