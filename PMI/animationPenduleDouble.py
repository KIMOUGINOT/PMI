import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.integrate import solve_ivp
import solveurDouble as sd


# set up du graphe
def animateDoublePendulum(phi1, phi2, x1, y1, x2, y2, t) :
    n = 500
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
    ax.grid()

    # création des lignes, trajectoires etc ...
    ligne1, = ax.plot([], [], 'o-', lw=2)
    ligne2, = ax.plot([], [], 'o-', lw=2)
    traj1, = ax.plot([], [], '--', color='gray')
    traj2, = ax.plot([],[],'--',color='red')
    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    # Initialisation de chaque tracé
    def init():
        ligne1.set_data([], [])
        ligne2.set_data([], [])
        time_text.set_text('')
        traj1.set_data([],[])
        traj2.set_data([],[])
        return ligne1, ligne2, traj1, traj2, time_text

    # update de l'animation à chaque pas de temps
    def anim(i):
        # Update
        ligne1.set_data([0, x1[i]], [0, y1[i]]) #Ligne entre origine et m1
        ligne2.set_data([x1[i], x2[i]], [y1[i], y2[i]]) #Ligne entre m1 et m2
        traj1.set_data(x1[:i+1],y1[:i+1]) #Trajectoire m1
        traj2.set_data(x2[:i+1],y2[:i+1]) #Trajectoire m2
        time_text.set_text('time = {:.2f}'.format(t[i])) #temps

        return ligne1, ligne2, traj1, traj2, time_text

    # Création d'animation d'objet
    ani = animation.FuncAnimation(fig, anim, frames=len(t),
                                interval=n*t[-1]/len(t), blit=True, init_func=init)

    # show l'animation
    plt.show()

def animateForcedDoublePendulum(varList) :
    n = 500
    phi1, phi2, x1, y1, x2, y2, xO, yO, t = sd.solveForcedDoublePendulum(varList)
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-4, 4), ylim=(-4, 4))
    ax.grid()

    # création des lignes, trajectoires etc ...
    ligne1, = ax.plot([], [], 'o-', lw=2)
    ligne2, = ax.plot([], [], 'o-', lw=2)
    traj1, = ax.plot([], [], '--', color='gray')
    traj2, = ax.plot([],[],'--',color='red')
    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    # Initialisation de chaque tracé
    def init():
        ligne1.set_data([], [])
        ligne2.set_data([], [])
        time_text.set_text('')
        traj1.set_data([],[])
        traj2.set_data([],[])
        return ligne1, ligne2, traj1, traj2, time_text

    # update de l'animation à chaque pas de temps
    def anim(i):
        # Update
        ligne1.set_data([xO, x1[i]], [yO[i], yO[i]+y1[i]]) #Ligne entre origine et m1
        ligne2.set_data([x1[i], x2[i]], [yO[i]+y1[i], yO[i]+y2[i]]) #Ligne entre m1 et m2
        traj1.set_data(x1[:i+1],yO[:i+1]+y1[:i+1]) #Trajectoire m1
        traj2.set_data(x2[:i+1],yO[:i+1]+y2[:i+1]) #Trajectoire m2
        time_text.set_text('time = {:.2f}'.format(t[i])) #temps

        return ligne1, ligne2, traj1, traj2, time_text

    # Création d'animation d'objet
    ani = animation.FuncAnimation(fig, anim, frames=len(t),
                                interval=n*t[-1]/len(t), blit=True, init_func=init)

    # show l'animation
    plt.show()