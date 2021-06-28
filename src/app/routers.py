from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CreateUserApi,
    ManageUserApi,
    CreateTokenView,
    CircleApiList,
    CircleApiDetail,
    Logout,
    PanchayatApiList,
    PanchayatApiDetail,
    MauzaApiList,
    MauzaApiDetail,
    ThanaApiList,
    ThanaApiDetail,
    VivadDetailApiViewSet,
    HearingApiList,
    HearingApiDetail,
    PlotTypeApiList,
    PlotTypeApiDetails,
    PlotNatureApiList,
    PlotNatureApiDetails,
    PlotDetailApiViewSet,
)

router = DefaultRouter()
router.register('vivad', VivadDetailApiViewSet)
router.register('plot', PlotDetailApiViewSet)

urlpatterns = [
    path('create/',CreateUserApi.as_view(), name = 'api-create-user'),
    path('manage/',ManageUserApi.as_view(), name = 'api-manage-user'),
    path('token/',CreateTokenView.as_view(), name = 'api-token'),
    path('logout/', Logout.as_view(), name = 'api-logout'),
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
    path('plot-type/',PlotTypeApiList.as_view(), name ='api-plot_type-list'),
    path('plot-type/<slug:pk>/', PlotTypeApiDetails.as_view(), name='api-plot_type-detail'),
    path('plot-nature/',PlotNatureApiList.as_view(), name ='api-plot_nature-list'),
    path('plot-nature/<slug:pk>/', PlotNatureApiDetails.as_view(), name='api-plot_nature-detail'),

]

urlpatterns = urlpatterns + router.urls