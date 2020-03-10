"""tistory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import posts_list, post_detail, post_write, comment_write, post_like

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls',)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('post/', posts_list),
    path('post/<int:post_id>', post_detail, name="post_detail"),
    path('post/write', post_write, name='post_write'),
    path('comment/write', comment_write, name='comment_write'),
    path('post_like/', post_like, name='post_like'),
]

# 어떤 URL을 정적으로 추가할래? > MEDIA_URL을 static 파일 경로로 추가
# 실제 파일은 어디에 있는데? > MEDIA_ROOT 경로내의 파일을 static 파일로 설정

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)