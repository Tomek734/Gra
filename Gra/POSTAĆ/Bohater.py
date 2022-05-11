from POSTAĆ.Postać import Postać
from random import randint,choice
import tkinter as tk
import os

class Bohater(Postać):
    def __init__(self) -> None:
        super().__init__()
        self.equipment = []
        while True:
            self.name = input("Jak się nazywasz?\t")
            if self.name == "":
                print("Podaj nazwę")
            else:
                break
        while True:
            inp2 = input("Wybierz kim chcesz grać n-nauczyciel, u-uczeń\t")
            if "n" == inp2.lower():
                self.p = 200
                self.name = self.name + " (Nauczyciel)"
                root = tk.Tk()
                base_folder = os.path.dirname(__file__)
                image_path = os.path.join(base_folder, 'Nauczyciel.png')
                img = tk.PhotoImage(file=image_path)

                button = tk.Button(root, image=img)
                button.pack()

                root.mainloop()
                break
            elif "u" == inp2.lower():
                self.p = 300
                self.name = self.name + " (Uczen)"
                root = tk.Tk()
                base_folder = os.path.dirname(__file__)
                image_path = os.path.join(base_folder, 'Uczen.png')

                img = tk.PhotoImage(file=image_path)

                button = tk.Button(root, image=img)
                button.pack()

                root.mainloop()
                break
            else:
                print('Nie ma takiej kategorii')
    def walka(self, Dres):
        print(f'Spotykasz dresa {Dres.name}')
        print('Możesz z nim waliczyć-a lub uciekać-b')
        inp=input('')
        if inp=='a':
            if self.p>Dres.p:
                self.p+=20
                print(f"Wygrywasz walkę {self.p}")
            else:
                self.p-= randint(20,30)
                print(f"Dres okazał się być śilniejszy {self.p}")
        elif inp=='b':
            inp=choice(['v','n','g'])
            if inp=='v' or 'g':
                self.p+=30
                print('Byłeś szybszy udało ci się uciec')
                print('Otrzymujesz 30 punktów')
            elif inp=='n':
                inp=randint(60,120)
                self.p-=inp
                print('Dres cię dogonił i porządnie sprał')
                print(f'Tracisz {inp} punktów')
    def informacje(self):
        print(f'Twoja nazwa\t{self.name}')
        print(f'Ilość p\t{self.p}')
        print(f'Twój ekwipunek\t{self.equipment}')
    def kartkowka(self):
        if 'ściąga' in self.equipment:
            print('Masz ściągę')
            inp=input('Czy chcesz ją wykorzystać?\t')
            if inp=='tak':
                self.equipment.remove('ściąga')
                inp2=choice(['d','l','k'])
                if inp2=='d'or'k':
                    inp=randint(50,70)
                    print(f'Udało ci się dostajesz {inp}')
                    self.p+=inp
                elif inp2=='l':
                    print('Zostaeś przyłapany')
                    self.p-=40
        else:
            inp=choice(['d','l'])
            if inp=='d':
                print('Brawo!!!')
                inp2=randint(40,100)
                print('Udało ci się zanłeś odpowiedzi na pytania')
                print(f'Dostajesz w nagrodę {inp2} punktów!')
                self.p+=inp2
            elif inp=='l':
                print('Niestety nie pryzgotowałeś się!')
                inp2=randint(20,40)
                print(f'Tracisz {self.p} punktów')
    def odpowiedz(self):
        while True:
            print('Spróbuj porzmawiać na inny teamt-a')
            print('Odpowiadaj na pytania-b')
            inp=input('Co wybierasz?\t')
            if inp=='a':
                inp=choice(['d','l'])
                if inp=='d':
                    print('Udało Ci się zagadać nauczyciela!!')
                    print('Nie musiałeś odpowiadać w nagrodę otrymujesz 45 punktów!!')
                    self.p+=45
                    break
                elif inp=='l':
                    print('Nauczyciel zorientowa się, że nie znasz odpowiedzi na jego pytania')
                    print('Tracisz 45 punktów!!')
                    self.p-=45
                    break
            elif inp=='b':
                inp=choice(['d','l'])
                if inp=='d':
                    print('Znałeś odpowiedzi na wszystkie pytania')
                    print('W nagrodę otzymujesz 50 punktów')
                    self.p+=50
                    break
                elif inp=='l':
                    print('Nieprzygotowałeś się')
                    print('Tracisz 40 punktów!!')
                    self.p-=40
                    break
            else:
                print('Wybierz jedną z opcji')
    def sprawdzian(self):
        while True:
            print('Możesz zrobić trudny sprawdzian - a lub łatwy - b')
            inp=input('Co wybierasz?\t')
            if inp=='a':
                inp=choice(['d','l','z'])
                if inp=='d' or 'z':
                    print('Niestety ucznowie nipodołali tak trudnym zadaniom')
                    inp=randint(60,100)
                    self.p-=inp
                    print(f'Tracisz {inp} punktów')
                    break
                elif inp=='l':
                    print('Uczniowie zdołali odpowiedzieć na pytania')
                    inp=randint(70,130)
                    self.p+=inp
                    print(f'W nagrodę otrzymujesz {inp} punktów')
                    break
            elif inp=='b':
                inp=choice(['d','l','z'])
                if inp=='d' or 'z':
                    print('Dzięki łatwemu sprawdzianowi wszystkim udaje się zaliczyć')
                    inp=randint(40,75)
                    self.p+=inp
                    print(f'W nagrodę otrzymujesz {inp} punktów')
                    break
                elif inp=='l':
                    print('Uczniowie nie odpowiedzili na tak proste pytania')
                    inp=randint(30,60)
                    self.p-=inp
                    print(f'Tracisz {inp} punktów')
                    break
            else:
                print('Wybierz jedną z opcji')
    def pytanie(self):
        print('Bierzesz ucznia do odpowiedzi')
        while True:
            print('Zadajesz mu trudne pytania-a lub łatwe-b')
            inp=input('?\t')
            if inp=='a':
                inp=choice(['d','l','z'])
                if inp=='d' or 'z':
                    print('Niestety uczeń nie odpowiedzaiał na twoje pytania')
                    inp=randint(60,100)
                    self.p-=inp
                    print(f'Tracisz {inp} punktów')
                    break
                elif inp=='l':
                    print('Uczń udzielił odpowiedzi na twoje trudne pytania')
                    inp=randint(70,130)
                    self.p+=inp
                    print(f'W nagrodę otrzymujesz {inp} punktów')
                    break
            elif inp=='b':
                inp=choice(['d','l','z'])
                if inp=='d' or 'z':
                    print('Dzięki łatwym pytaniom uczeń zdołał odpowiedzieć')
                    inp=randint(40,75)
                    self.p+=inp
                    print(f'W nagrodę otrzymujesz {inp} punktów')
                    break
                elif inp=='l':
                    print('Uczeń nie odpowiedział na ani jedno pytanie')
                    inp=randint(30,60)
                    self.p-=inp
                    print(f'Tracisz {inp} punktów')
                    break
            else:
                print('Wybierz jedną z opcji')

