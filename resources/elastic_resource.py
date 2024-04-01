from flask_restful import Resource

from managers.home_manager import HomeManager
from search import es
from schemas.response.home_response import HomeResponseSchema


class ElasticResource(Resource):
    def get(self, home_id):
        print(home_id)
        home = HomeManager.select_home_by_id(home_id)
        result = es.search(
            query={
                'bool': {
                    'must': {
                        'match': {
                            'city': {
                                'query': home.city
                            }
                        }
                    },
                    'must_not': {
                        'match': {
                            'id': {
                                'query': home.id
                            }
                        }
                    }
                }
            }
        ) 
        print(result['hits']['hits'])
        if len(result['hits']['hits']) == 0:
            return "No results."
        suggested_homes = [suggested_home['_source'] for suggested_home in result['hits']['hits']]
        resp_schema = HomeResponseSchema()
        return resp_schema.dump(suggested_homes, many=True), 200