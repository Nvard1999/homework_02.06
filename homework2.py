# Suppose you have a 5 × 5 list that consists of zeros and M’s. Write a program that creates a new 5 × 5 list that has M’s in the same place, but the zeroes are replaced by counts of how many M’s are in adjacent cells (adjacent either horizontally, vertically, or diagonally). An example is shown below. [Hint: short-circuiting may be helpful for avoiding index-out-of-range errors.]


# lst = [
# 	[0,'M',0,0,'M'],
# 	['M',0,'M',0,'M'],
# 	[0,0,'M',0,'M'],
# 	['M','M',0,'M',0],
# 	['M',0,0,'M',0]
# ]
# new_lst = [[0]*len(lst[0])for _ in range(len(lst))]
# count_lst = []
# for i in lst:
# 	count = 0
# 	for j in i:
# 		if j == 'M':
# 			count += 1
# 	count_lst.append(count)
# for i in range(len(lst)):
# 	for j in range(len(lst[0])):
# 		if lst[i][j] == 'M':
# 			new_lst[i][j] = 'M'
# 		else:
# 			new_lst[i][j] = count_lst[i]
# for i in new_lst:
# 	print(i)





# Write a program that rotates a matrix by 180 degrees.


# def rotate_180(matrix):
# 	rows = len(matrix)
# 	columns = len(matrix[0])
# 	rotated_matrix = [[0] * columns for _ in range(rows)]
# 	for i in range(rows):
# 		for j in range(columns):
# 			rotated_matrix[rows - i - 1][columns - j - 1] = matrix[i][j]
# 	return rotated_matrix
# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12],
#           [13,14,15,16]]
# rotated_matrix = rotate_180(matrix)
# for row in rotated_matrix:
# 	print(row)





# Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm, and asks them how many hours into the future they want to go. Print out what the hour will be that many hours into the future, printing am or pm as appropriate. An example is shown below.



def calculate_future_hour():
	hour = int(input("Enter the current hour between 1 and 12: "))
	period = input("Enter am or pm: ").lower()
	hours_into_future = int(input("Enter the number of hours into the future: "))
	if period == 'pm':
		hour += 12
	future_hour = (hour + hours_into_future) % 24
	if future_hour == 0:
		future_hour = 12
		period = 'am'
	elif future_hour < 12:
		period = 'am'
	elif future_hour == 12:
		period = 'am'
	else:
		future_hour -= 12
		period = 'pm'
	print(f"The hour {hours_into_future} hours into future will be {future_hour}:00 {period}.")
calculate_future_hour()