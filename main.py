class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print("Kitob:", self.title)
        print("Muallif:", self.author)
        print("Sahifalar:", self.pages)


book1 = Book("Python Basics", "muhammad", 250)
book2 = Book("AI Guide", "OpenAI", 180)

book1.info()
print("-" * 20)
book2.info()