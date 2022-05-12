import random
"""
JUEGO DEL AHORCADO
"""

class JuegoAhorcado:
    """
    #Esta clase permite gestionar objetos de tipp JuegoAhorcado
    ---
    """
    ESTADOS = [
        """
         +--+
         |  |
            |
            |
            |
            |
        =====""",
        """
         +--+
         |  |
         O  |
            |
            |
            |
        =====""",
        """
         +--+
         |  |
         O  |
         |  |
            |
            |
        =====""",
        """
         +--+
         |  |
         O  |
        /|  |
            |
            |
        =====""",
        """
         +--+
         |  |
         O  |
        /|\ |
            |
            |
        =====""",
        """
         +--+
         |  |
         O  |
        /|\ |
        /   |
            |
        =====""",
        """
         +--+
         |  |
         O  |
        /|\ |
        / \ |
            |
        ====="""]

    SALVADO = [
        """
         +--+
            |
            |
        \O/ |
         |  |
        / \ |
        ====="""]
#CATEGORIAS Y OPCIONES
    CATEGORIA = 'FRUTAS VERDURAS PASTA'
    opciones1 = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()
    opciones2 = 'LECHUGA PEPINO ZANAHORIA COL'
    opciones3 = 'ESPAGUETI MACARRONES CARACOLAS'

    def jugar(self):
        """
        ##Método que donde se elige la categoria y la palabra, devuelve un string cuando has ganado o has perdido
        :return: string
        """

        lista_introducir = []
        lista_contenido = []
        if random.choice(self.CATEGORIA) == 'FRUTAS':
            palabra_secreta = random.choice(self.opciones1)
        elif random.choice(self.CATEGORIA) == 'VERDURAS':
            palabra_secreta = random.choice(self.opciones2)
        else:
            palabra_secreta = random.choice(self.opciones3)

        while True:
            self.dibujar(lista_introducir, lista_contenido, palabra_secreta)

            letra_introducida = self.DIMELETRA(lista_introducir + lista_contenido)
            if letra_introducir == adivna.append('TERMINA') or letra_introducir == adivina.append('termina'):
                print(self.ESTADOS[6])
                print(palabra_secreta)
                quit()

            if letra_introducida in palabra_secreta:

                lista_contenido.append(letra_introducida)

                ganador = True
                for palabra in palabra_secreta:
                    if palabra not in lista_contenido:
                        ganador = False
                        break
                if ganador:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', palabra_secreta)
                    print('Has ganado,Paco!')
                    break
            else:
                lista_introducir.append(letra_introducida)

                if len(lista_introducir) == len(self.ESTADOS) - 1:
                    self.dibujar(lista_introducir, lista_contenido, palabra_secreta)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(palabra_secreta))
                    break

    def dibujar(self, lista_introducir, lista_contenido, secreto):
        """
        ##Método donde se dibuja el muñeco según avance la partida
        :param lista_introducir: string
        :param lista_contenido: string
        :param secreto: string
        :return:
        """
        print(self.ESTADOS[len(lista_introducir)])
        print('La categoría es: ', self.CATEGORIA)
        intentos = len(self.ESTADOS)
        print('Te quendan {} intentos'.format(intentos))

        print('Letras incorrectas: ')

        for letra in lista_introducir:
            print(letra, '\n')
        if len(lista_introducir) == 0 and 0 == len(lista_introducir):
            print('No hay letras incorrectas.')
        if len(lista_introducir) == len(lista_introducir) + 1:
            print('Letras diferentes.')
        if len(lista_introducir) == len(lista_introducir) + 2:
            print('No coinciden.')

        espacio = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in lista_contenido:
                espacio[i] = secreto[i]

        print(' '.join(espacio))

    def DIMELETRA(self, repetido):
        """
        ##Método el cual pregunta al usuario la letra que quiere introducir
        :param repetido: string
        :return:
        """

        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in repetido:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina

#INCIALIZAMOS LA CLASE
if __name__ == '__main__':
    juego1 = JuegoAhorcado()
    juego1.jugar()
