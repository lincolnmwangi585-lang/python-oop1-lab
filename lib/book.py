#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

        if not isinstance(self.page_count, int):
            print("page_count must be an integer")
            return

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


book1 = Book(title='Age is just a number', page_count='12')
book1.turn_page()