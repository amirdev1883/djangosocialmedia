from django.urls import path, include

urlpatterns = [
    path('blog/', include(('djangosocialmedia.blog.urls', 'blog'))),
    path('users/', include(('djangosocialmedia.users.urls', 'users'))),
]
