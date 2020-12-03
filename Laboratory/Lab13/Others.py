from Shape import Shape
import math
import random as rn
import pygame


class Triangle(Shape):
    def __init__(self, points, color, display):
        """
        points = [ p1, p2, p3 ]
        p1 = left
        p2 = right
        p3 = top

        assume this is an equilateral triangle
        """
        super().__init__(points, color, display)
        # TODO_TOGETHER: Part A
        self.base = self.get_base()
        self.height = self.get_height()


    def get_area(self):
        '''
        Return the area of the triangle
        '''
        # TODO_TOGETHER: Part B
        return self.base * self.height * .5

    def get_perimeter(self):
        """
        
        """
        # TODO_TOGETHER: Part C
        a = math.sqrt(math.pow(p1[0] - p3[0], 2) + math.pow(p1[1] - p3[1], 2))
        b = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))
        c = math.sqrt(math.pow(p2[0] - p3[0], 2) + math.pow(p2[1] - p3[1], 2))
        return a + b + c # maybe take this out
        
    def get_base(self):
        """

        """
        # TODO_TOGETHER: Part D
        p1 = self.points[0]
        p2 = self.points[1]
        return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

    def get_height(self):
        """
        
        """
        # TODO_TOGETHER: Part E
        p1 = self.points[0]  # maybe take this out\ refer to return and then ask what p1 and p3 should be
        p3 = self.points[2]  # maybe take this out/ taking this out could be a good idea because they were exposted to this ins get_base      
        return math.sqrt(math.pow(p1[0] - p3[0], 2) + math.pow(p1[1] - p3[1], 2)) * math.sin(math.radians(60))


    def __str__(self):
        # TODO_TALK: Part F
        return super().__str__() + " Triangle: base=" + str(self.base) + " height=" + str(self.height)



class Rectangle(Shape):
    def __init__(self, points, color, display):
        """
        points = [p1, p2, p3, p4]
        p1 = top left
        p2 = top right
        p3 = bottom right
        p4 = bottom left 
        """
        super().__init__(points, color, display)
        # TODO_SECTION: Part A
    
        self.length = self.get_length()
        self.width = self.get_width()


    def get_area(self):
        '''
        Return the area of a rectanlge
        '''
        # TODO_SECTION: Part B
        return self.length * self.width


    def get_perimeter(self):
        '''
        Return the perimeter of a rectangle
        '''
        # TODO_SECTION: Part C
        return self.length*2 + self.width*2

    
    def get_length(self):
        '''
        Get the length of the rectangle
        Hint:  the Y values of the bottom and top left points
        '''
        # TODO_SECTION: Part D
        p1,p2,p3,p4 = self.points
        return p3[1]- p1[1]

    def get_width(self):
        '''
        Get the width of the rectangle
        Hint: subtract the X values of the top left and right points
        '''
        # TODO_SECTION: Part E
        p1,p2,p3,p4 = self.points
        return p2[0] - p1[0]

    def __str__(self):
        # return "" # After complete above functions, delete this line, and un-comment line below
        return super().__str__() + " Rectangle: length=" + str(self.length) + " width=" + str(self.width)

    # Overridden method
    def draw(self):
        """
        Function draws a rectangle on a pygame window
        
        NOTE: An example of overriding: you don't call super()
        
        NOTE: DO NOT MODIFY this function, except to
            uncomment the single line.
        """
        # TODO: Uncomment this once you complete the above code.
        pygame.draw.rect(self.display, self.color, pygame.Rect(self.points[0][0], self.points[0][1], self.get_width(), self.get_length()))
        

class Circle(Shape):
    def __init__(self, center, outerPoint, color, display):
        """

        """
        super().__init__([center], color, display)
        # TODO_SECTION: Part F
        self.center = center 
        self.outer = outerPoint
        self.radius = self.get_radius(self.center,self.outer)
        self.perimeter = self.get_perimeter()
        
    def get_radius(self, center, outer):
        '''
        Hint: Use the distance formula
        '''
        # TODO_SECTION: Part G
        return math.sqrt((center[1]-outer[1])+(center[0]-outer[0])**2)
        
    def get_area(self):
        '''
        Find the area of a circle
        '''
        # TODO_SECTION: Part H
        return math.pi * self.radius** 2
        
    def get_perimeter(self):
        '''
        Find the perimeter of a circle
        '''
        # TODO_SECTION: Part I
        return math.pi * 2 * self.radius
        

    # Overridden Method
    def draw(self):
        """
        Function draws a rectangle in the pygame window

        NOTE: An example of overriding: you don't call super()

        NOTE: DO NOT MODIFY this function, except to
            uncomment the single line.
        """
        # TODO: Uncomment this once you complete above code.
        pygame.draw.circle(self.display, self.color, self.points[0], self.radius)

    def __str__(self):
        # return "" # After complete above functions, delete this line, and un-comment line below
        return super().__str__() + " Circle, center=" + str(self.points[0]) + " width=" + str(self.radius)


class Pentagon(Shape):
    def __init__(self, points, color, display):
        super().__init__(points, color, display)
        self.side_length = self.get_side_length()

    def get_area(self):
        x = (5 + 2) * math.sqrt(5)
        s = (1/4) * math.sqrt(5*x) 
        return s * (self.side_length**2)

    def get_perimeter(self):
        return 5 * self.side_length

    def get_side_length(self):
        p1, p2, p3, p4, p5 = self.points

        x1, y1 = p1
        x2, y2 = p2

        # use the distance forumla to find the length between 
        # any two consecutive points in a pentagon
        x_values = (x2 - x1)**2
        y_values = (y2 - y1)**2
        
        return math.sqrt(x_values + y_values)

    def __str__(self):
        return super().__str__() + " Pentagon, sidelength=" + str(self.side_length)
    
    """
    Why isn't there a draw method?
    """


class Square(Rectangle):
    """
    This is independent work at the end of the lab
    """

    def __init__(self, points, color, display):
        '''
        points = [p1, p2, p3, p4]
        p1 = top left
        p2 = top right
        p3 = bottom right
        p4 = bottom left 
        '''
        # Consider this line carefully:  What is Square inheriting from?
        super().__init__(points, color, display)
        
        # TODO: finish the rest
      
        self.side_length = self.get_side_length()

    def get_area(self):
        '''
        TODO: Find the area of a square
        '''
        p1,p2,p3,p4 = self.points
        return self.side_length**2

    def get_perimeter(self):
        '''
        TODO: Find the perimeter of a square
        '''
        p1,p2,p3,p4 = self.points
        return self.side_length * 4

    def get_side_length(self):
        """
        TODO: Get the length of any side
        """
        p1,p2,p3,p4 = self.points
        return math.sqrt((p1[1]-p3[1])**2 + (p1[0]-p3[0])**2)

    def draw(self):
        """
        TODO: We want you to implement this 

        HINT: This is one line and it includes `super()` 

        This function is explicitly calling from the superclass.
        """
        super().draw()


    def __str__(self):
        # return "" # After complete above functions, delete this line, and un-comment line below
        return super().__str__() + " Square, side length=" + str(self.side_length)

        