mport Tkinter
window = Tkinter.Tk()
window.title("Music Machine")
window.geometry("300x300")

def song():
	import os
	os.system("open oceanbyte.wav")

def song2():
	import os
	os.system("open solidsnaketheme.mp3")

def song3():
	stub

btn = Tkinter.Button(window, text = "play a song!", command = song)
btn.pack()
btn1 = Tkinter.Button(window, text = "play another song!", command = song2)
btn1.pack()
btn2 = Tkinter.Button(window, text = "play yet another song!", command = song3)
btn2.pack()


window.mainloop()
