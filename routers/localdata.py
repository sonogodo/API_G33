from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import databases

router = APIRouter()

class WineRequest(BaseModel):
    page: str
    subpage: str
    api_key: str


@router.post("/localdata/")
def get_dataframe(request: WineRequest):
    dict_return = {}
    dict_return['msg'] = "Retornando dados salvos na Base Local"
    dict_return['dado'] = databases.return_all_tables()
    return dict_return

