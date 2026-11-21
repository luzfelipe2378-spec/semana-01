from flask import Flask

app = Flask(__name__)

@app.get("/")
def mensagem():
    return jsonify({
        "mensagem": "API de chamados em funcionamento"
    }), 200
    
if __name__ == "__main__":
    app.run()
