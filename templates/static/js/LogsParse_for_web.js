let myChart1 = echarts.init(document.getElementById('chart-panel'));
option1 = {
    title : {
        text: '蜘蛛数量统计',
        subtext: '一组蜘蛛池 域名：www.aibding.com'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['百度蜘蛛','神马蜘蛛','360蜘蛛','搜狗蜘蛛']
    },
    toolbox: {
        show : true,
        feature : {
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            data : ['0606', '0607', '0608', '0609', '0610', '0611', '0612', '0613', '0614', '0615', '0616', '0617', '0618', '0619', '0620', '0621', '0622', '0623', '0624', '0625', '0626', '0627', '0628', '0629', '0630', '0701', '0702', '0703', '0704', '0705', '0706', '0707', '0708', '0709', '0710', '0711', '0712']
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
            type:'bar',
            data:[682, 3948, 4057, 1310, 14, 72, 2, 4, 1, 2, 7, 4, 8, 6, 5, 6, 5, 10, 5, 5, 6, 6, 8, 2, 6, 8, 5, 4, 6, 4, 6, 7, 7, 4, 6, 5, 3],
            markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: '平均值'}
                ]
            }
        },
        {
            name:'神马蜘蛛',
            type:'bar',
            data:[370, 784, 974, 798, 7, 5, 125, 2146, 113, 56, 64, 120, 129, 131, 134, 125, 159, 122, 97, 54, 96, 74, 69, 38, 115, 74, 50, 42, 78, 100, 91, 48, 52, 78, 66, 35, 33],
            markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : '平均值'}
                ]
            }
        },
        {
            name:'360蜘蛛',
            type:'bar',
            data:[7, 8, 659, 1555, 0, 6, 45, 31, 74, 5, 4, 0, 2, 4, 6, 37, 79, 8, 1, 7, 7, 0, 1, 28, 7, 0, 20, 50, 44, 5, 41, 6, 1, 112, 135, 43, 85],
            markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : '平均值'}
                ]
            }
        },
        {
            name:'搜狗蜘蛛',
            type:'bar',
            data:[156, 688, 965, 1162, 546, 716, 742, 794, 496, 32, 37, 38, 37, 35, 2, 72, 39, 38, 38, 82, 63, 77, 53, 79, 76, 88, 37, 80, 81, 78, 76, 79, 78, 78, 70, 69, 69],
            markPoint : {
                data : [
                    {type : 'max', name: '最大值'},
                    {type : 'min', name: '最小值'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : '平均值'}
                ]
            }
        }
    ]
};
myChart1.setOption(option1);