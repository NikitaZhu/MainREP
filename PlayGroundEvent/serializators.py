from PlayGroundEvent.models import Event, Ticket, Company, CustomUser
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'date', 'title']
        read_only_fields = ['id', ]

    def create(self, validated_data):
        validated_data["ticket_count"] = validated_data.get("ticket_count", 20)
        return super().create(validated_data)


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['event', 'price', 'number']


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['title']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"