from datetime import datetime

from typing import List, Dict
from .base import Base


class Audit(Base):
    """Audit log entry"""
    # TODO: replace with actual model
    username: str
    timestamp: datetime = datetime.utcnow()
