from rest_framework import routers
from users.viewsets import UsersViewSet


router = routers.SimpleRouter()
router.register(r'users', UsersViewSet, basename='users')


urlpatterns = [
    *router.urls,
    ]
