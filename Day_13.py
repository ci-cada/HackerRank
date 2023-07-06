from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
    
#Write MyBook class
class MyBook:
    def __init__(self, title, author, price):
        self.title = title 
        self.author = author 
        self.price = price
    
    def display(self):
        tit = f"Title: {self.title}"
        auth = f"Author: {self.author}"
        pri = f"Price: {self.price}"
        print(tit)
        print(auth)
        print(pri)
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()