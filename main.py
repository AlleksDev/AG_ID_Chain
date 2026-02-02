import matplotlib.pyplot as plt
import random

def generar_individuo(longitud, valores_posibles):
    individuo = random.sample(valores_posibles, min(longitud, len(valores_posibles)))
    vacios = [None] * (longitud - len(individuo))
    individuo += vacios
    random.shuffle(individuo)
    return individuo

def generar_poblacion(num_individuos, longitud_cromosoma):
    poblacion = []
    for ind in range(num_individuos):
        individuo = generar_individuo(longitud_cromosoma, valores_posibles=[0, 1, 5])
        poblacion.append(individuo)
    
    return poblacion

def main():
    num_individuos = 10
    longitud_cromosoma = 5
    valores_posibles = [0, 1, 2, 3, 4, 5]
    
    poblacion = generar_poblacion(num_individuos, longitud_cromosoma)
    
    for idx, individuo in enumerate(poblacion):
        print(f"Individuo {idx + 1}: {individuo}")
    
    

if __name__ == "__main__":
    main()