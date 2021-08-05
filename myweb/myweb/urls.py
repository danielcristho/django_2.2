from django.contrib import admin
from django.urls import path

from . import views
from blog import views as viewsBlog
from about import views as viewsAbout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', viewsBlog.index),
    path('about/',viewsAbout.index),
]
