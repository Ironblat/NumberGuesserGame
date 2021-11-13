from random import randrange

szam1 = int(randrange(1, 100))

tippek = 8

reset2 = True

lang = input("Válassz nyelvet! / Choose Language! (M-Magyar/E-English): ")

if lang == 'M':

    print('Ki kell találnod egy számot 1 és 100 kötül.')

    while reset2:
        szam1 = int(randrange(1, 100))
        for i in range(8):
            szam2 = int(input('A tipped: '))

            if szam1 == szam2:
                print("Kiatáltad a számot")
                break
            else:
                print("nem találtad ki próbáld újra.")


                if szam1 < szam2:
                 print("Tipp: A szám kisebb")

                else:
                    print("Tipp: A szám nagyobb")

                tippek -= 1


        if tippek == 0:
            print("Ezt kellet volna kitalálnod: ", szam1)

        reset = input("Szeretnél még egy számot? (Y/N): ")


        if reset == 'Y':
             reset2 = True

        if reset == 'N':
             reset2 = False
             print('Szia!!')


        if reset2 == False:
            break

        else:
            continue

if lang == 'E':
    print('You need to guess a number between 1 and 100')

    while reset2:
        szam1 = int(randrange(1, 100))
        for i in range(8):

            szam2 = int(input('your guess: '))

            if szam1 == szam2:
                print("Hurray, you guessed the number.")
                break
            else:
                print("Try again.")

                if szam1 < szam2:
                    print("Tipp: The number is lower")

                else:
                    print("Tipp: The number is higher")

                tippek -= 1

        if tippek == 0:
            print("The number you needed to guess: ", szam1)

        reset = input("Do you want to play again? (Y/N): ")

        if reset == 'Y':
            reset2 = True

        if reset == 'N':
            reset2 = False
            print('Goodbye!!')

        if reset2 == False:
            break

        else:
            continue
