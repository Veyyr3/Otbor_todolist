# main url
from django.contrib import admin
from django.urls import include, path


# views
from APPS.todo.views import TaskViewSet


# REST
from rest_framework import routers


# router
router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename='task'
) # чтобы было api/v1/task


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
