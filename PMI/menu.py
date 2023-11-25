####################
####  menu page ####
####################


from tkinter import *


# Windows parameters
root = Tk()
root.title("Pendulum simulation")
root.state("zoomed")
root.minsize(1000,600)
root.configure(bg = '#cbb9aa')

y0 = root.winfo_screenwidth()
x0 = root.winfo_screenheight()

# Main windows
mainFrame = Frame(root, bg = '#cbb9aa')
mainFrame.grid(row = 0, column = 0, sticky = 'nsew')
root.rowconfigure(index = 0, weight = 1)
root.columnconfigure(index = 0, weight = 1)

# Secondary windows
rootSimple = Canvas(root, height = x0, width = y0, bg = '#cbb9aa')
rootForcedSimple = Canvas(root, height = x0, width = y0, bg = '#cbb9aa')
rootDouble = Canvas(root, height = x0, width = y0, bg = '#cbb9aa')
rootForcedDouble = Canvas(root, height = x0, width = y0, bg = '#cbb9aa')
# Presentation parts

introFrame = Frame(mainFrame, bg = '#d3d3d3')
introFrame.grid(row = 0, column = 0, sticky = 'nsew',padx = 10, pady = 20)
introFrame.grid_propagate(False)

    # writting
titleLabel = Label(introFrame, text = "PMI", bg ='#d3d3d3', font=("Helvetica",80))
titleLabel.grid(row = 0, column = 0,padx = 10, pady = 20)
subtitleLabel = Label(introFrame, text = "Pendulum simulation", bg ='#d3d3d3', font=("Helvetica", 40))
subtitleLabel.grid(row = 1, column = 0, padx = 10, pady = 20)
nameLabel = Label(introFrame, text = "Kilian MOUGINOT\nVincent LEROI   \nNicolas OBRIER\nAntoine MICHEL", bg ='#d3d3d3', font="Helvetica")
nameLabel.grid(row = 2, column = 0, sticky = 'w',padx = 1, pady = 1)


introFrame.columnconfigure(index = 0, pad = 20, weight = 1)
introFrame.rowconfigure(index = 0, pad = 20, weight = 4)
introFrame.rowconfigure(index = 1, pad = 20, weight = 2)
introFrame.rowconfigure(index = 2, pad = 20, weight = 1)


# Buttons part
boutonsFrame = Frame(mainFrame, bg = '#d3d3d3')
boutonsFrame.grid(row = 0, column = 1, sticky = 'nsew',padx = 10, pady = 20)
boutonsFrame.grid_propagate(False)

    # functions
def loadSimplePendulum() :
    mainFrame.grid_remove()
    rootSimple.grid(sticky = 'nsew')

def loadForcedSimplePendulum() :
    mainFrame.grid_remove()
    rootForcedSimple.grid(sticky = 'nsew')

def loadDoublePendulum() :
    mainFrame.grid_remove()
    rootDouble.grid(sticky = 'nsew')

def loadForcedDoublePendulum() :
    mainFrame.grid_remove()
    rootForcedDouble.grid(sticky = 'nsew')
    # buttons
sPenduleBouton = Button(boutonsFrame, text = "Simple pendulum", command = loadSimplePendulum, bg = '#cbb9aa', font = ('Helvetica',15))
sPenduleBouton.grid(row = 0, column = 0, sticky = 'nsew',padx = 20, pady = 20)
sPenduleBouton.grid_propagate(False)

sfPenduleBouton = Button(boutonsFrame, text = "Forced simple\npendulum", command = loadForcedSimplePendulum, bg = '#cbb9aa', font = ('Helvetica',15))
sfPenduleBouton.grid(row = 0, column = 1, sticky = 'nsew',padx = 20, pady = 20)
sfPenduleBouton.grid_propagate(False)

dPenduleBouton = Button(boutonsFrame, text = "Double pendulum",command = loadDoublePendulum, bg = '#cbb9aa', font = ('Helvetica',15))
dPenduleBouton.grid(row = 1, column = 0, sticky = 'nsew',padx = 20, pady = 20)
dPenduleBouton.grid_propagate(False)

dfPenduleBouton = Button(boutonsFrame, text = "Forced double\npendulum", command=loadForcedDoublePendulum, bg = '#cbb9aa', font = ('Helvetica',15))
dfPenduleBouton.grid(row = 1, column = 1, sticky = 'nsew',padx = 20, pady = 20)
dfPenduleBouton.grid_propagate(False)

boutonsFrame.columnconfigure(index = 0, pad = 20, weight = 1)
boutonsFrame.columnconfigure(index = 1, pad = 20, weight = 1)
boutonsFrame.rowconfigure(index = 0, pad = 20, weight = 1)
boutonsFrame.rowconfigure(index = 1, pad = 20, weight = 1)

mainFrame.rowconfigure(index = 0, pad = 20, weight=1)
mainFrame.columnconfigure(index = 0, pad = 20, weight=2)
mainFrame.columnconfigure(index = 1, pad = 20, weight=1) 