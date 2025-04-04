import hashlib
from elasticsearch import Elasticsearch
from django.db import models

ELASTIC_HOST = "http://localhost:9200"
INDEX_NAME = "research_library"
es_client = Elasticsearch(hosts=[ELASTIC_HOST])

class ResearchDocument(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title", blank=False, null=False)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    author = models.CharField(max_length=255, verbose_name="Author", blank=False, null=False)
    
    keywords = models.JSONField(default=list, blank=True)
    publication_date = models.DateField(blank=False, null=False)
    university = models.CharField(max_length=255, blank=False, null=False)

    file = models.FileField(upload_to='uploads/research_papers/%y/%m/%d')

    file_size = models.BigIntegerField(blank=True, null=True, editable=False)
    file_type = models.CharField(max_length=50, blank=True, null=True, editable=False)
    file_hash = models.CharField(max_length=64, blank=True, null=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
       
        if self.file:
            # Compute File Hash (MD5)
            self.file_hash = hashlib.md5(self.file.read()).hexdigest()
            
            # Extract File Metadata
            self.file_size = self.file.size
            self.file_type = self.file.name.split('.')[-1].lower()

        super().save(*args, **kwargs)

        # Index document in Elasticsearch only if it's a new entry
        if not self.pk:
            document_data = {
                "title": self.title,
                "description": self.description or None,
                "author": self.author,
                "keywords": self.keywords,
                "publication_date": self.publication_date.isoformat(),
                "university": self.university,
                "file_path": self.file.url,
                "file_size": self.file_size,
                "file_hash": self.file_hash,
                "file_type": self.file_type,
                "created_at": self.created_at.isoformat(),
            }
            es_client.index(index=INDEX_NAME, id=self.id, document=document_data)

    def __str__(self):
        return self.title
