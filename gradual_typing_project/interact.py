# Helper library for creature interactions
 
from creature import Creature, Cat, Dog
from typing import Any


def are_enemies(a, b):
    return a in b.enemies or b in a.enemies

def are_friends(a, b):
    return a in b.friends and b in a.friends

def play(a, b):
    if are_friends(a, b):
        print("{} and {} get along!".format(a.name, b.name))
    elif are_enemies(a, b):
        print("{} and {} have a fight!".format(a.name, b.name))
    else:
        a.meet(b)
        b.meet(a)
    
