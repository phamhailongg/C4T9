# Mô tả một từ điển (tiếng anh, teen code, các từ viết tắt, pokedex)
d = {
    "gravity" : ''' The force that attracts objects in space towards each other;
 and that on the earth pulls them towards the centre of the planet,
 so that things fall to the ground when they are dropped. ''',
    "expectation" : "A belief that something will happen because it is likely",
    "believe" : '''  1. To feel certain that something is true or that somebody is telling you the truth,
  2. To think that something is true or possible, although you are not completely certain. ''',
    "neighbourhood" : ''' 1. A district or an area of a town; the people who live there
 2. The area that you are in or the area near a particular place. '''
}
search = input("Which word do you want to look up to? ")
if search not in ["gravity", "expectation", "believe", "neighbourhood"] : 
    print("The word you are looking up to does not exist in dictionary")
else : 
    print(d[search])