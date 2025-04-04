from django.urls import path
from . import views

urlpatterns = [
    path('document/<int:doc_id>/', views.document_view, name='document-view'),
]