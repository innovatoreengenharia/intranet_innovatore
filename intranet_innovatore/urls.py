"""
URL configuration for intranet_innovatore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(
        "admin/login/",
        auth_views.LoginView.as_view(template_name="login_admin.html"),
        name="login_admin",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("dashboard.urls")),
    path("admin/", admin.site.urls, name="admin"),
    path("documentos/", include("documentos.urls")),
    path("usuario/", include("usuario.urls")),
    path("institucional/", include("institucional.urls")),
    path("tarefas/", include("tarefas.urls")),
    path("cursos/", include("cursos.urls")),
    path("cartao_visitas/", include("cartao_visitas.urls")),
    path("aniversariantes/", include("aniversariantes.urls")),
    path("social/", include("social.urls")),
    path("calendario/", include("calendario.urls")),
    path("informativos/", include("informativos.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
