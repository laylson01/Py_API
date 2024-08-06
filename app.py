from flask import Flask, jsonify, request

app = Flask(__name__)

musics = [
    { 
   "id": 1,
   "musica" : "Carry On",
   "cantor" : "Angra",
},
{ 
   "id": 2,
   "musica" : "Fairy Tail",
   "cantor" : "André Matos",
}, 
{   
   "id": 3,
   "musica" : "Moonlight",
   "cantor" : "Víper",
},  
]
#Função Get/Obter.
@app.route ("/musics", methods=["GET"]) #Rota #Metodo (GET)
def obt_music ():
   return jsonify(musics)

#Função Consultar p/ID
@app.route ("/musics/<int:id>", methods = ["GET"])
def consult_music_id(id):
   for msc in musics:
      if msc.get("id") == id:
         return jsonify(msc)
      
      
      
##Função editar usando ID / Indice
@app.route ("/musics/<int:id>", methods = ["PUT"])
def edit_music_id(id):
   musica_alterada = request.get_json()      
   for indice, msc in enumerate(musics):
      if msc.get("id") == id:
         musics[indice].update(musica_alterada)
         return jsonify(musics[indice])
      
#Função para adicionar novos livros(criar)
@app.route ("/musics/", methods =["POST"])
def add_new_music():
   nova_musica = request.get_json()
   musics.append(nova_musica)   
   return jsonify(musics)


@app.route ("/musics/<int:id>", methods = ["DELETE"])
def del_music(id):
   
   for indice, msc in enumerate (musics):
      if msc.get("id") == id:
         del musics [indice]
         return jsonify(musics)
      





app.run(port=4000, host="localhost", debug=True) #Config para acesssar localmente.














'''
Test Cantor
@app.route("/musics/<string:cantor>",methods=["GET"] )

def consult_music_id(cantor):
   for msc in musics:
      if msc.get("cantor") == cantor:
         return jsonify(msc)
'''