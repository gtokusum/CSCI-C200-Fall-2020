import pygame
import random as rn

class Shape(object):

    def __init__(self,points,color,display):
        """
        - points should be a list of points
        - color should be a tuple in RBG format
        """
        self.points = points
        self.color = color
        self.display = display

        self.x_direction = 1
        self.y_direction = 1
        
    def draw(self):
        """
        - draw method will display the shape on the canvas
        - given class attributes draw a generic polygon
        - you shouldn't need to edit this much for the subclasses
        """
        pygame.draw.polygon(self.display, self.color, self.points)
    
    def set_color(self,newColor):
        self.color = newColor

    def get_color(self):
        return self.color

    def get_perimeter(self):
        """
        Find the distance between subsequent points 
        HINT: Find the sum distances between subsequent points
        ie distance between point 1,2 + p2,p3 + ... p(n-1),pn + pn,p1
        """
        total = 0
        def help_distance(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            return ( (x1-x2)**2 + (y1-y2)**2) ** (1/2)
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[i+1]
            total += help_distance(p1,p2)
        return total + help_distance(self.points[0],self.points[-1])


    def __str__(self):
        return "Shape Object ->"

    def move(self):
        # left, right, top = self.points
        shape_smallest_x = min([i[0] for i in self.points])
        shape_smallest_y = min([i[1] for i in self.points])
        shape_largest_x = max([i[0] for i in self.points])
        shape_largest_y = max([i[1] for i in self.points])

        # # first get bounds to check if points are hitting the edge
        max_w, max_h = self.display.get_size()

        # Will bounce if the shape hits one of the edges
        if shape_largest_x >= max_w or shape_smallest_x <= 0:
            self.x_direction = -int(self.x_direction / abs(self.x_direction)) * rn.randint(1, 5)

        if shape_largest_y >= max_h or shape_smallest_y <= 0:
            self.y_direction = -int(self.y_direction / abs(self.y_direction)) * rn.randint(1, 5)

        new_points = []
        for i in self.points:
            x = i[0] + self.x_direction
            y = i[1] + self.y_direction

            new_points.append((x,y))

        self.points = new_points