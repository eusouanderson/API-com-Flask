# models.py
class Jogo:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao
        }

jogos = [
    Jogo(1, "Akido Arena", "Um emocionante jogo de combate multiplayer 2D."),
    Jogo(2, "Outro Jogo", "Descrição de outro jogo aqui."),
]
