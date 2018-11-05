# pokedex
poke = {
    "raichu" : ''' Raichu has a regional variant that is Electric/Psychic.
 It evolves from Pikachu when exposed to a Thunder Stone.
 All Pikachu in Alola will evolve into this form regardless of their origin.''',
    "onix" : ''' Onix resembles a giant chain of gray boulders that become smaller towards the tail.
 It has a rocky spine on its head and a pair of black eyes right beneath it.
 This Pokémon has a magnet in its brain that serves as an internal compass.
 Its body absorbs many hard objects, making its body very solid.
 As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds.''',
    "charmander" : ''' The flame that burns at the tip of its tail is an indication of its emotions.
 The flame wavers when Charmander is enjoying itself.
 If the Pokémon becomes enraged, the flame burns fiercely.''',
    "mewtwo" : ''' Mewtwo is a Pokémon that was created by genetic manipulation.
 However, even though the scientific power of humans created this Pokémon's body, they failed to endow Mewtwo with a compassionate heart.''',
    "metapod" : ''' The shell covering this Pokémon's body is as hard as an iron slab.
 Metapod does not move very much. It stays still because it is preparing its soft innards for evolution inside the hard shell.'''
}

search = input("Which pokemon do you want to look up to? ")

while search in poke :  
    search = input("Which pokemon do you want to look up to? ")
    search = search.lower()
    print(poke[search])
  
    
