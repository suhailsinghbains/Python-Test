#Insert Square into a new List
start_list = [5, 3, 1, 2, 4]
square_list = []

start_list.sort()
for number in start_list:
  square_list.append(number**2)


print square_list
