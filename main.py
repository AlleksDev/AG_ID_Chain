import matplotlib.pyplot as plt
import random

def generar_individuo(longitud, valores_posibles):
    individuo = random.sample(valores_posibles, min(longitud, len(valores_posibles)))
    vacios = [None] * (longitud - len(individuo))
    individuo += vacios
    random.shuffle(individuo)
    return individuo

def generar_poblacion(num_individuos, longitud_cromosoma, valores_posibles):
    poblacion = []
    for ind in range(num_individuos):
        individuo = generar_individuo(longitud_cromosoma, valores_posibles)
        poblacion.append(individuo)
    
    return poblacion

def evaluar_individuo(individuo, vals_posiciones, valores_posibles):
    total = 0
    for idx, gene in enumerate(individuo):
        if gene is not None:
            peso = vals_posiciones.get(idx, 0)
            masa = valores_posibles.get(gene, 0)
            print(f"Posición: {idx}, Gene: {gene}, Masa: {masa}, Peso: {peso}")
            total += masa * peso
    return abs(total)

def main():
    num_individuos = 10
    valores_posibles = {
        1: 12.0,
        2: 15.5,
        3: 20.3,
        4: 7.8,
    }
    vals_posiciones = {
        0: -1,
        1: 0,
        2: 1,
    }
    
    poblacion = generar_poblacion(num_individuos, len(vals_posiciones), list(valores_posibles.keys()))
    print(poblacion[0])
    print("Aptitud", evaluar_individuo(poblacion[0], vals_posiciones, valores_posibles))
    for idx, individuo in enumerate(poblacion):
        print(f"Individuo {idx + 1}: {individuo}")
    
    

if __name__ == "__main__":
    main()