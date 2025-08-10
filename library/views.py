from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import MemberImageSerializer, GenreSerializer, AuthorSerializer, CreateBookSerializer, SimpleBookSerializer, MemberSerializer, BorrowRecordSerializer, UpdateBorrowRecordSerializer, ProfileSerializer, UpdateMemberSerializer
from .models import Book, Member, BorrowRecord, Author, Genre, MemberImage
from .pagination import DefaultPagination
from .filters import AuthorFilter


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'biography']

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @method_decorator(cache_page(60*5))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
    
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('author').prefetch_related('genres').all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author_id']
    pagination_class = DefaultPagination
    search_fields = ['author__first_name', 'author__last_name', 'genres__name', 'title', 'publisher', 'publication_year']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SimpleBookSerializer
        elif self.request.method == 'POST':
            return CreateBookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]
        

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.prefetch_related('borrowrecord_set__book__genres').all()
    filter_backends = [SearchFilter]
    permission_classes = [IsAdminUser]
    pagination_class = DefaultPagination
    search_fields = ['user__username', 'first_name', 'last_name', 'phone_number', 'email']

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateMemberSerializer
        return MemberSerializer

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated], serializer_class = ProfileSerializer)
    def me(self, request):
        member = Member.objects.get(user__id=request.user.id)
        if request.method == 'GET':
            serializer = ProfileSerializer(member)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(member, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class MemberImageViewSet(ModelViewSet):
    serializer_class = MemberImageSerializer

    def get_serializer_context(self):
        return {'member_id': self.kwargs['member_pk']}

    def get_queryset(self):
        return MemberImage.objects.filter(member__pk=self.kwargs['member_pk'])

class ExtentionViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateBorrowRecordSerializer
        return BorrowRecordSerializer

    def get_queryset(self):
        return BorrowRecord.objects.filter(member__pk=self.kwargs['member_pk'])

    def get_serializer_context(self):
        return {'member_id': self.kwargs['member_pk']}