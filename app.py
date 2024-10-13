from flask import Flask, render_template, jsonify
import threading

app = Flask(__name__)

# Função que será executada após um intervalo de tempo
def delayed_function():
    print("Função executada após 5 segundos!")

# Rota que renderiza a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota que inicia o 'setTimeout' equivalente
@app.route('/start-timer')
def start_timer():
    # Timer de 5 segundos que chama a função delayed_function
    t = threading.Timer(5.0, delayed_function)
    t.start()
    return jsonify({"message": "Timer iniciado, a função será executada após 5 segundos!"})

if __name__ == '__main__':
    app.run(debug=True)
