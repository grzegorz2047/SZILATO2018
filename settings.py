import os

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (60, 60, 60)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 55, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0,0,255)

# game settings
WIDTH = 800   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 500  # 16 * 48 or 32 * 24 or 64 * 12
MAP_WIDTH = 600
FPS = 60
TITLE = "Sztuczny Wiedźmin i przyjaciele"
BGCOLOR = DARKGREY

# default settings
TILESIZE = 50

GAME_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_FOLDER, "img")
MAP_FOLDER = os.path.join(GAME_FOLDER, "maps")

MAP = "test.map"
MAPLIST = []
MAP_PLACES = []
with open(MAP_FOLDER + "/" + MAP, "rt") as file:
    for line in file:
        MAPLIST.append(line.replace("\n","").split(" "))
GRIDWIDTH = len(MAPLIST)
GRIDHEIGHT = len(MAPLIST[0])

for i in range (0, GRIDWIDTH):
    for j in range (0, GRIDHEIGHT):
        if MAPLIST[i][j] == "." or MAPLIST[i][j] =='6' or MAPLIST[i][j] =='5' :
            MAP_PLACES.append([j,i])
