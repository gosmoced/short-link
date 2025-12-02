from django.contrib import admin
from django.urls import path, include
from shortlink.views import CreateLink, GetLink, DeleteLink
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/create/', CreateLink.as_view()),
    path('api/get-link/', GetLink.as_view()),
    path('api/delete-link/<int:pk>/', DeleteLink.as_view()),
]
