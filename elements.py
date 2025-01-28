import pygame

class Elements():
    def __init__(self, el_name, el_symbol, el_number, el_size):
        self.el_name = el_name
        self.el_symbol = el_symbol
        self.el_number = el_number
        self.el_size = el_size

    def get(self):
        print(f"Name: {self.el_name}, symbol: {self.el_symbol}, number: {self.el_number}")

    def set(self):
        pass