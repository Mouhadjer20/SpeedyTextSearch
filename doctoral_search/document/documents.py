# search/documents.py
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import ResearchDocument

@registry.register_document
class ResearchDocumentDocument(Document):
    class Index:
        name = 'research_library'

    # Meta Data of Document
    file_path = fields.TextField(attr='get_absolute_url')
    file_size = fields.IntegerField(attr='extract_file_size')
    file_type = fields.TextField(attr='extract_file_type')
    file_hash = fields.TextField(attr='compute_file_hash')

    # Special handling for keywords
    keywords = fields.KeywordField(
        attr='keywords',
        multi=True  # This will automatically split on commas
    )

    class Django:
        model = ResearchDocument
        model.keywords
        fields = [
            'title',
            'description',
            'author',
            'publication_date',
            'university',
            'created_at',
        ]
