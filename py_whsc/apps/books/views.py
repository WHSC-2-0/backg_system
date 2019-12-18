from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response

from apps.admins.WhAdminTokenAuthentication import WhTokenAuthentication
<<<<<<< HEAD
from apps.books import models
=======
>>>>>>> 5add4948dc349778cc15d3f8544390916c0fe4a5
from apps.books.serializers import *


class WhBookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
<<<<<<< HEAD
                     mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = WhBook.objects.all()
    serializer_class = WhBookSerializer
    authentication_classes = (WhTokenAuthentication,)
=======
                    mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = WhBook.objects.all()
    serializer_class = WhBookSerializer
    authentication_classes = [WhTokenAuthentication, ]
    print(66666666666666666666)
>>>>>>> 5add4948dc349778cc15d3f8544390916c0fe4a5

    def list(self, request, *args, **kwargs):
        print(131313212313131)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

<<<<<<< HEAD
    # 新增书籍
    @list_route(methods=["POST"], serializer_class=WhBookSerializer)
    def add_book(self, request, *args, **kwargs):
        c_id = request.query_params.get("c_id")
        status = request.query_params.get("status")

=======


    # 新增书籍
    @list_route(methods=["POST"])
    def add_book(self, request, *args, **kwargs):
        c_id = request.query_params.get("c_id")
        status = request.query_params.get("status")
        print(c_id, status)
        book = WhBook.objects.all()
        print(book)
>>>>>>> 5add4948dc349778cc15d3f8544390916c0fe4a5

        """
        此处获取用户选择的数据

        """
<<<<<<< HEAD
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
=======
        # new_book = WhBook(b_name='b_name')
        # new_book.save()
        return Response('Save OK!')



    # # 章节列表
    # @list_route(methods=['POST'])
    # def chapter_view(self, *args, **kwargs):
    #     res = WhCatalog.objects.all()
    #     if res:
    #         return Response(res)
    #     else:
    #         return Response('数据有误！')
    #
    # # 新增章节
    # @list_route(methods=['POST'])
    # def add_catalog(self, *args, **kwargs):
    #     """
    #     此处获取用户上传的数据
    #     """
    #     new_catalog = WhCatalog('字段名=获取值...')
    #     new_catalog.save()
    #     return Response('Insert OK!')
    #
    # # 编辑（章节）
    # def update_book(self, *args, **kwargs):
    #     """
    #     此处获取用户上传的数据
    #     """
    #     pass
    #     return Response('Update OK!')
    #
    # # 删除
    # def delete_book(self, *args, **kwargs):
    #     """
    #     此处获取用户上传的数据
    #     """
    #     WhBook.objects.filter(username='新用户').delete()
    #     return Response('Delete OK!')
>>>>>>> 5add4948dc349778cc15d3f8544390916c0fe4a5
