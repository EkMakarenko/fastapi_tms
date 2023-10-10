from hw.src.core.managers.hotel_manager import HotelManager


class HotelService:

    @staticmethod
    def create_hotel(hotel: dict, session):
        return HotelManager.create(input_data=hotel, session=session)
