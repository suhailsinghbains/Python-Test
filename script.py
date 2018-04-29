#First Ever Class Under Construction
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def description(name,age):
  	print name,age
hippo = Animal("Jake", 12)
sloth = Animal("Yo" ,13)
ocelot = Animal("Yo1", 14)
print hippo.health
print sloth.health
print ocelot.health
