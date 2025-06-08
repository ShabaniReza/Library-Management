from django_filters.rest_framework import FilterSet
from .models import Author

class AuthorFilter(FilterSet):
    class Meta:
        model = Author
        fields = {
            'date_of_birth': ['gt', 'lt'],
            'date_of_death': ['gt', 'lt']
        }