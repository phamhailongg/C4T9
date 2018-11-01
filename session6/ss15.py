# Alarm Clock
import pyglet
from datetime import * 

# Select wake up time
h = int(input("Hour? "))
m = int(input("Minute? "))

# Run until the time set
while True :
    if datetime.now().hour == h and datetime.now().minute == m :
        print("Wake up bae <3 ")
        
        music = pyglet.resource.media('sample.mp3')
        music.play()
        pyglet.app.run()

        break
    else : 
        print(datetime.now().second)
    