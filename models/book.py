import uuid
from datetime import datetime


class Book:
    """
    Représente un livre dans le système de bibliothèque.
    
    Attributs:
        id (UUID)
        title (str)
        author (str)
        added_at (datetime)
        is_available (bool)
    """
    
    def __init__(self, title: str, author: str, id=None, added_at=None, is_available: bool = True) -> None:
        """
        Crée une nouvelle instance de Book.
        """
        if not title.strip():
            raise ValueError("Le titre ne peut pas être vide")
        
        if not author.strip():
            raise ValueError("L'auteur ne peut pas être vide")
        
        self.id = id if id else uuid.uuid4()
        self.title = title.strip()
        self.author = author.strip()
        self.added_at = added_at if added_at else datetime.now()
        self.is_available = is_available

    def to_dict(self) -> dict:
        """
        Convertit l'objet Book en dictionnaire pour la sérialisation JSON.
        """
        return {
            "id": str(self.id),
            "title": self.title,
            "author": self.author,
            "added_at": self.added_at.isoformat(),
            "is_available": self.is_available
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """
        Crée un objet Book depuis un dictionnaire.
        Retourne une nouvelle instance de Book avec les données fournies
        """
        return cls(
            title=data["title"],
            author=data["author"],
            id=uuid.UUID(data["id"]),
            added_at=datetime.fromisoformat(data["added_at"]),
            is_available=data["is_available"]
        )
    
    def __str__(self) -> str:
        """
            str: Format "Titre - Auteur"
        """
        return f"{self.title} - {self.author}"
