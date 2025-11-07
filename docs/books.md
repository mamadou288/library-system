# Module Books

## Vue d'ensemble

Gestion des livres avec persistance JSON.

---

## Classe `Book` (models/book.py)

**Attributs :**
- `id` (UUID) : Identifiant unique
- `title` (str) : Titre du livre
- `author` (str) : Auteur du livre
- `added_at` (datetime) : Date d'ajout
- `is_available` (bool) : Disponibilité

**Méthodes :**
- `to_dict()` : Convertit en dictionnaire JSON
- `from_dict(data)` : Crée un Book depuis un dictionnaire

---

## Classe `BookManager` (managers/book_manager.py)

Gère la collection de livres avec sauvegarde automatique dans `data/books.json`.

**Méthodes :**
- `add_book(book)` : Ajoute un livre
- `delete_book(book_id)` : Supprime par ID
- `get_book_by_id(book_id)` : Récupère par ID
- `search_by_title(title)` : Recherche par titre (insensible à la casse)
- `list_all_books()` : Retourne tous les livres

**Exceptions :**
- `ValueError` : Si validation échoue ou ID introuvable

---

## Utilisation rapide

```python
from models.book import Book
from managers.book_manager import BookManager

manager = BookManager()
manager.add_book(Book("1984", "George Orwell"))

resultats = manager.search_by_title("1984")
for livre in resultats:
    print(livre)
```

---

**Persistance :** Automatique dans `data/books.json`