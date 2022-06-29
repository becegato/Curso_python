#Blibliotecas
import math

#Código

def main():

#Entradas

    a = float(input('Please, enter with a:'))
    b = float(input('Please, enter with b:'))
    c = float(input('Please, enter with c:'))

    delta = b**2 - 4 * a * c

    print('Delta:', delta)

#Função

    if delta > 0:s
        print('A equação de segundo grau possuí pelo menos uma raíz real')
        x_pos = ((-b + math.sqrt(delta))/(2*a))
        x_neg = ((-b - math.sqrt(delta))/(2*a))

        print('Ráiz 1:', x_pos)
        print('Raíz 2:', x_neg)

    else:
        print('A equação de segundo grau não possuí raíz real')

main()
