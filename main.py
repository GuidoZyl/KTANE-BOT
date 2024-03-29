from PIL import Image, ImageTk
import tkinter as tk
import threading

### SOLO HECHA LA SECCIÓN 1 ###
txt_elegir_modulo = """Ingrese el modulo de la bomba: 
1) Cables
2) Botón
3) Símbolos
4) Simón dice
5) Tablas palabras
6) Números orden
7) Código morse
8) Cables complicados
9) Cables RAN
10) Laberinto
11) Contraseña
"""

def abrir_img(nombre_img):
        img = Image.open(nombre_img)
        window = tk.Tk()

        # Convert the Image object to a PhotoImage object, which Tkinter can display
        tk_img = ImageTk.PhotoImage(img)

        # Add the image to a label in the window
        label = tk.Label(window, image=tk_img)
        label.pack()

        window.attributes('-topmost', True)

        # Start the Tkinter event loop (this will display the window)
        window.mainloop()

def cables():
    cant_cables = int(input("Ingrese la cantidad de cables: "))
    if cant_cables == 3:
        hay_rojo = input("Hay cables rojos? (s/n): ")
        if hay_rojo == "n":
            print("\nCorte el segundo cable")
            return
        ultimo_es_blanco = input("El último cable es blanco? (s/n): ")
        if ultimo_es_blanco == "s":
            print("\nCorte el último cable")
            return
        hay_varios_azules = input("Hay más de un cable azul? (s/n): ")
        if hay_varios_azules == "s":
            print("\nCorte el último cable azul")
            return
        print("\nCorte el último cable")
    
    elif cant_cables == 4:
        cant_rojos = int(input("Ingrese la cantidad de cables rojos: "))
        if cant_rojos > 1:
            ultimo_digito_impar = input("El último dígito del serial es impar? (s/n): ")
            if ultimo_digito_impar == "s":
                print("\nCorte el último cable rojo")
                return
        ultimo_es_amarillo = input("El último cable es amarillo? (s/n): ")
        if ultimo_es_amarillo == "s" and cant_rojos == 0:
            print("\nCorte el primer cable")
            return
        cant_azules = int(input("Ingrese la cantidad de cables azules: "))
        if cant_azules == 1:
            print("\nCorte el primer cable")
            return
        cant_amarillos = int(input("Ingrese la cantidad de cables amarillos: "))
        if cant_amarillos > 1:
            print("\nCorte el último cable")
            return
        print("\nCorte el segundo cable")
    
    elif cant_cables == 5:
        ultimo_es_negro = input("El último cable es negro? (s/n): ")
        if ultimo_es_negro == "s":
            ultimo_digito_impar = input("El último dígito del serial es impar? (s/n): ")
            if ultimo_digito_impar == "s":
                print("\nCorte el cuarto cable")
                return
        cant_rojos = int(input("Ingrese la cantidad de cables rojos: "))
        if cant_rojos == 1:
            cant_amarillos = int(input("Ingrese la cantidad de cables amarillos: "))
            if cant_amarillos > 1:
                print("\nCorte el primer cable")
                return
        hay_negros = input("Hay cables negros? (s/n): ")
        if hay_negros == "n":
            print("\nCorte el segundo cable")
            return
        print("\nCorte el primer cable")

    elif cant_cables == 6:
        cant_amarillos = int(input("Ingrese la cantidad de cables amarillos: "))
        if cant_amarillos == 0:
            ultimo_digito_impar = input("El último dígito del serial es impar? (s/n): ")
            if ultimo_digito_impar == "s":
                print("\nCorte el tercer cable")
                return
        if cant_amarillos == 1:
            cant_blancos = input("Ingrese la cantidad de cables blancos: ")
            if cant_blancos > 1:
                print("\nCorte el cuarto cable")
                return
        hay_rojo = input("Hay cables rojos? (s/n): ")
        if hay_rojo == "n":
            print("\nCorte el último cable")
        print("\nCorte el cuarto cable")

    else:
        print("Ingrese un número valido")
        cables()

