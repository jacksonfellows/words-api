from flask import Flask, request, Response
from flask_restful import Resource, Api
import pickle, random, json
from load_words import load_words

app = Flask(__name__)
api = Api(app)

class Words(Resource):
    def options (self):
        return {'Allow': 'POST'}, 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*'
            }

    def post(self):
        try:
            num_words = int(request.get_json()['num'])
        except:
            resp = Response(json.dumps({'error': 'Could not interpret the request {}.'.format(request)}), status=400)
        else:
            words = []
            while num_words > 0:
                words.append(words_list[random.randrange(0, stop=len(words_list))])
                num_words -= 1
            resp = Response(json.dumps({'words': words}))
        finally:
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        

api.add_resource(Words, '/')

def get_word_list():
    with open('words.pkl', 'rb') as words_file:
        return pickle.load(words_file)

if __name__ == '__main__':
    try:
        words_list = get_word_list()
    except:
        load_words()
        words_list = get_word_list()

    app.run(debug=True)