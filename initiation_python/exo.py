import numpy as np
import matplotlib.pyplot as plt

tab = np.array([1, 2, 3, 
                 4, 5, 6])

# print(tab)

# fonction qui prend le tableau en entrée et renvoie la somme des éléments du tableau
def sum(orig_tab):
    return np.sum(orig_tab)

sum_tab_elmt = sum(tab)
print(sum_tab_elmt)

