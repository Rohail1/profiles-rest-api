from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api.serializers import HelloSerializer, UserProfileSerializer
from profiles_api.models import UserProfile
from profiles_api.permissions import UpdateOwnProfilePermission


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
        """Create a Hello Message with our Name"""
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


class HelloViewSet(ViewSet):
    """Test API View Set"""

    serializer_class = HelloSerializer

    def list(self, request):
        """Returns a list of APIView Features """
        an_apiview = [
            "Uses Actions as a function (list, create, retrieve, update, partial update"
            ", destory)",
            "Provides more functionality with less code",
            'Gives you the most control over your application logic',
            'Auto-mapped to URLs',
        ]
        return Response({'message': 'Helloo !!', 'data': an_apiview},
                        status=status.HTTP_200_OK)


    def create(self, request):
        """Create a Hello Message with our Name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'message': f'Helloo {name}!!'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handling Get to an object"""
        return Response({'method': "This is retrieve Request"},
                        status=status.HTTP_200_OK)


    def update(self, request, pk=None):
        """Handling Update to an object"""
        return Response({'method': "This is update Request"},
                        status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        """Handling partial update to an object"""
        return Response({'method': "This is partial_update Request"},
                        status=status.HTTP_200_OK)


    def destroy(self, request, pk=None):
        """Handling Delete to an object"""
        return Response({'method': "This is destory Request"},
                        status=status.HTTP_200_OK)


class UserProfileViewSet(ModelViewSet):
    """Handle creating and updating Profiles"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnProfilePermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'name',)


class UserLoginApiView(ObtainAuthToken):
    """Handle Creating User Authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
