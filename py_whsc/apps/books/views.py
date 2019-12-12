from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response

from apps.admins import WhAdminTokenAuthentication
from apps.books import models
from apps.books.serializers import *


class WhBookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = WhBook.objects.all()
    serializer_class = WhBookSerializer
    authentication_classes = (WhAdminTokenAuthentication,)

    # 新增书籍
    @list_route(methods=["POST"], serializer_class=WhBookSerializer)
    def add_book(self, request, *args, **kwargs):
        c_id = request.query_params.get("c_id")
        status = request.query_params.get("status")
        

        """
        此处获取用户选择的数据

        """
        new_book = WhBook(b_name='b_name')
        new_book.save()
        return Response('Save OK!')

    # 章节列表
    @list_route(methods=['POST'], serializer_class=WhCatalogSerializer)
    def chapter_view(self, *args, **kwargs):
        res = WhCatalog.objects.all()
        if res:
            return Response(res)
        else:
            return Response('数据有误！')

    # 新增章节
    @list_route(methods=['POST'])
    def add_catalog(self, *args, **kwargs):
        """
        此处获取用户上传的数据
        """
        new_catalog = WhCatalog('字段名=获取值...')
        new_catalog.save()
        return Response('Insert OK!')

    # 编辑（章节）
    def update_book(self, *args, **kwargs):
        """
        此处获取用户上传的数据
        """
        pass
        return Response('Update OK!')

    # 删除
    def delete_book(self, *args, **kwargs):
        """
        此处获取用户上传的数据
        """
        WhBook.objects.filter(username='新用户').delete()
        return Response('Delete OK!')
