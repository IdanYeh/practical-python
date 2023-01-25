# bounce.py
#
# Exercise 1.5

starting_height = 100; 
bounce_reduction_ratio = 3/5;
curr_height = starting_height;
for i in range(10):
	curr_height = curr_height*bounce_reduction_ratio;	
	print(round(curr_height,ndigits = 4))