# a = 1,2,3,4,7,5
# m = max(a)
# idx = a.index(m)
# print(a[:idx] + (None,) + a[idx + 1]) 

class Circle:
  pi = 3.14
  def __init__(self, radius):
    self.radius = radius

  def cr(self):
    return 2 * Circle.pi * self.radius
  


c = Circle(1)
c.pi = 4
c = Circle(1)


print(c.cr())
