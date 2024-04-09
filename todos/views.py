from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
    """
    - Fore GET request, this methode will return the list of todos
    - Fore POST request, this methode accepts title, content and completed as params
     an will return the list of todos
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serialiser):
        # serialiser.save(user=self.request.user)
        print(serialiser.validated_data)
        title = serialiser.validated_data.get("title")
        content = serialiser.validated_data.get("content") or None
        if content is None:
            content = title
        serialiser.save(content=content)


todo_list_create_detail_view = TodoListCreateAPIView.as_view()


class TodoDetailAPIView(generics.RetrieveAPIView):
    """
    Get the details of a single todo based on the id
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


todo_detail_view = TodoDetailAPIView.as_view()


class TodoUpdateAPIView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


todo_update_view = TodoUpdateAPIView.as_view()


class TodoDeleteAPIView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"


todo_delete_view = TodoDeleteAPIView.as_view()
