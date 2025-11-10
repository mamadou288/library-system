# Module Users

## Vue d'ensemble

Gestion des utilisateurs avec persistance JSON.

---

## Classe `User` (models/user.py)

**Attributs :**
- `id` (UUID) : Identifiant unique
- `name` (str) : Nom de l'utilisateur
- `email` (str) : Email de l'utilisateur
- `joined_at` (datetime) : Date d'inscription

**Méthodes :**
- `to_dict()` : Convertit en dictionnaire JSON
- `from_dict(data)` : Crée un User depuis un dictionnaire

---

## Classe `UserManager` (managers/user_manager.py)

Gère la collection d'utilisateurs avec sauvegarde automatique dans `data/users.json`.

**Méthodes :**
- `add_user(user)` : Ajoute un utilisateur
- `delete_user(user_id)` : Supprime par ID
- `get_user_by_id(user_id)` : Récupère par ID
- `search_by_name(name)` : Recherche par nom (insensible à la casse)
- `list_all_users()` : Retourne tous les utilisateurs

**Exceptions :**
- `ValueError` : Si validation échoue ou ID introuvable

---

## Utilisation rapide

from models.user import User
from managers.user_manager import UserManager

manager = UserManager()
manager.add_user(User("Alice Dupont", "alice@example.com"))

resultats = manager.search_by_name("alice")
for user in resultats:
    print(user)---

**Persistance :** Automatique dans `data/users.json`