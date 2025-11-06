from models.book import Book
import json
import os 

class BookManager:
    def __init__(self):
        self.books = []  # Liste de livres
        self.json_file = "data/books.json"  # Chemin du fichier
        self.load_from_json()  # Charger automatiquement
    
    def load_from_json(self):
        """
        Charge les livres depuis books.json
        """
        if os.path.exists(self.json_file):
            # Le fichier existe, on peut le lire
            with open(self.json_file, "r") as f:
                books_data = json.load(f)
            self.books = [Book.from_dict(book) for book in books_data]
        else:
            # Première utilisation, le fichier n'existe pas encore
            # On laisse self.books = [] (déjà initialisé dans __init__)
            pass
    
    def save_to_json(self):
        """
        Sauvegarde tous les livres dans books.json
        """
        os.makedirs("data", exist_ok=True)
        # 1. Transformer self.books en liste de dictionnaires
        books = [book.to_dict() for book in self.books]
        # 2. Sauvegarder avec json.dump()
        with open(self.json_file, "w") as f:
            json.dump(books, f, indent=2)
    
    def add_book(self, book: Book):
        """
        Ajoute un livre à la bibliothèque et sauvegarde
        """
        if book is None:
            raise ValueError('Veuillez entrez un livre')
        
        self.books.append(book)  
        self.save_to_json()  

    def delete_book(self, book_id: str):
        """
        Supprime un livre par son ID
        """
        for book in self.books:
            if str(book.id) == book_id:
                self.books.remove(book)
                self.save_to_json()
                break
        else:
            raise ValueError(f"Livre avec l'ID {book_id} introuvable")
