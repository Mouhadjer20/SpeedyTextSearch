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
    keywords = models.TextField(help_text="put between each tow keywords ',' without any spaces")  # Store as comma-separated text
    #keywords_json = models.JSONField(default=list, blank=True, null=True) # Store as a list
    publication_date = models.DateField(blank=False, null=False)
    university = models.CharField(max_length=255, blank=False, null=False)

    file = models.FileField(upload_to='documents/')

    created_at = models.DateTimeField(auto_now_add=True)

    def get_keywords(self):
        """Return keywords as a list"""
        return self.keywords
    
    def get_absolute_url(self):
        return f"{self.file.path}" #reverse("model_detail", kwargs={"pk": self.pk})

    def compute_file_hash(self) -> str:
        """Compute File Hash (MD5)"""
        return hashlib.md5(self.file.read()).hexdigest()
    
    def extract_file_size(self):
        """Extract File Size"""
        return self.file.size

    def extract_file_type(self):    
        """Extract File Type"""
        return self.file.name.split('.')[-1].lower()

    def __str__(self):
        return self.title
