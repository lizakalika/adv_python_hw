class Point(object):
    
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        
    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def setX(self,new_x):
        self.X = new_x
        
    def setY(self,new_y):
        self.Y = new_y
        
    def distance(self, another_Point):
        return np.sqrt((self.getX() - another_Point.getX())**2 + (self.getY() - another_Point.getY())**2)
    
    def cos(self, another_Point1, another_Point2):
        a = self.distance(another_Point1)
        b = self.distance(another_Point2)
        c = another_Point1.distance(another_Point2)
        return (a**2 + b**2 - c**2) / (2 * a * b)
