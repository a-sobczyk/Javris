import random

import pygame_menu.events
from pygame_menu.examples import create_example_window

import pygame, sys
from pygame import *
from Point import Point

def Left_index(points):
    '''
    Finding the left most point
    '''
    minn = 0
    for i in range(1, len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn


def orientation(p, q, r):
    '''
    To find orientation of ordered triplet (p, q, r).
    The function returns following values
    0 --> p, q and r are collinear
    1 --> Clockwise
    2 --> Counterclockwise
    '''
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    if val == 0:
        print("punkty leza na prostej")
        return 0
    elif val > 0:
        print("punkty sa prawoskrentne")
        return 1
    else:
        print("punkty sa lewoskretne")
        return 2


def convexHull(points, n):
    # There must be at least 3 points
    if n < 3:
        return

    # Find the leftmost point
    l = Left_index(points)

    hull = []

    '''
    Start from leftmost point, keep moving counterclockwise
    until reach the start point again. This loop runs O(h)
    times where h is number of points in result or output.
    '''
    p = l
    q = 0
    while (True):

        # Add current point to result
        hull.append(p)

        '''
        Search for a point 'q' such that orientation(p, q,
        x) is counterclockwise for all points 'x'. The idea
        is to keep track of last visited most counterclock-
        wise point in q. If any point 'i' is more counterclock-
        wise than q, then update q.
        '''
        q = (p + 1) % n

        for i in range(n):

            # If i is more counterclockwise
            # than current q, then update q
            if (orientation(points[p],
                            points[i], points[q]) == 2):
                q = i

        '''
        Now q is the most counterclockwise with respect to p
        Set p as q for next iteration, so that q is added to
        result 'hull'
        '''
        p = q

        # While we don't come to first point
        if (p == l):
            break

    # Print Result
    for each in hull:
        print(points[each].x, points[each].y)
        eadgePoints.append(Point(points[each].x, points[each].y))

    return eadgePoints


# Driver Code
points = []
eadgePoints = []
centerPoint = Point(640, 400)

convexHull(points, len(points))

WIDTH = 1280
HEIGHT = 800
WHITE = (255, 255, 255)  # RGB
BLACK = (0, 0, 0)  # RGB
win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), 0, 32)
display.set_caption("PAKOWANIE PREZENTU")
screen.fill(BLACK)
timer = pygame.time.Clock()
# pos_on_screen, radius = (50, 50), 20

def start():
    temp = 0
    firstPoint = 0
    counter = 0

    if (len(points) == 1):
        pygame.draw.circle(win, "Red", (points[0].x, points[0].y), 4)
    if (len(points) == 2):
        pygame.draw.circle(win, "Red", (points[0].x, points[0].y), 4)
        pygame.draw.circle(win, "Red", (points[1].x, points[1].y), 4)
        pygame.draw.line(win, "Red", (points[0].x, points[0].y), (points[1].x, points[1].y), 2)
    if(len(points) >= 3):
        for n in points:
            pygame.draw.circle(win, "White", (n.x, n.y), 4)
        for n in eadgePoints:
            pygame.draw.circle(win, "Red", (n.x, n.y), 4)
            if(temp == 0):
                temp = n
                firstPoint = n
            else:
                pygame.draw.line(win, "Red", (temp.x, temp.y), (n.x, n.y), 2)
                counter += 1
                temp = n
        pygame.draw.line(win, "Red", (n.x, n.y), (firstPoint.x, firstPoint.y), 2)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        timer.tick(60)  # 60 times per second you can do the math for 17 ms
        display.update()


def prepRandomData(value = 10):
    for x in range(value):
        points.append(Point(random.randrange(0,1280, 1), random.randrange(0, 800, 1)))

def liczbaPunktow():
    global ilePunktow
    prepRandomData(int(ilePunktow.get_value()))
    randomStart()

def randomStart() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    Left_index(points)
    convexHull(points, len(points))
    # connetctPoints()
    menu.disable()
    timer.tick(60)
    surface.fill((0, 0, 0))
    pygame.display.update()
    start()

def fileStart():
    readFile()
    Left_index(points)
    convexHull(points, len(points))
    # connetctPoints()
    menu.disable()
    timer.tick(60)
    surface.fill((0, 0, 0))
    pygame.display.update()
    start()

menu = pygame_menu.Menu(
    position=(0, 0, False),
    height=800,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Algorytm Jarvisa',
    width=1240
)

about = pygame_menu.Menu(
    position=(0, 0, False),
    height=800,
    theme=pygame_menu.themes.THEME_BLUE,
    title='O nas',
    width=1240
)
about.add.label("Program do rysowania algorytmu ")
about.add.label("Pakowanie prezentu napisali:")
about.add.label("")
about.add.label("Andrzej Sobczyk")
about.add.label("Jakub Cieślik")
about.add.label("Rafał Iwan")
about.add.button('Powrót', pygame_menu.events.BACK)


manualTypeMenu = pygame_menu.Menu(
    position=(0, 0, False),
    height=800,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Ile punktów chcesz wpisac?',
    width=1280
)

manualTypeMenu.add.label("Wpisz liczbe punktów")
ilePunktow = manualTypeMenu.add.text_input('  ', maxchar=3, valid_chars=[0,1,2,3,4,5,6,7,8,9])
manualTypeMenu.add.button('Zatwierdź', liczbaPunktow)
manualTypeMenu.add.button('Powrót', pygame_menu.events.BACK)

menu.add.button('Losowe rozmieszcznie punktów', manualTypeMenu)
menu.add.button('Wczytaj punkty z pliku', fileStart)
menu.add.button('O nas', about)
menu.add.button('Wyjście', pygame_menu.events.EXIT)

surface = create_example_window('Algorytm Pakowania Prezentu', (1280, 800))

def readFile():
    file  = open("punkty.txt", "r")
    openedFile = file.read().splitlines()
    for j in openedFile:
        point = (j.split(","))
        x = int(point[0])
        y = int(point[1])
        if(y > 0):
            y = -abs(y)
        elif(y < 0):
            y = abs(y)

        points.append(Point(centerPoint.x + x*62, centerPoint.y + y*40))

if __name__ == '__main__':
    menu.mainloop(surface)