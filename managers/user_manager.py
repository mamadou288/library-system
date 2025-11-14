import json
import os
from models.user import User


class UserManager:
    """
    Gestionnaire de la collection de User avec JSON.
    
    Attributs:
        users (list[User])
        json_file (str): Chemin du fichier JSON de sauvegarde
    """
    
    def __init__(self) -> None:
        """
        Initialise le gestionnaire et charge les livres depuis le fichier JSON.
        """
        self.users = []
        self.json_file = "data/users.json"
        self.load_from_json()
    
    def load_from_json(self) -> None:
        """
        Charge les users depuis le fichier JSON.
        Si le fichier n'existe pas, initialise une liste vide.
        """
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as f:
                users_data = json.load(f)
            self.users = [User.from_dict(user) for user in users_data]
    
    def save_to_json(self) -> None:
        """
        Sauvegarde tous les users dans le fichier JSON.
        Crée le dossier data/ s'il n'existe pas.
        """
        os.makedirs("data", exist_ok=True)
        users = [user.to_dict() for user in self.users]
        with open(self.json_file, "w") as f:
            json.dump(users, f, indent=2)
    
    def add_user(self, user: User) -> None:
        """
        Ajoute un users et sauvegarde automatiquement.
        """
        if user is None:
            raise ValueError('Veuillez entrer un utilisateur')
        
        self.users.append(user)
        self.save_to_json()
    
    def delete_user(self, user_id: str) -> None:
        """
        Supprime un user par son ID et sauvegarde automatiquement.
        """
        for user in self.users:
            if str(user.id) == user_id:
                self.users.remove(user)
                self.save_to_json()
                break
        else:
            raise ValueError(f"L'utilisateur avec l'ID {user_id} introuvable")
    
    def get_user_by_id(self, user_id: str) -> User:
        """
        Retourne un user par son ID.
        """
        for user in self.users:
            if str(user.id) == user_id:
                return user
        else:
            raise ValueError(f"L'utilisateur avec l'ID {user_id} introuvable")
    
    def search_by_name(self, name: str) -> list[User]:
        """
        Recherche des utilisateurs dont le nom contient la chaîne donnée (insensible à la casse).
        """
        return [user for user in self.users if name.lower() in user.name.lower()]
    
    def list_all_users(self) -> list[User]:
        """
        Retourne tous les utilisateurs .
        """
        return self.users