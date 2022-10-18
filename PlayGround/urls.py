"""PlayGround URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

from PlayGroundEvent.views import return_ticket, high_s, del_met, view_tickets, ticket_view_set, EventGet, TicketGet, \
    CompanyGet, healt_status, CustomUserSetView

router = DefaultRouter()
router.register(r'users', CustomUserSetView)

urlpatterns = [

    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('base/', include('PlayGroundEvent.urls')),
    path('Seri/', high_s),
    path('del/<int:pk>', del_met),
    path('more/', view_tickets),
    path('one/<int:pk>', ticket_view_set),
    path('event/<int:pk>', EventGet.as_view()),
    path('ticket/<int:pk>', TicketGet.as_view()),
    path('company/<int:pk>', CompanyGet.as_view()),
    path('api-ping/', healt_status)

]
