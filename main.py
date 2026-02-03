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

def evaluar_poblacion(poblacion, vals_posiciones, valores_posibles):
    aptitudes = []
    for individuo in poblacion:
        aptitud = evaluar_individuo(individuo, vals_posiciones, valores_posibles)
        aptitudes.append((individuo, aptitud))
    return aptitudes

def generar_parejas(poblacion, prob_cruza):
    if not poblacion:
        raise ValueError("La población no puede estar vacía.")
    
    parejas = []
    n = len(poblacion)
    
    for i in range(n):
        for j in range(n):
            if i!= j and random.random() < prob_cruza:
                parejas.append((poblacion[i], poblacion[j]))
    
    return parejas

def cruzar_segmentos(padre1, padre2, puntos_corte):
    puntos = [0] + sorted(puntos_corte) + [len(padre1)]
    hijo1 = []
    hijo2 = []
    alternar = True
    for i in range(len(puntos)-1):
        ini, fin = puntos[i], puntos[i+1]
        if alternar:
            hijo1 += padre1[ini:fin]
            hijo2 += padre2[ini:fin]
        else:
            hijo1 += padre2[ini:fin]
            hijo2 += padre1[ini:fin]
        alternar = not alternar
    return hijo1, hijo2

def eliminar_repetidos_hijo(hijo, padre):
    hijo_limpio = hijo.copy()
    padre2 = padre[1] if isinstance(padre, tuple) else None
    if padre2 is not None:
        padre_unicos = list(set(list(padre[0]) + list(padre2)))
    else:
        padre_unicos = list(set(padre))
    valores_hijo = [g for g in hijo_limpio if g is not None]
    padre_menos_hijo = [v for v in padre_unicos if v not in valores_hijo]
    vistos = set()
    for i, gene in enumerate(hijo_limpio):
        if gene is not None:
            if gene in vistos:
                if padre_menos_hijo:
                    nuevo = random.choice(padre_menos_hijo)
                    hijo_limpio[i] = nuevo
                    padre_menos_hijo.remove(nuevo)
                else:
                    hijo_limpio[i] = None
            else:
                vistos.add(gene)
    return hijo_limpio

def cruzar(padre1, padre2):
    longitud = len(padre1)
    n_puntos = random.randint(1, longitud - 1)
    puntos = random.sample(range(1, longitud-2), n_puntos)
    puntos.sort()
    
    hijo1, hijo2 = cruzar_segmentos(padre1, padre2, puntos)
    hijo1 = eliminar_repetidos_hijo(hijo1, padre1)
    hijo2 = eliminar_repetidos_hijo(hijo2, padre2)
    return hijo1, hijo2

def mutar(individuo, prob_mut_ind, prob_mut_gen, valores_posibles):
    individuo_mutado = individuo.copy()
    if random.random() >= prob_mut_ind:
        return individuo_mutado

    for i in range(len(individuo_mutado)):
        if random.random() < prob_mut_gen and individuo_mutado[i] is not None:
            tipo_mut = random.choice(["reemplazo", "intercambio"])
            
            if tipo_mut == "reemplazo":
                valores_disponibles = [v for v in valores_posibles if v not in individuo_mutado]
                if valores_disponibles:
                    nuevo_valor = random.choice(valores_disponibles)
                    individuo_mutado[i] = nuevo_valor
                else:
                    tipo_mut = "intercambio"
            
            if tipo_mut == "intercambio":
                indices_validos = [j for j in range(len(individuo_mutado)) if j != i and individuo_mutado[j] is not None]
                if indices_validos:
                    j = random.choice(indices_validos)
                    individuo_mutado[i], individuo_mutado[j] = individuo_mutado[j], individuo_mutado[i]
    return individuo_mutado

def poda(aptitudes, tam_poblacion):
    # aptitudes: lista de tuplas (individuo, aptitud)
    if not aptitudes:
        return []
    # Ordenar por aptitud (menor es mejor si es minimización)
    aptitudes_ordenadas = sorted(aptitudes, key=lambda x: x[1])
    mejor = aptitudes_ordenadas[0][0]
    restantes = [ind for ind, _ in aptitudes_ordenadas[1:]]
    seleccionados = [mejor]
    if len(restantes) > 0:
        seleccionados += random.sample(restantes, min(tam_poblacion-1, len(restantes)))
    return seleccionados

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
    
    aptitudes = evaluar_poblacion(poblacion, vals_posiciones, valores_posibles)

if __name__ == "__main__":
    main()