from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('authors', views.AuthorViewSet, basename='author')
router.register('genres', views.GenreViewSet)
router.register('books', views.BookViewSet)
router.register('members', views.MemberViewSet)

extention_router = routers.NestedDefaultRouter(router, 'members', lookup='member')
extention_router.register('extentions', views.ExtentionViewSet, basename='member-extentions')
extention_router.register('images', views.MemberImageViewSet, basename='member-images')

urlpatterns = router.urls + extention_router.urls