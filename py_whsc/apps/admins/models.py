from django.db import models


# 角色模型
class WhAdminRole(models.Model):
    role_id = models.AutoField(primary_key=True, verbose_name='角色ID')
    parent_role_id = models.IntegerField(verbose_name='父级角色ID', blank=True, null=True)
    role_name = models.CharField(max_length=64, verbose_name='角色名称', blank=True, null=True)
    add_time = models.IntegerField(verbose_name='添加时间')
    description = models.CharField(max_length=200, name='角色描述', verbose_name='角色描述')

    class Meta:
        db_table = 'wh_admin_role'


# 权限模型
class WhAdminRight(models.Model):
    right_id = models.AutoField(primary_key=True, verbose_name='权限ID')
    parent_right_id = models.IntegerField(verbose_name='父级权限ID', blank=True, null=True)
    right_name = models.CharField(max_length=64, verbose_name='权限名称', blank=True, null=True)
    description = models.CharField(max_length=200, verbose_name='权限描述', blank=True, null=True)

    class Meta:
        db_table = 'wh_admin_right'


# 管理员分组模型
class WhAdminGroup(models.Model):
    group_id = models.AutoField(primary_key=True, verbose_name='分组ID')
    parent_group_id = models.IntegerField( verbose_name='父级分组ID', blank=True, null=True)
    group_name = models.CharField(max_length=64, verbose_name='分组名称', blank=True, null=True)
    description = models.CharField(max_length=200, verbose_name='分组描述', blank=True, null=True)

    class Meta:
        db_table = 'wh_admin_group'


# 管理员模型
class WhAdmin(models.Model):
    admin_id = models.AutoField(primary_key=True, verbose_name='管理员id', auto_created=True)
    group = models.ForeignKey(WhAdminGroup, on_delete=models.CASCADE, verbose_name='所属组织', blank=True, null=True)
    admin_name = models.CharField(max_length=60, verbose_name='管理员名称', blank=True, null=True)
    admin_mobile = models.CharField(max_length=20,  verbose_name='手机号', blank=True, null=True)
    login_name = models.CharField(max_length=60, verbose_name='管理员账号', blank=True, null=True)
    login_pwd = models.CharField(max_length=32, verbose_name='管理员密码', blank=True, null=True)
    login_pwd1 = models.CharField(max_length=32, verbose_name='确认管理员密码', blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    last_login_time = models.DateTimeField(auto_now_add=True, verbose_name='上次登录时间', blank=True, null=True)
    login_time = models.DateTimeField(auto_now_add=True, verbose_name='登录时间', blank=True, null=True)
    last_ip = models.CharField(max_length=15, verbose_name='上次登录ip', blank=True, null=True)
    pwd2 = models.CharField(max_length=32, verbose_name='二级密码', blank=True, null=True)

    # 验证管理员密码(返回True或False)
    def verify_password(self, password):
        return self.login_pwd == password

    class Meta:
        db_table = 'wh_admin'


# 角色权限模型
class WhRoleRightRelation(models.Model):
    rrr_id = models.AutoField(primary_key=True, verbose_name='角色权限ID')
    role = models.ForeignKey(WhAdminRole, on_delete=models.CASCADE, verbose_name='角色ID')
    right = models.ForeignKey(WhAdminRight, on_delete=models.CASCADE, verbose_name='权限ID')
    right_type = models.PositiveSmallIntegerField(name='', verbose_name='权限类型', default=0,
                                                  choices=(('0', '可访问'),
                                                           ('1', '可操作')))

    class Meta:
        db_table = 'wh_role_right'


# 组权限模型
class WhGroupRightRelation(models.Model):
    grr_id = models.AutoField(primary_key=True, verbose_name='分组权限ID')
    group = models.ForeignKey(WhAdminGroup, on_delete=models.CASCADE, verbose_name='分组ID')
    right = models.ForeignKey(WhAdminRight, on_delete=models.CASCADE, verbose_name='权限ID')
    right_type = models.PositiveSmallIntegerField(name='', verbose_name='权限类型', default=0,
                                                  choices=(('0', '可访问'),
                                                           ('1', '可操作')))

    class Meta:
        db_table = 'wh_group_right'


# 组角色模型
class WhGroupRoleRelation(models.Model):
    grr_id = models.AutoField(primary_key=True, verbose_name='组角色ID')
    group = models.ForeignKey(WhAdminGroup, on_delete=models.CASCADE, verbose_name='分组ID')
    role = models.ForeignKey(WhAdminRole, on_delete=models.CASCADE, verbose_name='角色ID')

    class Meta:
        db_table = 'wh_group_role'


# 管理员角色模型
class WhAdminRoleRelation(models.Model):
    grr_id = models.AutoField(primary_key=True, verbose_name='管理员角色ID')
    admin = models.ForeignKey(WhAdmin, on_delete=models.CASCADE, verbose_name='管理员ID')
    role = models.ForeignKey(WhAdminRole, on_delete=models.CASCADE, verbose_name='角色ID')

    class Meta:
        db_table = 'wh_admin_role_relation'


# 管理员分组模型
class WhAdminGroupRelation(models.Model):
    grr_id = models.AutoField(primary_key=True, verbose_name='管理员分组ID')
    admin = models.ForeignKey(WhAdmin, on_delete=models.CASCADE, verbose_name='管理员ID')
    role = models.ForeignKey(WhAdminGroup, on_delete=models.CASCADE, verbose_name='分组ID')

    class Meta:
        db_table = 'wh_admin_group_relation'


# 组织模型
class WhOrganization(models.Model):
    o_id = models.AutoField(primary_key=True, verbose_name='组织ID')
    parent_o_id = models.IntegerField(name='', verbose_name='父级组织ID')
    o_name = models.CharField(max_length=64, verbose_name='组织名称')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    description = models.CharField(max_length=200, verbose_name='组织描述', blank=True, null=True)
    right_type = models.PositiveSmallIntegerField(name='', verbose_name='权限类型', default=0,
                                                  choices=(('0', '可访问'),
                                                           ('1', '可操作')))

    class Meta:
        db_table = 'wh_organization'


# 操作日志模型
class WhAdminLog(models.Model):
    log_id = models.AutoField(primary_key=True, verbose_name='日志ID')
    op_type = models.IntegerField(name='', verbose_name='操作类型')
    o_name = models.CharField(max_length=200, verbose_name='操作内容')
    o_admin = models.ForeignKey(WhAdmin, on_delete=models.CASCADE, verbose_name='操作人')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='操作时间')

    class Meta:
        db_table = 'wh_admin_log'
