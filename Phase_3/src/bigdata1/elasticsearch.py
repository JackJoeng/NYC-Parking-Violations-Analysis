from datetime import datetime
from elasticsearch import Elasticsearch

def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
        es.indices.put_mapping(index=index_name, doc_type=doc_type)
    except:
        pass
    return es

def convert_dtype(item):
    for key, value in item.items():
        if 'amount' in key:
            item[key] = float(value)
        elif 'number' in key:
            item[key] = int(value)
        elif 'date' in key:
            item[key] = datetime.strptime(item[key], '%m/%d/%Y').date()
