from os import walk
import pygame

def importFolder(path):
    surfaceList = []
    for roots, dirs, imageFiles in walk(path):
        for image in imageFiles:
            fullPath = path + f'\{image}'
            imageSurface = pygame.image.load(fullPath).convert_alpha()
            surfaceList.append(imageSurface)

    return surfaceList