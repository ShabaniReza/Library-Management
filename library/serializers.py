from rest_framework.serializers import ModelSerializer, SerializerMethodField, DateField, CharField, PrimaryKeyRelatedField, HyperlinkedRelatedField
from .models import Book, Member, BorrowRecord, Author, Genre, MemberImage

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death', 'biography']

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class SimpleGenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class SimpleBookSerializer(ModelSerializer):
    author = HyperlinkedRelatedField(
        queryset = Author.objects.all(), 
        view_name = 'author-detail',
    )
    genres = SimpleGenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_year', 'genres', 'available_copies']

class CreateBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_year', 'genres', 'available_copies']

class ProfileSerializer(ModelSerializer):
    username = SerializerMethodField(read_only=True)
    date_joined = DateField(read_only=True)
    national_code = CharField(read_only=True)
    class Meta:
        model = Member
        fields = ['username', 'national_code', 'first_name', 'last_name', 'address', 'phone_number', 'email', 'date_joined']

    def get_username(self, obj):
        return obj.user.username
    

class MemberImageSerializer(ModelSerializer):
    def create(self, validated_data):
        member_id = self.context['member_id']
        return MemberImage.objects.create(member_id=member_id, **validated_data)
    class Meta:
        model = MemberImage
        fields = ['id', 'image']

class MemberSerializer(ModelSerializer):
    borrowed_books = SerializerMethodField()
    images = MemberImageSerializer(many=True, read_only=True)
    class Meta:
        model = Member
        fields = ['national_code', 'first_name', 'last_name', 'address', 'phone_number', 'email', 'date_joined', 'borrowed_books', 'images']

    def get_borrowed_books(self, obj):
        borrowed_books_list = [
            record.book for record in obj.borrowrecord_set.all() if not record.is_returned
        ]
        return CreateBookSerializer(borrowed_books_list, many=True).data
    
class UpdateMemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'email']


# extentions
class BorrowBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']

class UpdateBorrowRecordSerializer(ModelSerializer):
    book = BorrowBookSerializer(read_only=True)
    class Meta:
        model = BorrowRecord
        fields = ['book', 'borrow_date', 'due_date']


class BorrowRecordSerializer(ModelSerializer):
    book = PrimaryKeyRelatedField(
        queryset=Book.objects.select_related('author').all(),
    )
    class Meta:
        model = BorrowRecord
        fields = ['id', 'book', 'borrow_date', 'due_date']

    def create(self, validated_data):
        member_id = self.context['member_id']
        return BorrowRecord.objects.create(member_id=member_id, **validated_data)
