from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('users', views.UserProfileViewSet)

urlpatterns = [
	url(r'', include(router.urls))
]