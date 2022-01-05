from src.main.main import app

@app.get('/', status_code=200)
def consult():
    return {'mensagem': 'Olá, mundo!'}