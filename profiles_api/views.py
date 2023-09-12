from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView Features """
        an_apiview = [
            "Uses HTTP Methods as a function (get, post, patch, put, delete)",
            "Is similar to a traditional django view",
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Helloo !!', 'data': an_apiview},
                        status=status.HTTP_200_OK)
