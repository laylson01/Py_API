# Music API (Basic API)

Este projeto é uma API simples desenvolvida em Flask para gerenciar uma lista de músicas. A API permite obter a lista de músicas, consultar uma música por ID, e editar uma música por ID.

## Instalação

Para instalar e executar este projeto, siga os seguintes passos:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/music-api.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd music-api
    ```
3. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```
4. Instale as dependências:
    ```bash
    pip install Flask
    ```
## Como usar

1. Inicie o servidor Flask:
    ```bash
    python app.py
    ```
2. O servidor estará rodando em `http://localhost:4000`.

## Endpoints
### Obter todas as músicas

- **URL:** `/musics`
- **Método:** `GET`
- **Descrição:** Retorna a lista de todas as músicas.
- **Resposta:**
    ```json
    [
        { 
            "id": 1,
            "musica": "Carry On",
            "cantor": "Angra"
        },
        { 
            "id": 2,
            "musica": "Fairy Tail",
            "cantor": "André Matos"
        },
        {   
            "id": 3,
            "musica": "Moonlight",
            "cantor": "Víper"
        }
    ]
    ```
### Consultar uma música por ID
- **URL:** `/musics/<int:id>`
- **Método:** `GET`
- **Descrição:** Retorna uma música específica pelo ID.
- **Parâmetros de URL:**
    - `id` (int): O ID da música a ser consultada.
- **Resposta:**
    ```json
    {
        "id": 1,
        "musica": "Carry On",
        "cantor": "Angra"
    }
    ```

### Editar uma música por ID
- **URL:** `/musics/<int:id>`
- **Método:** `PUT`
- **Descrição:** Edita uma música específica pelo ID.
- **Parâmetros de URL:**
    - `id` (int): O ID da música a ser editada.
- **Corpo da Requisição:**
    ```json
    {
        "musica": "Nova Música",
        "cantor": "Novo Cantor"
    }
    ```
- **Resposta:**
    ```json
    {
        "id": 1,
        "musica": "Nova Música",
        "cantor": "Novo Cantor"
    }
    ```
### Adicionar nova musica
- **Endpoint:** `/musics/`
- **Method:** POST
- **Description:** Add a new music record.
    **Request Body:**
    ```json
    {
        "id": 4,
        "musica": "New Song",
        "cantor": "New Artist"
    }
    ```
    **Response:**
    ```json
    [
        {
            "id": 4,
        "musica": "New Song",
        "cantor": "New Artist"
        },
    ]
    ```
   Delete Music Record by ID
- **Endpoint:** `/musics/<id>`
- **Method:** DELETE
- **Description:** Delete a specific music record by its ID.
    **Response:**
    ```json
    [
        {
            "id": 1,
            "musica": "Carry On",
            "cantor": "Angra"
        },
      
     
    ]    
    ```
## Testar com Cantor (Comentado no Código)
Há um trecho comentado no código para testar a consulta de música pelo nome do cantor:

```python
@app.route("/musics/<string:cantor>", methods=["GET"])
def consult_music_cantor(cantor):
    for msc in musics:
        if msc.get("cantor") == cantor:
            return jsonify(msc)
```
Para ativar esse teste, descomente o código e ajuste conforme necessário.
## Configuração
- O servidor Flask está configurado para rodar localmente na porta 4000.
- Debug mode está ativado para facilitar o desenvolvimento e a depuração.
```python
app.run(port=4000, host="localhost", debug=True)
```
## Contribuição
Sinta-se à vontade para contribuir com este projeto enviando pull requests ou abrindo issues no repositório.
## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
