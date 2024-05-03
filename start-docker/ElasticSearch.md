## To start ElasticSearch docker container without security layers

docker run -p 9200:9200 -d --name elasticsearch 
  -e "discovery.type=single-node" 
  -e "xpack.security.enabled=false" 
  -e "xpack.security.http.ssl.enabled=false" 
  -e "xpack.license.self_generated.type=trial" 
  -m 1g
  docker.elastic.co/elasticsearch/elasticsearch:8.13.0

