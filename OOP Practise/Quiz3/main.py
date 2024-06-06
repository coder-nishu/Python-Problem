class Book:
    def __init__(self, name, author_name, publication_date, isbn_number, book_type):
        self.__name = name
        self.__author_name = author_name
        self.__publication_date = publication_date
        self.__isbn_number = isbn_number
        self.__book_type = book_type
    
    # Getter methods
    def get_name(self):
        return self.__name
    
    def get_author_name(self):
        return self.__author_name
    
    def get_publication_date(self):
        return self.__publication_date
    
    def get_isbn_number(self):
        return self.__isbn_number
    
    def get_book_type(self):
        return self.__book_type
    
    # Setter methods
    def set_name(self, name):
        self.__name = name
    
    def set_author_name(self, author_name):
        self.__author_name = author_name
    
    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date
    
    def set_isbn_number(self, isbn_number):
        self.__isbn_number = isbn_number
    
    def set_book_type(self, book_type):
        self.__book_type = book_type
    
    def display_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Author Name: {self.get_author_name()}")
        print(f"Publication Date: {self.get_publication_date()}")
        print(f"ISBN Number: {self.get_isbn_number()}")
        print(f"Type: {self.get_book_type()}")
    
    def default_values(self):
        self.set_name("Default Name")
        self.set_author_name("Default Author")
        self.set_publication_date("01-01-2000")
        self.set_isbn_number("0000000000")
        self.set_book_type("Default Type")
        print("Default values set.")

class LiteratureBook(Book):
    def __init__(self, name, author_name, publication_date, isbn_number, book_type, quantity, literature_type, edition):
        super().__init__(name, author_name, publication_date, isbn_number, book_type)
        self.__quantity = quantity
        self.__literature_type = literature_type
        self.__edition = edition
    
    # Getter methods
    def get_quantity(self):
        return self.__quantity
    
    def get_literature_type(self):
        return self.__literature_type
    
    def get_edition(self):
        return self.__edition
    
    # Setter methods
    def set_quantity(self, quantity):
        self.__quantity = quantity
    
    def set_literature_type(self, literature_type):
        self.__literature_type = literature_type
    
    def set_edition(self, edition):
        self.__edition = edition
    
    def display_info(self):
        super().display_info()
        print(f"Quantity: {self.get_quantity()}")
        print(f"Literature Type: {self.get_literature_type()}")
        print(f"Edition: {self.get_edition()}")
    
    def default_values(self):
        super().default_values()
        self.set_quantity(10)
        self.set_literature_type("Default Literature Type")
        self.set_edition("1st Edition")
        print("Default values set for LiteratureBook.")

# Example usage
book = Book("Python Programming", "John Doe", "2023-01-01", "1234567890", "Educational")
book.display_info()
print("\nSetting default values for Book:")
book.default_values()
book.display_info()

print("\n---------------------------\n")

literature_book = LiteratureBook("Shakespeare's Works", "William Shakespeare", "1623-01-01", "0987654321", "Literature", 5, "Classic", "First Edition")
literature_book.display_info()
print("\nSetting default values for LiteratureBook:")
literature_book.default_values()
literature_book.display_info()
