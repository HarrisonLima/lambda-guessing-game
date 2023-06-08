# Jogo de Adivinhação

# Descrição:
Esta é uma API para um jogo de adivinhação de números. O jogador deve descobrir o número secreto que está entre 01 á 10. O mesmo deve realizar uma requisição de método POST para a API informando o número que deseja e a API retornará o resultado indicando se o número informado está correto ou não. Conforme o número secreto.

# Como usar a API
Endpoint
O endpoint da API é: "https://r51iihzax8.execute-api.us-east-2.amazonaws.com/play"

# Método HTTP
A API suporta o método HTTP POST.

# Parâmetros
A requisição POST deve conter um corpo (body) em formato JSON conforme exemplo abaixo:
user_number: Um número inteiro que representa o número escolhido pelo jogador.

Exemplo do corpo da requisição:

```json
{
    "user_number": 1
}
```

Observação: Substitua o valor 1 pelo número desejado para jogar.

# Exemplo de Requisição
Faça uma requisição POST para o endpoint utilizando o corpo (body) descrito acima para enviar o número escolhido pelo jogador.

# Exemplo de Resposta
A resposta da API será um JSON contendo as seguintes informações:

secret_number: O número secreto gerado pela API.
user_number: O número escolhido pelo jogador.
result: O resultado do jogo, indicando se o número escolhido é igual ao número secreto ou não.

Caso o jogador adivinhe o número secreto, a resposta será:

```json
{
    "secret_number": 9,
    "user_number": 9,
    "result": "Parabéns, você descobriu o número secreto!"
}
```

Caso o jogador não adivinhe o número secreto, a resposta será:

```json
{
    "secret_number": 1,
    "user_number": 9,
    "result": "Número incorreto!"
}
```

# Exemplo de Uso com o Postman
1. Abra o Postman ou um aplicativo similar para realizar requisições HTTP;
2. Crie uma nova requisição do tipo POST;
3. Insira o endpoint da API;
4. No corpo (body) da requisição, selecione a opção "Raw" e escolha o formato "JSON".
5. Cole o exemplo do corpo da requisição descrito anteriormente e altere o valor de "user_number" para o número desejado.
6. Envie a requisição e aguarde a resposta da API.
7. A resposta da API será exibida no painel de visualização do Postman e seguirá o formato descrito anteriormente.

