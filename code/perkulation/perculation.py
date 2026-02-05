from enum import Enum
import matplotlib
import matplotlib.pyplot as plt
import random

random.seed(0)

class Feld(Enum):
    DESERT = 0
    TREE = 1
    BURNING = 2
    ASH = 3

def initialize_map(probability_tree, size):
    map = []
    for _ in range(size):
        row = []
        for _ in range(size):
            if random.random() < probability_tree:
                row.append(Feld.TREE)
            else:
                row.append(Feld.DESERT)
        map.append(row)
    return map

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def periodic_neighbors(point, map):
    neighbors = []
    # for illustration:
    # map = [[0, 1, 2], 
    #           [3, 4, 5], 
    #           [6, 7, 8]]
    # map[1][2] = 5
    l = len(map[0])
    neighbors.append(map[point.x][(point.y - 1 + l) % l])
    neighbors.append(map[point.x][(point.y + 1) % l])
    if point.x >= 1:
        neighbors.append(map[point.x - 1][point.y])
    if point.x <= l - 2:
        neighbors.append(map[point.x + 1][point.y])
    return neighbors

def neighbor_burns(point, map):
    neighbors = periodic_neighbors(point, map)
    for neighbor in neighbors:
        if neighbor == Feld.BURNING:
            return True
    return False

def begins_to_burn(point, map):
    if map[point.x][point.y] == Feld.TREE:
        if neighbor_burns(point, map):
            return True
    return False

def ignite_front_row(map):
    for i in range(len(map[0])):
        map[0][i] = Feld.BURNING

def perculation_step(map):
    new_map = []
    for i in range(0, len(map)):
        row = []
        for j in range(0, len(map)):
            row.append(map[i][j])
            if begins_to_burn(Point(i, j), map):
                row[-1] = Feld.BURNING
            if map[i][j] == Feld.BURNING:
                row[-1] = Feld.ASH
        new_map.append(row)
    return new_map

def still_burning(map):
    for i in range(len(map[0])):
        for j in range(len(map[0])):
            if map[i][j] == Feld.BURNING:
                return True
    return False

def perculate(map):
    while still_burning(map):
        map = perculation_step(map)
    return map

def plotable_map(map):
    m = []
    for i in range(len(map)):
        row = []
        for j in range(len(map)):
            row.append(map[i][j].value)
        m.append(row)
    return m

colors = ['yellow', 'green', 'red', 'black']
cmap = matplotlib.colors.ListedColormap(colors, name='colors', N=None)

def fix_color_schema(map):
    map[0][0] = Feld.ASH

def main():
    map = initialize_map(0.55, 50)
    ignite_front_row(map)
    fix_color_schema(map)
    plt.imshow(plotable_map(map), cmap=cmap)
    plt.show()
    map = perculate(map)
    plt.imshow(plotable_map(map), cmap=cmap)
    plt.show()


if __name__ == "__main__":
    main()

