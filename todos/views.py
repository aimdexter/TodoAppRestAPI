from rest_framework import generics
from .models import Board, List, Card, Item, BoardMembership, CardAssignment
from .serializers import (
    BoardSerializer,
    ListSerializer,
    CardSerializer,
    ItemSerializer,
    BoardMembershipSerializer,
    CardAssignmentSerializer,
)


# Board Views
class BoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


board_list_create_view = BoardListCreateAPIView.as_view()


class BoardDetailAPIView(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


board_detail_view = BoardDetailAPIView.as_view()


class BoardUpdateAPIView(generics.UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    lookup_field = "id"


board_update_view = BoardUpdateAPIView.as_view()


class BoardDeleteAPIView(generics.DestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    lookup_field = "id"


board_delete_view = BoardDeleteAPIView.as_view()


# List Views
class ListListCreateAPIView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


list_list_create_view = ListListCreateAPIView.as_view()


class ListDetailAPIView(generics.RetrieveAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


list_detail_view = ListDetailAPIView.as_view()


class ListUpdateAPIView(generics.UpdateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = "id"


list_update_view = ListUpdateAPIView.as_view()


class ListDeleteAPIView(generics.DestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    lookup_field = "id"


list_delete_view = ListDeleteAPIView.as_view()


# Card Views
class CardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


card_list_create_view = CardListCreateAPIView.as_view()


class CardDetailAPIView(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


card_detail_view = CardDetailAPIView.as_view()


class CardUpdateAPIView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = "id"


card_update_view = CardUpdateAPIView.as_view()


class CardDeleteAPIView(generics.DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = "id"


card_delete_view = CardDeleteAPIView.as_view()


# Item Views
class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


item_list_create_view = ItemListCreateAPIView.as_view()


class ItemDetailAPIView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


item_detail_view = ItemDetailAPIView.as_view()


class ItemUpdateAPIView(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"


item_update_view = ItemUpdateAPIView.as_view()


class ItemDeleteAPIView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"


item_delete_view = ItemDeleteAPIView.as_view()


# BoardMembership Views
class BoardMembershipListCreateAPIView(generics.ListCreateAPIView):
    queryset = BoardMembership.objects.all()
    serializer_class = BoardMembershipSerializer


board_membership_list_create_view = BoardMembershipListCreateAPIView.as_view()


class BoardMembershipDetailAPIView(generics.RetrieveAPIView):
    queryset = BoardMembership.objects.all()
    serializer_class = BoardMembershipSerializer


board_membership_detail_view = BoardMembershipDetailAPIView.as_view()


class BoardMembershipUpdateAPIView(generics.UpdateAPIView):
    queryset = BoardMembership.objects.all()
    serializer_class = BoardMembershipSerializer
    lookup_field = "id"


board_membership_update_view = BoardMembershipUpdateAPIView.as_view()


class BoardMembershipDeleteAPIView(generics.DestroyAPIView):
    queryset = BoardMembership.objects.all()
    serializer_class = BoardMembershipSerializer
    lookup_field = "id"


board_membership_delete_view = BoardMembershipDeleteAPIView.as_view()


# CardAssignment Views
class CardAssignmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = CardAssignment.objects.all()
    serializer_class = CardAssignmentSerializer


card_assignment_list_create_view = CardAssignmentListCreateAPIView.as_view()


class CardAssignmentDetailAPIView(generics.RetrieveAPIView):
    queryset = CardAssignment.objects.all()
    serializer_class = CardAssignmentSerializer


card_assignment_detail_view = CardAssignmentDetailAPIView.as_view()


class CardAssignmentUpdateAPIView(generics.UpdateAPIView):
    queryset = CardAssignment.objects.all()
    serializer_class = CardAssignmentSerializer
    lookup_field = "id"


card_assignment_update_view = CardAssignmentUpdateAPIView.as_view()


class CardAssignmentDeleteAPIView(generics.DestroyAPIView):
    queryset = CardAssignment.objects.all()
    serializer_class = CardAssignmentSerializer
    lookup_field = "id"


card_assignment_delete_view = CardAssignmentDeleteAPIView.as_view()
