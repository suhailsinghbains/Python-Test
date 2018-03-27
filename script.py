#Find Class Average
students = [ alice, lloyd, tyler]
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}
def average(numbers):
  total = float(sum(numbers))
  total /= len(numbers)
  return total;
def get_average(Stu):
  homework = average(Stu["homework"])
  quizzes = average(Stu["quizzes"])
  tests = average(Stu["tests"])
  sum = (homework*10 + quizzes*30 + tests*60)/100.
  return sum
def get_letter_grade(score):
  if score>=90:
    return "A"
  elif score>=80:
    return "B"
  elif score>=70:
    return "C"
  elif score>=60:
    return "D"
  else:
    return "F"
def get_class_average(class_list):
  results = []
  for Stu in class_list:
    results.append(get_average(Stu))
  return average(results)
print get_class_average(students)
print get_letter_grade(get_class_average(students))