def boton():
    def barra():
        color_banda = input("Ingrese el color de la banda: ")
        if color_banda == "azul":
            print("\nSoltar cuando el temporizador tenga un 4 en cualquier posición")
            return
        elif color_banda == "amarillo" or color_banda == "amarilla":
            print("\nSoltar cuando el temporizador tenga un 5 en cualquier posición")
            return
        elif color_banda == "blanco" or color_banda == "blanca":
            print("\nSoltar cuando el temporizador tenga un 1 en cualquier posición")
            return
        else:
            print("\nSoltar cuando el temporizador tenga un 1 en cualquier posición")
            return

    color = input("Ingrese el color del botón: ")
    texto = input("Ingrese el texto del botón: ")
    if color == "azul" and texto == "abort":
        print("\nMantenga presionado el botón")
        barra()
        return
    if color == "amarillo":
        print("\nMantenga presionado el botón")
        barra()
        return
    if color == "rojo" and texto == "hold":
        print("\nPresione y suelte el botón")
        return
    if texto == "detonate":
        cant_baterias = int(input("Ingrese la cantidad de baterías: "))
        if cant_baterias > 1:
            print("\nPresione y suelte el botón")
            return
    if color == "blanco":
        hay_car = input("Hay una etiqueta CAR? (s/n): ")
        if hay_car == "s":
            print("\nMantenga presionado el botón")
            barra()
            return
    hay_frk = input("Hay una etiqueta FRK? (s/n): ")
    if hay_frk == "s":
        cant_baterias = int(input("Ingrese la cantidad de baterías: "))
        if cant_baterias > 2:
            print("\nPresione y suelte el botón")
            return
    barra()

def simbolos():
    thread = threading.Thread(target=abrir_img, args=("simbolos.png",))
    thread.start()

    ### HACER CLICKEABLES LAS IMAGENES ###

    listas_simb = [[1, 2, 3, 4, 5, 6, 7], [8, 1, 7, 9, 10, 6, 11], 
                   [12, 13, 9, 14, 15, 3, 10], [16, 17, 18, 5, 14, 11, 19], 
                   [20, 19, 18, 21, 17, 22, 23], [16, 8, 24, 25, 20, 26, 27]]
    
    simbs_bomba = input("Ingrese los símbolos de la bomba: ")
    simbs_bomba = simbs_bomba.split(" ")
    simbs_bomba = list(map(int, simbs_bomba))

    i = 0
    for combinacion in listas_simb:
            if all(simb in combinacion for simb in simbs_bomba):
                break
            i += 1

    orden_correcto = []
    for simb in listas_simb[i]:
        if simbs_bomba == []:
            break
        for simb_bomba in simbs_bomba:
            if simb == simb_bomba:
                orden_correcto.append(simb)
                simbs_bomba.remove(simb_bomba)
                break

    print(orden_correcto)
    input("Presione enter para continuar")
    thread.join()

def simon():
    tiene_vocal =  input("El serial tiene vocal? (s/n): ")
    cant_strikes = int(input("Ingrese la cantidad de strikes: "))
    if tiene_vocal == "s":
        while True:
            colores = input("Ingrese el/los color(es) o 'c' para cancelar: ")
            if colores == "c":
                break
            colores = colores.split(" ")
            for color in colores:
                if cant_strikes == 0:
                    if color == "rojo" or color == "ro" or color == "r":
                        print("Azul")
                    elif color == "azul" or color == "az":
                        print("Rojo")
                    elif color == "verde" or color == "ve" or color == "v":
                        print("Amarillo")
                    elif color == "amarillo" or color == "am":
                        print("Verde")
                elif cant_strikes == 1:
                    if color == "rojo" or color == "ro" or color == "r":
                        print("Amarillo")
                    elif color == "azul" or color == "az":
                        print("Verde")
                    elif color == "verde" or color == "ve" or color == "v":
                        print("Azul")
                    elif color == "amarillo" or color == "am":
                        print("Rojo")
                else:
                    if color == "rojo" or color == "ro" or color == "r":
                        print("Verde")
                    elif color == "azul" or color == "az":
                        print("Rojo")
                    elif color == "verde" or color == "ve" or color == "v":
                        print("Amarillo")
                    elif color == "amarillo" or color == "am":
                        print("Azul")

    elif tiene_vocal == "n":
        while True:
            colores = input("Ingrese el/los color(es) o 'c' para cancelar: ")
            if colores == "c":
                break
            colores = colores.split(" ")
            for color in colores:
                if cant_strikes == 0:
                    if color == "rojo" or color == "ro" or color == "r":
                        print("Azul")
                    elif color == "azul" or color == "az":
                        print("Amarillo")
                    elif color == "verde" or color == "ve" or color == "v":
                        print("Verde")
                    elif color == "amarillo" or color == "am":
                        print("Rojo")
                elif cant_strikes == 1:
                    if color == "rojo" or color == "ro" or color == "r":
                        print("Rojo")
                    elif color == "azul" or color == "az":
                        print("Azul")
                    elif color == "verde" or color == "ve" or color == "v":
                        print("Amarillo")
                    elif color == "amarillo" or color == "am":
                        print("Verde")
                else:
                    if color == "rojo" or color == "ro" or color == "r":
                        print("Amarillo")
                    elif color == "azul" or color == "az":
                        print("Verde")
                    elif color == "verde" or color == "ve" or color == "v":
                        print("Azul")
                    elif color == "amarillo" or color == "am":
                        print("Rojo")

