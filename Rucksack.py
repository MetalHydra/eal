
import random

# worst case ist immer, wenn alle Objekte in den Rucksack reinpassen

G = 15
N = 10

items = ['a','b','c','d','e','f','g','h','i']
weights = [random.randint(1,6)for _ in range(N)]

# h ist kapazität i ist items
def knap(h, i):
    if i == N or h < G:
        return 0
    
