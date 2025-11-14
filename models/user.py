import uuid
from datetime import datetime


class User:
    """
    Représente un User dans le système de bibliothèque.
    
    Attributs:
    - id (UUID généré automatiquement)
    - name (obligatoire, non vide)
    - email (obligatoire, non vide)
    - joined_at (date générée automatiquement)
    """
    
    def __init__(self, name: str, email: str, id=None, joined_at=None) -> None:
        """
        Crée une nouvelle instance de User.
        """
        if not name.strip():
            raise ValueError("Le nom ne peut pas être vide")
        
        if not email.strip():
            raise ValueError("L'email ne peut pas être vide")
        
        self.id = id if id else uuid.uuid4()
        self.name = name.strip()
        self.email = email.strip()
        self.joined_at = joined_at if joined_at else datetime.now()

    def to_dict(self) -> dict:
        """
        Convertit l'objet User en dictionnaire pour la sérialisation JSON.
        """
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "joined_at": self.joined_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        """
        Crée un objet User depuis un dictionnaire.
        Retourne une nouvelle instance de User avec les données fournies
        """
        return cls(
            name=data["name"],
            email=data["email"],
            id=uuid.UUID(data["id"]),
            joined_at=datetime.fromisoformat(data["joined_at"])
        )
    
    def __str__(self) -> str:
        """
            str: Format "name - email"
        """
        return f"{self.name} - {self.email}"
