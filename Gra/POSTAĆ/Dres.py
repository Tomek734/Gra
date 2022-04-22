from POSTAĆ.Postać import Postać
from random import randint
class Dres(Postać):
    def __init__(self) -> None:
        super().__init__()
        self.name="Seba"
        self.p=randint(100,400)