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
@app.route("/musics/<int:id>",methods=["GET"] )

def consult_music_id(id):
   for musica in musics:
      if musica.get ("id") == id:
       return jsonify(musica)






app.run(port=4000, host="localhost", debug=True) #Config para acesssar localmente.