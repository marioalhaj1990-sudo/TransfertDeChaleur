from tdc_fct import *

lambdas = [-0.5, 0, 0.5] # Valeurs demandées [cite: 63]

for l in lambdas:
    Matrice_T = cas_3(l)
    
    # Création du maillage pour plot_surface [cite: 79, 82]
    X_grid, T_grid = np.meshgrid(t, x)
    
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(T_grid, X_grid, Matrice_T, cmap=cm.coolwarm , antialiased=False , alpha = 0.5)


    ax.set_title(f"Profil de température Cas 3 (lambda = {l})")
    ax.set_xlabel("Espace x")
    ax.set_ylabel("Temps t")
    ax.set_zlabel("Température T")
    fig.colorbar(surf, shrink=0.5, aspect=15)
    plt.show()
