import sys
import math
""" Compability check for Python """
if sys.version_info >= (3,0): 
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter import filedialog
else:
    from Tkinter import *
    import ttk as ttk
    import tkMessageBox as messagebox
    import tkFileDialog as filedialog
import numpy as np

d = [ 'Start', 
      'End', 
      'Color1',
      'Color2',
      'Delay1',
      'Delay2',
      'Sustain1',
      'Sustain2',
      'Probability1',
      'Probability2',
      'Stop1',
      'Stop2',
      'Frequency1_1',
      'Frequency1_2',
      'Frequency1_3',
      'Frequency1_4',
      'Frequency1_5',
      'Frequency2_1',
      'Frequency2_2',
      'Frequency2_3',
      'Frequency2_4',
      'Frequency2_5' ]

### This is for window
class App():
    def __init__ (self):
        self.var = []
        self.conds = []
        self.root = self.makeWindow()
    
    def makeWindow (self):
        root = Tk()
        root.configure(background='#eeeeee')
        root.title("OptoPAD SPC v0.91 (Beta)")
        root.resizable(width=False, height=False)
        root.geometry("650x900")
    
        """
        # create a menu
        menu = Menu(root)
        root.config(menu=menu)

        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.restart)
        filemenu.add_command(label="Open...", command=self.open_file)
        filemenu.add_command(label="Save...")
        filemenu.add_separator()
        filemenu.add_command(label="Import...")
        filemenu.add_command(label="Export...")
        filemenu.add_separator()
        filemenu.add_command(label="Exit")
    
        viewmenu = Menu(menu)
        menu.add_cascade(label="View", menu=viewmenu)
        viewmenu.add_command(label="View experiment")
        viewmenu.add_command(label="View history")

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...")
        """
        
        root = self.getTop(root)        
        root = self.getCenter(root)
        root = self.getBottom(root)
        
        return root
    
    def getTop(self, root):
        top = Frame(root, background='#eeeeee')
        xtop = Frame(top, relief=RIDGE, borderwidth=2, background='#eeeeee')
        Label(xtop, text="Please type in information about experimental protocol", background='#eeeeee').grid(row=0, column = 0,  columnspan=3, sticky=W+E, pady=2)
        Label(xtop, text="From arena", background='#eeeeee').grid(row=1, column = 0, sticky=W)
        self.var.append(Scale(xtop, from_=1, to=32, orient=HORIZONTAL, showvalue=8, tickinterval=0, length=120, takefocus=True, background='#eeeeee'))
        self.var[-1].grid(row=1, column = 1, columnspan=2, sticky=W+E)
        Label(xtop, text="To arena", background='#eeeeee').grid(row=2, column = 0, sticky=W)
        self.var.append(Scale(xtop, from_=1, to=32, orient=HORIZONTAL, showvalue=8, tickinterval=0, length= 120, takefocus=True, background='#eeeeee'))
        self.var[-1].grid(row=2, column = 1, columnspan=2, sticky=W+E)
        xtop.pack()
        top.pack(fill=BOTH)
        return root
    
    def getCenter(self, root):
        ctop = Frame(root, background='#eeeeee')
        xctop = Frame(ctop, relief=RIDGE, borderwidth=2, background='#eeeeee')
        
        Label(xctop, text="Channel 1", background='#eeeeee').grid(row=1, column = 2, sticky=W+E)
        Label(xctop, text="Channel 2", background='#eeeeee').grid(row=1, column = 3, sticky=W+E)
        
        Label(xctop, text="Color:", background='#eeeeee').grid(row=2, column = 0, sticky=W)
        MODES = [
        ("red", 1),
        ("green", 2),
        ("blue", 3),
        ("yellow", 4),
        ("magenta", 5),
        ("cyan", 6),
        ("white", 7)
        ]

        for channel in range(2):
            self.var.append(IntVar())
            self.var[-1].set(1)

            for text, mode in MODES:
                if int(mode) < 4:
                    Label(xctop, text=text, fg ="white", bg = text).grid(row=1+int(mode), column = 1, sticky=W+E)
                else:
                    Label(xctop, text=text, fg ="black",  bg = text).grid(row=1+int(mode), column = 1, sticky=W+E)
                b1 = Radiobutton(xctop, text="", variable=self.var[-1], value=mode, background='#eeeeee')
                b1.grid(row=1+int(mode), column = 2+channel)
        
        
        Label(xctop, text="Delay [ms]:", background='#eeeeee').grid(row=9, column = 0, sticky=W)
        for channel in range(2):
            self.var.append(Scale(xctop, from_=0, to=60000, orient=HORIZONTAL, length=200, resolution=10, showvalue=8, tickinterval=0, takefocus=True, background='#eeeeee'))
            self.var[-1].grid(row=9, column = 2+channel, sticky=W+E)
        
        Label(xctop, text="Sustain [ms]:", background='#eeeeee').grid(row=10, column = 0, sticky=W)
        for channel in range(2):
            self.var.append(Scale(xctop, from_=0, to=60000, orient=HORIZONTAL, length=200, resolution=10, showvalue=8, tickinterval=0, takefocus=True, background='#eeeeee'))
            self.var[-1].grid(row=10, column = 2+channel, sticky=W+E)
        
        Label(xctop, text="Probability:", background='#eeeeee').grid(row=11, column = 0, sticky=W)
        for channel in range(2):
            self.var.append(Scale(xctop, from_=0, to=1, orient=HORIZONTAL, length=200, resolution=0.01, showvalue=8, tickinterval=0, takefocus=True, background='#eeeeee'))
            self.var[-1].grid(row=11, column = 2+channel, sticky=W+E)
        
        Label(xctop, text="Stop with activity:", background='#eeeeee').grid(row=12, column = 0, sticky=W)
        for channel in range(2):
            self.var.append(IntVar())
            Checkbutton(xctop, text="", variable=self.var[-1], background='#eeeeee').grid(row=12, column = 2+channel)
        
        ttk.Separator(xctop, orient=HORIZONTAL).grid(row=13,column=0,columnspan=5, sticky=W+E)
        
        
        for channel in range(2):
            for ind in range(5):
                if channel==0:
                    Label(xctop, text="Frequency " + str(ind+1) +" [Hz]:", background='#eeeeee').grid(row=ind+14, column = 0, sticky=W)
                self.var.append(Scale(xctop, from_=0, to=250, orient=HORIZONTAL, length=200, resolution=1, showvalue=8, tickinterval=0, takefocus=True, background='#eeeeee'))
                self.var[-1].grid(row=ind+14, column = 2+channel, sticky=W+E)
        
        copy1 = Button(xctop,text="Copy from 2", command=self.copyFrom2)
        copy2 = Button(xctop,text="Copy from 1", command=self.copyFrom1)
        copy1.grid(row=20, column = 2, sticky=W+E)
        copy2.grid(row=20, column = 3, sticky=W+E)
        xctop.pack()
        ctop.pack(fill=BOTH)
        
        return root
    
    def getBottom(self, root):
        botbuttons = Frame(root)       # Row of buttons
        botbuttons.pack()
        b1 = Button(botbuttons,text="Save Protocol", command=self.saveProto)
        b2 = Button(botbuttons,text="Add Condition", command=self.addCond)
        b3 = Button(botbuttons,text="Edit Condition", command=self.editCond)
        b4 = Button(botbuttons,text="Delete Condition", command=self.delCond)
        b1.pack(side=LEFT) 
        b2.pack(side=LEFT)
        b3.pack(side=LEFT)
        b4.pack(side=LEFT)

        botlist = Frame(root)       # select of names
        botlist.pack()
        scroll = Scrollbar(botlist, orient=VERTICAL)
        self.select = Listbox(botlist, yscrollcommand=scroll.set, height=12, width=51)
        self.select.bind('<Double-Button-1>', self.dclick)
        scroll.config (command=self.select.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.select.pack(side=LEFT,  fill=BOTH, expand=1)
        return root
    
    def dclick(self, event):
        for ind, var in enumerate(self.var):
            temp = self.conds[self.whichSelected()].get(ind)
            var.set(temp)
    
    def saveProto(self):
        if len(self.conds)==0:
            self.addCond()
        datalen = (len(d)-2)
        Times = [('t'+str(i), np.int64) for i in range(6)]
        Freqs = [('f'+str(i), np.int64) for i in range(12)]
        dt = np.dtype(Times + [('prob1', np.float64), ('prob2', np.float64)] + Freqs)
        #print(dt)
        fields = np.zeros(len(Times)+2+len(Freqs), dtype=dt)
        myfmt = len(Times)*'%u ' + '%1.2f %1.2f ' + len(Freqs)*'%3u '
        outdata = np.zeros((32,datalen), np.float64)
    
        
        for cond in self.conds:
            for ind in range(cond.get(0)-1, cond.get(1)):
                #print(ind)
                outdata[ind,:] = cond.getall()
                    
        #outdata = np.reshape(outdata,(1,32*datalen))
        name=filedialog.asksaveasfilename(defaultextension=".dat")
        if name is not None:
            print("Saved to %s" % name)
            #print(outdata)
            with open(name,'wb') as f:
                np.savetxt(f, outdata, fmt=myfmt)
    
    def copyFrom1(self):
        for ind, data in enumerate(self.var):
            if math.fmod(ind,2) > 0 and ind < 12 and ind > 1:
                data.set(self.var[ind-1].get())
            elif ind >= 17:
                data.set(self.var[ind-5].get())
            
    def copyFrom2(self):
        for ind, data in enumerate(self.var):
            if math.fmod(ind,2) < 1 and ind < 12 and ind > 1:
                data.set(self.var[ind+1].get())
            elif ind >= 12 and ind < 17:
                data.set(self.var[ind+5].get())
    
    def addCond(self):
        tempdata = []
        for data in self.var:
            tempdata.append(data.get())
        newCond = Condition(tempdata)
        self.conds.append(newCond)
        self.setSelect()
    
    def editCond(self):
        tempdata = []
        for data in self.var:
            tempdata.append(data.get())
        self.conds[self.whichSelected()] = Condition(tempdata)
    
    def delCond(self):
        if self.whichSelected() == None:
            print("")
        else:
            del self.conds[self.whichSelected()]
        self.setSelect ()
    
    def whichSelected (self) :
        if len(self.select.curselection()) > 0:
            return int(self.select.curselection()[0])
        else:
            print("Warning: No entry selected.")
            return None
    
    def setSelect (self) :
        self.select.delete(0,END)
        for ind, cond in enumerate(self.conds):
            self.select.insert (END, "Condition " + "{:03}".format(ind+1))
 
class Condition:
    def __init__(self, indata):
        self.data = []
        for vals in indata:
            self.data.append(vals)
            
    def getall(self):
        #print("This condition has", np.asarray(self.data[2:]).shape, "entries")
        return np.asarray(self.data[2:])
        
    def get(self, ind):
        return self.data[ind]
    
    def set(self, ind, val):
        self.data[ind] = val 

def main(): 
    app = App()
    app.root.mainloop()

if __name__ == '__main__':   
    main()