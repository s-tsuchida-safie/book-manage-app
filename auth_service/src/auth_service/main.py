from fastapi import FastAPI

from auth_service.app.router.admin import router as AdminRouter
from auth_service.app.router.auth import router as AuthRouter
from auth_service.app.router.user import router as UserRouter

app = FastAPI()
app.include_router(AdminRouter)
app.include_router(AuthRouter)
app.include_router(UserRouter)
