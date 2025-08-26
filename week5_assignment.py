# ================================
# OOP Example: Book and ComicBook
# ================================

class Book:
    def __init__(self, title, author, pages, price):
        """Constructor to initialize a Book object"""
        self.title = title
        self.author = author
        self.pages = pages
        self.__price = price  # Encapsulation (private attribute)

    def book_info(self):
        """Display book details"""
        print(f"📖 '{self.title}' by {self.author} - {self.pages} pages - ${self.__price}")

    def read(self):
        """Simulate reading the book"""
        print(f"📚 You start reading '{self.title}'...")

    # Getter for encapsulated price
    def get_price(self):
        return self.__price

    # Setter for encapsulated price
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print(f"💲 Price updated to ${self.__price}")
        else:
            print("❌ Invalid price! Must be greater than 0.")


# Subclass to demonstrate inheritance & polymorphism
class ComicBook(Book):
    def __init__(self, title, author, pages, price, illustrator):
        """Constructor calls parent and adds illustrator attribute"""
        super().__init__(title, author, pages, price)
        self.illustrator = illustrator

    # Polymorphism: override book_info() to add illustrator
    def book_info(self):
        print(f"🎨 Comic: '{self.title}' by {self.author}, Illustrated by {self.illustrator} - ${self.get_price()}")

    def show_art(self):
        """Extra method unique to ComicBook"""
        print(f"🖼️ Enjoying artwork by {self.illustrator} in '{self.title}'...")
# ================================
# OOP Example: Book and ComicBook
# ================================

class Book:
    def __init__(self, title, author, pages, price):
        """Constructor to initialize a Book object"""
        self.title = title
        self.author = author
        self.pages = pages
        self.__price = price  # Encapsulation (private attribute)

    def book_info(self):
        """Display book details"""
        print(f"📖 '{self.title}' by {self.author} - {self.pages} pages - ${self.__price}")

    def read(self):
        """Simulate reading the book"""
        print(f"📚 You start reading '{self.title}'...")

    # Getter for encapsulated price
    def get_price(self):
        return self.__price

    # Setter for encapsulated price
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print(f"💲 Price updated to ${self.__price}")
        else:
            print("❌ Invalid price! Must be greater than 0.")


# Subclass to demonstrate inheritance & polymorphism
class ComicBook(Book):
    def __init__(self, title, author, pages, price, illustrator):
        """Constructor calls parent and adds illustrator attribute"""
        super().__init__(title, author, pages, price)
        self.illustrator = illustrator

    # Polymorphism: override book_info() to add illustrator
    def book_info(self):
        print(f"🎨 Comic: '{self.title}' by {self.author}, Illustrated by {self.illustrator} - ${self.get_price()}")

    def show_art(self):
        """Extra method unique to ComicBook"""
        print(f"🖼️ Enjoying artwork by {self.illustrator} in '{self.title}'...")

# ============================
# Activity 2: Polymorphism
# ============================

class Animal:
    def move(self):
        print("This animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("🐕 Running on four legs!")

class Bird(Animal):
    def move(self):
        print("🐦 Flying in the sky!")

class Fish(Animal):
    def move(self):
        print("🐟 Swimming in water!")


# Create instances of both classes
book1 = Book("1984", "George Orwell", 328, 15)
comic1 = ComicBook("Spider-Man", "Stan Lee", 120, 20, "Steve Ditko")

# Display info
book1.book_info()
comic1.book_info()

# Use methods
book1.read()
comic1.show_art()

# Test encapsulation (private price)
print("\n--- Testing Encapsulation ---")
print(f"Original Price: ${book1.get_price()}")
book1.set_price(18)     # Valid update
book1.set_price(-5)     # Invalid update


# ============================
# Test Animal Polymorphism
# ============================

print("\n--- Animal Movement (Polymorphism) ---")
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
