###############################################
##### Resolution analytique pendule simple ####
###############################################

import numpy as np

g = 9.81 # constante de gravitation


def solveSimplePendulum(theta0, thetaPoint0, l, n, a, b) :
    """solve the simple pendulum equation with Euler method

    Returns:
        float array * float array * float array: return theta, thetaPoint and the time
    """
    eps = (b - a)/n
    t = np.linspace(a,b,n)
    theta = np.zeros(n)
    thetaPoint = np.zeros(n)
    theta[0] = theta0
    thetaPoint[0] = thetaPoint0

    for i in range(1,n) :
        thetaPoint[i] = thetaPoint[i-1] - eps * g/l * np.sin(theta[i-1])
        theta[i] = theta[i-1] + eps * thetaPoint[i]

    return theta, thetaPoint, t

def solveForcedSimplePendulum(varList) :
    """solve the forced simple pendulum equation with Euler method

    Returns:
        float array * float array * float array: return theta, thetaPoint and the time
    """
    theta0, l, a, w, thetaPoint0, n0, b, A = varList
    n = int(n0)
    eps = (b - a)/n
    t = np.linspace(int(a), int(b),n)
    theta = np.zeros(n)
    thetaPoint = np.zeros(n)
    theta[0] = np.radians(theta0)
    thetaPoint[0] = thetaPoint0

    for i in range(1,n) :
        thetaPoint[i] = thetaPoint[i-1] + eps * (-g/l + w**2/l * A * np.sin(w*t[i])) * np.sin(theta[i-1]) 
        theta[i] = theta[i-1] + eps * thetaPoint[i]

    return theta, thetaPoint, t