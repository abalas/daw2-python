# Referencia completa de funciones del módulo random en Python
# Este archivo sirve para tenerlo como guía durante estudios y exámenes
import random

import aleatorio

# 1. random.random()
# Genera un número flotante aleatorio en el rango [0.0, 1.0)
numero_aleatorio = random.random()
print("random():", numero_aleatorio)

# 2. random.uniform(a, b)
# Genera un número flotante aleatorio entre a y b (ambos incluidos)
numero_uniforme = random.uniform(5, 10)
print("uniform(5, 10):", numero_uniforme)

# 3. random.randint(a, b)
# Devuelve un entero aleatorio N tal que a <= N <= b
numero_entero = random.randint(1, 100)
print("randint(1, 100):", numero_entero)

# 4. random.randrange(start, stop[, step])
# Devuelve un entero seleccionado de range(start, stop, step)
numero_rango = random.randrange(0, 10, 2)  # solo pares entre 0 y 8
print("randrange(0, 10, 2):", numero_rango)

# 5. random.choice(seq)
# Selecciona un elemento aleatorio de una secuencia (lista, tupla, string)
lista = [10, 20, 30, 40]
elemento = random.choice(lista)
print("choice([10,20,30,40]):", elemento)

# 6. random.choices(population, weights=None, k=1)
# Selecciona k elementos aleatorios de la población con reemplazo, opcionalmente ponderados
poblacion = ['a','b','c']
elegidos = random.choices(poblacion, k=5)
print("choices(['a','b','c'], k=5):", elegidos)

# 7. random.sample(population, k)
# Selecciona k elementos distintos de la población sin reemplazo
muestra = random.sample(lista, 3)
print("sample([10,20,30,40], 3):", muestra)

# 8. random.shuffle(x)
# Mezcla la lista x in-place (modifica la lista original)
lista_mezclada = [1,2,3,4,5]
random.shuffle(lista_mezclada)
print("shuffle([1,2,3,4,5]):", lista_mezclada)

# 9. random.seed(a=None)
# Inicializa el generador de números aleatorios para reproducibilidad
random.seed(123)
print("random.random() con semilla 123:", random.random())

# 10. random.getrandbits(k)
# Devuelve un entero con k bits aleatorios
bits = random.getrandbits(8)  # número de 8 bits
print("getrandbits(8):", bits)

# 11. random.betavariate(alpha, beta)
# Distribución Beta, útil en simulaciones estadísticas
beta_valor = random.betavariate(2, 5)
print("betavariate(2,5):", beta_valor)

# 12. random.expovariate(lambd)
# Distribución exponencial
exp_valor = random.expovariate(1.5)
print("expovariate(1.5):", exp_valor)

# 13. random.gammavariate(alpha, beta)
# Distribución gamma
gamma_valor = random.gammavariate(2, 2)
print("gammavariate(2,2):", gamma_valor)

# 14. random.gauss(mu, sigma)
# Distribución normal (Gaussiana) con media mu y desviación sigma
gauss_valor = random.gauss(0,1)
print("gauss(0,1):", gauss_valor)

# 15. random.lognormvariate(mu, sigma)
# Distribución log-normal
lognorm_valor = random.lognormvariate(0,1)
print("lognormvariate(0,1):", lognorm_valor)

# 16. random.vonmisesvariate(mu, kappa)
# Distribución de Von Mises (angular)
von_valor = random.vonmisesvariate(0,1)
print("vonmisesvariate(0,1):", von_valor)

# 17. random.paretovariate(alpha)
# Distribución de Pareto
pareto_valor = random.paretovariate(1.5)
print("paretovariate(1.5):", pareto_valor)

# 18. random.weibullvariate(alpha, beta)
# Distribución Weibull
weibull_valor = random.weibullvariate(1, 1.5)
print("weibullvariate(1,1.5):", weibull_valor)

# Fin de la referencia completa del módulo randomda