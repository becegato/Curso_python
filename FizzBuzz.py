def main():

    entrada = int(input('Insira um inteiro:'))

    if (entrada % 3) == 0 and (entrada % 5) == 0:
        print('FizzBuzz')

    else:
        print(entrada)

main()
