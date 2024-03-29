(function () {
    if (window.frameElement) {
        window.frameElement.contentWindow.parent.callback()
    }

    window.addEventListener('hashchange', function (e) {
        if (e.newURL !== e.oldURL) {
            openByHash()
        }
    });

    function openByHash() {
        let hash = location.hash;
        hash = hash.substring(1);
        for (let i = 0; i < app.menuData.length; i++) {
            let item = app.menuData[i];
            if ((item.url || '/') === hash) {
                app.openTab(item, item.index);
                break;
            }
        }
    }

    function changeUrl(data) {
        location.href = '#' + (data.url || '/')
    }

    window.callback = function () {
        window.location.reload()
    };

    const fontConfig = new Vue({
        el: '#dynamicCss',
        data: {
            fontSize: 14
        },
        created: function () {
            const val = getCookie('fontSize');
            if (val) {
                this.fontSize = parseInt(val);
            } else {
                this.fontSize = 0;
            }
        },
        methods: {}
    });

    //为元素注册水波纹效果
    Vue.directive('waves', {
        // 当被绑定的元素插入到 DOM 中时……
        inserted: function (el) {
            // 聚焦元素
            Waves.attach(el);
            Waves.init();
        }
    });

    window.getTranslate = function (key) {
        if (!window.Lanuages) {
            return "";
        }
        let val = Lanuages[key];
        if (!val || val === "") {
            val = key;
        }
        return val
    };

    var main = new Vue({
        el: '#main',
        data: {
            isResize: false,
            searchInput: '',
            height: 1000,
            fold: false,
            zoom: false,
            timeline: true,
            tabs: [home],
            tabModel: 0,
            tabIndex: 0,
            menus: [],
            menuActive: '0',
            breadcrumbs: [],
            language: window.language,
            pwdDialog: {},
            themeDialogVisible: false,
            small: false,
            themes: SimpleuiThemes,
            theme: "",
            themeName: "",
            popup: {
                left: 0,
                top: 0,
                show: false,
                tab: null,
                menus: [{
                    text: getTranslate('Refresh'),
                    icon: 'el-icon-refresh',
                    handler: function (tab, item) {
                        try {
                            document.getElementById(tab.id).contentWindow.location.reload(true);
                        } catch (e) {
                            console.log(e)
                            var url = tab.url.split('?')[0];
                            tab.url = url + '?_=' + new Date().getTime()
                        }
                    }
                }, {
                    text: getTranslate('Close current'),
                    icon: 'el-icon-circle-close',
                    handler: function (tab, item) {
                        app.handleTabsEdit(tab.id, 'remove');
                    }
                }, {
                    text: getTranslate('Close other'),
                    icon: 'far fa-copy',
                    handler: function (tab) {
                        app.tabs.forEach(item => {
                            if (item.id !== tab.id) {
                                app.handleTabsEdit(item.id, 'remove');
                            }
                        })
                    }
                }, {
                    text: getTranslate('Close all'),
                    icon: 'el-icon-close',
                    handler: function (tab, item) {

                        app.$confirm(Lanuages["Are you sure you want them all closed"], Lanuages.Tips, {
                            confirmButtonText: Lanuages.ConfirmYes,
                            cancelButtonText: Lanuages.ConfirmNo,
                            type: 'warning'
                        }).then(function () {
                            app.tabs.forEach((tab, index) => {
                                if (index !== 0) {
                                    app.handleTabsEdit(tab.id, 'remove');
                                }
                            });
                            app.menuActive = '1';
                        }).catch(function () {

                        });

                    }
                }, {
                    text: getTranslate('Open in a new page'),
                    icon: 'el-icon-news',
                    handler: function (tab, item) {
                        window.open(tab.newUrl);
                    }
                }]
            },
            //菜单里面的模块
            models: [],
            fontDialogVisible: false,
            fontSlider: 14,
            loading: false,
            menuTextShow: true,
            menuData: []
        },
        watch: {
            fold: function (newValue, oldValue) {
                console.log(newValue);
                console.log(oldValue);
            },
            menus: function (newValue, oldValue) {
                let self = this;
                newValue.forEach(item => {
                    if (item.id === '0') {
                        return;
                    }
                    if (item.models) {
                        item.models.forEach(child => {
                            self.models.push(child);
                        });
                    } else {
                        self.models.push(item);
                    }
                });
            }
        },
        created: function () {
            const self = this;
            let val = getCookie('fold') === 'true';
            self.small = self.fold = val;
            self.menuTextShow = !this.fold;
            window.onresize = function () {
                self.height = document.documentElement.clientHeight || document.body.clientHeight;
                const width = document.documentElement.clientWidth || document.body.clientWidth;
                if (!self.small) {
                    self.menuTextShow = !(width < 800);
                    self.$nextTick(() => {
                        self.fold = width < 800;
                    })
                }
                self.isResize = true;
                //判断全屏状态
                try {
                    self.zoom = document.webkitIsFullScreen;
                } catch (e) {
                    console.log(e);
                }
            };
            //导致页面不能正常撑开，调用resize使其重新计算
            if(window.onresize){
                window.onresize(undefined);
            }
            window.app = this;
            window.menus.forEach(item => {
                item.icon = getIcon(item.name, item.icon);

                if (item.models) {
                    item.models.forEach(mItem => {
                        mItem.icon = getIcon(mItem.name, mItem.icon);
                        self.menuData.push(mItem)
                    });
                } else {
                    self.menuData.push(item)
                }
            });
            this.menus = window.menus;
            this.theme = getCookie('theme');
            this.themeName = getCookie('theme_name');
            //接收子页面的事件注册
            window.themeEvents = [];
            window.fontEvents = [];
            window.addEvent = function (name, handler) {
                if (name === 'theme') {
                    themeEvents.push(handler);
                } else if (name === 'font') {
                    fontEvents.push(handler);
                }
            };
            const temp_tabs = sessionStorage['tabs'];
            if (temp_tabs && temp_tabs !== '') {
                this.tabs = JSON.parse(temp_tabs);
            }
            if (location.hash !== '') {
                openByHash();
            }
        },
        methods: {
            syncTabs: function () {
                if (window.sessionStorage) {
                    sessionStorage['tabs'] = JSON.stringify(this.tabs);
                }
            },
            reset: function () {
                this.fontSlider = 14;
                fontConfig.fontSize = 0;
                setCookie('fontSize', 0);
                this.fontDialogVisible = false;
                fontEvents.forEach(handler => {
                    handler(0);
                });
            },
            fontClick: function () {
                this.fontSlider = fontConfig.fontSize;
                this.fontDialogVisible = !this.fontDialogVisible;
            },
            fontSlideChange: function (value) {
                fontConfig.fontSize = value;
                //写入cookie
                setCookie('fontSize', value);
                fontEvents.forEach(handler => {
                    handler(value);
                });

            },
            iframeLoad: function (tab, e) {
                const url = e.target.contentWindow.location.href;
                tab.newUrl = url;
                tab.loading = false;
                this.$forceUpdate();
                let self = this;
                e.target.contentWindow.beforeLoad = function () {
                    tab.loading = true;
                    self.$forceUpdate();
                };
                this.loading = false;
            },
            setTheme: function (item) {
                const url = window.themeUrl;
                if (item.file && item.file !== '') {
                    this.theme = url + item.file;
                } else {
                    this.theme = '';
                }
                this.themeName = item.text;
                setCookie('theme', this.theme);
                setCookie('theme_name', item.text);
                let self = this;
                //通知子页面
                window.themeEvents.forEach(handler => {
                    handler(self.theme)
                });
            },
            openUrl: function (url) {
                window.open(url);
            },
            contextmenu: function (item, e) {

                //home没有popup menu
                if (item.id === '0') {
                    return;
                }
                this.popup.tab = item;
                this.popup.left = e.clientX;
                this.popup.top = e.clientY;
                this.popup.show = true;
            },
            mainClick: function (e) {
                this.popup.show = false;
            },
            tabClick: function (tab) {
                var item = this.tabs[tab.index];
                var index = item.index;
                this.menuActive = index;
                this.breadcrumbs = item.breadcrumbs;
                changeUrl(item);
            },
            handleTabsEdit: function (targetName, action) {
                var self = this;
                if (action === 'remove') {
                    var next = '0';
                    this.tabs.forEach((tab, index) => {
                        if (tab.id == targetName) {
                            var temp = self.tabs[index + 1] || self.tabs[index - 1];
                            if (temp) {
                                next = temp.id;
                                self.menuActive = temp.index;
                                self.breadcrumbs = temp.breadcrumbs;
                                changeUrl(temp)
                            }
                        }
                    });
                    this.tabModel = next;

                    if (targetName != 0) {
                        this.tabs = this.tabs.filter(tab => tab.id !== targetName);
                    }
                    this.syncTabs();
                }
            },
            openTab: function (data, index) {
                this.breadcrumbs = data.breadcrumbs;
                var exists = null;
                //判断是否存在，存在就直接打开
                for (var i = 0; i < this.tabs.length; i++) {
                    var tab = this.tabs[i];
                    if (tab.name == data.name) {
                        exists = tab;
                        continue;
                    }
                }

                if (exists) {
                    this.tabModel = exists.id;
                } else {
                    //其他的网址loading会一直转
                    if (data.url.indexOf('http') != 0) {
                        data.loading = true;
                        this.loading = true;
                    }
                    data.id = new Date().getTime() + "" + Math.random();
                    data.index = index;
                    this.tabs.push(data);
                    this.tabModel = data.id;
                }
                changeUrl(data)
                this.syncTabs();
            },
            foldClick: function () {
                this.menuTextShow = !this.menuTextShow;
                this.$nextTick(() => {
                    this.fold = !this.fold;
                    this.small = this.fold;
                    //设置进cookie
                    setCookie('fold', this.fold);
                });
            },
            changePassword: function () {
                var width = document.documentElement.clientWidth || document.body.clientWidth;
                if (width > 800) {
                    this.pwdDialog = {
                        url: window.urls.changePassword + '?dialog=1',
                        name: language.change_password,
                        show: true
                    };
                } else {
                    this.openTab({
                        url: window.urls.changePassword,
                        icon: 'far fa-edit',
                        name: language.change_password,
                        breadcrumbs: [{
                            name: language.change_password,
                            icon: 'far fa-edit'
                        }]
                    })
                    app.breadcrumbs = [language.change_password];
                }
            },
            logout: function () {
                this.$confirm(language.confirm, Lanuages.Tips, {
                    confirmButtonText: language.yes,
                    cancelButtonText: language.no,
                    type: 'warning'
                }).then(function () {
                    window.location.href = window.urls.logout;
                }).catch(function () {

                });
            },
            goIndex: function (url) {
                if (!url || url === 'None') {
                    url = '/';
                }
                window.open(url);
            },
            getTranslate: getTranslate,
            getIcon: getIcon,
            goZoom: function () {
                var el = window.document.body;
                if (!this.zoom) {
                    var isFullscreen = document.fullScreen || document.mozFullScreen || document.webkitIsFullScreen;
                    if (!isFullscreen) {//进入全屏,多重短路表达式
                        (el.requestFullscreen && el.requestFullscreen()) ||
                        (el.mozRequestFullScreen && el.mozRequestFullScreen()) ||
                        (el.webkitRequestFullscreen && el.webkitRequestFullscreen()) || (el.msRequestFullscreen && el.msRequestFullscreen());
                    }
                    this.zoom = true;
                } else {
                    document.exitFullscreen ? document.exitFullscreen() :
                        document.mozCancelFullScreen ? document.mozCancelFullScreen() :
                            document.webkitExitFullscreen ? document.webkitExitFullscreen() : '';
                    this.zoom = false;
                }
            },
            displayTimeline: function () {
                this.timeline = !this.timeline;
            },
            report: function () {
                window.open('https://github.com/newpanjing/simpleui/issues')
            },
            selectEnrollYear: function() {
                console.log(1231);
            }
        }
    })
})();