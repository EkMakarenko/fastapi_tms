from src.core.db import Session
from src.core.managers.base_manager import BaseManager
from src.models.hotel_model import Hotel


class HotelManager(BaseManager):

    table = Hotel

    @classmethod
    def create_hotel(cls, hotel, session: Session):
        return cls.create(input_data=hotel, session=session)
