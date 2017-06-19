from Tkinter import *
import tkFileDialog
import os
import subprocess

class CubeMapperApp(Frame):
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        
        #reference to the master widget, which is the tk window
        self.master = master
        
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("CUBEMAPPER")
            
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
            
        # creating a button instance
        browseButton = Button(self, text="Browse",command=self.load_file)
            
        # placing the button on my window
        browseButton.place(x=100, y=70)
    
    def load_file(self):
        fname = tkFileDialog.askdirectory()
        if fname:
            print("Converting Equirectangulars to Cubemaps")
            p = subprocess.Popen(['python','CubeMapper.py',fname])
        exit()
        #equiToCube(fname)

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("300x200")

#creation of an instance
app = CubeMapperApp(root)
#mainloop
root.mainloop()