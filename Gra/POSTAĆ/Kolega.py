from POSTAĆ.Postać import Postać
class Kolega(Postać):
    def __init__(self) -> None:
        super().__init__()
    def oferta(self):
        print('Mogę odsprzedać Ci ściąge przydatną na lekcji')
        print('Jęśli chcesz skorzystać z ofrty napisz tak')
        print('Jeśli nie napisz nie')