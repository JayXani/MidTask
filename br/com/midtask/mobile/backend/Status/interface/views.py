from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .serializer import (
    StatusInputSerializer,
    StatusOutputSerializer
)
from ..application.use_case.create_status_use_case import CreateStatusUseCase
from ..infra.messages import format_response


class StatusView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
        try:
            serializer = StatusInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            use_case = CreateStatusUseCase()
            status_created = use_case.execute(serializer.validated_data, request.user.use_id)
    
            serializer_output = StatusOutputSerializer(instance=status_created, many=True)

            return Response(format_response(
                success=True,
                message="Success ! Status created",
                data=serializer_output.data
            ))
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error status not created",
                err=e
            ))