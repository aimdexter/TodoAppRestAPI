from django.urls import path
from .views import (
    board_list_create_view,
    board_detail_view,
    board_update_view,
    board_delete_view,
    list_list_create_view,
    list_detail_view,
    list_update_view,
    list_delete_view,
    card_list_create_view,
    card_detail_view,
    card_update_view,
    card_delete_view,
    item_list_create_view,
    item_detail_view,
    item_update_view,
    item_delete_view,
    board_membership_list_create_view,
    board_membership_detail_view,
    board_membership_update_view,
    board_membership_delete_view,
    card_assignment_list_create_view,
    card_assignment_detail_view,
    card_assignment_update_view,
    card_assignment_delete_view,
)

urlpatterns = []

urlpatterns = [
    # Board URLs
    path("boards/", board_list_create_view, name="board-list-create"),
    path("boards/<int:id>/", board_detail_view, name="board-detail"),
    path("boards/<int:id>/update/", board_update_view, name="board-update"),
    path("boards/<int:id>/delete/", board_delete_view, name="board-delete"),
    # List URLs
    path("lists/", list_list_create_view, name="list-list-create"),
    path("lists/<int:id>/", list_detail_view, name="list-detail"),
    path("lists/<int:id>/update/", list_update_view, name="list-update"),
    path("lists/<int:id>/delete/", list_delete_view, name="list-delete"),
    # Card URLs
    path("cards/", card_list_create_view, name="card-list-create"),
    path("cards/<int:id>/", card_detail_view, name="card-detail"),
    path("cards/<int:id>/update/", card_update_view, name="card-update"),
    path("cards/<int:id>/delete/", card_delete_view, name="card-delete"),
    # Item URLs
    path("items/", item_list_create_view, name="item-list-create"),
    path("items/<int:id>/", item_detail_view, name="item-detail"),
    path("items/<int:id>/update/", item_update_view, name="item-update"),
    path("items/<int:id>/delete/", item_delete_view, name="item-delete"),
    # BoardMembership URLs
    path(
        "board-memberships/",
        board_membership_list_create_view,
        name="board-membership-list-create",
    ),
    path(
        "board-memberships/<int:id>/",
        board_membership_detail_view,
        name="board-membership-detail",
    ),
    path(
        "board-memberships/<int:id>/update/",
        board_membership_update_view,
        name="board-membership-update",
    ),
    path(
        "board-memberships/<int:id>/delete/",
        board_membership_delete_view,
        name="board-membership-delete",
    ),
    # CardAssignment URLs
    path(
        "card-assignments/",
        card_assignment_list_create_view,
        name="card-assignment-list-create",
    ),
    path(
        "card-assignments/<int:id>/",
        card_assignment_detail_view,
        name="card-assignment-detail",
    ),
    path(
        "card-assignments/<int:id>/update/",
        card_assignment_update_view,
        name="card-assignment-update",
    ),
    path(
        "card-assignments/<int:id>/delete/",
        card_assignment_delete_view,
        name="card-assignment-delete",
    ),
]
