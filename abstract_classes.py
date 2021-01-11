class MyBook(Book):
    price = 0

    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price

    def display(self):
        print("Title: " + title)
        print("Author: " + author)
        print("Price: " + str(price))


author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
