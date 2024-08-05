from flask import Flask, jsonify, request

app = Flask(__name__)

music = [
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
@app.route ("/music")
def obt_music ():
   return jsonify(music)

app.run(port=4000, host="localhost", debug=True)