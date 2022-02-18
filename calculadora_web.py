# criar uma calculadora web
# front-end deve ser um form com 3 campos e um botão
#   dois campos para os numeros e um campo para a operação a ser aplicada
# back-end deve ser feito em flask.
#   recebe a requisição e processa a operação e retorna uma resposta.

#from cProfile import run
from flask import Flask, request, render_template
from operacoes import adicao, subtracao, multiplicacao, divisao

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calcular", methods = ["GET", "POST"])
def calcula():
    num1  = int(request.form["num1"])
    num2  = int(request.form["num2"])
    operacao = request.form["oper"]
    if operacao == "somar":
        return str(adicao(num1, num2))
    elif operacao == "subtrair":
        return str(subtracao(num1, num2))
    elif operacao == "multiplicar":
        return str(multiplicacao(num1, num2))
    else:
        return str(divisao(num1, num2))


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)