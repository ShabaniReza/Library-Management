from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('authors', views.AuthorViewSet, basename='author')
router.register('genres', views.GenreViewSet)
router.register('books', views.BookViewSet)
router.register('members', views.MemberViewSet)

members_router = routers.NestedDefaultRouter(router, 'members', lookup='member')
members_router.register('extentions', views.ExtentionViewSet, basename='member-extentions')
members_router.register('images', views.MemberImageViewSet, basename='member-images')

urlpatterns = router.urls + members_router.urls