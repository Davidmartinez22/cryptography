from cryptography.fernet import Fernet
import os

# 1. Generar una clave secreta
clave = Fernet.generate_key()
cipher = Fernet(clave)

texto = "Hola, esto es un mensaje secreto"


texto = input("\nDame un texto a cifrar:")

#Crear la carpeta si no existe
if not os.path.exists('archivos'):
    os.makedirs('archivos')


# 2. Cifrar un mensaje
mensaje = texto.encode()
print("-----------------------------------")
print("Mensaje a Cifrar:", texto)
print("-----------------------------------")


mensaje_cifrado = cipher.encrypt(mensaje)
print("Mensaje Cifrado:", mensaje_cifrado)

#Guardar en archivo texto cifrado
with open("archivos/cifrado.txt", "wb") as file:
    file.write(mensaje_cifrado)



# Descifrar mensaje
mensaje_descifrado = cipher.decrypt(mensaje_cifrado).decode()
print("Mensaje Descifrado:", mensaje_descifrado)

#Guardar en archivo texto cifrado
with open("archivos/descifrado.txt", "w") as file:
    file.write(mensaje_descifrado)