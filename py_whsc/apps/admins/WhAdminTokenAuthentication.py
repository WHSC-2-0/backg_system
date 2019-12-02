from django.core.cache import cache
from rest_framework.authentication import TokenAuthentication, get_authorization_header

from admins.models import WhAdmin
from util.errors import ParameterException


class WhAdminTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        try:
            token = request.data.get('token') if request.data.get('token') else request.query_params.get(
                'token')  # 获取请求体中的名称为token的参数

            user_id = cache.get(token)  # 获取token对相应的用户id
            user = WhAdmin.objects.get(admin_id=user_id)  # 如果用户未登录，则此处报错
            return user, token
        except Exception as e:
            print('用户登录异常：', e)
            raise ParameterException({'code': 10086, 'msg': '您还未登录，请先登录'})
            # return Response({'code': 10086, 'msg': '未登录，不能加入购物车'})