def tablas_palabras():
    def abrir_img1():
        img1 = Image.open("tablas_palabras1.JPG")
        window1 = tk.Tk()

        # Convert the Image object to a PhotoImage object, which Tkinter can display
        tk_img1 = ImageTk.PhotoImage(img1)

        # Add the image to a label in the window
        label1 = tk.Label(window1, image=tk_img1)
        label1.pack()

        window1.attributes('-topmost', True)        

        # Segunda ventana
        img2 = Image.open("tablas_palabras2.JPG")
        window2 = tk.Toplevel(window1)

        window2.geometry("860x680+1000+50")
        # Convert the Image object to a PhotoImage object, which Tkinter can display
        tk_img2 = ImageTk.PhotoImage(img2)

        # Add the image to a label in the window
        label2 = tk.Label(window2, image=tk_img2)
        label2.pack()

        window2.attributes('-topmost', True)
        window1.mainloop()

    thread = threading.Thread(target=abrir_img1)
    thread.start()
        
    input("Presione enter para continuar")
    thread.join()

def numeros_orden():
    lista_numeros = []
    # Etapa 1
    num_pantalla = int(input("Ingrese el número en pantalla: "))
    if num_pantalla in [1, 2]:
        print("Pulse la segunda posición")
        pos = 1
        num = int(input("Ingrese el número: "))
        lista_numeros.append((pos, num))

    elif num_pantalla == 3:
        print("Pulse la tercera posición")
        pos = 2
        num = int(input("Ingrese el número: "))
        lista_numeros.append((pos, num))
    
    elif num_pantalla == 4:
        print("Pulse la cuarta posición")
        pos = 3
        num = int(input("Ingrese el número: "))
        lista_numeros.append((pos, num))

    # Etapa 2
    num_pantalla = int(input("Ingrese el número en pantalla: "))
    if num_pantalla == 1:
        print("Pulse el número 4")
        pos = int(input("Ingrese la posición: ")) - 1
        num = 4
        lista_numeros.append((pos, num))
    
    elif num_pantalla in [2, 4]:
        print(f"Pulse la posición {lista_numeros[0][0]}")
        pos = lista_numeros[0][0]
        num = int(input("Ingrese el número: "))
        lista_numeros.append((pos, num))

    elif num_pantalla == 3:
        print("Pulse la primera posición")
        pos = 0
        num = int(input("Ingrese el número: "))
        lista_numeros.append((pos, num))
    
    # Etapa 3
    num_pantalla = int(input("Ingrese el número en pantalla: "))
    if num_pantalla == 1:
        print(f"Pulse el número {lista_numeros[1][1]}")
        pos = int(input("Ingrese la posición: ")) - 1
        num = lista_numeros[1][1]
        lista_numeros.append((pos, num))

    elif num_pantalla == 2:
        print(f"Pulse el número {lista_numeros[0][1]}")
        pos = int(input("Ingrese la posición: ")) - 1
        num = lista_numeros[0][1]
        lista_numeros.append((pos, num))

    elif num_pantalla == 3:
        print("Pulse la tercera posición")
        pos = 2
        num = int(input("Ingrese el número: "))
        lista_numeros.append((pos, num))

    elif num_pantalla == 4:
        print("Pulse el número 4")
        pos = int(input("Ingrese la posición: ")) - 1
        num = 4
        lista_numeros.append((pos, num))

    # Etapa 4
    num_pantalla = int(input("Ingrese el número en pantalla: "))
    if num_pantalla == 1:
        print(f"Pulse la posición {lista_numeros[0][0]}")
        pos = lista_numeros[0][0]
        num = int(input("Ingrese el número: "))
        lista_numeros.append((pos, num))

    elif num_pantalla == 2:
        print("Pulse la primera posición")
        pos = 0
        num = int(input("Ingrese el número: "))
        lista_numeros.append((pos, num))

    elif num_pantalla in [3, 4]:
        print(f"Pulse la posición {lista_numeros[1][0]}")
        pos = lista_numeros[1][0]
        num = int(input("Ingrese el número: "))
        lista_numeros.append((pos, num))

    # Etapa 5
    num_pantalla = int(input("Ingrese el número en pantalla: "))
    if num_pantalla == 1:
        print(f"Pulse el número {lista_numeros[0][1]}")

    elif num_pantalla == 2:
        print(f"Pulse el número {lista_numeros[1][1]}")

    elif num_pantalla == 3:
        print(f"Pulse el número {lista_numeros[3][1]}")

    elif num_pantalla == 4:
        print(f"Pulse el número {lista_numeros[2][1]}")
    
def codigo_morse():
    pass

funciones = [cables, boton, simbolos, simon, tablas_palabras, numeros_orden, codigo_morse]

while True:
    modulo = int(input(txt_elegir_modulo))
    
    funciones[modulo - 1]()
    if modulo in [3, 5]:
        input("Presione enter para continuar")