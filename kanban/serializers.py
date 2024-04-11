from rest_framework import serializers
from .models import Board, List, Card, Item, BoardMembership, CardAssignment


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class BoardMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMembership
        fields = "__all__"


class CardAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardAssignment
        fields = "__all__"
