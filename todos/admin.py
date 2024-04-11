from django.contrib import admin
from todos.models import Board, BoardMembership, Card, CardAssignment, Item, List


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_at", "updated_at"]
    pass


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ["title", "board", "ord", "created_at", "updated_at"]
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["title", "list", "description", "ord", "created_at", "updated_at"]
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["title", "card", "done", "created_at", "updated_at"]
    pass


@admin.register(BoardMembership)
class BoardMembershipAdmin(admin.ModelAdmin):
    list_display = ["user", "board", "created_at", "updated_at"]
    pass


@admin.register(CardAssignment)
class CardAssignmentAdmin(admin.ModelAdmin):
    list_display = ["card", "user", "created_at", "updated_at"]
    pass
