from .base import Base, ObjectID


class Rating(Base):
    rating: float
    item_id: ObjectID
    username: str
