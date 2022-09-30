from django.shortcuts import render
from django.http import JsonResponse

from PlayGroundEvent.models import Ticket


def return_ticket(request, evid):
    ticket = Ticket.objects.get(pk=evid)
    return JsonResponse({
        'event': {"id": ticket.event_id},
        'price': ticket.price,
        'number': ticket.number,
    })