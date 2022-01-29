from random import randrange



reset2 = True

print("The Number Guesser Game v1.2      Created by: Ironblyat")

while True:
    lang = input("Válassz nyelvet! / Choose Language! (M-Magyar/E-English): ")
    lang_invalid = False

    if lang == 'M' or lang == 'E':
        break
    print("Nem jó/Invalid")



if lang == 'M':

    print('Ki kell találnod egy számot 1 és 100 között. Írd be hogy "exit" a kilépéshez. Van 8 lehetőséged tippelni')

    while reset2:
        szam1 = int(randrange(1, 100))
        tippek = 7

        for i in range(7):
            szam2 = input('A tipped: ')

            if szam2 == "exit":
                break
            else:
                szam2 = int(szam2)

            if szam1 == szam2:
                print("Kiatáltad a számot")
                break
            else:
                print("nem találtad ki próbáld újra. Még ennyi tipped van: ", tippek)


                if szam1 < szam2:
                 print("Tipp: A szám kisebb")

                else:
                    print("Tipp: A szám nagyobb")

                tippek -= 1


        if tippek == 0:
            print("Ezt kellet volna kitalálnod: ", szam1)

        reset = input("Szeretnél még egy számot? (Y/N): ")


        if reset == 'Y' or reset == 'y':
             reset2 = True

        if reset == 'N' or reset == 'n':
             reset2 = False
             print('Szia!!')


        if reset2 == False:
            break

        else:
            continue

if lang == 'E':
    print('You need to guess a number between 1 and 100. Type "exit" to exit the game. You have 8 guesses.')

    while reset2:
        szam1 = int(randrange(1, 100))
        tippek = 7

        for i in range(7):

            szam2 = input('your guess: ')

            if szam2 == "exit":
                break
            else:
                szam2 = int(szam2)

            if szam1 == szam2:
                print("Hurray, you guessed the number.")
                break
            else:
                print("Try again. Number of tries left: ", tippek)

                if szam1 < szam2:
                    print("Tipp: The number is lower")

                else:
                    print("Tipp: The number is higher")

                tippek -= 1

        if tippek == 0:
            print("The number you needed to guess: ", szam1)

        reset = input("Do you want to play again? (Y/N): ")

        if reset == 'Y' or reset2 == 'y':
            reset2 = True

        if reset == 'N' or reset == 'n':
            reset2 = False
            print('Goodbye!!')

        if reset2 == False:
            break

        else:
            continue
