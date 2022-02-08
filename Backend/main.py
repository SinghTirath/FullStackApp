from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
import uuid
app = Flask(__name__)

app.config.from_object(__name__)

cors = CORS(app)
#(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})
#CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app, resources={r"/*":{'origins':'*',"allow_headers":"Access-Control-Allow-Origin"}})
#CORS(app,resources={r"/*":{'origins':'http://localhost:8080', "allow_headers":"Access-Control-Allow-Origin"}})

#hello world route
@app.route('/',methods=['GET'])
@cross_origin()
def greetings():
    return("Hello, World")

@app.route('/shark',methods=['GET'])
@cross_origin()
def shark():
    return("Shark!")


GAMES = [
    {   'id':uuid.uuid4().hex,
        'title':'2021',
        'genre':'Sports',
        'played':True,
    },
    {
        'id':uuid.uuid4().hex,
        'title':'Spider Man',
        'genre':'Thriller',
        'played':False,
    },
    {
        'id':uuid.uuid4().hex,
        'title':'Call of Duty',
        'genre':'Action',
        'played':True,
    },
    {
        'id':uuid.uuid4().hex,
        'title':'FIFA 2020',
        'genre':'Sports',
        'played':True,
    },
]


# The GET Route Handler
@app.route('/games', methods=['GET','POST'])
@cross_origin()
def all_games():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'id':uuid.uuid4().hex,
            'title':post_data.get('title'),
            'genre':post_data.get('genre'),
            'played':post_data.get('played')})
        response_object['message'] = 'Game Added!'
    else:
        response_object['games']=GAMES
    return jsonify(response_object)


#The PUT and DELTE route handler
@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
@cross_origin()
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game updated!'
    if request.method == 'DELETE':
        remove_game(game_id)
        response_object['message'] = 'Game removed!'
    return jsonify(response_object)

 

def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False








if __name__ == "__main__":
    app.run(debug=True)


