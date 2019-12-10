#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-07-29 15:07
# @Author : ryuchen
# @File : simpleui.py
# @Desc :
# ==================================================

# SimpleUI settings
# https://github.com/newpanjing/simpleui/blob/master/QUICK.md
SIMPLEUI_STATIC_OFFLINE = True  # 离线模式 在2.1.3或以上的版本中生效 在settings.py中加入
SIMPLEUI_FAVICON_ICON = "/static/bistu/img/whsc_logo.png"
SIMPLEUI_LOGIN_LOGO = "/static/bistu/img/whsc_caiselogo.png"
SIMPLEUI_INDEX_LOGO = "/static/bistu/img/whsc_logo.png"
SIMPLEUI_LOGO = "/static/bistu/img/whsc_logo.png"  # 自定义SIMPLEUI的Logo
SIMPLEUI_HOME_TITLE = '工作台'  # 首页标题
# SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'  # 首页配置
SIMPLEUI_HOME_ICON = 'fas fa-tachometer-alt'  # 首页图标,支持element-ui和fontawesome的图标，
# 参考https://fontawesome.com/icons图标
# SIMPLEUI_INDEX = 'https://www.baidu.com'  # 设置simpleui 点击首页图标跳转的地址
SIMPLEUI_LOGIN_PARTICLES = True  # 开启或关闭登录页粒子动画
# SIMPLEUI_DEFAULT_THEME = 'admin.Default.css'  # 指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取
SIMPLEUI_LOADING = False  # 关闭Loading遮罩层
SIMPLEUI_HOME_INFO = False  # 服务器信息（隐藏/显示）
SIMPLEUI_HOME_QUICK = False  # 快速操作（隐藏/显示）
SIMPLEUI_HOME_ACTION = False  # 最近动作（隐藏/显示）
# 默认开启，统计分析信息只是为了更好的帮助simpleui改进，并不会读取敏感信息。并且分析数据不会分享至任何第三方。
SIMPLEUI_ANALYSIS = False

SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menus': [
        {
            'app': 'auth',
            'name': '账户管理',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-users-cog',
                    'url': 'auth/group/'
                }
            ]
        },
        # {
        #     'app': 'accounts',
        #     'name': '学生管理',
        #     'icon': 'fa fa-graduation-cap',
        #     'url': 'accounts/student/'
        # },
        # {
        #     'app': 'accounts',
        #     'name': '教师管理',
        #     'icon': 'fa fa-id-card',
        #     'url': 'accounts/tutor/'
        # },
        # {
        #     'app': 'colleges',
        #     'name': '学院管理',
        #     'icon': 'fa fa-university',
        #     'models': [
        #         {
        #             'name': '学院',
        #             'icon': 'fa fa-university',
        #             'url': 'colleges/academy/'
        #         },
        #         {
        #             'name': '专业',
        #             'icon': 'fa fa-university',
        #             'url': 'colleges/major/'
        #         },
        #         {
        #             'name': '班级',
        #             'icon': 'fa fa-university',
        #             'url': 'colleges/class/'
        #         },
        #         {
        #             'name': '教改',
        #             'icon': 'fa fa-university',
        #             'url': 'colleges/reform/'
        #         },
        #         {
        #             'name': '统计',
        #             'icon': 'fa fa-university',
        #             'url': 'colleges/reformresults/'
        #         }
        #     ]
        # },
        # {
        #     'app': 'education',
        #     'name': '教学管理',
        #     'icon': 'fas fa-book',
        #     'models': [
        #         {
        #             'name': '论文',
        #             'icon': 'fa fa-book',
        #             'url': 'education/thesis/'
        #         },
        #         {
        #             'name': '论文查重',
        #             'icon': 'fa fa-book',
        #             'url': 'education/thesisplacheck/'
        #         },
        #         {
        #             'name': '论文盲审',
        #             'icon': 'fa fa-book',
        #             'url': 'education/thesisblindreview/'
        #         },
        #     ]
        # }
    ]
}
