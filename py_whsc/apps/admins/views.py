from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework.response import Response

from admins.serializers import *
from util.errors import ParameterException


# 用户视图


class WhAdminViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = WhAdmin.objects.all()
    serializer_class = WhAdminSerializer
    # authentication_classes = (WhAdminTokenAuthentication,)

    def list(self, request, *args, **kwargs):
        token = request.query_params.get("token")
        user_id = cache.get(token)
        user = WhAdmin.objects.filter(admin_id=user_id).first()
        if user:  # 如果用户已经登录的情况
            serializer = self.get_serializer(user)  # 返回serializer_class指向的序列化类的对象
            res = {
                "user_info": serializer.data,
                "flag": True  # 是否登录的标识
            }
            return Response(res)
        else:
            res = {
                "flag": False  # 是否登录的标识
            }
            return Response(res)

    # @list_route注册一个新API，形如：/methodname/
    @list_route(methods=["POST"], serializer_class=WhAdminRegisterSerializer)
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # raise_exception=False,未通过验证，不抛出异常，返回值，继续往下执行
        # is_valid()会联动调用序列化对象的validate（）方法
        result = serializer.is_valid(raise_exception=True)
        if not result:
            raise ParameterException({"code": "1005", "msg": "注册数据未通过验证！"})

        print("serializer.data=====")
        print(type(serializer.data))
        data = serializer.register_data(serializer.data)  # 调用封装的注册方法，返回字典
        return Response(data)

    @list_route(methods=["POST"], serializer_class=WhAdminLoginSerializer)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        result = serializer.is_valid(raise_exception=False)
        if not result:
            raise ParameterException({'code': '1005', 'msg': '注册数据未通过验证！'})
        res = serializer.login_data(serializer.data)
        return Response(res)

    @list_route(methods=['POST', "GET"],)
    def logout(self, request, *args, **kwargs):
        print(11111111111111111111)
        token = request.data.get("token")
        print(token)
        user_id = cache.get(token)  # 获取token对相应的用户id
        print(user_id)
        user = WhAdmin.objects.filter(admin_id=user_id).exists()
        data = {}
        if user:
            cache.delete(token)
            data['code'] = 200
            data['msg'] = '账户已退出！！'
        return Response(data)

