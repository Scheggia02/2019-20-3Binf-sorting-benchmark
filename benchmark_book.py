from book import Book
from selection_sort_book import selection_sort


book1 = Book("Calzoniere", "Petrarca")
book2 = Book("Divina Commedia", "Dante")
book3 = Book("Decamerone", "Boccaccio")

book_list = [book1, book2, book3]

selection_sort(book_list)