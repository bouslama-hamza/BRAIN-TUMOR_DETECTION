from rest_framework.views import APIView, Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ModelAPIView(APIView):
    
    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        print(request)
        return Response(200)