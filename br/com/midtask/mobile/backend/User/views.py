from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import HttpRequest

class UserViewer(APIView):
    def post(self, request):
        return Response({
            "success": True,
            "message": "Hello world !"
        })
    
  