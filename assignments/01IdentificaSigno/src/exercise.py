  
'''
Autor: María del Carmen Estrada Ibarra
'''

def main():
    #El mensaje para recibir el dato debe ser **"Dame un número: **"
    #El mensaje para la salida debe ser **"Es positivo, Es negativo ó Es cero **"
    
    numero = int(input("Dame un número: "))

    if ( numero < 0 ):
        print("Es negativo")
    elif(numero == 0):
        print("Es cero")
    else:
        print("Es positivo")

if __name__ == '__main__':
    main()
