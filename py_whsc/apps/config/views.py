import os

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.config.models import *
from apps.config.serializers import WhBannerSerializer, WhBanPlaceSerializer


class WhBannerViewSet(ModelViewSet):
    queryset = WhBanner.objects.all()
    serializer_class = WhBannerSerializer
    # authentication_classes = (WhTokenAuthentication,)

    # 新增广告
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # 删除
    @list_route(methods=['POST'])
    def delete_adv(self, request, *args, **kwargs):
        adv_id = request.POST.get('id')
        result = WhBanner.objects.filter(id=adv_id).delete()
        if result:
            return Response('delete OK!')
        else:
            return Response('delete Failed!')

    # 首页展示
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:

            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # 编辑
    @list_route(methods=['POST'])
    def update_adv(self, request, *args, **kwargs):
        adv_id = request.POST.get('id')
        adv_name = request.POST.get('name')
        adv_place = request.POST.get('place')
        adv_img = request.POST.get('img')
        adv_url = request.POST.get('url')
        if adv_place:
            wh_banner = WhBanner.objects.filter(id=adv_id).update(place=adv_place)
            if wh_banner:
                return Response('编辑成功！')
            else:
                return Response('编辑失败！')
        elif adv_name:
            wh_banner = WhBanner.objects.filter(id=adv_id).update(name=adv_name)
            if wh_banner:
                return Response('编辑成功！')
            else:
                return Response('编辑失败！')
        elif adv_img:
            wh_banner = WhBanner.objects.filter(id=adv_id).update(img=adv_img)
            if wh_banner:
                return Response('编辑成功！')
            else:
                return Response('编辑失败！')
        elif adv_url:
            wh_banner = WhBanner.objects.filter(id=adv_id).update(jump_url=adv_url)
            if wh_banner:
                return Response('编辑成功！')
            else:
                return Response('编辑失败！')
        else:
            return Response('请上传正确数据！')

    # 按分类搜索
    @list_route(methods=['POST'])
    def search_adv(self, request, *args, **kwargs):
        p_id = request.POST.get('place_id')
        if p_id:
            result = WhBanner.objects.filter(place_id=p_id)
            """
            serializer = self.get_serializer(result)
            只适用于单条记录的匹配，
            如果匹配的结果是结果集，是多条记录，则需要加上 many=True
            serializer = self.get_serializer(result, many=True)
            """
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)
        else:
            return Response('请上传正确的数据！')

    # 按名称搜索
    @list_route(methods=['POST'])
    def search_name(self, request):
        adv_name = request.POST.get('name')
        if adv_name:
            result = WhBanner.objects.filter(name=adv_name)
            serializer = self.get_serializer(result, many=True)
            return Response(serializer.data)
        else:
            return Response('请上传正确的数据！')

    # 重写get_serializer方法
    def get_serializer_adv(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = WhBanPlaceSerializer
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    # 广告位置
    @list_route(methods=['POST', 'GET'])
    def adv_place(self, request, *args, **kwargs):
        result = WhBanPlace.objects.all()
        serializer = self.get_serializer_adv(result, many=True)
        if result:
            return Response(serializer.data)
        else:
            return Response('数据有误！')

    # 新增广告位
    @list_route(methods=['POST'])
    def add_place(self, request):
        new_name = request.POST.get('name', None)
        new_wight = request.POST.get('wight', None)
        new_height = request.POST.get('height', None)
        new_desc = request.POST.get('desc', None)
        new_status = request.POST.get('status', None)
        result = WhBanPlace.objects.create(name=new_name, wight=new_wight,
                                           height=new_height, desc=new_desc,
                                           status=new_status)
        if result:
            return Response('添加成功！')
        else:
            return Response('添加失败！')

    # 查看广告
    @list_route(methods=['POST'])
    def adv_info(self, request):
        adv_name = request.POST.get('name')
        if adv_name:
            result = WhBanPlace.objects.filter(name=adv_name)
            serializer = self.get_serializer(result, many=True)
            if serializer:
                return Response(serializer.data)
            else:
                return Response('查询失败！')
        else:
            return Response('请上传正确的数据！')

    # 编辑广告位置
    @list_route(methods=['POST'])
    def adv_update(self, request):
        adv_id = request.POST.get('id')
        adv_wight = request.POST.get('wight')
        adv_name = request.POST.get('name')
        adv_height = request.POST.get('height')
        adv_desc = request.POST.get('desc')
        adv_status = request.POST.get('status')
        if adv_wight:
            result = WhBanPlace.objects.filter(id=adv_id).update(wight=adv_wight)
            if result:
                return Response('编辑成功！')
            else:
                return Response('编辑失败！')
        elif adv_name:
            result = WhBanPlace.objects.filter(id=adv_id).update(name=adv_name)
            if result:
                return Response('编辑成功！')
            else:
                return Response('编辑失败！')
        elif adv_height:
            result = WhBanPlace.objects.filter(id=adv_id).update(height=adv_height)
            if result:
                return Response('编辑成功！')
            else:
                return Response('编辑失败！')
        elif adv_desc:
            result = WhBanPlace.objects.filter(id=adv_id).update(desc=adv_desc)
            if result:
                return Response('编辑成功！')
            else:
                return Response('编辑失败！')
        elif adv_status:
            result = WhBanPlace.objects.filter(id=adv_status).update(status=adv_status)
            if result:
                return Response('编辑成功！')
            else:
                return Response('编辑失败！')
        else:
            return Response('请上传正确数据！')

    # 删除广告位
    @list_route(methods=['POST'])
    def adv_del(self, request):
        adv_id = request.POST.get('id')
        result = WhBanPlace.objects.filter(id=adv_id).delete()
        if result:
            return Response('delete OK!')
        else:
            return Response('delete Failed!')
