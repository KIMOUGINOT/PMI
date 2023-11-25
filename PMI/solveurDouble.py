##################################
#### Double pendulum solving #####
##################################

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.integrate import solve_ivp

g = 9.81

# equation for phi1_point and phi2_point
def double_pendule(t, y, l1, l2, m1, m2):
    phi1, phi1_point, phi2, phi2_point = y
    dydt = [phi1_point,
            (m2*g*np.sin(phi2)*np.cos(-phi1+phi2) - m2*l1*phi1_point**2*np.sin(phi2-phi1)*np.cos(phi2-phi1) - (m1+m2)*g*np.sin(phi1))/(m1 + m2*np.sin(phi2-phi1)**2),
            phi2_point,
            (m1*l1*phi1_point**2*np.sin(phi2-phi1) - m1*g*np.sin(phi1)*np.cos(phi2-phi1) + m2*g*np.sin(phi2))/(l2*(m1 + m2*np.sin(phi2-phi1)**2))]
    return dydt

# ODE solving
#Utilisation de solve_ivp qui utilise RK4
def solveDoublePendulum(varList): 
    phi1_0, phi1_point_0, l1, m1, t0, phi2_0, phi2_point_0, l2, m2, ti = varList   
    phi1_0 = np.radians(phi1_0)
    phi2_0 = np.radians(phi2_0)
    n = 500
    t = np.linspace(int(t0), int(ti), n)
    y = solve_ivp(double_pendule, [int(t0), int(ti)], [phi1_0, phi1_point_0, phi2_0, phi2_point_0], args=(l1, l2, m1, m2), t_eval=t).y

    # x et y de chaques masses
    x1 = l1*np.sin(y[0])
    y1 = -l1*np.cos(y[0])
    x2 = x1 + l2*np.sin(y[2])
    y2 = y1 - l2*np.cos(y[2])
    return y[0], y[2], x1, y1, x2, y2, t

def double_pendulef(t, y, l1, l2, m1, m2,A,w):
    phi1, phi1_point, phi2, phi2_point = y
    c=np.cos(phi1-phi2)
    s=np.sin(phi1-phi2)

    phi1_point_point=(3*m2*(l2**2)*(phi2_point**2)*s+phi1_point*phi2_point*2*m1*(l2**2)-(phi1**2)*s*(m2*(l2**2)-2*m2*l1*l2*c)
    -l2*m2*A*w*phi1_point*np.cos(w*t)*np.cos(phi1)-(m1+m2)*l2*g*np.sin(phi1)+m2*l2*g*c*np.sin(phi2))/(l2*((m1+3*m2)*l1+3*m2*l2*c-2*m2*l2*l1*(c**2)))

    phi2_point_point=((-2*l1*(phi1_point**2)-g*np.sin(phi2))/l2)-((2*l1*c)/(l2))*phi1_point_point

    dydt = [phi1_point,phi1_point_point,phi2_point,phi2_point_point]
    return dydt

def solveForcedDoublePendulum(varlist) :
    n = 500
    phi1_0, phi1_point_0, l1, m1, t0, w, phi2_0, phi2_point_0, l2, m2, ti, A = varlist
    t = np.linspace(int(t0), int(ti), n)
    y = solve_ivp(double_pendulef, [t0, ti], [phi1_0, phi1_point_0, phi2_0, phi2_point_0], args=(l1, l2, m1, m2,A,w), t_eval=t).y
    # x et y de chaques masses
    x1 = l1*np.sin(y[0])
    y1 = -l1*np.cos(y[0])
    x2 = x1 + l2*np.sin(y[2])
    y2 = y1 - l2*np.cos(y[2])

    xO = 0
    yO = A*np.sin(w*t)
    return y[0], y[2], x1, y1, x2, y2, xO, yO, t