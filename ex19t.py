
def boystudent_and_girlstudent(boystudent_count,grilstudent_count):
	print ("I have %d boy students." % boystudent_count)
	print ("I have %d gril students." % grilstudent_count)
	print ("We are family!")
	print ("Time flies by,friendship lives on.\n")
 
print ("CASE 1:")
boystudent_and_girlstudent(11,11)
 
print ("CASE 2:")
part_one = 22
part_two = 22
boystudent_and_girlstudent(part_one , part_two)
 
print ("CASE 3:")
part_one = 33
boystudent_and_girlstudent(part_one, 33)
 
print ("CASE 4:")
part_two = 44
boystudent_and_girlstudent(44,part_two)
 
print ("CASE 5:")
boystudent_and_girlstudent(22+33,22+33)
 
print ("CASE 6:")
part_one = 22
part_two = 22
boystudent_and_girlstudent(part_one + 44, part_two + 44)
 
print ("CASE 7:")
part_one = int(input(">>>>>part_one:"))
part_two = int(input(">>>>>part_two:"))
boystudent_and_girlstudent(part_one , part_two)
 
print ("CASE 8:")
all_student = int(input(">>>>>all_student:"))
boystudent_count = 88
boystudent_and_girlstudent(boystudent_count , all_student - boystudent_count)
 
print ("CASE 9:")
part_one = 198 - int(input(">>>>>part_one:"))
part_two = 198 - int(input(">>>>>part_two:"))
boystudent_and_girlstudent(part_one , part_two)
 
print ("CASE 10:")
part_one = int(input(">>>>>part_one:"))
part_two = int(input(">>>>>part_two:"))
boystudent_and_girlstudent(part_one + int(input(">>>>>50:")), part_two + int(input(">>>>>50:")))
 
