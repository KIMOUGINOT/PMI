##############################################
##### Interface graphique pendule double #####
##############################################


import solveurDouble as sd
import animationPenduleDouble as anim
from menu import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter import *



# creation frames graphiques et variables

graphFrame = Frame(rootDouble, bg = '#d3d3d3')
variablesFrame = Frame(rootDouble, bg = '#d3d3d3')
graphFrame.grid(row = 0, column = 0, sticky = 'nsew',padx = 10, pady = 20)
graphFrame.grid_propagate(False)
variablesFrame.grid(row = 0, column = 1, sticky = 'nsew',padx = 10, pady = 20)
variablesFrame.grid_propagate(False)


# creation sous-frames de la frame variables
subFrame1 = Frame(variablesFrame, bg = '#d3d3d3')
subFrame2 = Frame(variablesFrame, bg = '#d3d3d3')
subFrame1.grid(row = 0, column = 0, sticky = 'nsew',padx = 10, pady = 10)
subFrame1.grid_propagate(False)
subFrame2.grid(row = 0, column = 1, sticky = 'nsew',padx = 10, pady = 10)
subFrame2.grid_propagate(False)


variablesFrame.rowconfigure(index = 0, weight=1)
variablesFrame.columnconfigure(index = 0, weight=1)
variablesFrame.columnconfigure(index = 1, weight=1) 

# widget interne de la frame variables
    # fonctions utiles aux sous-frames

def clearAll() :
    """clear all the entries given in parameters"""
    for widget in (subFrame1.winfo_children() + subFrame2.winfo_children()):
        if type(widget) == type(Entry()):
            widget.delete(0,END)

def loadfdGraph() :
    """ Retrieve the parameters given in entries and call solving functions to show the graph"""
    variablesList = []
    for  widget in (subFrame1.winfo_children() + subFrame2.winfo_children()):
        if type(widget) == type(Entry()):
            variablesList.append(float(widget.get()))
    phi1, phi2, x1, y1, x2, y2, t = sd.solveDoublePendulum(variablesList)
    
    fig = Figure(figsize = (13.3, 9.8), dpi = 60)        
    plot1 = fig.add_subplot(221)                # phi en fonction de t
    plot1.plot(t, phi1, label = chr(966)+"1(t)", color='black')
    plot1.set_xlabel("t (s)")
    plot1.set_ylabel(chr(966) + " (rad)")
    plot1.legend()

    plot2 = fig.add_subplot(222)                # phiPoint en fonction de t
    plot2.plot(t, phi2, label = chr(966)+"2(t)", color='black')
    plot2.set_xlabel("t (s)")
    plot2.set_ylabel(chr(966) + " (rad)")
    plot2.legend()

    plot3 = fig.add_subplot(223)                # portrait de phase de phi
    plot3.plot(x1, y1, label ='m1 movement in space', color = 'orange')
    plot3.legend()

    plot4 = fig.add_subplot(224)                # portrait de phase de phi
    plot4.plot(x2, y2, label ='m2 movement in space', color = 'orange')
    plot4.legend()

    canvas = FigureCanvasTkAgg(fig, master = graphFrame)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 0, column = 0, sticky = 'nsew',padx = 10, pady = 10)
    anim.animateDoublePendulum(phi1, phi2, x1, y1, x2, y2, t)
    
def back() :
    for widget in root.winfo_children() :
        widget.grid_remove()
    mainFrame.grid(sticky = 'nsew')

    # subFrame1

phi10Entry = Entry(subFrame1, bg ='#cbb9aa')
phi10Label = Label(subFrame1, text=chr(966)+"1(t0)  (deg)", bg ='#d3d3d3', font="Helvetica")
phi1Point0Entry = Entry(subFrame1, bg ='#cbb9aa')
phi1Point0Label = Label(subFrame1, text="d"+chr(966)+"1/dt(t0)  (rad/s)", bg ='#d3d3d3', font="Helvetica")
l1Entry = Entry(subFrame1, bg ='#cbb9aa')
l1Label = Label(subFrame1, text="L1", bg ='#d3d3d3', font="Helvetica")
m1Entry = Entry(subFrame1, bg ='#cbb9aa')
m1Label = Label(subFrame1, text="m1", bg ='#d3d3d3', font="Helvetica")
aEntry = Entry(subFrame1, bg ='#cbb9aa')
aLabel = Label(subFrame1, text="t0", bg ='#d3d3d3', font="Helvetica")
clearButton = Button(subFrame1, text = "clear", command = clearAll, bg ='#cbb9aa', font="Helvetica")
backButton = Button(subFrame1, text = "back to the\nmenu", command = back, bg ='#cbb9aa', font="Helvetica")

phi10Entry.grid(row = 1, column = 0 , sticky = 'nsew',padx = 3, pady = 3)
phi10Entry.grid_propagate(False)
phi10Label.grid(row = 0, column = 0, sticky = 'nsew',padx = 3, pady = 3) 
phi10Label.grid_propagate(False)
phi1Point0Label.grid(row = 2, column = 0, sticky = 'nsew',padx = 3, pady = 3) 
phi1Point0Label.grid_propagate(False)
phi1Point0Entry.grid(row = 3, column = 0, sticky = 'nsew',padx =3, pady = 3) 
phi1Point0Entry.grid_propagate(False)
l1Entry.grid(row = 5, column = 0, sticky = 'nsew',padx = 3, pady = 3)
l1Entry.grid_propagate(False)
l1Label.grid(row = 4, column = 0, sticky = 'nsew',padx = 3, pady = 3)
l1Label.grid_propagate(False)
m1Label.grid(row = 6, column = 0, sticky = 'nsew',padx = 3, pady = 3)
m1Label.grid_propagate(False)
m1Entry.grid(row = 7, column = 0, sticky = 'nsew',padx = 3, pady = 3)
m1Entry.grid_propagate(False)
aEntry.grid(row = 9, column = 0, sticky = 'nsew',padx = 3, pady = 3)
aEntry.grid_propagate(False)
aLabel.grid(row = 8, column = 0, sticky = 'nsew',padx = 3, pady = 3)
aLabel.grid_propagate(False)
clearButton.grid(row = 10, column = 0, sticky = 'nsew',padx = 10, pady = 10)
clearButton.grid_propagate(False)
backButton.grid(row = 11, column = 0, sticky = 'nsew',padx = 10, pady = 10)
backButton.grid_propagate(False)

