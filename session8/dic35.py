from random import randint
import random
# int check:
def not_int (a):
    try:
        int (a)
        return False 
    except ValueError:
        return True

level = 0
not_int(level) 