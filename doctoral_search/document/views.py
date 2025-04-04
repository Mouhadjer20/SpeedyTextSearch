from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse
from .models import ResearchDocument

def document_view(request, doc_id):
    document = ResearchDocument.objects.get(id=doc_id)
    return FileResponse(document.file.open(), as_attachment=False)