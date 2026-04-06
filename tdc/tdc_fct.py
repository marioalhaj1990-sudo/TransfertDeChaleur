import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Données
rho = 2.0          # Masse volumique 
Cp = 0.9           # Capacité thermique 
k0 = 0.2           # Conductivité de base 
tf = 12.0          # Temps final 
x_start, x_end = 1.0, 3.0 # Domaine spatial 

# Choix des pas 
dx = 0.05          
dt = 0.1           
nx = int((x_end - x_start) / dx) + 1      #nb total de points selon x
nt = int(tf / dt) + 1                     #nb total de points selon t

x = np.linspace(x_start, x_end, nx)
t = np.linspace(0, tf, nt)

# FONCTION POUR LE CAS 3
def cas_3(lambda_val):
    # Initialisation de la matrice de résultats (T[espace, temps]) 
    T = np.zeros((nx, nt))
    
    # Condition initiale 
    T[:, 0] = 2 - (x - 1)/2 + (x - 1)*(x - 3)
    
    # Boucle temporelle (Euler semi-implicite)
    for n in range(0, nt - 1):
        # Température au temps actuel
        Tn = T[:, n]
        
        # Calcul de la conductivité locale k(T) 
        k = k0 * np.exp(lambda_val * Tn)
        
        # Construction du système A * T_futur = B
        A = np.zeros((nx, nx))
        B = np.zeros(nx)
        
        # Points intérieurs (Différences finies 2ème ordre) 
        for i in range(1, nx - 1):
            alpha = (k[i] * dt) / (rho * Cp * dx**2)
            
            # Matrice A (termes implicites pour la courbure)
            A[i, i-1] = -alpha
            A[i, i]   = 1 + 2*alpha
            A[i, i+1] = -alpha
            
            # Vecteur B (terme source non-linéaire calculé au temps n)
            pente_carre = ((Tn[i+1] - Tn[i-1]) / (2*dx))**2
            terme_lambda = lambda_val * alpha * (dx**2) * pente_carre
            B[i] = Tn[i] + terme_lambda
            
        # Conditions limites (Dirichlet) 
        A[0, 0] = 1.0
        B[0] = 2.0
        A[-1, -1] = 1.0
        B[-1] = 1.0
        print(B)
        # Résolution du système linéaire 
        T[:, n+1] = np.linalg.solve(A, B)
        
    return T
