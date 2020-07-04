import solr
import json


# create a connection to a solr server
s = solr.SolrConnection('http://localhost:8983/solr/skillmatrix')
with open('Master.json') as f:
    data=json.load(f)
# print(data)


# add a document to the index
doc = dict(
    id=2,
    title='Lucene in Action',
    author=['Erik Hatcher', 'Otis Gospodnetić'],
    )
s.add(data, commit=True)

# # do a searchgit
# response = s.select('title:lucene')
# for hit in response.results:
#     print(hit['title'])