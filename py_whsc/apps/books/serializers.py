from rest_framework import serializers

from apps.books.models import *


class WhTypeOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhTypeOne
        fields = "__all__"


class WhTypeChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhTypeChild
        fields = "__all__"


class WhBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhBook
        fields = "__all__"


class WhCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhCatalog
        fields = "__all__"


class WhNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhNotice
        fields = "__all__"


class WhReadlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhReadlog
        fields = "__all__"

