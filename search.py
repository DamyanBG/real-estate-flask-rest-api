import json
from pprint import pprint

from elasticsearch import Elasticsearch
from decouple import config
from managers.home_manager import HomeManager
from schemas.response.home_response import HomeResponseSchema

class Search:
    def __init__(self) -> None:
        self.es = Elasticsearch(api_key=config("ELASTIC_API_KEY"), cloud_id=config("ELASTIC_CLOUD_ID"))
        client_info = self.es.info()
        print("Connected to Elasticsearch!")
        pprint(client_info.body)

    def create_index(self):
        self.es.indices.delete(index='real_estate_homes', ignore_unavailable=True)
        self.es.indices.create(index='real_estate_homes')

    def insert_document(self, document):
        return self.es.index(index="real_estate_homes", body=document)
    
    def insert_documents(self, documents):
        operations = []
        for document in documents:
            operations.append({'index': {'_index': "real_estate_homes"}})
            operations.append(document)
        return self.es.bulk(operations=operations)
    
    def reindex_homes(self):
        self.create_index()
        homes = HomeManager.select_all_homes()
        resp_schema = HomeResponseSchema()
        return self.insert_documents(resp_schema.dump(homes, many=True))


    def search(self, **query_args):
        return self.es.search(index="real_estate_homes", **query_args)

es = Search()