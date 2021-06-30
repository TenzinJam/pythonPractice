# with Class you can define a datatype you want to implement
#self is the js equivalent of "this"
# comma after each attributes should not be used
# is_on_probation property was deleted for future exercise

class Student:

  def __init__(self, name, major, gpa):
    self.name = name
    self.major = major
    self.gpa = gpa

  def on_honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False


