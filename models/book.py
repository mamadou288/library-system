import uuid
from datetime import datetime

class Book:
    """
    La classe Book représente un livre dans notre système
    """
    def __init__(self, title: str, author: str, id=None, added_at=None, is_available=True):
        if not title.strip():
            raise ValueError("Le titre ne peut pas être vide")
        
        if not author.strip():
            raise ValueError("L'auteur ne peut pas être vide")
        
        self.id = id if id else uuid.uuid4()  
        self.title = title.strip()
        self.author = author.strip()
        self.added_at = added_at if added_at else datetime.now()  
        self.is_available = is_available  

    def to_dict(self):
        """
        Convertit l'objet Book en dictionnaire pour la sérialisation JSON
        """
        return {
            "id": str(self.id),  # UUID → string (car JSON ne comprend pas UUID)
            "title": self.title,  # string → reste string
            "author": self.author,  # string → reste string
            "added_at": self.added_at.isoformat(),  # datetime → string au format ISO (ex: "2024-11-06T10:30:00")
            "is_available": self.is_available  # bool → reste bool (JSON comprend les booléens)
        }
    

    @classmethod
    def from_dict(cls, data: dict):
        """
        Convertit le JSON en dict
        """
        return cls(
            title=data["title"],
            author=data["author"],
            id=uuid.UUID(data["id"]),
            added_at=datetime.fromisoformat(data["added_at"]),
            is_available=data["is_available"]
        )
    

    def __str__(self):
        return f"{self.title} - {self.author}"
