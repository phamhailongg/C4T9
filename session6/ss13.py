import pyglet

music = pyglet.resource.media('sample.wav')
music.play()

pyglet.app.run()