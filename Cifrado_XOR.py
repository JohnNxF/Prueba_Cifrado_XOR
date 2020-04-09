clave="\x05"															# Clave de ejemplo
def cifrado_xor(xor_c, k):												# Funcion para el cifrado
	xor_c=chr((ord(xor_c)^ord(k)))										# Valor unicode de la operacion XOR de la clave sobre el mensaje
	return xor_c		

Fuente = 'CS.txt'														# Archivo a leer
with open(Fuente) as F:													# Control del archivo, asignado a F
	linea = F.readline()												# Leer la linea 1 del archivo de texto
	cont = 0															# Inicio contador de linea
	while linea:														# Mientras haya lineas que leer, hacer: 
		cadena = linea.strip()[24:26]									# Separar las lineas unas de otras agregandolas a una lista
																		# Tambien se extrae la parte del texto que quermos cifrar.
		print("Linea {}: {}".format(cont,linea))						# Fomato de impresion de datos, mostrando los ultimos 2 digitos
		hex_a = int(cadena,16)
		hex_d = chr(hex_a)
		#print("\nExtaccion y conversion de ultimo octeto a hexadecimal de linea {} es {} \n".format(cont,hex_d))														
		print(cifrado_xor(hex_d,clave))									# Pasamos los argumentos a la funcion de cifrado
		linea = F.readline()											# Leer la siguiente linea
		cont += 1														# Aumentar contador		
















#---------------------------------Conversion de la cadena a el valor hexadecimal o unicode-----------------------------#
'''
cifrados = "02:30:40:B9"
m_c = cifrados.strip()[-2:]
print(m_c)
hex_d = int(m_c,16)
uni_d = m_c.encode()
print(uni_d)
print(hex_d)
'''
#----------------------------------------Cifrado-------------------------------------#
'''
mensaje = "\xB9"														# Mensaje de prueba 
clave = "5"															    # Clave de cifrado 
#res = ''.join(format(ord(i), 'b') for i in mensaje)  					# Obtener valor binario del mensaje
#print("Valor del mensaje en binario es: ", res)							
print("El mensaje es: ", mensaje)
print("El valor para codificar es: ", clave)

def cifrado_xor(xor_c, k):												# Funcion para el cifrado
	xor_c=chr(ord(xor_c)^ord(k) for i,j in zip(xor_c,k))				#Valor unicode de la operacion XOR de la clave sobre el mensaje
	return xor_c
print(cifrado_xor(mensaje,clave))																
'''