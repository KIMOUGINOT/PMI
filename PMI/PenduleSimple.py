##############################################
##### Interface graphique pendule simple #####
##############################################


import solveurSimple as sv
import energie as nrj
from animationPenduleSimple import *
from menu import *
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter import *

m = 1

# creation frames graphiques et variables

graphFrame = Frame(rootSimple, bg = '#d3d3d3')
variablesFrame = Frame(rootSimple, bg = '#d3d3d3')
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

def loadGraph() :
    """ Retrieve the parameters given in entries and call solving functions to show the graph"""
    variablesList = []
    tmp = 0
    for  widget in (subFrame1.winfo_children() + subFrame2.winfo_children()):
        if type(widget) == type(Entry()):
            variablesList.append(widget.get())
    variablesList[1], variablesList[3] = variablesList[3],variablesList[1]
    variablesList[2], variablesList[3] = variablesList[3],variablesList[2]
    variablesList[4], variablesList[3] = variablesList[3],variablesList[4]
    theta, thetaPoint, t = sv.solveSimplePendulum(np.radians(float(variablesList[0])), float(variablesList[1]), float(variablesList[2]), int(variablesList[3]), int(variablesList[4]), int(variablesList[5]))
    
    fig = Figure(figsize = (13.3, 9.8), dpi = 60)        
    plot1 = fig.add_subplot(221)                # theta en fonction de t
    plot1.plot(t, theta, label=chr(952) + '(t)', color='black')
    plot1.set_xlabel("t (s)")
    plot1.set_ylabel(chr(952) + " (rad)")
    plot1.grid()
    plot1.legend()

    plot2 = fig.add_subplot(222)                # Ec, Ep et Em en fonction de t
    Ec = nrj.EcSimple(thetaPoint, float(variablesList[2]), m)
    Ep = nrj.EpSimple(theta, float(variablesList[2]),m)
    plot2.plot(t, Ec, label='Ec', color = 'green')
    plot2.plot(t, Ep, label='Ep', color = 'red')
    plot2.set_xlabel("t (s)")
    plot2.set_ylabel("Energy")
    plot2.grid()
    plot2.legend()

    plot3 = fig.add_subplot(223)                # portrait de phase de theta
    plot3.plot(theta, thetaPoint, label='Phase portrait', color = 'orange')
    plot3.set_xlabel(chr(952) + " (rad) ")
    plot3.set_ylabel(chr(952) + "_point (rad)")
    plot3.grid()
    plot3.legend()

    canvas = FigureCanvasTkAgg(fig, master = graphFrame)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 0, column = 0, sticky = 'nsew',padx = 10, pady = 10)
    animateSimplePendulum(theta, t, float(variablesList[2]))
    
def back() :
    for widget in root.winfo_children() :
        widget.grid_remove()
    mainFrame.grid(sticky = 'nsew')

    # subFrame1

theta0Entry = Entry(subFrame1, bg ='#cbb9aa')
theta0Label = Label(subFrame1, text=chr(952)+"(t0)  (deg)", bg ='#d3d3d3', font="Helvetica")
lEntry = Entry(subFrame1, bg ='#cbb9aa')
lLabel = Label(subFrame1, text="L", bg ='#d3d3d3', font="Helvetica")
aEntry = Entry(subFrame1, bg ='#cbb9aa')
aLabel = Label(subFrame1, text="t0", bg ='#d3d3d3', font="Helvetica")
clearButton = Button(subFrame1, text = "clear", command = clearAll, bg ='#cbb9aa', font="Helvetica")
backButton = Button(subFrame1, text = "back to the\nmenu", command = back, bg ='#cbb9aa', font="Helvetica")

