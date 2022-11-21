from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from user import user_api
from front import front_api
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(user_api)
app.include_router(front_api)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        debug=True,
        reload=True,
        lifespan="on",
        host="0.0.0.0",
    )
