from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from ..infra.messages import format_response
from .serializers import (
    LabelInputSerializer, 
    LabelOutputSerializer
)
from ..application.use_cases.create_label_use_case import CreateLabelUseCase
from ..application.use_cases.find_label_use_case import FindLabelUseCase

class LabelView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
        try:
            serializer = LabelInputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            use_case = CreateLabelUseCase()
            labels_created = use_case.execute(serializer.validated_data, request.user.use_id)
            output_serializer = LabelOutputSerializer(data=labels_created, many=True)
            output_serializer.is_valid()

            return Response(format_response(
                success=True,
                message="Success ! Labels created.",
                data=output_serializer.data
            ))
        
        except Exception as e:
            return Response(
                format_response(
                    success=False,
                    message="Exception in request !",
                    err=e
                )
            )
        
    def get(self, request: Request, id: str):
        try:
            user_id = request.user.use_id
            use_case = FindLabelUseCase()
            label_founded = use_case.execute(id, user_id)
            
            output_serializer = LabelOutputSerializer(data=label_founded, many=True)
            output_serializer.is_valid()

            return Response(format_response(
                success=True,
                data=output_serializer.data,
                message="Success ! Returned data."
            ))
        
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error exception in get data",
                err=e
            ))