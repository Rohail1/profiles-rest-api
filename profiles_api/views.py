from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api.serializers import HelloSerializer


class HelloApiView(APIView):
    """ Test API View"""

    serializer_class = HelloSerializer

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


    def post(self, request):
        """Create a Hello Message with out Name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': f'Helloo {name}!!'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Handling Update to an object"""
        return Response({'method': "This is Put Request"},
                        status=status.HTTP_200_OK)

    def patch(self, request, pk=None):
        """Handling partial update to an object"""
        return Response({'method': "This is PATCH Request"},
                        status=status.HTTP_200_OK)


    def delete(self, request, pk=None):
        """Handling Delete to an object"""
        return Response({'method': "This is Delete Request"},
                        status=status.HTTP_200_OK)
