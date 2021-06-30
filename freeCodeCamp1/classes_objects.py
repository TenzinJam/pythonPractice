# with Class you can define a datatype you want to implement
#self is the js equivalent of "this"
# comma after each attributes should not be used
# is_on_probation property was deleted for future exercise
# so the syntax of inheritance is a little different from js, there is no "extends" equivalent keyword and no "super()" function we need to add. All we need to do is input the parent class into the parameters of the child class.
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


class Chef:
  def make_chicken(self):
    print("The check makes a chicken")
  def make_salad(self):
    print("The check makes a salad")
  def make_special_dish(self):
    print("The check makes bbq ribs")

class ChineseChef(Chef):
  def make_special_dish(self):
    print("The check makes orange chicken")
  def make_friend_rice(self):
    print("The check makes fried rice")

