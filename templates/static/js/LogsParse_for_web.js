let myChart1 = echarts.init(document.getElementById('chart1'));
let myChart2 = echarts.init(document.getElementById('chart2'));
option1 = {
    title: {
        text: '蜘蛛类型'
    },
    tooltip : {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    legend: {
        data:['百度蜘蛛','神马蜘蛛','360蜘蛛','搜狗蜘蛛']
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data : []
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'百度蜘蛛',
            type:'line',
            stack: '总量',
            areaStyle: {normal: {}},
            data:[]
        },
        {
            name:'神马蜘蛛',
            type:'line',
            stack: '总量',
            areaStyle: {normal: {}},
            data:[]
        },
        {
            name:'360蜘蛛',
            type:'line',
            stack: '总量',
            areaStyle: {normal: {}},
            data:[]
        },
        {
            name:'搜狗蜘蛛',
            type:'line',
            stack: '总量',
            areaStyle: {normal: {}},
            data:[]
        }
    ]
};

option2 = {
    title: {
        text: '世界人口总量',
        subtext: '数据来自网络'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    legend: {
        data: ['2011年', '2012年', '2013年']
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: {
        type: 'value',
        boundaryGap: [0, 0.01]
    },
    yAxis: {
        type: 'category',
        data: ['巴西','印尼','美国','印度','中国','世界人口']
    },
    series: [
        {
            name: '2011年',
            type: 'bar',
            data: [18203, 23489, 29034, 104970, 131744, 630230]
        },
        {
            name: '2012年',
            type: 'bar',
            data: [19325, 23438, 31000, 121594, 134141, 681807]
        },
        {
            name: '2013年',
            type: 'bar',
            data: [19325, 23438, 31000, 101594, 100141, 601807]
        }
    ]
};

myChart1.setOption(option1);
myChart2.setOption(option2);

function getdata(){
            post_data = {
                'url':$("#post_url").val(),
                'ip':$("#post_ip").val(),
                'pwd':$("#post_pwd").val(),
            };
            $.getJSON('/data/',post_data).done(function (data) {
            myChart1.setOption({
                series: [{
                    name:'百度蜘蛛',
                    type:'line',
                    stack: '总量',
                    areaStyle: {normal: {}},
                    data: data['baidu']
                },
                {
                    name:'神马蜘蛛',
                    type:'line',
                    stack: '总量',
                    areaStyle: {normal: {}},
                    data: data['shenma']
                },
                {
                    name:'360蜘蛛',
                    type:'line',
                    stack: '总量',
                    areaStyle: {normal: {}},
                    data: data['s360']
                },
                {
                    name:'搜狗蜘蛛',
                    type:'line',
                    stack: '总量',
                    areaStyle: {normal: {}},
                    data: data['shougou']
                }],
                xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data : data['category']
                }]
            });
        });
    }
