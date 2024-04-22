from pprint import pprint

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError
from decouple import config

from managers.home_manager import HomeManager
from schemas.response.home_response import HomeResponseSchema

mapping = {
    "mappings": {
        "properties": {
            "pin": {"properties": {"location": {"type": "geo_point"}}},
        }
    }
}


class Search:
    _connected: bool = True

    def __init__(self) -> None:
        try:
            # Cloud confguration
            # self.es = Elasticsearch(
            #     api_key=config("ELASTIC_API_KEY"), cloud_id=config("ELASTIC_CLOUD_ID")
            # )
            # Container config without pass and keys
            self.es = Elasticsearch(config("ELASTIC_HOST"))
            client_info = self.es.info()
            print("Connected to Elasticsearch!")
            pprint(client_info.body)
        except ConnectionError:
            self._connected = False
            print("Can't connect")

    def create_index(self):
        self.es.indices.delete(index="real_estate_homes", ignore_unavailable=True)
        self.es.indices.create(index="real_estate_homes", body=mapping)

    def insert_document(self, document):
        return self.es.index(index="real_estate_homes", body=document)

    def insert_documents(self, documents):
        operations = []
        for document in documents:
            operations.append({"index": {"_index": "real_estate_homes"}})
            operations.append(document)
        return self.es.bulk(operations=operations)

    def reindex_homes(self):
        if not self._connected:
            return
        self.create_index()
        homes = HomeManager.select_all_homes()
        for home in homes:
            if home.latitude and home.longitude:
                home.pin = {
                    "location": {
                        "lat": float(home.latitude),
                        "lon": float(home.longitude),
                    }
                }
            else:
                home.pin = None
        resp_schema = HomeResponseSchema()
        resp = resp_schema.dump(homes, many=True)
        return self.insert_documents(resp)

    def search(self, **query_args):
        if self._connected:
            return self.es.search(index="real_estate_homes", **query_args)
        return None


es = Search()
