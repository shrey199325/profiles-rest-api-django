from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializer, models


class HelloAPIView(APIView):
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """
        HTTP get response method which
        returns a list of api view features.
        :param request: GET Request Data
        :param format: End points of URL
        :return: Response class object
        """
        res = ["Use HTTP methods (get put patch post delete)",
               "Similar to trasditional django view",
               "Gives control over app logic",
               "Mapped manually to URLs"]
        return Response({"message": "Hello",
                         "an_apiview": res})

    def post(self, request):
        """
        Create a hello msg with the name in request
        :param request: Request object to get the name
        :return: Response object
        """
        srlz = self.serializer_class(data=request.data)
        if srlz.is_valid():
            name = srlz.validated_data.get("name")
            msg = "Hello {}".format(name)
            return Response({"message": msg})
        else:
            return Response(srlz.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, req, pk=None):
        return Response({"method": "PUT"})

    def patch(self, req, pk=None):
        return Response({"method": "PATCH"})

    def delete(self, req, pk=None):
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """
    Test API viewset
    """
    serializer_class = serializer.HelloSerializer

    def list(self, req):
        """
        Return hello msg
        """
        msg = ["Use actions (list create retrieve update partial-update)",
               "More fns less code",
               "Mapped automatically to URLs using Routers"]
        return Response({"message": "Hello",
                         "a_viewset": msg})

    def create(self, req, pk=None):
        """Create new hello msg"""
        srlz = self.serializer_class(data=req.data)
        if srlz.is_valid():
            name = srlz.validated_data.get("name")
            msg = "Hello {}".format(name)
            return Response({"message": msg})
        else:
            return Response(srlz.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, req, pk=None):
        return Response({"method": "GET"})

    def update(self, req, pk=None):
        return Response({"method": "PUT"})

    def partial_update(self, req, pk=None):
        return Response({"method": "PATCH"})

    def destroy(self, req, pk=None):
        return Response({"method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
