## Entendendo a API
Uma Rest API usando Flask que recebe através do método GET um peso e uma altura, calcula e retorna o IMC juntamente com as classificações em formato Json.

![Captura de tela de 2020-07-12 21-49-30](https://user-images.githubusercontent.com/48656494/87260761-c30a0980-c489-11ea-87bf-384fed539df5.png)


### Requisitos 
 - Possuir o python3 instalado corretamete
 - Ter o PIP instalado na máquina
 - Ter o Flask instalado na máquina

### Configurar requisitos no linux ubuntu
- Python3: ```sudo apt-get install python3```
- PIP3: ```sudo apt-get install python3-pip```
- Flask: ```pip3 install Flask```
- Clonar o repositório: ```git clone https://github.com/dassaev-lima/flask-api-imc```

### Como executar
- Acesse o diretório da aplicação via terminal e execute o seguinte comando.

```python3 app.py runserver```

### Acessar de forma online

http://flask-api-imc.herokuapp.com/imc/peso=58/altura=1.60
