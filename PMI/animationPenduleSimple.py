"""
Animation pendule simple
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.integrate import solve_ivp

n = 500
g = 9.81

def animateSimplePendulum(theta, t, l) :
    x = l*np.sin(theta)
    y = -l*np.cos(theta)

    #set up du graphe
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-3, 3), ylim=(-3, 3))
    ax.grid()

    #creation de la ligne, texte
    ligne, = ax.plot([],[],'o-', lw=2)
    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    #initialisation des tracés
    def init():
        ligne.set_data([],[])
        time_text.set_text('')
        return ligne, time_text

    #update de l'animation
    def anim(i):
        ligne.set_data([0,x[i]],[0,y[i]]) #ligne entre origine et la masse
        time_text.set_text('time = {:.2f}'.format(t[i])) #temps

        return ligne, time_text

    #creation d'animation objet
    ani = animation.FuncAnimation(fig, anim, frames=len(t),
                                interval=n*t[-1]/len(t), blit=True, init_func=init)

    plt.show()

def animateSimpleForcedPendulum(varList) :
    theta0, l, t0, w, thetaPoint0, n0, ti, A = varList 
    t = np.linspace(t0, ti, n)

    #equation
    def pendul_simple_force(t, y, l, m, A, w):
        phi, phi_point = y
        dydt = [phi_point, ((w**2)*np.sin(w*t)-g)*(np.sin(phi)/l)]

        return dydt

    #conditions initiales
    phi0=np.pi/4
    phi0_point=0

    #Résolution de l'EDO
    y=solve_ivp(pendul_simple_force, [0,20],[phi0,phi0_point],args=(l,1,A,w),t_eval=t).y

    #x et y de la masse et du point d'accroche
    x = l*np.sin(y[0])
    y = -l*np.cos(y[0])

    xO = 0
    yO = A*np.sin(w*t)

    #set up du graphe
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-3, 3), ylim=(-3, 3))
    ax.grid()

    #creation de la ligne, texte
    ligne, = ax.plot([],[],'o-', lw=2)
    time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    #initialisation des tracés
    def init():
        ligne.set_data([],[])
        time_text.set_text('')
        return ligne, time_text

    #update de l'animation
    def anim(i):
        ligne.set_data([xO,x[i]],[yO[i],yO[i]+y[i]]) #ligne entre origine et la masse
        time_text.set_text('time = {:.2f}'.format(t[i])) #temps

        return ligne, time_text

    #creation d'animation objet
    ani = animation.FuncAnimation(fig, anim, frames=len(t),
                                interval=n*t[-1]/len(t), blit=True, init_func=init)

    plt.show()