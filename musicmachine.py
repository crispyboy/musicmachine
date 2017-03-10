
from random import randint

import Tkinter
window = Tkinter.Tk()
window.title("Music Machine")
window.geometry("300x300")

music_array = ['oceanbyte.wav', 'solidsnaketheme.mp3', 'solidsnaketheme1.mp3', 'solidsnaketheme2.mp3', 'solidsnaketheme3.mp3']

array_length = len(music_array)

# diagnostic code for your edification mr. medvitz (in lower case!)
#for num, song in enumerate(music_array):
	#print num
	#print song
	#print music_array[num]


def song():
	import os
	os.system("open music/oceanbyte.wav")

def song2():
	import os
	os.system("open music/solidsnaketheme1.mp3")

def song3():
	random_song_index = randint(0, array_length - 1)
	random_song = 'music/'+ music_array[random_song_index]
	import os
	os.system("open " + random_song)

btn = Tkinter.Button(window, text = "play a song!", command = song)
btn.pack()
btn1 = Tkinter.Button(window, text = "play another song!", command = song2)
btn1.pack()
btn2 = Tkinter.Button(window, text = "play yet another song!", command = song3)
btn2.pack()


window.mainloop()
