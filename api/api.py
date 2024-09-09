##############################
###  KENA MOBILE REST API  ###
###      By @Matt0550      ###
##############################

import datetime

from fastapi import FastAPI
from typing import Any

from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from functions import KenaMobileWorker

# New response structure: {"details": ..., "status_code": ..., "success": ...}
class ResponseStructure(BaseModel):
    details: Any
    success: bool = True
    status_code: int

# New response class
class CustomResponse(JSONResponse):
    def __init__(self, content: Any, status_code: int = 200, *args, **kwargs):
        # Customize content and pass my new content...
        content = ResponseStructure(details=content, success=False if status_code != 200 else True, status_code=status_code)
        super().__init__(content=content.dict(), status_code=status_code, *args, **kwargs)

class PHPSESSID(BaseModel):
    PHPSESSID: str

limiter = Limiter(key_func=get_remote_address, application_limits=["20/day", "2/minute"])

app = FastAPI(default_response_class=CustomResponse, title="KenaMobile Unofficial REST API", description="An unofficial REST API for KenaMobile", version="1.0.0")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SlowAPIMiddleware)

KENA_WORKER = KenaMobileWorker()

UP_START_TIME = datetime.datetime.now() # For the uptime

# Handle the 404 error. Use HTTP_exception_handler to handle the error
@app.exception_handler(StarletteHTTPException)
async def my_custom_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(content={"message": "Not found", "success": False, "code": exc.status_code}, status_code=exc.status_code)
    elif exc.status_code == 405:
        return JSONResponse(content={"message": "Method not allowed", "success": False, "code": exc.status_code}, status_code=exc.status_code)
    else:
        # Just use FastAPI's built-in handler for other errors
        return await http_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    status_code = 422
    print(exc.errors())

    if exc.errors()[0]["type"] == "value_error.any_str.max_length":
        limit = str(exc.errors()[0]["ctx"]["limit_value"])
        return JSONResponse(content={"message": "The value entered is too long. Max length is " + limit, "success": False, "code": status_code}, status_code=status_code)
    elif exc.errors()[0]["type"] == "value_error.missing":
        missing = []
        for error in exc.errors():
            try:
                missing.append(error["loc"][1])
            except:
                missing.append(error["loc"][0])

        return JSONResponse(content={"message": "One or more fields are missing: " + str(missing), "succes": False, "code": status_code}, status_code=status_code)
    else:
        return JSONResponse(content={"message": exc.errors()[0]["msg"], "success": False, "code": status_code}, status_code=status_code)

@app.get("/")
async def root():
    return "Welcome to KenaMobile Unofficial API! By @Matt0550 on GitHub"

@app.get("/status")
def api_status(request: Request):
    # Get the API uptime without microseconds
    uptime = datetime.datetime.now() - UP_START_TIME
    uptime = str(uptime).split(".")[0]

    url = request.url
    url = url.scheme + "://" + url.netloc

    return {"status": "online", "uptime": uptime, "url": url}

def validatePhoneNumber(phoneNumber: str):
    if phoneNumber[0:3] == "+39":
        phoneNumber = phoneNumber[3:]
    if len(phoneNumber) != 10:
        return False
    return True

@app.get("/getCreditInfo")
def getCreditInfo(request: Request, phoneNumber: str, PHPSESSID: PHPSESSID):
    if not validatePhoneNumber(phoneNumber):
        return CustomResponse(content="Invalid phone number", status_code=400)
    
    KENA_WORKER.setPhpSession(PHPSESSID.PHPSESSID)
    return KENA_WORKER.getUserCreditInfo(phoneNumber)

@app.get("/getCustomerDTO")
def getCustomerDTO(request: Request, phoneNumber: str, PHPSESSID: PHPSESSID):
    if not validatePhoneNumber(phoneNumber):
        return CustomResponse(content="Invalid phone number", status_code=400)
    
    KENA_WORKER.setPhpSession(PHPSESSID.PHPSESSID)
    return KENA_WORKER.getCustomerDTO(phoneNumber)

@app.get("/getPromo")
def getPromo(request: Request, phoneNumber: str, PHPSESSID: PHPSESSID):
    if not validatePhoneNumber(phoneNumber):
        return CustomResponse(content="Invalid phone number", status_code=400)
    
    KENA_WORKER.setPhpSession(PHPSESSID.PHPSESSID)
    return KENA_WORKER.getUserPromo(phoneNumber)
