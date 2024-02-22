from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ChatCommunicationApp.urls')),
    path('rooms/', include('ChatRoom.urls')),
    path('admin/', admin.site.urls),
]
