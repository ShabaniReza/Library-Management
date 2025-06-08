from django.contrib import admin, messages
from .models import Author, Genre, Member, BorrowRecord, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    #! list page
    list_display_links = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'biography']
    list_editable = ['date_of_birth', 'date_of_death']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith', 'date_of_birth', 'date_of_death']

    #! form page
    fieldsets = [
        ['Basic information', {
            'fields': ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'biography'],
            'description': 'اطلاعات نویسنده'
        }]
    ]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    #! list page
    list_display = ['name']
    list_per_page = 10
    search_fields = ['name__istartswith']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #! list page
    list_display = ['title', 'author', 'publisher', 'publication_year', 'total_copies', 'available_copies']
    list_filter = ['author', 'publication_year', 'genres']
    list_editable = ['publisher', 'publication_year', 'total_copies', 'available_copies']
    list_per_page = 10
    search_fields = ['title__istartswith', 'author__first_name__istartswith', 'author__last_name__istartswith', 'publisher__istartswith', 'publication_year']

    #! form page
    autocomplete_fields = ['author']
    filter_horizontal = ['genres']
    fieldsets =[
        ['Basic information', {
            'fields': ['title', 'author', 'publisher', 'publication_year'],
            'description': 'اطلاعات پایه درباره کتاب'
        }],
        ['Availability', {
            'fields': ['total_copies', 'available_copies'],
            'description': 'اطلاعات مربوط به موجودی کتاب در کتابخانه'
        }],
        ['Categorization', {
            'fields': ['genres'],
            'description': 'ژانرها و دسته‌بندی‌های کتاب'
        }],
    ]

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    #! list page
    list_display_links = ['__str__']
    list_display = ['user', '__str__','national_code', 'address', 'phone_number', 'email', 'date_joined']
    list_filter = ['date_joined']
    list_editable = ['phone_number', 'email']
    list_per_page = 10
    search_fields = ['user__username__istartswith', 'first_name__istartswith', 'last_name__istartswith', 'national_code__startswith', 'phone_number__startswith', 'email__istartswith']

    #! form page
    autocomplete_fields = ['user']
    readonly_fields = ['date_joined']
    fieldsets =[
        ['Basic information', {
            'fields': ['national_code', 'first_name', 'last_name', 'address'],
            'description': 'اطلاعات پایه درباره کاربر'
        }],
        ['Ways of communication', {
            'fields': ['phone_number', 'email'],
            'description': 'راه های ارتباطی'
        }],
        ['Date joined', {
            'fields': ['date_joined'],
            'description': 'تاریخ عضویت'
        }],
        ['User', {
            'fields': ['user'],
            'description': 'کاربر'
        }]
    ]

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    #! list page
    list_display_links = ['__str__']
    list_display = ['__str__', 'book', 'member', 'borrow_date', 'due_date']
    list_editable = ['due_date']
    list_filter = ['borrow_date', 'due_date']
    list_per_page = 10
    search_fields = ['book__title__istartswith', 'member__national_code__startswith']

    #! form page
    autocomplete_fields = ['book', 'member']
    exclude = ['return_date']
    readonly_fields = ['borrow_date']
    fieldsets =[
        ['Basic information', {
            'fields': ['book', 'member'],
            'description': 'اطلاعات پایه درباره امانت'
        }],
        ['Borrow date', {
            'fields': ['borrow_date'],
            'description': 'تاریخ امانت'
        }],
        ['Due date', {
            'fields': ['due_date'],
            'description': 'تاریخ بازگشت'
        }]
    ]

    #! actions
    actions = ['mark_as_returned_action']
    @admin.action(description='علامت زدن کتاب‌های انتخاب شده به عنوان بازگردانده شده')
    def mark_as_returned_action(self, request, queryset):
        updated_count = 0
        for record in queryset:
            record.mark_as_returned()
            record.delete()
            updated_count += 1
        
        if updated_count == 1:
            message = "۱ کتاب با موفقیت بازگردانده شد."
        else:
            message = f"{updated_count} کتاب با موفقیت بازگردانده شدند."
        self.message_user(request, message, messages.SUCCESS)
