####################################
#### calcul d'energie cinétique ####
####################################

import numpy as np

g = 9.81 # constante de gravitation

def EcSimple(thetaPoint, l, m) :
    return 1/2 * m * (l * thetaPoint)**2

def EpSimple(theta, l, m) :
    return m * g * l * (1 - np.cos(theta))

def EpForcedSimple(theta, t, l, m, w, A) :
    return -m * g * l * np.cos(theta) + m * (w**2) * A * np.sin(w*t) * l * np.cos(theta) - (-m*g*l*np.cos(theta[0]) + m*(w**2)*A*np.sin(w*t[0])*l*np.cos(theta[0]))