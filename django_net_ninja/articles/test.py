import pytest
from articles.models import Article


# Create your tests here.
@pytest.mark.django_db
def test_create_model_instance():
    article = Article.objects.create(title="name test")
    saved_model_instance = MyModel.objects.get(title="name test")
    assert saved_model_instance.name == "name test"
