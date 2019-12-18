from rest_framework import serializers
<<<<<<< HEAD

from apps.config.models import *


=======
from apps.config.models import *


# 轮播图模型序列化
>>>>>>> 5add4948dc349778cc15d3f8544390916c0fe4a5
class WhBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhBanner
        fields = "__all__"
<<<<<<< HEAD


class WhBanPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhBanPlace
        fields = "__all__"
=======
>>>>>>> 5add4948dc349778cc15d3f8544390916c0fe4a5
