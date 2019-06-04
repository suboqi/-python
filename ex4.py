#命名一个变量为car
cars = 100
#命名一个space_in_a_car
space_in_a_car = 4.0
#命名一个变量为drivers
drivers = 30
#命名一个变量位为passengers
passengers = 90
#命名一个车辆减去乘客的变量cars_not_driven 
cars_not_driven = cars -drivers
#命名一个cars_driven，汽车驱动
cars_driven = drivers
#命名一个carpool_capacity,拼车能力
carpool_capacity = cars_driven*space_in_a_car
#命名一个average_passage_per_car，平均数
average_assag_per_car = passengers / cars_driven
#
print("There are",cars,"cars available")
#
print("There are only",drivers,"drivers available")
#
print("There will be",cars_not_driven,"empty cars today")
#
print("We can tansport",carpool_capacity,"people today")
#
print("We have",passengers,"to carpool today")
#
print("We need to put about",average_assag_per_car,"in each car")