theta0Entry.grid(row = 1, column = 0 , sticky = 'nsew',padx = 10, pady = 10)
theta0Entry.grid_propagate(False)
theta0Label.grid(row = 0, column = 0, sticky = 'nsew',padx = 10, pady = 10) 
theta0Label.grid_propagate(False)
lEntry.grid(row = 3, column = 0, sticky = 'nsew',padx = 10, pady = 10)
lEntry.grid_propagate(False)
lLabel.grid(row = 2, column = 0, sticky = 'nsew',padx = 10, pady = 10)
lLabel.grid_propagate(False)
aEntry.grid(row = 5, column = 0, sticky = 'nsew',padx = 10, pady = 10)
aEntry.grid_propagate(False)
aLabel.grid(row = 4, column = 0, sticky = 'nsew',padx = 10, pady = 10)
aLabel.grid_propagate(False)
clearButton.grid(row = 6, column = 0, sticky = 'nsew',padx = 10, pady = 10)
clearButton.grid_propagate(False)
backButton.grid(row = 7, column = 0, sticky = 'nsew',padx = 10, pady = 10)
backButton.grid_propagate(False)

subFrame1.rowconfigure(index = 0, pad = 5, weight=5)
subFrame1.rowconfigure(index = 1, pad = 5, weight=5)
subFrame1.rowconfigure(index = 2, pad = 5, weight=5)
subFrame1.rowconfigure(index = 3, pad = 5, weight=5)
subFrame1.rowconfigure(index = 4, pad = 5, weight=5)
subFrame1.rowconfigure(index = 5, pad = 5, weight=5)
subFrame1.rowconfigure(index = 6, pad = 5, weight=7)
subFrame1.rowconfigure(index = 7, pad = 5, weight=7)
subFrame1.columnconfigure(index = 0, pad = 5, weight=1)

    # subFrame2

thetaPoint0Entry = Entry(subFrame2, bg ='#cbb9aa')
thetaPoint0Label = Label(subFrame2, text="d" + chr(952) +"/dt" +"(t0)  (rad/s)", bg ='#d3d3d3', font="Helvetica")
nEntry = Entry(subFrame2, bg ='#cbb9aa')
nLabel = Label(subFrame2, text="n", bg ='#d3d3d3', font="Helvetica")
bEntry = Entry(subFrame2, bg ='#cbb9aa')
bLabel = Label(subFrame2, text="ti", bg ='#d3d3d3', font="Helvetica")
loadButton = Button(subFrame2, text = "load", command = loadGraph , bg ='#cbb9aa', font="Helvetica")


thetaPoint0Entry.grid(row = 1, column = 0, sticky = 'nsew',padx = 10, pady = 10)
thetaPoint0Label.grid(row = 0, column = 0, sticky = 'nsew',padx = 10, pady = 10)
nEntry.grid(row = 3, column = 0, sticky = 'nsew',padx = 10, pady = 10)
nLabel.grid(row = 2, column = 0, sticky = 'nsew',padx = 10, pady = 10)
bEntry.grid(row = 5, column = 0, sticky = 'nsew',padx = 10, pady = 10)
bLabel.grid(row = 4, column = 0, sticky = 'nsew',padx = 10, pady = 10)
loadButton.grid(row = 6, column = 0, sticky = 'nsew',padx = 10, pady = 10)

subFrame2.rowconfigure(index = 0, pad = 5, weight=1)
subFrame2.rowconfigure(index = 1, pad = 5, weight=1)
subFrame2.rowconfigure(index = 2, pad = 5, weight=1)
subFrame2.rowconfigure(index = 3, pad = 5, weight=1)
subFrame2.rowconfigure(index = 4, pad = 5, weight=1)
subFrame2.rowconfigure(index = 5, pad = 5, weight=1)
subFrame2.rowconfigure(index = 6, pad = 5, weight=4)
subFrame2.columnconfigure(index = 0, pad = 5, weight=1)

# Pre-remplissage des entries
theta0Entry.insert(0,"30")
thetaPoint0Entry.insert(0,"0")
lEntry.insert(0,"2")
nEntry.insert(0,"100")
aEntry.insert(0,"0")
bEntry.insert(0,"5")

rootSimple.rowconfigure(index = 0, pad = 20, weight=1)
rootSimple.columnconfigure(index = 0, pad = 20, weight=2)
rootSimple.columnconfigure(index = 1, pad = 20, weight=1) 