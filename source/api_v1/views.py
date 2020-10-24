from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import action
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from api_v1.permissions import GETModelPermissions
from api_v1.serializers import PhotoSerializer, UserSerializer
from webapp.models import Photo


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class PhotoViewSet(ViewSet):
    queryset = Photo.objects.all()
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_permissions(self):
        print(self.action)
        print(self.request.method)
        if self.action in ['list', 'retrieve']:  # self.request.method == "GET"
            return [GETModelPermissions()]
        else:
            return [AllowAny()]

    def list(self, request):
        objects = Photo.objects.all()
        slr = PhotoSerializer(objects, many=True, context={'request': request})
        return Response(slr.data)

    def create(self, request):
        slr = PhotoSerializer(data=request.data, context={'request': request})
        if slr.is_valid():
            photo = slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def retrieve(self, request, pk=None):
        photo = get_object_or_404(Photo, pk=pk)
        slr = PhotoSerializer(photo, context={'request': request})
        return Response(slr.data)

    def update(self, request, pk=None):
        photo = get_object_or_404(Photo, pk=pk)
        slr = PhotoSerializer(data=request.data, instance=photo, context={'request': request})
        if slr.is_valid():
            photo = slr.save()
            return Response(slr.data)
        else:
            return Response(slr.errors, status=400)

    def destroy(self, request, pk=None):
        photo = get_object_or_404(Photo, pk=pk)
        photo.delete()
        return Response({'pk': pk})


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
