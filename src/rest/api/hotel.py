from fastapi import APIRouter, status


from src.core.db import session
from src.core.managers.hotel_manager import HotelManager
from src.rest.schemas.hotel_schema import HotelCreateSchema, HotelUpdateResponseSchema, HotelUpdateInputSchema, \
    HotelRetrieveSchema
from src.services.hotel_service import HotelService

router = APIRouter()


@router.get('/hotels', response_model=list[HotelCreateSchema], status_code=status.HTTP_200_OK)
def get_hotel(name):
    return HotelManager.list(session=session)


@router.get('/hotels/{hotel_id}', response_model= HotelRetrieveSchema, status_code=status.HTTP_200_OK)
def get_hotel(hotel_id: int):
    return HotelManager.retrieve(pk=hotel_id, session=session)


@router.post('/hotels', status_code=status.HTTP_201_CREATED)
def create_hotel(hotel: HotelCreateSchema, status_code=status.HTTP_201_CREATED):
    return HotelService.create_hotel(hotel=hotel.__dict__, session=session)


@router.patch('/hotels/{hotel_id}', response_model=HotelUpdateResponseSchema, status_code=status.HTTP_202_ACCEPTED)
def update_hotel(hotel_id: int, input_data: HotelUpdateInputSchema):
    return HotelManager.update(pk=hotel_id, input_data=input_data.__dict__, session=session)


@router.delete('/hotel/{hotel_id}', status_code=status.HTTP_200_OK)
def delete_hotel(hotel_id: int):
    return HotelManager.delete(pk=hotel_id, session=session)
