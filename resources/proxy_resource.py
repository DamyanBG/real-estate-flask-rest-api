from flask_restful import Resource, request


class Proxy(Resource):
    def get(self):
        args = request.args 
        url = args.get("url")
        print(url)
        return