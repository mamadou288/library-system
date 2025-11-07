import json
import os
from models.book import Book


class BookManager:
    """
    Gestionnaire de la collection de livres avec JSON.
    
    Attributs:
        books (list[Book])
        json_file (str): Chemin du fichier JSON de sauvegarde
    """
    
    def __init__(self) -> None:
        """
        Initialise le gestionnaire et charge les livres depuis le fichier JSON.
        """
        self.books = []
        self.json_file = "data/books.json"
        self.load_from_json()
    
    def load_from_json(self) -> None:
        """
        Charge les livres depuis le fichier JSON.
        Si le fichier n'existe pas, initialise une liste vide.
        """
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as f:
                books_data = json.load(f)
            self.books = [Book.from_dict(book) for book in books_data]
    
    def save_to_json(self) -> None:
        """
        Sauvegarde tous les livres dans le fichier JSON.
        Crée le dossier data/ s'il n'existe pas.
        """
        os.makedirs("data", exist_ok=True)
        books = [book.to_dict() for book in self.books]
        with open(self.json_file, "w") as f:
            json.dump(books, f, indent=2)
    
    def add_book(self, book: Book) -> None:
        """
        Ajoute un livre à la bibliothèque et sauvegarde automatiquement.
        """
        if book is None:
            raise ValueError('Veuillez entrer un livre')
        
        self.books.append(book)
        self.save_to_json()
    
    def delete_book(self, book_id: str) -> None:
        """
        Supprime un livre par son ID et sauvegarde automatiquement.
        """
        for book in self.books:
            if str(book.id) == book_id:
                self.books.remove(book)
                self.save_to_json()
                break
        else:
            raise ValueError(f"Livre avec l'ID {book_id} introuvable")
    
    def get_book_by_id(self, book_id: str) -> Book:
        """
        Retourne un livre par son ID.
        """
        for book in self.books:
            if str(book.id) == book_id:
                return book
        else:
            raise ValueError(f"Livre avec l'ID {book_id} introuvable")
    
    def search_by_title(self, title: str) -> list[Book]:
        """
        Recherche des livres dont le titre contient la chaîne donnée (insensible à la casse).
        """
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def list_all_books(self) -> list[Book]:
        """
        Retourne tous les livres de la bibliothèque.
        """
        return self.books