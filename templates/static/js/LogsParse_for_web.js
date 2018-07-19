/*图表控制*/
let hours = ['12a', '1a', '2a', '3a', '4a', '5a', '6a',
        '7a', '8a', '9a','10a','11a',
        '12p', '1p', '2p', '3p', '4p', '5p',
        '6p', '7p', '8p', '9p', '10p', '11p'];

let days = ['Saturday', 'Friday', 'Thursday',
        'Wednesday', 'Tuesday', 'Monday', 'Sunday'];

let data = [[0,0,5],[0,1,1],[0,2,0],[0,3,0],[0,4,0],[0,5,0],[0,6,0],[0,7,0],[0,8,0],[0,9,0],[0,10,0],[0,11,2],[0,12,4],[0,13,1],[0,14,1],[0,15,3],[0,16,4],[0,17,6],[0,18,4],[0,19,4],[0,20,3],[0,21,3],[0,22,2],[0,23,5],[1,0,7],[1,1,0],[1,2,0],[1,3,0],[1,4,0],[1,5,0],[1,6,0],[1,7,0],[1,8,0],[1,9,0],[1,10,5],[1,11,2],[1,12,2],[1,13,6],[1,14,9],[1,15,11],[1,16,6],[1,17,7],[1,18,8],[1,19,12],[1,20,5],[1,21,5],[1,22,7],[1,23,2],[2,0,1],[2,1,1],[2,2,0],[2,3,0],[2,4,0],[2,5,0],[2,6,0],[2,7,0],[2,8,0],[2,9,0],[2,10,3],[2,11,2],[2,12,1],[2,13,9],[2,14,8],[2,15,10],[2,16,6],[2,17,5],[2,18,5],[2,19,5],[2,20,7],[2,21,4],[2,22,2],[2,23,4],[3,0,7],[3,1,3],[3,2,0],[3,3,0],[3,4,0],[3,5,0],[3,6,0],[3,7,0],[3,8,1],[3,9,0],[3,10,5],[3,11,4],[3,12,7],[3,13,14],[3,14,13],[3,15,12],[3,16,9],[3,17,5],[3,18,5],[3,19,10],[3,20,6],[3,21,4],[3,22,4],[3,23,1],[4,0,1],[4,1,3],[4,2,0],[4,3,0],[4,4,0],[4,5,1],[4,6,0],[4,7,0],[4,8,0],[4,9,2],[4,10,4],[4,11,4],[4,12,2],[4,13,4],[4,14,4],[4,15,14],[4,16,12],[4,17,1],[4,18,8],[4,19,5],[4,20,3],[4,21,7],[4,22,3],[4,23,0],[5,0,2],[5,1,1],[5,2,0],[5,3,3],[5,4,0],[5,5,0],[5,6,0],[5,7,0],[5,8,2],[5,9,0],[5,10,4],[5,11,1],[5,12,5],[5,13,10],[5,14,5],[5,15,7],[5,16,11],[5,17,6],[5,18,0],[5,19,5],[5,20,3],[5,21,4],[5,22,2],[5,23,0],[6,0,1],[6,1,0],[6,2,0],[6,3,0],[6,4,0],[6,5,0],[6,6,0],[6,7,0],[6,8,0],[6,9,0],[6,10,1],[6,11,0],[6,12,2],[6,13,1],[6,14,3],[6,15,4],[6,16,0],[6,17,0],[6,18,0],[6,19,0],[6,20,1],[6,21,2],[6,22,2],[6,23,6]];
option_1 = {
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

option_2 = {
    tooltip: {},
    visualMap: {
        max: 20,
        inRange: {
            color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
        }
    },
    xAxis3D: {
        type: 'category',
        data: ['12a', '1a', '2a', '3a', '4a', '5a', '6a',
        '7a', '8a', '9a','10a','11a',
        '12p', '1p', '2p', '3p', '4p', '5p',
        '6p', '7p', '8p', '9p', '10p', '11p']
    },
    yAxis3D: {
        type: 'category',
        data: days
    },
    zAxis3D: {
        type: 'value'
    },
    grid3D: {
        boxWidth: 200,
        boxDepth: 80,
        light: {
            main: {
                intensity: 1.2
            },
            ambient: {
                intensity: 0.3
            }
        }
    },
    series: [{
        type: 'bar3D',
        data: data.map(function (item) {
            return {
                value: [item[1], item[0], item[2]]
            }
        }),
        shading: 'color',

        label: {
            show: false,
            textStyle: {
                fontSize: 16,
                borderWidth: 1
            }
        },

        itemStyle: {
            opacity: 0.4
        },

        emphasis: {
            label: {
                textStyle: {
                    fontSize: 20,
                    color: '#900'
                }
            },
            itemStyle: {
                color: '#900'
            }
        }
    }]
};
let myChart = echarts.init(document.getElementById('chart-panel'));
myChart.setOption(option_2);
function setCharts(option){
    let myChart_old = echarts.init(document.getElementById('chart-panel'));
    myChart_old.clear();
    let myChart_new = echarts.init(document.getElementById('chart-panel'));
    myChart_new.setOption(option);
}

/*菜单控制*/
$('.dropdown > a').click(function () {
    $(this).siblings('ul').toggle("slow");
});

$('.dropdown-menu > li > a').click(function (e) {
    e.stopPropagation();
    $('.dropdown-menu').hide("slow");
    let id = $(this).attr('id');
    let text = $(this).text();
    $('.code-info-type-info').text(text);
});

/*异步请求*/
let obj = {};
$(document).ready(function () {
    $.get("/dirs/", { 'group': "9" },
        function(data){
            obj = JSON.parse(data);
            for(let p in obj){
                let elem = '<li><a href="#">' + p + '</a></li>';
                $('#spider_group').append(elem);
            }
    });

});
$(document).on('click', '.dropdown-menu > li > a', function () {
    $('.dropdown-menu').hide('slow');
    let text = $(this).text();
    $('.code-info-time').text(text);

    setCharts(option_1);
    let arry = obj[text];
    let elem = $('#spider_group_url').empty();
    for(let x = 0; x < arry.length; x++){
        let url = '<div class="ace_scrollbar-inner spider_url" style="height: 22px; width: 546px;">' +
                        '<span>' + format(x) + '</span>'
                      + '<span>  http://' + arry[x] + '</span>' +
                  '</div>';
        elem.append(url)
    }
});

$(document).on('click','.spider_url', function () {
    $.get('/spider_data/',{'spider_url':$(this).text()},function (data) {
        obj = JSON.parse(data);
        myChart.setOption({
        title : {
            text: '蜘蛛数量统计',
            subtext: obj['title']
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
                data : obj['category']
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
                data: obj['Baiduspider'],
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
                data: obj['Yisouspider'],
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
                data: obj['360Spider'],
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
                data: obj['sougou'],
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
    });
    });
});

function format(x) {
    if(x < 10){
        return '00' + x
    }
    if(x < 100){
        return '0' + x
    }
    else {
        return x
    }
}