#New Class Car
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
  def display_car(self):
    x = "This is a "+ self.color +" "+ self.model +" with "+ str(self.mpg) +" MPG."
    return x
  def drive_car(self):
    self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

print my_car.model
print my_car.color
print my_car.mpg
print my_car.condition
my_car.drive_car()
print my_car.condition
