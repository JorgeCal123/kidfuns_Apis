"""projectkind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from registro.viewsAPI import view_user, view_kid, view_level, view_progres, view_profe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', view_user.Registro_UserApiView.as_view(), name='user'),
    path('user/<id>', view_user.Registro_UserDetailApiView.as_view(), name='userDetail'),
    path('kid/', view_kid.Registro_KidApiView.as_view(), name='kid'),
    path('kid/<id>',view_kid.Registro_KidDetailApiView.as_view(), name='kidDetail'),
    path('level/', view_level.Registro_LevelApiView.as_view(), name='level'),
    path('level/<id>',view_level.Registro_LevelDetailApiView.as_view(), name='levelDetail'),
    path('progres/profe', view_profe.KidProgress.as_view({'get': 'list'}), name='profe'),
    path('progres/', view_progres.Registro_ProgressApiView.as_view(), name='progres'),
    path('progres/<id>',view_progres.Registro_ProgressDetailApiView.as_view(), name='progresDetail'),
]