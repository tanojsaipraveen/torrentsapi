from flask import Flask
from flask_restful import Api,Resource
import requests
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)
api = Api(app)




class TorrentbyName(Resource):
    def get(self,name):
        response = requests.get("https://api-torrent.vercel.app/api/v1/search?query="+name+"&key=U2FsdGVkX1+n6JlCR3BgA/NkTFI1fWA1rBpg1J+qBHBx2aWt1ZxwHvN0kQXRIjoN")
        return response.json()

class TorrentbyId(Resource):
    def get(self,id):
        response = requests.get("https://api-torrent.vercel.app/api/v1/detail/"+id+"?key=U2FsdGVkX1+n6JlCR3BgA/NkTFI1fWA1rBpg1J+qBHBx2aWt1ZxwHvN0kQXRIjoN")
        return response.json()




api.add_resource(TorrentbyName,"/TorrentbyName/<string:name>")
api.add_resource(TorrentbyId,"/TorrentbyId/<string:id>")



if __name__ == "__main__":
    app.run(debug=True)
