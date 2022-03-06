# The level is represented by a grid system
# Each item in levelMap is one horizontal row
# The rows are sorted in vertical order
# Each column and row represents the x & y axises, respectively
# The location of an element is determined by their place in the map

# 'X' represents ground tile
# 'P' represents player
levelMap = [
'                            ',
'                            ', 
'                            ',
' XX     XXX            XX   ',
' XX                         ',
' XXXX          XX         XX',
' XXXX   P    XX             ',
' XX     X  XXXX    XX  XX   ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

tileSize = 64 # The size of each ground tile
screenWidth = 1200
screenHeight = len(levelMap) * 64 # The height of the window is dynamically determined by the space needed to render every tile