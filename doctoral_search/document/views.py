from django.shortcuts import render
from django.http import FileResponse
from .models import ResearchDocument
from .forms import ResearchDocumentForm

def document_view(request, doc_id):
    document = ResearchDocument.objects.get(id=doc_id)
    return FileResponse(document.file.open(), as_attachment=False)

def document_upload(request):
    if request.method == "POST":
        dataForm = ResearchDocumentForm(request.POST, request.FILES)
        if dataForm.is_valid():
            dataForm.save()
            return render(request=request, template_name="upload/upload.html", context={'form': ResearchDocumentForm, 'message': 'Document Added successfully!!'})
        return render(request=request, template_name="upload/upload.html", context={'form': ResearchDocumentForm, 'message': 'Faild Register Document'})
    return render(request=request, template_name="upload/upload.html", context={'form': ResearchDocumentForm, 'message': 'Add You Document Here!!'})