import tkinter
import pyttsx3

app = tkinter.Tk()
ent = tkinter.Text(app)
ent.pack()

def say():
    mouth = pyttsx3.init()
    mouth.say(ent.get(1.0, tkinter.END))
    mouth.runAndWait()


btn = tkinter.Button(app, text="Convert To Speech", command=say, width=91)
btn.pack()
app.mainloop()
