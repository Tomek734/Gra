from html.entities import name2codepoint
from unicodedata import name
from POSTAĆ.Bohater import Bohater
from POSTAĆ.Dres import Dres
from random import choice
from POSTAĆ.Kolega import Kolega
def main():
    bohater = Bohater()
    kolega = Kolega()
    x=0
    while True:
        if x==15:
            print('Koniec gry')
            print('Twój wynik to',bohater.p)
            break
        elif 'Nauczyciel' in bohater.name:
            print('Zrób kartkówekę - k Poproś do odpowiedzi - o')
            co_chcesz_zrobić_n = input("Co chcesz zrobić?\t")
            if co_chcesz_zrobić_n.lower() == 'k':
                bohater.sprawdzian()
            elif co_chcesz_zrobić_n.lower() == 'o':
                d
        elif 'Uczen' in bohater.name:
            print('Idź na lekcję - l | Idź na wagary - w | Informacje - i')
            co_chcesz_zrobić_u = input("Co chcesz zrobić?\t")
            if co_chcesz_zrobić_u.lower() == 'l':
                inp = choice(['z','d'])
                if inp=='z':
                    print('Nauczycielka każe wyjąć karteczki')
                    bohater.kartkowka()
                elif inp=='d':
                    print('Nauczycielka prosi cię do odpowiedzi')
                    bohater.odpowiedz()
            elif co_chcesz_zrobić_u.lower() == 'w':
                inp = choice(['z','d','j'])
                if inp=='z':
                    dres=Dres()
                    bohater.walka(dres)
                elif inp=='d':
                    kolega.oferta()
                    inp=input('')
                    if inp=='tak':
                        if bohater.p>=30:
                            bohater.p-=30
                            bohater.equipment.append('ściąga')
                        else:
                            print('Sorry przyjacielu nie masz wystarczającej iliości p')
                elif inp=='j':
                    print('Złapał Cię nauczyciel!!!')
                    bohater.p-=50
                    print('Tracisz 50 punktów')
            elif co_chcesz_zrobić_u.lower() == 'i':
                bohater.informacje()
                x-=1
            else:
                print("Nie ma takiej komendy")
                x-=1

        x += 1
        print('Runda',x)
    with open('Ranking.txt','a') as myfile:
        myfile.write(f'{bohater.name} punkty {bohater.p}\n')
main()