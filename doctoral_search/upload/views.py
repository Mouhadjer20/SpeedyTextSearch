from django.shortcuts import render

def upload_view(request):
    return render(request=request, template_name="upload/upload.html", context={'message': 'Bonjour'})