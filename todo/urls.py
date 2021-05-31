from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


from todo.views import TodoViewSet

router = DefaultRouter()
router.register('todo', TodoViewSet, "todo")

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]