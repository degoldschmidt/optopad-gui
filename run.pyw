import sys
import math
import numpy as np
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

d = { 'Start':          0, 
      'End':            1, 
      'Color1':         2,
      'Color2':         3,
      'Delay1':         4,
      'Delay2':         5,
      'Sustain1':       6,
      'Sustain2':       7,
      'Probability1':   8,
      'Probability2':   9,
      'Stop1':          10,
      'Stop2':          11,
      'Frequency1':     12,
      'Frequency2':     13,
      'DutyCycle1':     14,
      'DutyCycle2':     15,
      'ConstOnCycle1':  16,
      'ConstOnCycle2':  17,
      'OnPeriod1':      18,
      'OnPeriod2':      19
      }

def diff(list1, list2):
    sum=0.
    for ind, elems in enumerate(list1):
        sum += math.fabs(elems-list2[ind])
    return sum
        

### This is for window
class App():
    def __init__ (self):
        self.var = []
        self.conds = []
        self.root = self.makeWindow()
    
    def makeWindow (self):
        root = Tk()
        root.configure(background='#eeeeee')
        root.title("OptoPAD SPC v0.9.3 (Beta)")
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
        
        
        Label(xctop, text="Delay [s]:", background='#eeeeee').grid(row=9, column = 0, sticky=W)
        for channel in range(2):
            self.var.append(Scale(xctop, from_=0, to=60, orient=HORIZONTAL, length=200, resolution=0.1, showvalue=8, tickinterval=0, takefocus=True, background='#eeeeee'))
            self.var[-1].grid(row=9, column = 2+channel, sticky=W+E)
        
        Label(xctop, text="Sustain [s]:", background='#eeeeee').grid(row=10, column = 0, sticky=W)
        for channel in range(2):
            self.var.append(Scale(xctop, from_=0, to=60, orient=HORIZONTAL, length=200, resolution=0.1, showvalue=8, tickinterval=0, takefocus=True, background='#eeeeee'))
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
            if channel==0:
                Label(xctop, text="Frequency [Hz]:", background='#eeeeee').grid(row=14, column = 0, sticky=W)
            self.var.append(Scale(xctop, from_=0, to=250, orient=HORIZONTAL, length=200, resolution=1, showvalue=8, tickinterval=0, takefocus=True, background='#eeeeee'))
            self.var[-1].grid(row=14, column = 2+channel, sticky=W+E)
            
        Label(xctop, text="Duty cycle:", background='#eeeeee').grid(row=16, column = 0, sticky=W)
        for channel in range(2):
            self.var.append(Scale(xctop, from_=0, to=1, orient=HORIZONTAL, length=200, resolution=0.01, showvalue=8, tickinterval=0, takefocus=True, background='#eeeeee'))
            self.var[-1].grid(row=16, column = 2+channel, sticky=W+E)
            
        Label(xctop, text="Constant on-cycle:", background='#eeeeee').grid(row=15, column = 0, sticky=W)
        self.var.append(IntVar())
        Checkbutton(xctop, text="", variable=self.var[-1], background='#eeeeee', command= lambda: self.disableDuty(d["ConstOnCycle1"])).grid(row=15, column = 2)
        self.var.append(IntVar())
        Checkbutton(xctop, text="", variable=self.var[-1], background='#eeeeee', command= lambda: self.disableDuty(d["ConstOnCycle2"])).grid(row=15, column = 3)
        
        for channel in range(2):
            if channel==0:
                Label(xctop, text="On period [s]:", background='#eeeeee').grid(row=17, column = 0, sticky=W)
            self.var.append(Scale(xctop, from_=0, to=1, orient=HORIZONTAL, length=200, resolution=0.001, showvalue=8, tickinterval=0, takefocus=True, background='#eeeeee', state = DISABLED))
            self.var[-1].grid(row=17, column = 2+channel, sticky=W+E)
        
        
        copy1 = Button(xctop,text="Copy from 2", command= lambda: self.copyFrom(2), background='#eeeeee')
        copy2 = Button(xctop,text="Copy from 1", command= lambda: self.copyFrom(1), background='#eeeeee')
        copy1.grid(row=18, column = 2, sticky=W+E)
        copy2.grid(row=18, column = 3, sticky=W+E)
        xctop.pack()
        ctop.pack(fill=BOTH)
        
        return root
    
    def getBottom(self, root):
        saveload = Frame(root)       # Row of buttons
        saveload.pack()
        save = Button(saveload,text="Save Protocol", command=self.saveProto, background='#eeeeee')
        save.pack(side=LEFT) 
        load = Button(saveload,text="Load Protocol", command=self.loadProto, background='#eeeeee')
        load.pack(side=LEFT) 
        condbs = Frame(root)       # Row of buttons
        condbs.pack()
        add = Button(condbs,text="Add Condition", command=self.addCond, background='#eeeeee')
        edit = Button(condbs,text="Edit Condition", command=self.editCond, background='#eeeeee')
        delete = Button(condbs,text="Delete Condition", command=self.delCond, background='#eeeeee')
        add.pack(side=LEFT)
        edit.pack(side=LEFT)
        delete.pack(side=LEFT)

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
            if ind < self.conds[self.whichSelected()].length():
                temp = self.conds[self.whichSelected()].get(ind)
                var.set(temp)
            
    def disableDuty(self, ch):
        if self.var[ch].get() == 0:
            self.var[ch-2].config(state=NORMAL)
            self.var[ch+2].config(state=DISABLED)
        else:
            self.var[ch-2].config(state=DISABLED)
            self.var[ch+2].config(state=NORMAL)
            
    def loadProto(self):
        # load data
        name = filedialog.askopenfilename()
        with open(name) as f:
            f=[x.strip() for x in f if x.strip()]
            data=[x.split() for x in f]
            length = len(data)
            oldrow=14*[0]
            count = 0
            for ind,row in enumerate(data):
                row[0:2] = map(int,row[0:2])
                row[2:8] = map(float,row[2:8])
                row[8:12] = map(int,row[8:12])
                row[12:] = map(float,row[12:])
                if sum(row) > 0.:
                    #print(sum(row), diff(row,oldrow))
                    if (diff(row,oldrow) > 0. or ind == len(data)-1) and ind > 0:
                        #print("Condition %u for arena %u to %u" % (len(self.conds)+1, ind-count, ind))
                        tempdata = [ind-count, ind]
                        for all in oldrow:
                            tempdata.append(all)
                        newCond = Condition(tempdata)
                        self.conds.append(newCond)
                        self.setSelect()
                        count = 0
                    else:
                        count +=1
                oldrow = row
    
    def saveProto(self):
        if len(self.conds)==0:
            self.addCond()
        datalen = (len(d)-6)
        myfmt = 2 *'%u ' + 4 * '%2.1f ' + 2 * '%1.2f ' + 4 * '%3u ' + 2 * '%1.2f '
        outdata = np.zeros((32,datalen), np.float64)   
        for cond in self.conds:
            for ind in range(cond.get(0)-1, cond.get(1)):
                outdata[ind,:] = cond.getall()       
        name=filedialog.asksaveasfilename(defaultextension=".dat")
        if name is not None:
            print("Saved to %s" % name)
            with open(name,'wb') as f:
                np.savetxt(f, outdata, fmt=myfmt)
    
    def copyFrom(self, val):
        if val == 1:
            fac = -1
            mod = 1
        elif val == 2:
            fac = 1
            mod = 0
        else:
            fac = 0
            print("Warning: copyFrom used invalid value.")
        for ind, data in enumerate(self.var):
            if int(math.fmod(ind,2)) == mod and ind > 1:
                data.set(self.var[ind+fac].get())

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
        if self.data[-4] == 1:
            self.data[-6] = self.data[-2] * self.data[-8]
        if self.data[-3] == 1:
            self.data[-5] = self.data[-1] * self.data[-7]
        return np.asarray(self.data[2:-4])
        
    def get(self, ind):
        return self.data[ind]
    
    def set(self, ind, val):
        self.data[ind] = val 
        
    def length(self):
        return len(self.data)

def main(): 
    app = App()
    app.root.mainloop()

if __name__ == '__main__':   
    main()