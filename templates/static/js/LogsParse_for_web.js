/* 二维图表 */
option_1 = {
    title : {
        text: '蜘蛛数量统计',
        subtext: '蜘蛛池 域名：http://aidshe.com'
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
            type:'bar',
            data:[],
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
            data:[],
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
            data:[],
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
            data:[],
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

/* 图表控制 */
let myChart = echarts.init(document.getElementById('chart-panel'));
myChart.setOption(option_1);
function setCharts(option){
    myChart.showLoading();
    let myChart_old = echarts.init(document.getElementById('chart-panel'));
    myChart_old.clear();
    let myChart_new = echarts.init(document.getElementById('chart-panel'));
    myChart.hideLoading();
    myChart_new.setOption(option);
}

/* 菜单控制 */
$('.dropdown > a').click(function () {
    $(this).siblings('ul').toggle("slow");
});
/* 异步请求 */
let obj = {};
$('.dropdown-menu > li > a').click(function (e) {
    e.stopPropagation();
    $('.dropdown-menu').hide("slow");
    let id = $(this).attr('id');
    let text = $(this).text();
    $('.code-info-type-info').text(text);
    $.get('/dirs/',{'group_id': '8'}, function () {
        $('#spider_group > li').remove();
        obj = JSON.parse(data);
            for(let p in obj){
                let elem = '<li><a href="#">' + p + '</a></li>';
                $('#spider_group').append(elem);
            }
            $('.dropdown-menu > li > a:last').trigger('click');
            $('.spider_url:first').trigger('click');
    });
});

/* 页面加载完毕后执行 读取域名和分组*/
$(document).ready(function () {
    $.get("/dirs/", { 'group_id': "8" }, function(data){
            obj = JSON.parse(data);
            for(let p in obj){
                let elem = '<li><a href="#">' + p + '</a></li>';
                $('#spider_group').append(elem);
            }
            $('.dropdown-menu > li > a:last').trigger('click');
            $('.spider_url:first').trigger('click');
    });

});
/* 菜单点击事件 */
$(document).on('click', '.dropdown-menu > li > a', function () {
    $('.dropdown-menu').hide('slow');
    let text = $(this).text();
    $('.code-info-time').text(text);


    setCharts(option_1);
    let arry = obj[text];
    let elem = $('#spider_group_url').empty();
    for(let x = 0; x < arry.length; x++){
            let url = '<div class="ace_scrollbar-inner spider_url " style="height: 22px; width: 546px;">' +
                        '<span>' + format(x) + '</span>'
                      + '<span>  http://' + arry[x] + '</span>' +
                  '</div>';
        elem.append(url)
    }
});

/* 域名点击事件 */
$(document).on('click','.spider_url', function () {
    myChart.showLoading();
    let group_id = $('.code-info-type-info').text()[0];
    $.get('/spider_data/',{'spider_url':$(this).text(),'group_id': group_id},function (data) {
        let spider_data = JSON.parse(data);
        let domain = $('#domain');
        domain.attr('href', spider_data['url']);
        myChart.hideLoading();
        myChart.setOption({
        title : {
            text: '蜘蛛数量统计',
            subtext: spider_data['title']
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
                data : spider_data['category']
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
                data: spider_data['Baiduspider'],
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
                data: spider_data['Yisouspider'],
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
                data: spider_data['360Spider'],
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
                data: spider_data['sogou'],
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
/* 格式化字符 */
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
// /* 刷新数据 */
// $('#refresh_url').click(function () {
//     let option = myChart.getOption();
//     $.get('/refresh_data/',{'group_id': '9','subtext':option['title'][0]['subtext']},function (data) {
//         let refresh_data = JSON.parse(data);
//         alert(refresh_data['message'])
//     });
// });