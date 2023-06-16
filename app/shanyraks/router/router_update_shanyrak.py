from fastapi import Depends, Response, status
from typing import Any

from app.utils import AppModel
from pydantic import Field

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from ..service import Service, get_service
from . import router


class UpdateShanyrakRequest(AppModel):
    id: Any = Field(alias="_id")
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str
    user_id: Any

@router.patch("/{shanyrak_id:str}")
def Update_shanyrak(
    shanyrak_id: str,
    input: UpdateShanyrakRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    update_result = svc.repository.update_shanyrak(shanyrak_id, jwt_data.user_id, input.dict())
    if update_result.modified_count == 1:
        return Response(status_code=200)
    return Response(status_code=404)