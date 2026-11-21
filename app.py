from flask import Flask

app = Flask(__name__)

@app.get("/")
def mensagem():
    return {
      "mensagem": "API de chamados em funcionamento"
    }
if __name__ == "__main__":
    app.run()
