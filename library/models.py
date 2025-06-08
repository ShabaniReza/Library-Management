from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.core.validators import RegexValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.CharField(max_length=100, null=True, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    total_copies = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    available_copies = models.IntegerField(default=models.F('total_copies'))

    def __str__(self):
        return f'{self.title} by {self.author.first_name} {self.author.last_name}'
    
    class Meta:
        ordering = ['title']

class Member(models.Model):
    national_code = models.CharField(
        max_length=255, 
        primary_key=True,
        validators=[RegexValidator(r'^\d{10}$', 'شماره ملی باید شامل 10 رقم باشد و فقط از اعداد تشکیل شده باشد.')]
        )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, validators=[RegexValidator(r'^\d{11}$', 'شماره تماس باید شامل ۱۱ رقم باشد.')])
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return f'{self.book.title} borrowed by {self.member.get_full_name()}'
    
    def mark_as_returned(self):
        self.book.available_copies += 1
        self.book.save()
    
    class Meta:
        ordering = ['book', 'member', 'borrow_date', 'due_date']