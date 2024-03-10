from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer


class TodoListCreateAPIView(generics.ListCreateAPIView):
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
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


todo_detail_view = TodoDetailAPIView.as_view()

# Same loogic using function based views
# @api_view(["GET", "POST"])
# def todo_alt_view(request, pk=None, *args, **kwards):
#     method = request.method
#     if method == "GET":
#         if pk is not None:
#             obj = get_object_or_404(Todo, pk=pk)
#             data = TodoSerializer(obj, many=False).data
#             return Response(data)
#         # list view
#         qs = Todo.objects.all()
#         data = TodoSerializer(qs, many=True).data
#         return Response(data)
#     if method == "POST":
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get("title")
#             content = serializer.validated_data.get("content") or None
#             if content is None:
#                 content = title
#         serializer.save(content=content)
#         return Response(serializer.data)
#     return Response({"invalid": "Bad data"}, status=400)
