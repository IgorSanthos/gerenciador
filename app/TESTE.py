
from flask  import Flask

app = Flask(__name__)

@app.route('/')
def ola():
    
    if __name__ == "__main__":              # Obrigatorio - Atualiza a pagina automaticamente
        app.run(debug=True)