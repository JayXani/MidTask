from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request 
from rest_framework.response import Response
from ..infra.messages import format_response
from .serializer import (LinksInputSerializer, LinksOutputSerializer, LinksInputUpdateSerializer)
from ..application.use_cases.create_link_use_case import CreateLinksUseCase
from ..application.use_cases.update_link_use_case import UpdateLinksUseCase
# Create your views here.
class LinksView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        try:
            input_serializer = LinksInputSerializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)

            use_case = CreateLinksUseCase()
            link_created = use_case.execute(
                input_serializer.validated_data,
                request.user.use_id
            )

            output_serializer = LinksOutputSerializer(instance=link_created)

            return Response(format_response(
                success=True,
                message="Success ! Link inserted",
                data=output_serializer.data
            ))

        except Exception as e:
            return Response(format_response(
                success=False,
                message="A error was founded in create links",
                err=e
            ))
    
    def patch(self, request: Request, id: str):
        try: 
            serializer = LinksInputUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            use_case = UpdateLinksUseCase()
            link_updated = use_case.execute(id, serializer.validated_data, request.user.use_id)
            output_serializer = LinksOutputSerializer(instance=link_updated)

            return Response(format_response(
                success=True,
                message="Success ! Data returned.",
                data=output_serializer.data
            ))
        except Exception as e:
            return Response(format_response(
                success=False,
                message="Error to update user",
                err=e
            ))