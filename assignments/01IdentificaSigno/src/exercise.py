
'''
Autor: María del Carmen Estrada Ibarra
'''

def main():
    numero = int(input("Dame un número: "))

    if ( numero < 0 ):
        print("Es negativo")
    elif(numero == 0):
        print("Es cero")
    else:
        print("Es positivo")

if __name__ == '__main__':
    main()
