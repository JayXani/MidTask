from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from setup.utils.messages.format_response import format_response
from .serializers import (
    LabelInputSerializer, 
    LabelOutputSerializer,
    LabelFilterInputSerializer
)
from ..application.use_cases.create_label_use_case import CreateLabelUseCase
from ..application.use_cases.find_label_use_case import FindLabelUseCase
from ..application.use_cases.find_all_use_case import FindAllLabelsUseCase 
from ..application.use_cases.delete_label_use_case import DeleteLabelUseCase 

class LabelView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request: Request):
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
        

    def get(self, request: Request, id: str):
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

    def delete(self, request: Request):
        serializer = LabelInputSerializer(data=request.data)
        serializer.is_valid()

        use_case = DeleteLabelUseCase()
        labels_deleted = use_case.execute(serializer.validated_data, request.user.use_id)
        if(labels_deleted >= 1): 
            return Response(
            format_response(
                success=True,
                message="Labels deleted !"
            ))
        return Response(
            format_response(
                success=True,
                message="Labels not exists !"
            )) 
  
        

class LabelListView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request: Request):
        serializer = LabelFilterInputSerializer(data=request.data)
        serializer.is_valid()
        
        use_case = FindAllLabelsUseCase();
        labels_founded = use_case.execute(serializer.validated_data.get("labels", {}), request.user.use_id)
        
        output_serializer = LabelOutputSerializer(data=labels_founded, many=True)
        output_serializer.is_valid()
        
        return Response(format_response(
            success=True,
            message="Success ! Data returned",
            data=output_serializer.data
        ))
