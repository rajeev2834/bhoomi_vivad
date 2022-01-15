from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, authentication, permissions, status, viewsets

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from django.contrib.auth import get_user_model
from django.http import JsonResponse

from .models import (
    Circle,
    Panchayat,
    Mauza,
    Thana,
    Vivad,
    Hearing,
    PlotType,
    PlotNature,
    PlotDetail,
)

from .serializers import (
    UserSerializer,
    AuthTokenSerializer,
    CircleSerializer,
    PanchayatSerializer,
    MauzaSerializer,
    ThanaSerializer,
    VivadSerializer,
    VivadWithDetailSerializer,
    HearingSerilaizer,
    PlotNatureSerializer,
    PlotTypeSerializer,
    PlotDetailSerializer,
    PlotWithDetailSerializer,
    PlotImageSerializer,
)

import logging

class BaseApiListView(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


    def get_queryset(self):
        queryset = self.queryset
        if queryset.model is Mauza:
            circle = self.request.query_params.get('circle')
            panchayat = self.request.query_params.get('panchayat')

            if circle:
                circle_ids = [str_id for str_id in circle.split(',')]
                queryset = queryset.filter(circle__circle_id__in=circle_ids)

            if panchayat:
                panchayat_ids = [str_id for str_id in panchayat.split(',')]
                queryset = queryset.filter(panchayat__panchayat_id__in=panchayat_ids)

        if queryset.model in (Panchayat, Thana):
            circle = self.request.query_params.get('circle')

            if circle:
                circle_ids = [str_id for str_id in circle.split(',')]
                queryset = queryset.filter(circle__circle_id__in=circle_ids)

        is_super = self.request.user.is_superuser
        if is_super:
            return queryset.all()

        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class BaseApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        is_super = self.request.user.is_superuser
        if is_super:
            return self.queryset.all()

        return self.queryset.filter(user=self.request.user).distinct()

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)

class CreateUserApi(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class ManageUserApi(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class CircleApiDetail(BaseApiDetailView):

    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

class CircleApiList(BaseApiListView):

    queryset = Circle.objects.all()
    serializer_class = CircleSerializer

class PanchayatApiList(BaseApiListView):
    queryset = Panchayat.objects.all()
    serializer_class = PanchayatSerializer

class PanchayatApiDetail(BaseApiDetailView):
    queryset = Panchayat.objects.all()
    serializer_class = PanchayatSerializer

class MauzaApiList(BaseApiListView):

    queryset = Mauza.objects.all()
    serializer_class = MauzaSerializer

class MauzaApiDetail(BaseApiDetailView):
    queryset = Mauza.objects.all()
    serializer_class = MauzaSerializer

class ThanaApiList(BaseApiListView):

    queryset = Thana.objects.all()
    serializer_class = ThanaSerializer

class ThanaApiDetail(BaseApiDetailView):

    queryset = Thana.objects.all()
    serializer_class = ThanaSerializer

class PlotTypeApiList(generics.ListCreateAPIView):

    queryset = PlotType.objects.all()
    serializer_class = PlotTypeSerializer

class PlotTypeApiDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = PlotType.objects.all()
    serializer_class = PlotTypeSerializer

class PlotNatureApiList(generics.ListCreateAPIView):

    queryset = PlotNature.objects.all()
    serializer_class = PlotNatureSerializer

class PlotNatureApiDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = PlotNature.objects.all()
    serializer_class = PlotNatureSerializer

class PlotDetailApiViewSet(viewsets.ModelViewSet):

    queryset = PlotDetail.objects.all()
    serializer_class = PlotDetailSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PlotWithDetailSerializer
        elif self.action == 'upload_image':
            return PlotImageSerializer

        return self.serializer_class


    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        plot = self.get_object()
        serializer = self.get_serializer(
            plot,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def _params_to_ints(self, qs):

        return [int(str_id) for str_id in qs.split(',')]


    def get_queryset(self):
        circle = self.request.query_params.get('circle')
        panchayat = self.request.query_params.get('panchayat')
        mauza = self.request.query_params.get('mauza')
        vivad = self.request.query_params.get('vivad')
        queryset = self.queryset

        if circle:
            circle_ids = [str_id for str_id in circle.split(',')]
            queryset = queryset.filter(circle__circle_id__in=circle_ids)

        if panchayat:
            panchayat_ids = [str_id for str_id in panchayat.split(',')]
            queryset = queryset.filter(panchayat_id__panchayat_id__in=panchayat_ids)

        if mauza:
            mauza_ids = self._params_to_ints(mauza)
            queryset = queryset.filter(mauza__mauza_id__in=mauza_ids)
        
        if vivad:
            vivad_ids = [str_id for str_id in vivad.split(',')]
            queryset = queryset.filter(vivad__vivad_id__in=vivad_ids)

        return queryset.filter().order_by('plot_id')

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)


class VivadDetailApiViewSet(viewsets.ModelViewSet):

    queryset = Vivad.objects.all()
    serializer_class = VivadSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VivadWithDetailSerializer

        return self.serializer_class

    def _params_to_ints(self, qs):

        return [int(str_id) for str_id in qs.split(',')]


    def get_queryset(self):
        circle = self.request.query_params.get('circle')
        panchayat = self.request.query_params.get('panchayat')
        mauza = self.request.query_params.get('mauza')
        queryset = self.queryset

        if circle:
            circle_ids = [str_id for str_id in circle.split(',')]
            queryset = queryset.filter(circle__circle_id__in=circle_ids)

        if panchayat:
            panchayat_ids = [str_id for str_id in panchayat.split(',')]
            queryset = queryset.filter(panchayat__panchayat_id__in=panchayat_ids)

        if mauza:
            mauza_ids = self._params_to_ints(mauza)
            queryset = queryset.filter(mauza__mauza_id__in=mauza_ids)


        return queryset.filter(user=self.request.user).order_by('vivad_id')

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class HearingApiList(generics.ListCreateAPIView):
    queryset = Hearing.objects.all()
    serializer_class = HearingSerilaizer

    def get_queryset(self):
        queryset = self.queryset
        vivad = self.request.query_params.get('vivad')

        if vivad:
            vivad_ids = [str_id for str_id in vivad.split(',')]
            queryset = queryset.filter(vivad__vivad_uuid__in=vivad_ids)

        return queryset.all()

class HearingApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hearing.objects.all()
    serializer_class = HearingSerilaizer