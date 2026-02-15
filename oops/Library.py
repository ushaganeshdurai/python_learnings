class Book:
    def __init__(self, title, author, isbn, genre="Unknown"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.is_available = True
        self.checkout_history = []
    
    def __str__(self):
        status = "✓ Available" if self.is_available else "✗ Checked Out"
        return f"'{self.title}' by {self.author} [{self.genre}] - {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, title, author, isbn, genre="Unknown"):
        # Check if book already exists
        for book in self.books:
            if book.isbn == isbn:
                print(f"Book with ISBN {isbn} already exists!")
                return False
        
        new_book = Book(title, author, isbn, genre)
        self.books.append(new_book)
        print(f"✓ Added: {new_book}")
        return True
    
    def remove_book(self, isbn):
        """Remove a book from the library"""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"✓ Removed: '{book.title}'")
                return True
        print(f"✗ Book with ISBN {isbn} not found!")
        return False
    
    def checkout_book(self, isbn, borrower_name):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    from datetime import datetime
                    book.checkout_history.append({
                        'borrower': borrower_name,
                        'date': datetime.now().strftime("%Y-%m-%d %H:%M")
                    })
                    print(f"✓ '{book.title}' checked out to {borrower_name}")
                    return True
                else:
                    print(f"✗ '{book.title}' is currently unavailable")
                    return False
        print(f"✗ Book not found")
        return False
    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_available:
                    book.is_available = True
                    print(f"✓ '{book.title}' returned successfully")
                    return True
                else:
                    print(f"✗ '{book.title}' wasn't checked out")
                    return False
        print(f"✗ Book not found")
        return False
    
    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def search_by_genre(self, genre):
        return [book for book in self.books if genre.lower() in book.genre.lower()]
    
    def get_available_books(self):
        return [book for book in self.books if book.is_available]
    
    def get_checked_out_books(self):
        return [book for book in self.books if not book.is_available]
    
    def display_statistics(self):
        total = len(self.books)
        available = len(self.get_available_books())
        checked_out = len(self.get_checked_out_books())
        
        print(f"\n{'='*50}")
        print(f"{self.name} - Statistics")
        print(f"{'='*50}")
        print(f"Total Books: {total}")
        print(f"Available: {available}")
        print(f"Checked Out: {checked_out}")
        print(f"{'='*50}\n")
    
    def display_all_books(self):
        if not self.books:
            print("📚 The library is empty!")
            return
        
        print(f"\n{'='*60}")
        print(f"📚 {self.name} - All Books")
        print(f"{'='*60}")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print(f"{'='*60}\n")


# Demo
library = Library("Central Library")

library.add_book("Harry Potter", "J.K. Rowling", "001", "Fantasy")
library.add_book("The Hobbit", "J.R.R. Tolkien", "002", "Fantasy")
library.add_book("1984", "George Orwell", "003", "Dystopian")

library.display_all_books()
library.checkout_book("001", "Alice")
library.display_statistics()

results = library.search_by_genre("fantasy")
print(f"\nFantasy books: {len(results)}")
for book in results:
