# Crea una funzione denominata calculate() in mean_var_std.py
# L'input della funzione dovrebbe essere una lista contenente 9 cifre.
# La funzione converte la lista in un array Numpy 3x3, quindi restituisce
# un dizionario contenente la media, varianza, deviazione standard, numero massimo, numero minimo,
# e somma su entrambi gli assi e per la matrice appiattita.
#
import numpy as np    # Importa la libreria Numpy.

def jls_extract_def():
    # Restituisce il dizionario dei calcoli.
    return 


def calculate(list):    # Definisce la funzione.

    # Se nella funzione viene passato un elenco contenente meno di 9 elementi, solleva un'eccezione
    # ValueError con il messaggio: 'List must contain nine numbers.'
    #
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        array = np.array(list)    # Converte il parametro list in un array di Numpy.
        array3x3 = np.reshape(array, (3, 3))    # Trasforma l'array di dimensione 9 in un array 3x3.
        calculations = {}
        mean_list = var_list = std_list = max_list = min_list = sum_list = []
        mean_axis1 = var_axis1 = std_axis1 = max_axis1 = min_axis1 = sum_axis1 = []
        mean_axis2 = var_axis2 = std_axis2 = max_axis2 = min_axis2 = sum_axis2 = []

        # I valori nel dizionario restituito sono liste e non array Numpy.
        #
        mean_axis1 = np.mean(array3x3, axis=0).tolist()    # Calcola la media lungo gli assi verticali.
        var_axis1 = np.var(array3x3, axis=0, dtype=np.float64).tolist()    # Calcola la varianza lungo gli assi verticali.
        std_axis1 = np.std(array3x3, axis=0).tolist()    # Calcola la dev. standard lungo gli assi verticali.
        max_axis1 = np.max(array3x3, axis=0).tolist()    # Calcola il massimo lungo gli assi verticali.
        min_axis1 = np.min(array3x3, axis=0).tolist()    # Calcola la minimo lungo gli assi verticali.
        sum_axis1 = np.sum(array3x3, axis=0).tolist()    # Calcola la somma lungo gli assi verticali.

        # I valori nel dizionario restituito sono liste e non array Numpy.
        #
        mean_axis2 = np.mean(array3x3, axis=1).tolist()    # Calcola la media lungo gli assi orizzontali.
        var_axis2 = np.var(array3x3, axis=1, dtype=np.float64).tolist()    # Calcola la varianza lungo gli assi orizzontali.
        std_axis2 = np.std(array3x3, axis=1).tolist()    # Calcola la dev. standard lungo gli assi orizzontali.
        max_axis2 = np.max(array3x3, axis=1).tolist()    # Calcola il massimo lungo gli assi orizzontali.
        min_axis2 = np.min(array3x3, axis=1).tolist()    # Calcola la minimo lungo gli assi orizzontali.
        sum_axis2 = np.sum(array3x3, axis=1).tolist()    # Calcola la somma lungo gli assi orizzontali.

        # I valori nel dizionario restituito sono liste e non array Numpy.
        #
        mean_flattened = np.mean(array).tolist()
        var_flattened = np.var(array, dtype=np.float64).tolist()
        std_flattened = np.std(array).tolist()
        max_flattened = np.max(array).tolist()
        min_flattened = np.min(array).tolist()
        sum_flattened = np.sum(array).tolist()
    
        mean_list.append(mean_axis1)
        mean_list.append(mean_axis2)
        mean_list.append(mean_flattened)
    
        var_list.append(var_axis1)
        var_list.append(var_axis2)
        var_list.append(var_flattened)
    
        std_list.append(std_axis1)
        std_list.append(std_axis2)
        std_list.append(std_flattened)
    
        max_list.append(max_axis1)
        max_list.append(max_axis2)
        max_list.append(max_flattened)
    
        min_list.append(min_axis1)
        min_list.append(min_axis2)
        min_list.append(min_flattened)
    
        sum_list.append(sum_axis1)
        sum_list.append(sum_axis2)
        sum_list.append(sum_flattened)
    
        calculations['mean'] = mean_list    # Inserisce la lista dei valori di media nel dizionario.
        calculations['variance'] = var_list    # Inserisce la lista dei valori di varianza nel dizionario.
        calculations['standard deviation'] = std_list    # Inserisce la lista dei valori di dev. standard nel dizionario.
        calculations['max'] = max_list    # Inserisce la lista dei valori di massimo nel dizionario.
        calculations['min'] = min_list    # Inserisce la lista dei valori di minimo nel dizionario.
        calculations['sum'] = sum_list    # Inserisce la lista dei valori di somma nel dizionario.
        
        return calculations    # Restituisce il dizionario dei calcoli. = jls_extract_def()