subFrame1.rowconfigure(index = 0, pad = 5, weight=5)
subFrame1.rowconfigure(index = 1, pad = 5, weight=5)
subFrame1.rowconfigure(index = 2, pad = 5, weight=5)
subFrame1.rowconfigure(index = 3, pad = 5, weight=5)
subFrame1.rowconfigure(index = 4, pad = 5, weight=5)
subFrame1.rowconfigure(index = 5, pad = 5, weight=5)
subFrame1.rowconfigure(index = 6, pad = 5, weight=5)
subFrame1.rowconfigure(index = 7, pad = 5, weight=5)
subFrame1.rowconfigure(index = 8, pad = 5, weight=5)
subFrame1.rowconfigure(index = 9, pad = 5, weight=5)
subFrame1.rowconfigure(index = 10, pad = 5, weight=7)
subFrame1.rowconfigure(index = 11, pad = 5, weight=7)

subFrame1.columnconfigure(index = 0, pad = 5, weight=1)

    # subFrame2

phi20Entry = Entry(subFrame2, bg ='#cbb9aa')
phi20Label = Label(subFrame2, text=chr(966)+"2(t0)  (deg)", bg ='#d3d3d3', font="Helvetica")
phi2Point0Entry = Entry(subFrame2, bg ='#cbb9aa')
phi2Point0Label = Label(subFrame2, text="d"+chr(966)+"2/dt(t0)  (rad/s)", bg ='#d3d3d3', font="Helvetica")
l2Entry = Entry(subFrame2, bg ='#cbb9aa')
l2Label = Label(subFrame2, text="L2", bg ='#d3d3d3', font="Helvetica")
m2Entry = Entry(subFrame2, bg ='#cbb9aa')
m2Label = Label(subFrame2, text="m2", bg ='#d3d3d3', font="Helvetica")
bEntry = Entry(subFrame2, bg ='#cbb9aa')
bLabel = Label(subFrame2, text="ti", bg ='#d3d3d3', font="Helvetica")
loadButton = Button(subFrame2, text = "load" , command = loadfdGraph, bg ='#cbb9aa', font="Helvetica")

phi20Label.grid(row = 0, column = 0, sticky = 'nsew',padx = 3, pady = 3)
phi20Entry.grid(row = 1, column = 0, sticky = 'nsew',padx = 3, pady = 3)
phi2Point0Label.grid(row = 2, column = 0, sticky = 'nsew',padx = 3, pady = 3)
phi2Point0Entry.grid(row = 3, column = 0, sticky = 'nsew',padx = 3, pady = 3)
l2Label.grid(row = 4, column = 0, sticky = 'nsew',padx = 3, pady = 3)
l2Entry.grid(row = 5, column = 0, sticky = 'nsew',padx = 3, pady = 3)
m2Label.grid(row = 6, column = 0, sticky = 'nsew',padx = 3, pady = 3)
m2Entry.grid(row = 7, column = 0, sticky = 'nsew',padx = 3, pady = 3)
bLabel.grid(row = 8, column = 0, sticky = 'nsew',padx = 3, pady = 3)
bEntry.grid(row = 9, column = 0, sticky = 'nsew',padx = 3, pady = 3)
loadButton.grid(row = 10, column = 0, sticky = 'nsew',padx = 10, pady = 10)

subFrame2.rowconfigure(index = 0, pad = 5, weight=1)
subFrame2.rowconfigure(index = 1, pad = 5, weight=1)
subFrame2.rowconfigure(index = 2, pad = 5, weight=1)
subFrame2.rowconfigure(index = 3, pad = 5, weight=1)
subFrame2.rowconfigure(index = 4, pad = 5, weight=1)
subFrame2.rowconfigure(index = 5, pad = 5, weight=1)
subFrame2.rowconfigure(index = 6, pad = 5, weight=1)
subFrame2.rowconfigure(index = 7, pad = 5, weight=1)
subFrame2.rowconfigure(index = 8, pad = 5, weight=1)
subFrame2.rowconfigure(index = 9, pad = 5, weight=1)
subFrame2.rowconfigure(index = 10, pad = 5, weight=4)
subFrame2.columnconfigure(index = 0, pad = 5, weight=1)

# Pre-remplissage des entries

phi10Entry.insert(0,"30")
phi1Point0Entry.insert(0,"0")
phi20Entry.insert(0,"30")
phi2Point0Entry.insert(0,"0")
l1Entry.insert(0,"1")
l2Entry.insert(0,"1")
m1Entry.insert(0,"1")
m2Entry.insert(0,"1")
aEntry.insert(0,"0")
bEntry.insert(0,"15")

rootDouble.rowconfigure(index = 0, pad = 20, weight=1)
rootDouble.columnconfigure(index = 0, pad = 20, weight=2)
rootDouble.columnconfigure(index = 1, pad = 20, weight=1) 