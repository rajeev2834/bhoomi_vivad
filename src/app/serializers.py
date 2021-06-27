from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    Serializer,
    ValidationError,
    CharField,
)
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

from .models import (
    Circle,
    Panchayat,
    Mauza,
    Thana,
    Vivad,
    Hearing,
    PlotType,
    PlotNature,
)

class UserSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username','password','first_name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self,validated_data):
         return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password',None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        
        return user

class AuthTokenSerializer(Serializer):
    username = CharField()
    password = CharField(
        style={'input_type': 'password'},
        trim_whitespace= False
    )

    def validate(self,attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username = username.upper(),
            password = password,
        )

        if not user:
            msg = ('username or password is not correct.')
            raise ValidationError(msg, code='authentication')

        attrs['user'] = user

        if not attrs:
            attrs = Token.objects.create(user=user)
            
        return attrs

class CircleSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(
        view_name = "api-circle-detail",
    )

    class Meta:
        model = Circle
        fields = ('circle_id','circle_name_hn','url')
        read_only_fields = ('circle_id',)

class PanchayatSerializer(ModelSerializer):

    circle = serializers.PrimaryKeyRelatedField(
        queryset = Circle.objects.all()
    )

    url = HyperlinkedIdentityField(
        view_name = "api-panchayat-detail"
    )

    class Meta:
        model = Panchayat
        fields = ("__all__")
        read_only = ('panchayat_id',)

class MauzaSerializer(ModelSerializer):

    circle = serializers.PrimaryKeyRelatedField(
        queryset = Circle.objects.all()
    )

    panchayat = serializers.PrimaryKeyRelatedField(
        queryset = Panchayat.objects.all()
    )

    url = HyperlinkedIdentityField(
        view_name = "api-mauza-detail"
    )

    class Meta:
        model = Mauza
        fields = ('circle','panchayat','mauza_name_hn','url',)
        read_only = ('mauza_id',)


class ThanaSerializer(ModelSerializer):

    circle = serializers.PrimaryKeyRelatedField(
        queryset = Circle.objects.all()
    )

    url = HyperlinkedIdentityField(
        view_name = "api-thana-detail"
    )

    class Meta:
        model = Thana
        fields = ('circle','thana_name_hn','url',)
        read_only = ('thana_id',)

class PlotTypeSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(
        view_name = "api-plot_type-detail"
    )

    class Meta:
        model = PlotType
        fields = ('id', 'plot_type', 'url',)
        read_only = ('id',)

class PlotNatureSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(
        view_name = "api-plot_nature-detail"
    )

    class Meta:
        model = PlotNature
        fields = ('id', 'plot_nature', 'url',)
        read_only = ('id',)


class VivadSerializer(ModelSerializer):

    circle = serializers.PrimaryKeyRelatedField(
        queryset = Circle.objects.all()
    )

    panchayat = serializers.PrimaryKeyRelatedField(
        queryset = Panchayat.objects.all()
    )

    mauza = serializers.PrimaryKeyRelatedField(
        queryset = Mauza.objects.all()
    )

    url = HyperlinkedIdentityField(
        view_name = "api-vivad-detail"
    )

    class Meta:
        model = Vivad
        fields = ("__all__")
        read_only = ('vivad_id',)

class VivadWithDetailSerializer(VivadSerializer):
    circle = CircleSerializer(read_only = True)
    panchayat = PanchayatSerializer(read_only = True)
    mauza =  MauzaSerializer(read_only = True)


class HearingSerilaizer(ModelSerializer):
    vivad = serializers.PrimaryKeyRelatedField(
        queryset = Vivad.objects.all()
    )

    url = HyperlinkedIdentityField(
        view_name = "api-hearing-detail"
    )

    class Meta:
        model = Hearing
        fields = ("__all__")