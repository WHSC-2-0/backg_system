from rest_framework import serializers
from apps.config.models import *


# 轮播图模型序列化
class WhBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhBanner
        fields = "__all__"


class WhBanPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhBanPlace
        fields = "__all__"
