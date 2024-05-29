class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, other):
        return Vector(self.x + other.x, 
                      self.y + other.y)
        
    def add(self, factor):
        return Vector(self.x * factor, 
                      self.y * factor)
        
    def dot(self, other):
        return self.x * other.x + \
               self.y * other.y
               
    def norm(self):
        return (self.x * self.x +
                self.y * self.y) ** 0.5 