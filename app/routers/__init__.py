from .health import router as health_router
from .hello import router as hello_router

routers = [
    health_router,
    hello_router,
]