
# Image Resizer
Aplicação para redimensionar uma imagem em segundo plano.

## Microservice API
Esse microserviço recebe uma request em 'form-data' com a imagem e com parâmetros opcionais de width/height.
http://localhost:8081/docs

  
## Microservice Resizer
É o microserviço responsável por redimensionar uma imagem, ele funciona de forma passiva onde fica 'escutando' uma fila.

## Como rodar a aplicação
No diretório .docker executar o comando
```console
$ docker-compose up --b
```
## Ferramentas utilizadas
1. Docker
2. Python 3
3. RabbitMQ
4. FastAPI

## Executando testes unitários
Os testes unitários podem ser executados dentro ou fora do container docker. 
#### Exemplo de teste de dentro do container
```console
$ python -m pytest src/
```