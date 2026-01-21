"""
=============================================
 CÁLCULO DE LA CONSTANTE DE KAPREKAR (6174)
---------------------------------------------
 Autor: ChatGPT (GPT-5)
 Descripción:
   Este programa aplica el proceso de Kaprekar:
   - Se toma un número de 4 cifras (pueden repetirse dígitos).
   - No se permiten los números con los 4 dígitos iguales.
   - Se ordenan las cifras en orden ascendente y descendente.
   - Se resta el menor al mayor.
   - Se repite hasta llegar a la constante 6174.
=============================================
"""

# ---------------------------------------------------------------
# FUNCION 1: Calcula un paso del proceso de Kaprekar
# ---------------------------------------------------------------
def kaprekar(num: int) -> int:
    """Devuelve el siguiente número en el proceso de Kaprekar."""

    # Convertimos el número en cadena de 4 dígitos (rellenando con ceros si hace falta)
    s = f"{num:04d}"

    # Ordenamos los dígitos en orden ascendente (ej: 3524 → 2345)
    asc = int("".join(sorted(s)))

    # Ordenamos los dígitos en orden descendente (ej: 3524 → 5432)
    desc = int("".join(sorted(s, reverse=True)))

    # Calculamos la diferencia entre ambos
    resultado = desc - asc

    # Mostramos la operación en pantalla (siempre en 4 dígitos)
    print(f"{desc:04d} - {asc:04d} = {resultado:04d}")

    # Devolvemos el resultado (será el nuevo número en la siguiente iteración)
    return resultado


# ---------------------------------------------------------------
# FUNCION 2: Controla todo el proceso, entrada y repeticiones
# ---------------------------------------------------------------
def proceso_kaprekar():
    """Ejecuta el proceso completo de Kaprekar con validaciones."""

    while True:
        # Solicitamos al usuario el número de 4 cifras
        numero = input("Introduce un número de 4 cifras: ")

        # 1️⃣ Validamos que solo tenga números
        if not numero.isdigit():
            print("❌ Debes introducir solo números.")
            continue  # Vuelve a pedir el número

        # 2️⃣ Validamos que tenga exactamente 4 cifras
        if len(numero) != 4:
            print("❌ El número debe tener exactamente 4 cifras.")
            continue

        # 3️⃣ Validamos que no tenga los 4 dígitos iguales
        # Ejemplo: 1111 o 7777 no sirven porque se quedan en 0000
        if len(set(numero)) == 1:
            print("❌ Los cuatro dígitos no pueden ser iguales.")
            continue

        # ✅ Si pasa todas las comprobaciones, salimos del bucle
        break

    # Convertimos el número válido a entero
    n = int(numero)

    # Contador de iteraciones
    contador = 0

    print("\n--- Proceso de Kaprekar ---")

    # 🔁 Mientras no lleguemos a la constante 6174...
    while n != 6174:
        n = kaprekar(n)   # Aplicamos un paso del proceso
        contador += 1     # Contamos cuántas veces se repite

    # Cuando termina el bucle, mostramos el resultado final
    print(f"\n✅ Se ha alcanzado la constante de Kaprekar (6174) en {contador} iteraciones.")


# ---------------------------------------------------------------
# PUNTO DE ENTRADA DEL PROGRAMA
# ---------------------------------------------------------------
# Esta parte hace que el programa solo se ejecute si lo lanzas directamente,
# y no si lo importas como módulo desde otro archivo.
if __name__ == "__main__":
    proceso_kaprekar()
