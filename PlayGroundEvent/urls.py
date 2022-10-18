
from django.urls import path, include

from PlayGroundEvent.views import return_ticket, high_s

urlpatterns = [
    path('return_ticket/<int:evid>/', return_ticket),

]

