from django.shortcuts import render
from .search import lookup

def search_view(request):
    query_params = request.GET
    query = query_params.get('q')
    field_choose = query_params.getlist('fields')
    fields = ['title', 'description', 'author', 'keywords', 'university', 'file_content']

    if query:
        documents = lookup(query, fields=field_choose)
        return render(request, "search/search.html", {
            'query': query,
            'field_choose': field_choose,
            'fields': fields,
            'documents': documents
        })

    return render(request, "search/search.html", {
        'query': '',
        'field_choose': fields,
        'fields': fields,
        'documents': ''
    })
