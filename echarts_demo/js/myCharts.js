/**
 * Created by qimi on 2016/8/13.
 */

// 处理接口返回的原始JSON数据
function handleData(rawData) {
    var handleData = {};
    rawData.map(function (item) {  // 遍历原始数据进行分类处理
        if (typeof handleData[item.timestamp] == "undefined") {  // 如果没有该时间戳，就新创建一个
            handleData[item.timestamp] = {"total": 0, "done": 0, "restart": 0, "rollback": 0};  // 初始化分类统计对象
        }
        handleData[item.timestamp][item.step] ++;  // 上线step项 +1
        handleData[item.timestamp]["total"] ++;  // 上线的total项 +1
    });  // end map
    return handleData;  // 将处理过的数据返回
}

// 分离数据供画图
function splitData(jsonObj) {
    var timeData = [];  // 时间数组
    var values = [];  // 上线数据
    for (var timeStamp in jsonObj) {
        timeData.push(timeStamp);  // x轴时间
        values.push(jsonObj[timeStamp]);  // Y轴数据
    }
    return {
        timeData: timeData,
        values: values
    }
}

// 画图
function drawChart(chartID1, chartID2, titleStr) {
    var myChart1 = echarts.init(document.getElementById(chartID1), "shine");  // 默认chartID1是折线图
    var myChart2 = echarts.init(document.getElementById(chartID2), "shine");  // 默认chartID2是柱状图
    myChart1.showLoading();  //显示加载动画
    myChart2.showLoading();  //显示加载动画

    myChart1.setOption({
        title: {
            text: titleStr+"上线统计-折线图"
        },
        tooltip: {  // 提示框
            trigger: 'axis'  //坐标轴触发
        },
        legend: {
            data: ['total', 'done', 'restart', 'rollback']
        },
        toolbox: {  // 工具
            feature: {
                saveAsImage: {}  // 保存图片
            }
        },
        xAxis: {
            data: []
        },
        yAxis: {},
        dataZoom: [
            {
                type: 'slider'
            }
        ],
        series: []
    });

    myChart2.setOption({
        title: {
          text: titleStr+"上线统计-柱状图"
        },
        tooltip: {  // 提示框
            trigger: 'axis'  //坐标轴触发
        },
        legend:{
            data:['done', 'restart', 'rollback']
        },
        toolbox: {  // 工具
          feature: {
              saveAsImage: {}  // 保存图片
          }
        },
        xAxis: {
            data: []
        },
        yAxis: {},
        dataZoom: [
            {
                type: 'slider'
            }
        ],
        series: []
    });

    myChart1.hideLoading();  //隐藏加载图
    myChart2.hideLoading();  //隐藏加载图

    $.getJSON("source.json").done(function (data) {
        var rawData = handleData(data);  // 处理数据
        var dataInfo = splitData(rawData);  // 分拣数据
        console.log(dataInfo);
        var option1 = {
            xAxis: {
                name: "日期",
                nameLocation: "end",
                data: dataInfo.timeData
            },
            yAxis: {
              name: "次数"
            },
            series: [
                {
                    name: "total",
                    type: "line",
                    data: dataInfo.values.map(function (item) {
                        return item["total"];
                    })
                },
                {
                    name: "done",
                    type: "line",
                    data: dataInfo.values.map(function (item) {
                        return item["done"];
                    })
                },
                {
                    name: "restart",
                    type: "line",
                    data: dataInfo.values.map(function (item) {
                        return item["restart"]
                    })
                },
                {
                    name: "rollback",
                    type: "line",
                    data: dataInfo.values.map(function (item) {
                        return item["rollback"]
                    })
                }
            ]
        };
        var option2 = {
            xAxis: {
                name: "日期",
                nameLocation: "end",
                data: dataInfo.timeData
            },
            yAxis: {
              name: "次数"
            },
            series: [
                {
                    name: "done",
                    type: "bar",
                    stack: "总数",
                    data: dataInfo.values.map(function (item) {
                        return item["done"];
                    })
                },
                {
                    name: "restart",
                    type: "bar",
                    stack: "总数",
                    data: dataInfo.values.map(function (item) {
                        return item["restart"]
                    })
                },
                {
                    name: "rollback",
                    type: "bar",
                    stack: "总数",
                    data: dataInfo.values.map(function (item) {
                        return item["rollback"]
                    })
                }
            ]
        };
        myChart1.setOption(option1);  // 设置图表1
        myChart2.setOption(option2);  // 设置图表2

        $(chartID1).resize(function () {
           $(myChart1).resize();  // 根据父DIV自适应大小
        });
        $(chartID2).resize(function () {
            $(myChart2).resize();  // 根据父DIV自适应大小
        });
        echarts.connect([myChart1, myChart2]);  // 将myChat1和myChart2联动
    });
}

// 监控product和module的select变化
function monitorSelect(productSelectID, moduleSelectID) {
    $("#"+productSelectID).change(function () {
        console.log($("#"+productSelectID).val());
        $("#"+productSelectID).attr({disabled: "disabled"});
        // 限制1.5s点击一次，减轻后台压力
        var changeLimit = setTimeout(function () {
            $("#"+productSelectID).removeAttr("disabled");
        }, 1500)
    })
}