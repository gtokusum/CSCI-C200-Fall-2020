import pygame
import random as rn
from Shape import Shape


from Others import Triangle 
from Others import Rectangle 
from Others import Circle 
from Others import Pentagon 
from Others import Square 


def get_random_color():
    return (rn.randint(0, 255), rn.randint(0, 255), rn.randint(0, 255))

pygame.init()
GAME_SIZE = (500,500)
GAME_DISPLAY = pygame.display.set_mode(GAME_SIZE)
CLOCK = pygame.time.Clock()


shape1 = Shape([(200,200),(250,250),(280,250),(300,200)],
                (123,32,234),
                GAME_DISPLAY)
shape2 = Shape([(100,100),(125,125),(150,100),(175,125),(200,100),(150,75)],
                (45,182,148),
                GAME_DISPLAY)

#### Triangle, Rectangle, Circle, Square, Pentagon instances
tri1 = Triangle([(10, 410), (16, 410), (13, 414)],
    get_random_color(), 
    GAME_DISPLAY)
tri2 = Triangle([(50, 50), (50, 110), (80, 10)],
    get_random_color(), 
    GAME_DISPLAY)

rect1 = Rectangle([(10,5), (50,5), (50,25), (10,25)], 
    get_random_color(), 
    GAME_DISPLAY)
rect2 = Rectangle([(250,350), (400,350), (400,450), (250,450)], 
    get_random_color(), 
    GAME_DISPLAY)

# center, outerPoint, color, display
circle1 = Circle((255, 255), (210, 255),
    get_random_color(),
    GAME_DISPLAY)
circle2 = Circle((420, 100), (400, 120),
    get_random_color(),
    GAME_DISPLAY)


pent1 = Pentagon([(26.8, 49.0), (60.9, 58.0), (80.0, 28.3), (57.6, 1.0), (24.8, 13.8)], 
    get_random_color(),
    GAME_DISPLAY)
pent2 = Pentagon([(86.8, 68.5), (59.7, 42.0), (76.6, 8.1), (114.0, 13.7), (120.3, 51.0)], 
    get_random_color(),
    GAME_DISPLAY)


sq1 = Square([(400,25), (450,25), (450,75), (400,75)], 
    get_random_color(), 
    GAME_DISPLAY)
sq2 = Square([(20,400), (40,400), (40,420), (20,420)], 
    get_random_color(), 
    GAME_DISPLAY)
####

shapeOrder = ["shape1", "shape2", "rect1", "rect2", "circle1", "circle2", "sq1", "sq2", "pent1", "pent2", "tri1", "tri2"]
allShapes = [shape1, shape2, rect1, rect2, circle1, circle2, sq1, sq2, pent1, pent2, tri1, tri2]
##### Example of a useful function:
# isinstance()

print("Showing off the function: isinstance\n")

headerRow = "{:>10} |" + "{:>8}" * (len(shapeOrder)) # From: https://www.educba.com/python-print-table/
print(headerRow.format("Class", *shapeOrder))
print("=" * len(headerRow.format("Class", *shapeOrder)))
print(headerRow.format("Shape", *[str(isinstance(s, Shape)) for s in allShapes]))
print(headerRow.format("Triangle", *[str(isinstance(s, Triangle)) for s in allShapes]))
print(headerRow.format("Rectangle", *[str(isinstance(s, Rectangle)) for s in allShapes]))
print(headerRow.format("Circle", *[str(isinstance(s, Circle)) for s in allShapes]))
print(headerRow.format("Pentagon", *[str(isinstance(s, Pentagon)) for s in allShapes]))
print(headerRow.format("Square", *[str(isinstance(s,Square)) for s in allShapes]))

print()
print()

print("Printing each shape:")
for s in allShapes:
    print("\t" + str(s))

print()
print()

while True:
    CLOCK.tick(60)
    GAME_DISPLAY.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    for s in allShapes:
        s.draw()
        s.move()
    
    
    pygame.display.update()
    