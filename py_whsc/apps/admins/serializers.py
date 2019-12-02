import uuid


from django.core.cache import cache
from rest_framework import serializers
from admins.models import *
from py_whsc.settings import AUTH_TOKEN_AGE
from util.errors import ParameterException

# 角色模型序列化
from py_whsc.helper import make_password


class WhAdminRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhAdminRole
        fields = "__all__"


# 权限模型序列化
class WhAdminRightSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhAdminRight
        fields = "__all__"


# 管理员分组模型序列化
class WhAdminGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhAdminGroup
        fields = "__all__"


# 管理员模型序列化
class WhAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhAdmin
        fields = "__all__"


# 角色权限模型序列化
class WhRoleRightRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhRoleRightRelation
        fields = "__all__"


# 组权限模型序列化
class WhGroupRightRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhGroupRightRelation
        fields = "__all__"


# 组角色模型序列化
class WhGroupRoleRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhGroupRoleRelation
        fields = "__all__"


# 管理员角色模型序列化
class WhAdminRoleRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhAdminRoleRelation
        fields = "__all__"


# 管理员分组模型序列化
class WhAdminGroupRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhAdminGroupRelation
        fields = "__all__"


# 组织模型序列化
class WhOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhOrganization
        fields = "__all__"


# 操作日志模型序列化
class WhAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhAdminLog
        fields = "__all__"


class WhAdminRegisterSerializer(serializers.Serializer):
    login_name = serializers.CharField(max_length=32, min_length=3, required=True,
                                       error_messages={
                                           "max_length": "用户名过长（不能超过32个字符）！",
                                           "min_length": "用户名太短（至少3个字符）！",
                                           "required": "必须填写用户名！"
                                       })
    login_pwd = serializers.CharField(max_length=256, min_length=3, required=True, error_messages={
        "required": "必须填写密码！"
    })
    login_pwd1 = serializers.CharField(max_length=256, min_length=3, required=True, error_messages={
        "required": "必须填写密码！"
    })
    # group_id = WhAdminGroupSerializer()
    admin_name = serializers.CharField(max_length=32, required=True, error_messages={
        "required": "必须填写管理员名称！！"
    })
    admin_mobile = serializers.CharField(max_length=11, error_messages={
        'max_length': '手机号格式错误（不能超过11个字符）！'
    })

    def validate(self, attrs):
        print("validate attrs type:", type(attrs))
        login_name = attrs.get("login_name")  # 接收用户传递的数据(用户姓名)
        login_pwd = attrs.get("login_pwd")  # 接收用户传递的数据(用户密码)
        login_pwd1 = attrs.get("login_pwd1")  # 接收用户传递的数据(用户确认密码)
        if login_pwd != login_pwd1:
            raise ParameterException({"code": "1001", "msg": "密码不对，请重新注册！"})
        if WhAdmin.objects.filter(login_name=login_name).exists():
            raise ParameterException({"code": "1001", "msg": "用户已经存在，请重新注册！"})

        return attrs

    def register_data(self, validated_data):
        print('register_data......')
        #   接收序列化后验证码
        login_name = validated_data.get('login_name')
        login_pwd = validated_data.get('login_pwd')
        print(login_name, login_pwd)
        print(validated_data)
        password = make_password(validated_data['login_pwd'])  # 对接收到的密码进行加密

        new_user = WhAdmin.objects.create(login_name=login_name,
                                          login_pwd=password)
        result = {
            "code": 200,
            "msg": "恭喜，注册成功！",
            "user_id": new_user.admin_id
        }
        return result


class WhAdminLoginSerializer(serializers.Serializer):  # 登录序列化类
    login_name = serializers.CharField(max_length=32, min_length=3, required=True,
                                       error_messages={
                                           "max_length": "用户名过长（不能超过32个字符）！",
                                           "min_length": "用户名太短（至少3个字符）！",
                                           "required": "必须填写用户名！"
                                       })
    login_pwd = serializers.CharField(required=True,
                                      error_messages={
                                          "required": "必须填写用户名！"
                                      })

    def validate(self, attrs):  # 登录逻辑验证
        login_name = attrs.get("login_name")  # 接收用户传递的数据(用户姓名)
        login_pwd = attrs.get("login_pwd")  # 接收用户传递的数据(用户密码)
        if not WhAdmin.objects.filter(login_name=login_name).exists():
            print(111111)
            raise ParameterException({'code': '1004', 'msg': '用户不存在'})

        user = WhAdmin.objects.filter(login_name=login_name).first()
        print('加密密码：', user.login_pwd)
        if make_password(login_pwd) != user.login_pwd:
            print(222222)
            raise ParameterException({'code': '1004', 'msg': '用户不存在'})
        return attrs

    def login_data(self, validated_data):
        token = uuid.uuid4().hex
        user = WhAdmin.objects.filter(login_name=validated_data.get('login_name')).first()

        cache.set(token, user.admin_id, timeout=AUTH_TOKEN_AGE)  # 将token作为缓存的而言存储到缓存中，对应的value是用户id
        res = {
            'token': token
        }
        return res



