# bd/bd.py
from models import jogos  

def find_jogo_by_id(jogo_id):
    for jogo in jogos:
        if jogo.id == jogo_id:
            return jogo
    return None
