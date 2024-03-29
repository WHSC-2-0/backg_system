(function () {
    new Vue({
        el: '#display-pie-chart',
        data: function () {
            const ratioStatistic = {
                ratioData: [],
                enrollYears: [],
                radioYear: ''
            };
            const year = new Date().getFullYear();
            for (let i = 0; i < 5; i++) {
                ratioStatistic.enrollYears.push(year - i);
            }
            ratioStatistic.radioYear = year;
            return ratioStatistic;
        },
        methods: {
            drawLine(data, total) {
                const chart = new G2.Chart({
                    container: "pie-chart",
                    forceFit: true,
                    width: '420',
                    height: '420',
                    padding: [20, 'auto', 30, 'auto'],
                });

                chart.source(data, {
                    percent: {
                        formatter: function formatter(val) {
                            val = `${(val * 100).toFixed(2)}%`;
                            return val;
                        },
                    },
                });
                chart.coord('theta', {
                    radius: 1,
                    innerRadius: 0.7,
                });
                chart.tooltip({
                    showTitle: false,
                    itemTpl: '<li><span style="background-color:{color};" class="g2-tooltip-marker"></span>{name}: {value}</li>',
                });
                chart.legend({
                    layout: 'vertical',
                    allowAllCanceled: false,
                    useHtml: true,
                    container: 'pie-chart-tooltip',
                    itemTpl: (value, color, checked, index) => {
                        const obj = data[index];
                        return (
                            '<tr class="g2-legend-list-item item-{index} {checked}" data-value="{value}" data-color={color} style="cursor: pointer;font-size: 14px;margin: 20px 0">' +
                            '<td width="240" style="border: none;padding:0;text-align:left;">' +
                            '<i class="g2-legend-marker" style="width:10px;height:10px;display:inline-block;margin-right:16px;background-color:{color};"></i>' +
                            `<span class="g2-legend-text">${obj.item}</span> <strong>|</strong> <span class="g2-pie__legend-percent">${obj.percent}%</span>` +
                            '</td>' +
                            `<td width="80" style="border: none;padding:0;text-align:end;"> 人数: ${obj.count}</td>` +
                            '</tr>'
                        );
                    },
                });
                // 辅助文本
                chart.guide().html({
                    position: ['50%', '50%'],
                    html: `<div style="color:#8c8c8c;font-size: 14px;text-align: center;width: 10em;"><strong><div>${ this.radioYear } 年招生人数 </div><div>${total}</div></strong></div>`,
                    alignX: 'middle',
                    alignY: 'middle',
                });
                chart
                    .intervalStack()
                    .position('percent')
                    .color('item')
                    .tooltip('item*percent', (item, percent) => {
                        percent = `${(percent * 100).toFixed(2)}%`;
                        return {
                            name: item,
                            value: percent,
                        };
                    })
                    .style({
                        lineWidth: 1,
                        stroke: '#fff',
                    });
                chart.render();
            },
            getEnrollRatioData(callback) {
                Vue.prototype.$http = axios;
                let _this = this;
                this.$http.get(pieChartUrl, {})
                    .then(function (res) {
                        _this.ratioData = res.data.data.ratio;
                        const total = _this.ratioData.reduce((pre, now) => now.total + pre, 0);
                        const data = _this.ratioData.map((item) => {
                            return {
                                item: item.aca_cname,
                                count: item.total,
                                percent: item.total / total,
                            };
                        });
                        callback(data, total);
                    })
                    .catch(function (error) {
                        console.log(error);
                        //_this.$notify.error({
                        //  title: '错误',
                        // message: '查询过程中发现错误'
                        //});
                    });
            },
            selectEnrollYear: function() {
                console.log(1231);
            }
        }
    });
})();