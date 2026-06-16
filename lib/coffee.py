#!/usr/bin/env python3

class Coffee:
    size = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        self.size = size
        self.price = price

        if isinstance(self.size, str):
            if self.size not in Coffee.size:
                print("Size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.prize += 1

