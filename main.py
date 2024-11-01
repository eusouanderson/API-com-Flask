from flask import Flask, make_response, jsonify, request
from bd import jogos, find_jogo_by_id
from models import *

app = Flask(__name__)

@app.route('/jogos', methods=['GET'])
def get_jogos():
    return make_response(
        jsonify([jogo.to_dict() for jogo in jogos]), 200  # Retorna todos os jogos
    )

@app.route('/jogos/<int:jogo_id>', methods=['GET'])
def get_jogo(jogo_id):
    jogo = find_jogo_by_id(jogo_id)
    if jogo:
        return make_response(jsonify(jogo.to_dict()), 200)
    return make_response(jsonify({'error': 'Jogo não encontrado'}), 404)

@app.route('/jogos', methods=['POST'])
def create_jogo():
    jogo_data = request.json
    if not jogo_data or 'nome' not in jogo_data or 'descricao' not in jogo_data:
        return make_response(jsonify({'error': 'Dados do jogo inválidos'}), 400)
    
    new_id = max(jogo.id for jogo in jogos) + 1  # Gera um novo ID
    novo_jogo = Jogo(new_id, jogo_data['nome'], jogo_data['descricao'])
    jogos.append(novo_jogo)
    return make_response(jsonify(novo_jogo.to_dict()), 201)

@app.route('/jogos/<int:jogo_id>', methods=['PUT'])
def update_jogo(jogo_id):
    jogo = find_jogo_by_id(jogo_id)
    if not jogo:
        return make_response(jsonify({'error': 'Jogo não encontrado'}), 404)

    jogo_data = request.json
    if 'nome' in jogo_data:
        jogo.nome = jogo_data['nome']
    if 'descricao' in jogo_data:
        jogo.descricao = jogo_data['descricao']

    return make_response(jsonify(jogo.to_dict()), 200)

@app.route('/jogos/<int:jogo_id>', methods=['DELETE'])
def delete_jogo(jogo_id):
    jogo = find_jogo_by_id(jogo_id)
    if not jogo:
        return make_response(jsonify({'error': 'Jogo não encontrado'}), 404)

    jogos.remove(jogo)
    return make_response(jsonify({'message': 'Jogo excluído com sucesso.'}), 204)

if __name__ == '__main__':
    app.run(debug=True)
