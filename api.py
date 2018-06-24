from flask import Flask, request
from flask_restful import Resource, Api
import pickle, random
from load_words import load_words

app = Flask(__name__)
api = Api(app)

class Words(Resource):
    def put(self):
        num_words = int(request.form['num'])
        words = []
        while num_words > 0:
            words.append(words_list[random.randrange(0, stop=len(words_list))])
            num_words -= 1
        return {'words': words}
        

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