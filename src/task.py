


class Task:
    def __init__(
        self,
        id: int,
        description: str,
        status: str,
        created_at: str,
        updated_at: str
    ):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        }


    def add(self):
        ...
    

    def update(self):
        ...

    
    def delete(self):
        ...

