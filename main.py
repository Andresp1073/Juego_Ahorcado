import random
import palabras
import arte

# Obtención de listas de nombres y equipos
lista_nombres = palabras.nombres
lista_equipos = palabras.equipos_futbol

print('MENU DE OPCIONES AHORCADO')
print('1. Adivinar nombres')
print('2. Adivinar equipos de futbol')
print('3. Salir')
op = int(input('Elija una opción: '))

# Selección de la palabra secreta según la opción elegida
if op == 1:
    palabra_secreta = random.choice(lista_nombres)
elif op == 2:
    palabra_secreta = random.choice(lista_equipos)
else:
    print('Saliendo del juego.')
    exit()

# Inicialización de variables para el juego
intentos_fallidos = 0
max_intentos = len(arte.ahorcado) - 1  
letras_correctas = ''
letras_incorrectas = ''

# Bucle principal del juego
while intentos_fallidos < max_intentos:
    print(arte.ahorcado[intentos_fallidos])
    print(f"Letras incorrectas: {' '.join(letras_incorrectas)}")
    
    # Crear la representación actual de la palabra secreta con los espacios vacíos
    espacios_vacios = ''
    for letra in palabra_secreta:
        if letra in letras_correctas or letra == ' ':
            espacios_vacios += letra
        else:
            espacios_vacios += '_'
    
    print(f"Palabra: {' '.join(espacios_vacios)}")
    
    intento = input('Adivina una letra: ').lower()

    # Validar el intento del usuario
    if len(intento) != 1:
        print('Por favor, introduce una sola letra.')
    elif intento in letras_correctas + letras_incorrectas:
        print('Ya has probado esa letra. Elige otra.')
    elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
        print('Por favor ingresa una LETRA.')
    else:
        # Verificar si la letra está en la palabra secreta
        if intento in palabra_secreta:
            letras_correctas += intento
            # Comprobar si se ha adivinado la palabra completa
            if all(letra in letras_correctas or letra == ' ' for letra in palabra_secreta):
                print(f'La palabra secreta es "{palabra_secreta}" ¡Ganaste!')
                break
        else:
            letras_incorrectas += intento
            intentos_fallidos += 1
            if intentos_fallidos == max_intentos:
                print(arte.ahorcado[intentos_fallidos])
                print(f'La palabra secreta era "{palabra_secreta}". ¡Sigue intentando!')

print('Juego terminado.')
