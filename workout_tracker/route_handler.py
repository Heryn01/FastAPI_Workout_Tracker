from fastapi import APIRouter

from workout_tracker.auth.views import router as auth_router
from workout_tracker.users.views import router as users_router

sub_router = APIRouter()
routes = [
    (users_router, "/users", ["users"]),
]
# generate routes for every non-auth subdomain
for _route, _prefix, _tags in routes:
    sub_router.include_router(_route, prefix=_prefix, tags=_tags)

# add auth domain route
router = APIRouter()
router.include_router(
    auth_router,
    tags=["auth"],
)
# add sub-domain routes
router.include_router(
    sub_router,
)
