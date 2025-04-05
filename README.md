# SpeedyTextSearch

This project demonstrates how to integrate Elasticsearch with a Django web application to build an efficient search system.

## Features

- Django-based web application
- Integration with Elasticsearch for fast, full-text search
- Ability to index and search data from Django models
- Use of Elasticsearch query DSL for advanced search functionality

## Prerequisites

- Python 3.8 or higher
- Django 4.x or higher
- Elasticsearch 7.x or higher
- pip

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Mouhadjer20/SpeedyTextSearch.git
    cd SpeedyTextSearch.git
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv env
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Elasticsearch**:
   - Follow the official Elasticsearch installation guide for your OS: [Elasticsearch Installation](https://www.elastic.co/guide/en/elasticsearch/reference/index.html)
   - OR Download From Ducker

5. **Configure Django settings**:
   - Open `settings.py` and configure the Elasticsearch settings. Example:

    ```python
    # settings.py
    ELASTICSEARCH_DSL = {
        'default': {
            'hosts': ['localhost:9200'],  # Change to your Elasticsearch host
        }
    }
    ```

6. **Run migrations**:

    ```bash
    python manage.py migrate
    ```

7. **Run the Django development server**:

    ```bash
    python manage.py runserver
    ```

8.  **Test Elasticsearch integration**:
    - Once the server is running, visit your app's search page and test the Elasticsearch functionality by searching for indexed data.


## Troubleshooting

- **Elasticsearch is not running**: Ensure that Elasticsearch is running on the correct host and port (default is `localhost:9200`). You can verify this by visiting `http://localhost:9200` in your browser or using `curl`:

    ```bash
    curl -X GET "localhost:9200/"
    ```

- **Indexing error**: If you encounter an error while indexing, check your model and Elasticsearch connection settings. Common issues include incorrect index names or fields, and Elasticsearch not being available.

- **No search results**: If searches aren't returning results, ensure that data is properly indexed in Elasticsearch. You can check this by querying Elasticsearch directly:

    ```bash
    curl -X GET "localhost:9200/products/_search?q=your-search-term"
    ```

- **Django settings not applied**: Ensure that your `settings.py` is correctly configured for the production environment. This includes database settings, Elasticsearch configuration, and static files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [django-elasticsearch-dsl](https://django-elasticsearch-dsl.readthedocs.io/)
