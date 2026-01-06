from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from ..infra.messages import format_response
from .serializer import TaskInputSerializer

class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        try:
            serializer = TaskInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response({})
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to create a task",
                err=e
            ))