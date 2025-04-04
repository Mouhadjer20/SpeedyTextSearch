from django.shortcuts import render
from .search import lookup

def search_view(request):
    query_params = request.GET
    query = query_params.get('q')
    if query is not None :
        documents =  lookup(query)
        return render(request, template_name="search/search.html", context={'query': query, 'documents': documents})
    return render(request, template_name="search/search.html", context={'query': '', 'documents': ''})