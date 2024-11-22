
from clases import Detector, Radiacion, Virus, Sanador

def main():
    while True:

        print("Ingrese el ADN en formato de matriz 6x6 (6 filas de 6 caracteres):")
        print("Solo es posible ingresar los caracteres A, C, T, G")

        adn = []
        while len(adn) < 6:
            fila = input(f"Fila {len(adn) + 1}: ").upper()
            if len(fila) != 6:
                print("Error: Cada fila debe tener exactamente 6 caracteres.")
                continue

            if not all(c in ['A', 'T', 'C', 'G'] for c in fila):
                print("Error: La fila solo puede contener las letras A, T, C y G.")
                continue
            adn.append(fila)


        def validar_opcion(opcion):

            # Valida que la opción ingresada sea un número entero entre 1 y 4
            try:
                opcion = int(opcion)
                if 1 <= opcion <= 4:
                    return opcion
                else:
                    print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
            return None


        def validar_tipo_mutacion(tipo):
            # Valida que el tipo de mutación ingresado sea 1 o 2
            if tipo in ['1', '2']:
                return tipo
            else:
                print("Opción no válida. Por favor, ingrese 1 o 2.")
            return None


        def validar_base_nitrogenada(base):
            # Valida que la base nitrogenada ingresada sea una de las opciones disponibles
            if base in ['A', 'T', 'C', 'G']:
                return base
            else:
                print("Error: La base nitrogenada debe ser una de las siguientes: A, T, C, G.")
                return None


        def validar_posicion_inicial(posicion):
            # Valida que la posición inicial ingresada sea un par de números válidos
            try:
                fila, columna = map(int, posicion.split(','))
                if 1 <= fila <= 6 and 1 <= columna <= 6:
                    return posicion
                else:
                    print("Error: La posición inicial debe estar en el rango de 1 a 6 para ambas coordenadas.")
            except ValueError:
                print("Error: La posición inicial debe ser un par de números separados por una coma (fila,columna).")
            return None


        def validar_orientacion(orientacion):
            # Valida que la orientación ingresada sea H o V
            if orientacion in ['H', 'V']:
                return orientacion
            else:
                print("Error: La orientación debe ser H (horizontal) o V (vertical).")
            return None


        while True:
            print("Menú")
            print("¿Qué desea hacer con el ADN?")
            print("1. Detectar mutaciones")
            print("2. Mutar el ADN")
            print("3. Sanar el ADN")
            print("4. Salir del programa")

            opcion = validar_opcion(input("Seleccione una opción (1, 2, 3 o 4): "))
            if opcion is None:
                continue

            if opcion == 1:
                detector = Detector()
                print("¿Hay mutaciones?")
                es_mutante = detector.detectar_mutantes(adn)
                print(es_mutante)

            elif opcion == 2:
                print("Seleccione el tipo de mutación:")
                print("1. Radiación (horizontal o vertical)")
                print("2. Virus (diagonal)")

                while True:
                    tipo_mutacion = validar_tipo_mutacion(input("Seleccione una opción (1 o 2): "))
                    if tipo_mutacion:
                        break

                if tipo_mutacion == '1':
                    while True:
                        base_nitrogenada = input("Ingrese la base nitrogenada a repetir (A, T, C, G): ")
                        base_nitrogenada = validar_base_nitrogenada(base_nitrogenada)
                        if base_nitrogenada:
                            break


                    while True:
                        posicion_inicial = input("Ingrese la posición inicial (fila,columna): ")
                        posicion_inicial = validar_posicion_inicial(posicion_inicial)
                        if posicion_inicial:
                            break


                    while True:
                        orientacion_de_la_mutacion = input("Ingrese la orientación (H para horizontal, V para vertical): ")
                        orientacion_de_la_mutacion = validar_orientacion(orientacion_de_la_mutacion)
                        if orientacion_de_la_mutacion:
                            break


                    radiacion = Radiacion(base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion)
                    try:
                        matriz_mutada = radiacion.crear_mutante(adn)
                        print("ADN mutado:")
                        for fila in matriz_mutada:
                            print(fila)
                    except Exception as e:
                        print(f"Error al crear la mutación: {e}")


                elif tipo_mutacion == '2':

                    while True:
                        base_nitrogenada = input("Ingrese la base nitrogenada a repetir (A, T, C, G): ")
                        base_nitrogenada = validar_base_nitrogenada(base_nitrogenada)
                        if base_nitrogenada:
                            break
                    while True:
                        posicion_inicial = input("Ingrese la posición inicial (fila,columna): ")
                        posicion_inicial = validar_posicion_inicial(posicion_inicial)
                        if posicion_inicial:
                            break
                    virus = Virus(base_nitrogenada)
                    try:
                        matriz_mutada = virus.crear_mutante(base_nitrogenada, posicion_inicial, adn)
                        print("ADN mutado:")
                        for fila in matriz_mutada:
                            print(fila)
                    except Exception as e:
                        print(f"Error al crear la mutación: {e}")

                else:
                    print("Opción no válida.")


            elif opcion == 3:
                sanador = Sanador()
                matriz_sanada = sanador.sanar_mutantes(adn)
                print("ADN sanado:")
                for fila in matriz_sanada:
                    print(fila)
                print(f"Mutaciones detectadas: {sanador.mutaciones_detectadas}")
                print(f"Mutaciones sanadas: {sanador.mutaciones_sanadas}")

            elif opcion == 4:
                print("Programa finalizado.")
                return

            continuar = input("¿Desea continuar? (Si/No): ")
            while continuar.lower() not in ['si', 'no']:
                print("Opción inválida. Por favor, ingrese 'Si' para continuar o 'No' para salir.")
                continuar = input("¿Desea continuar? (Si/No): ")

            if continuar.lower() == 'no':
                print("Programa finalizado.")
                return

if __name__ == "__main__":
    main()