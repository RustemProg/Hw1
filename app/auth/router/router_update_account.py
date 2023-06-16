from typing import Any, Optional

from fastapi import Depends, Response
from pydantic import Field

from app.utils import AppModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data


class UpdateAccountResponse(AppModel):
    phone: Optional[str]
    name: Optional[str]
    city: Optional[str]


@router.patch("/users/me", response_model=UpdateAccountResponse)
def update_my_account(
    inpu: UpdateAccountResponse,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    svc.repository.update_user(jwt_data.user_id, input)
    return Response(status_code=200)
