from flask import Flask,jsonify,request
import json
app = Flask(__name__)

@app.route("/imc/peso=<int:peso>/altura=<float:altura>",methods=['GET'])
def imc(peso,altura):
    if request.method == 'GET':
        imc = peso / altura**2
        status = valida_imc(imc)
        return jsonify({'imc':imc,'Classificacao':status})

def valida_imc(imc):
    if imc < 18.5:
        status = 'Peso Baixo'
    elif imc <= 24.9:
        status = 'Peso normal'
    elif imc <= 29.9:
        status = 'sobrepeso'
    elif imc <= 34.9:
        status = 'Obesidade (Grau I)'
    elif imc <= 39.9:
        status = 'Obesidade severa (Grau II)'
    else:
        status = 'Obesidade Morbida (Grau III)'
    return status

if __name__ == '__main__':
    app.run(debug=False)