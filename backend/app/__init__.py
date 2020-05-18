from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from starlette.staticfiles import StaticFiles

from .core import core as core_router
from app.utils.db_loader import connect_db, disconnect_db
from app.utils.error_handlers import http_error_handler, http_422_error_handler

import config


app = FastAPI(openapi_prefix="/api",
              openapi_url='/static/openapi.json',
              docs_url=None, redoc_url=None)

# handling static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# adding schema documentation routes


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# connect to database
app.add_event_handler("startup", connect_db)
app.add_event_handler("shutdown", disconnect_db)

# error handling
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(
    HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)


# include various routes
app.include_router(core_router, prefix="/core", tags=["core"])
