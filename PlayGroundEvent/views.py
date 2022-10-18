from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, mixins, status
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from PlayGroundEvent.models import Ticket, Company, Event, CustomUser
from PlayGroundEvent.serializators import EventSerializer, TicketSerializer, CompanySerializer, UserSerializer


def return_ticket(request, evid):
    ticket = Ticket.objects.get(pk=evid)
    return JsonResponse({
        'event': {"id": ticket.event_id},
        'price': ticket.price,
        'number': ticket.number,
    })

@csrf_exempt
@api_view(['GET', 'POST'])
def high_s(request):
    if request.method == 'GET':
        snippets = Event.objects.all()
        serializer = EventSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['DELETE'])
def del_met(request, pk: int):
    try:
        Event.objects.get(pk=pk).delete()
    except:
        print('Ивента не существует')
    return Response(status = 204)

@api_view(['GET'])
@permission_classes
def view_tickets(request):
    serializer = TicketSerializer(Ticket.objects.all(), many=True)
    return Response(serializer.data)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def ticket_view_set(request, pk: int):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "GET":
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    elif request.method == "POST":
        ticket.user = request.user
        # TODO придумать что-нибудь с балансом
        ticket.save()
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

@api_view(['GET'])
def healt_status(request):
    return Response({'status': 'OK'}, status=status.HTTP_200_OK)

class EventGet(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class TicketGet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CompanyGet(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]


class CustomUserSetView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination



class EventViewSet(viewsets.ModelViewSet):
    pass

