"""
Animation du double pendule forcé
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.integrate import solve_ivp

# equation pour phi1_point et phi2_point

def ani() :
    def double_pendule(t, y, l1, l2, m1, m2,A,w):
        phi1, phi1_point, phi2, phi2_point = y
        c=np.cos(phi1-phi2)
        s=np.sin(phi1-phi2)

        phi1_point_point=(3*m2*(l2**2)*(phi2_point**2)*s+phi1_point*phi2_point*2*m1*(l2**2)-(phi1**2)*s*(m2*(l2**2)-2*m2*l1*l2*c)
        -l2*m2*A*w*phi1_point*np.cos(w*t)*np.cos(phi1)-(m1+m2)*l2*g*np.sin(phi1)+m2*l2*g*c*np.sin(phi2))/(l2*((m1+3*m2)*l1+3*m2*l2*c-2*m2*l2*l1*(c**2)))

        phi2_point_point=((-2*l1*(phi1_point**2)-g*np.sin(phi2))/l2)-((2*l1*c)/(l2))*phi1_point_point

        dydt = [phi1_point,phi1_point_point,phi2_point,phi2_point_point]
        return dydt

    # Paramètre pendule
    l1 = 1  
    l2 = 1  
    m1 = 1  
    m2 = 1  
    g = 9.8 

    #Parèmetre origine
    A=0.25
    w=1

    # Conditions initiales
    phi1_0 = np.pi/4 
    phi1_point_0 = 0    
    phi2_0 = np.pi/4  
    phi2_point_0 = 0   

    # Résolution de l'EDO
    #Utilisation de solve_ivp qui utilise RK4
    dt = 500
    t = np.linspace(0, 20, dt)
    y = solve_ivp(double_pendule, [0, 20], [phi1_0, phi1_point_0, phi2_0, phi2_point_0], args=(l1, l2, m1, m2,A,w), t_eval=t).y

    # x et y de chaques masses
    x1 = l1*np.sin(y[0])
    y1 = -l1*np.cos(y[0])
    x2 = x1 + l2*np.sin(y[2])
    y2 = y1 - l2*np.cos(y[2])

    xO = 0
    yO = A*np.sin(w*t)

    # set up du graphe
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
                                interval=dt*t[-1]/len(t), blit=True, init_func=init)

    # show l'animation
    plt.show()


""" NE FONCTIONNE PAS
# Création fichier .mp4, dpi = résolution, fps = im/s
name = "c://Utilisateurs/MICHEL/Vidéos/animation.gif"
writergif = animation.PillowWriter(fps=30)
ani.save(filename= name, writer=writergif)
"""
