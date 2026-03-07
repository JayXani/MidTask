from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .serializer import (
    StatusInputSerializer,
    StatusOutputSerializer,
    StatusListInputSerializer
)
from ..application.use_case.create_status_use_case import CreateStatusUseCase
from ..application.use_case.findall_status_use_case import FindAllStatusUseCase
from ..application.use_case.delete_status_use_case import DeleteStatusUseCase
from setup.utils.messages.format_response import format_response


class StatusView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
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

        
    def delete(self, request: Request):
        input_serializer = StatusListInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        use_case = DeleteStatusUseCase()
        status_deleted = use_case.execute(input_serializer.validated_data, request.user.use_id)

        if(status_deleted == 0): return Response(format_response(
            success=True,
            message="Success ! Cannot be founded the status because not exists.",
            data=[]
        ))
        
        return Response(format_response(
            success=True,
            message="Success ! Status deleted.",
            data=[]
        ))

        
class StatusListView(APIView):
    permission_classes=[IsAuthenticated]

    
    def post(self, request: Request):
        serializer = StatusListInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = FindAllStatusUseCase()
        status_founded = use_case.execute(serializer.validated_data, request.user.use_id)

        output_serializer = StatusOutputSerializer(instance=status_founded, many=True)

        return Response(format_response(
            success=True,
            message="Success ! Data returned.",
            data= output_serializer.data
        ))
    
