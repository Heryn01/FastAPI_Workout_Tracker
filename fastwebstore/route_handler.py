from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)

from fastapi import APIRouter
from fastwebstore.auth.views import router as auth_router
from fastwebstore.models import HTTPException

routes = [
    (),
]
    

    

router = APIRouter()
router.include_router(
    auth_router,
    tags=["auth"],
    responses={
        HTTP_400_BAD_REQUEST: {"model": HTTPException},
        HTTP_403_FORBIDDEN: {"model": HTTPException},
    },
)