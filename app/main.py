import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.exception_handlert import custom_exception_response
from app.routers import auth

app = FastAPI(
    title=settings.project_name,
    description="API for PicStory application",
    version="0.1.0",
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HTTP 예외 처리기 등록
app.add_exception_handler(
    exc_class_or_status_code=HTTPException,
    handler=custom_exception_response,
)

# 라우터 등록
app.include_router(router=auth.router)


def main() -> None:
    uvicorn.run(
        app="app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()
