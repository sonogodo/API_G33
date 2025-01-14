from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from utils import webscrapping
from utils import databases

router = APIRouter()

class WineRequest(BaseModel):
    page: str
    subpage: str
    api_key: str


@router.post("/webdata/")
def get_dataframe(request: WineRequest):
    dict_return = {}
    web_message = webscrapping.get_all()
    if isinstance(web_message, int):
        dict_return['msg_conexao']  = f"Falha da conexão com o site, retornando dados salvos na DB"
    else:
        databases.save_tables_in_db()
    dict_return['msg'] = web_message
    dict_return['dado'] = databases.return_all_tables()
    return dict_return

