from elasticsearch import Elasticsearch
from django_elasticsearch_dsl.search import Search
from decouple import config
from doctoral_search.settings import ELASTICSEARCH_DSL
import json

# Elasticsearch Configuration
client = Elasticsearch(hosts=ELASTICSEARCH_DSL['default']['hosts'])
INDEXES = ['research_library']

def lookup(query, index=INDEXES, fields=['title', 'description', 'author', 'keywords', 'university']):
    if not query:
        return {'error': 'No query provided', 'results': []}
    
    # Execute the search
    search = Search(index=index).using(client).query(
        "multi_match", 
        fields=fields, 
        fuzziness="AUTO", 
        query=query
    )
    
    try:
        response = search.execute()
        
        # Convert to clean JSON format
        results = {
            'took': response.took,
            'timed_out': response.timed_out,
            'total': response.hits.total.value,
            'max_score': response.hits.max_score,
            'results': [
                {
                    'id': hit.meta.id,
                    'score': hit.meta.score,
                    **hit.to_dict()  # Include all document fields
                } 
                for hit in response
            ],
            'suggestions': getattr(response, 'suggest', {}),
            'aggregations': getattr(response, 'aggregations', {})
        }
        
        return results
        
    except Exception as e:
        return {
            'error': str(e),
            'results': []
        }