# Maths Stuff using Students of a class
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print (grade)

def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  return sum_of_grades/len(grades_input)

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)
def grades_std_deviation(variance):
  return variance**0.5

#Print all Stuff
for item in grades:
  print (item)
print (grades_sum(grades))
print (grades_average(grades))
variance = grades_variance(grades)
print (variance)
print (grades_std_deviation(variance))
