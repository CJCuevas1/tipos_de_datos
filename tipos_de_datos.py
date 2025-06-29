# ===================================================================
# Este programa ejecuta el cálculo del área para un rectángulo.
# El sistema solicita los datos y presenta el resultado final.
# ===================================================================
# Este programa ejecuta el cálculo del área para un rectángulo.

# Esta función presenta la lógica principal del cálculo.
def calcular_area(base_figura, altura_figura):
    resultado = base_figura * altura_figura
    return resultado

# En este bloque inicia el programa.

# Esta variable almacena el nombre del usuario.
nombre_usuario = input("Ingrese su nombre: ")

try:
    medida_base = float(input(f"Hola {nombre_usuario}, ingrese la base del rectángulo: "))
    medida_altura = float(input("Ahora, ingrese la altura del rectángulo: "))
except ValueError:
    # Este bloque gestiona los errores de entrada.
    print("Error: El valor ingresado no es un número válido.")
    exit()

# Esta línea invoca la función para procesar los datos.
area_calculada = calcular_area(medida_base, medida_altura)

# Esta variable booleana controla la visualización del resultado.
decision = input("¿Desea ver el resultado completo? (s/n): ")
ver_completo = (decision.lower() == 's')


# Se presentan los resultados 
print("\n-------------------------------------------")

# En caso de presionar 's', se ejecuta este bloque.
if ver_completo:
    print("      --- Resultado Completo ---")
    print(f"Cálculo solicitado por: {nombre_usuario}")
    print(f"Para un rectángulo de base {medida_base} y altura {medida_altura}:")
    print(f"El área final es: {area_calculada}")

# En caso de presionar otra tecla como 'n', se ejecuta este.
else:
    print("      --- Resultado Simple ---")
    print(f"Área: {area_calculada}")

print("-------------------------------------------")