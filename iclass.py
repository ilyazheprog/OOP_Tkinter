from PIL import ImageTk, Image

from tkinter import Tk, Label, Button


class Window:
    def __init__(self, width, heigth, tranform, xpos, ypos, title, logo):
        self.width = width
        self.heigth = heigth
        self.tranform = tranform
        self.xpos = xpos
        self.ypos = ypos
        self.title = title
        self.logo = logo
        self.root = Tk()
    
    def build(self):
        self.root.geometry(f"{self.width}x{self.heigth}"
                           f"+{self.xpos}+{self.ypos}")
        self.root.resizable(*self.tranform)
        self.root.iconbitmap(default=self.logo)
        self.root.title(self.title)
    
    def run(self):
        self.root.mainloop()
    
    def set_text(self, txt, fg, position, font_param, rel=None, textvar=None, bg=None):
        Label(self.root, text=txt, background=bg, foreground=fg, font=font_param, textvariable=textvar, relief=rel).place(x=position[0],
                                                                                        y=position[1])
    
    def set_image(self, image, size, position):
        global tkimage
        img = Image.open(image)
        img = img.resize(size)
        tkimage = ImageTk.PhotoImage(img)
        Label(self.root, image=tkimage).place(x=position[0], y=position[1])
    
    def set_button(self, txt, font_param, position, event=None, background=None):
        Button(self.root, text=txt, bg=background, command=event, font=font_param).place(x=position[0],
                                                                                         y=position[1])