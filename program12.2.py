class shape:
    def __init__(self,color):
        self.color=color
    def area(self):
        pass
class circle(shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius=radius
        def area(self):
            return 3.14*self.radius**2
class rectangle(shape):
     def __init__(self,color,width,height):
         super().__init__(color)
         self.width=width
         self.height=height
     def area(self):
        return self.width*self.height
circle=circle("red",5)
rectangle=rectangle("blue",4,6)
print("circle area:",circle.area())
print("rectangle area:",rectangle.area())
        
