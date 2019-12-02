from rest_framework.renderers import JSONRenderer


class MyJSONRender(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):

        try:
            # 如果响应数据中包含自己添加的code与msg,则可弹出
            code = data.pop("code")
            msg = data.pop("msg")
        except:
            code = 200
            msg = "ok"
        renderer_context['response'].status_code = 200
        result = {
            "code": code,
            "msg": msg,
            "data": data
        }
        return super().render(result)  # 还是调用了父类JSONRenderer的render()方法逻辑
