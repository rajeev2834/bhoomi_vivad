from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CreateUserApi,
    ManageUserApi,
    CreateTokenView,
    CircleApiList,
    CircleApiDetail,
    PanchayatApiList,
    PanchayatApiDetail,
    MauzaApiList,
    MauzaApiDetail,
    ThanaApiList,
    ThanaApiDetail,
    VivadDetailApiViewSet,
    HearingApiList,
    HearingApiDetail,
)

router = DefaultRouter()
router.register('vivad', VivadDetailApiViewSet)

urlpatterns = [
    path('create/',CreateUserApi.as_view(), name = 'api-create-user'),
    path('manage/',ManageUserApi.as_view(), name = 'api-manage-user'),
    path('token/',CreateTokenView.as_view(), name = 'api-token'),
    path('circle/', CircleApiList.as_view(), name = 'api-circle-list'),
    path('circle/<slug:pk>/', CircleApiDetail.as_view(), name = 'api-circle-detail'),
    path('panchayat/', PanchayatApiList.as_view(), name = 'api-panchayat-list'),
    path('panchayat/<slug:pk>', PanchayatApiDetail.as_view(), name = 'api-panchayat-detail'),
    path('mauza/',MauzaApiList.as_view(), name = 'api-mauza-list'),
    path('mauza/<slug:pk>/', MauzaApiDetail.as_view(), name = 'api-mauza-detail'),
    path('thana/', ThanaApiList.as_view(), name = 'api-thana-list'),
    path('thana/<slug:pk>/', ThanaApiDetail.as_view(), name = 'api-thana-detail'),
    path('hearing/', HearingApiList.as_view(), name = 'api-hearing-list'),
    path('hearing/<slug:slug>/', HearingApiDetail.as_view(), name='api-hearing-detail'),
]

urlpatterns = urlpatterns + router.urls