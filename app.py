from flask import Flask, jsonify, request

app = Flask(__name__)

musica = [
    
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