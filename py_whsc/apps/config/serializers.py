from rest_framework import serializers

from apps.config.models import *


class WhBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhBanner
        fields = "__all__"


class WhBanPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhBanPlace
        fields = "__all__"
