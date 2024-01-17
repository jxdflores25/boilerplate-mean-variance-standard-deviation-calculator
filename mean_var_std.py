import numpy as np

def calculate(list):

  calculations={}
  
  if len(list) != 9:
    #Error al no tener la cantidad de numeros especificado
    raise ValueError('List must contain nine numbers.')

  else:
    #Crea y redimensiona la lista 
    a = np.array(list)
    b = a.reshape(3,3)

    #Se realizan los calculos deseados
    mean=[np.mean(b,axis=0,).tolist(),np.mean(b,axis=1).tolist(),np.mean(b)]
    variance=[np.var(b,axis=0,).tolist(),np.var(b,axis=1).tolist(),np.var(b)]
    standard_deviation=[np.std(b,axis=0,).tolist(),np.std(b,axis=1).tolist(),np.std(b)]
    max=[np.max(b,axis=0,).tolist(),np.max(b,axis=1).tolist(),np.max(b)]
    min=[np.min(b,axis=0,).tolist(),np.min(b,axis=1).tolist(),np.min(b)]
    sum=[np.sum(b,axis=0,).tolist(),np.sum(b,axis=1).tolist(),np.sum(b)]

    #Se guarda todo en un diccionario
    calculations={
      'mean': mean,
      'variance': variance,
      'standard deviation': standard_deviation,
      'max': max,
      'min': min,
      'sum': sum
    }

  #Se devuelve los datos encontrados
  return calculations