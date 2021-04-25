from rest_framework.views import APIView
from rest_framework.response import Response


class PlovoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'test': 'test'})