from models.book import Book
from managers.book_manager import BookManager

print("=== TEST delete_book() ===\n")

# 1. Vider books.json (repartir à zéro)
# Tu peux le faire manuellement : ouvre data/books.json et mets juste []

# 2. Créer un manager et ajouter des livres
manager = BookManager()
livre1 = Book("1984", "George Orwell")
livre2 = Book("Le Petit Prince", "Antoine de Saint-Exupéry")
livre3 = Book("Harry Potter", "J.K. Rowling")

manager.add_book(livre1)
manager.add_book(livre2)
manager.add_book(livre3)

print(f"1. Livres ajoutés : {len(manager.books)}")
for book in manager.books:
    print(f"   - {book} (ID: {book.id})")

# 3. Supprimer le livre 2
print(f"\n2. Supprimer '{livre2.title}'")
manager.delete_book(str(livre2.id))
print(f"   Livres restants : {len(manager.books)}")
for book in manager.books:
    print(f"   - {book}")

# 4. Vérifier la persistance
print("\n3. Redémarrage simulé")
manager2 = BookManager()
print(f"   Livres chargés : {len(manager2.books)}")
for book in manager2.books:
    print(f"   - {book}")

# 5. Tester avec un ID inexistant
print("\n4. Tester avec un ID inexistant")
try:
    manager2.delete_book("id-inexistant-999")
    print("   ❌ Erreur : devrait avoir levé une exception !")
except ValueError as e:
    print(f"   ✅ Erreur capturée : {e}")