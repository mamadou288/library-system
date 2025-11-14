from models.user import User
from managers.user_manager import UserManager

print("=== TEST UserManager ===\n")

# 1. Créer un manager
manager = UserManager()
print(f"1. Users au départ : {len(manager.users)}")

# 2. Ajouter des users
print("\n2. Ajouter 3 users")
manager.add_user(User("Alice Dupont", "alice@example.com"))
manager.add_user(User("Bob Martin", "bob@example.com"))
manager.add_user(User("Charlie Alice", "charlie@example.com"))
print(f"   Users en mémoire : {len(manager.users)}")

# 3. Lister tous les users
print("\n3. Liste complète :")
for user in manager.list_all_users():
    print(f"   - {user}")

# 4. Recherche par nom
print("\n4. Recherche : 'alice' (insensible à la casse)")
results = manager.search_by_name("alice")
print(f"   Trouvé : {len(results)} user(s)")
for user in results:
    print(f"   - {user}")

# 5. Redémarrage (vérifier persistance)
print("\n5. Redémarrage simulé")
manager2 = UserManager()
print(f"   Users chargés : {len(manager2.users)}")

# 6. Supprimer un user
print("\n6. Supprimer 'Bob Martin'")
bob = results[0] if "Bob" in results[0].name else None
if not bob:
    bob = [u for u in manager2.users if "Bob" in u.name][0]
manager2.delete_user(str(bob.id))
print(f"   Users restants : {len(manager2.users)}")
for user in manager2.list_all_users():
    print(f"   - {user}")