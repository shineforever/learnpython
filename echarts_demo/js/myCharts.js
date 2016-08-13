/**
 * Created by qimi on 2016/8/13.
 */

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

function drawChart(chartID, titleStr) {
    var myChart = echarts.init(document.getElementById(chartID), "shine");
    myChart.showLoading();  //显示加载动画

    myChart.setOption({
        title: {
          text: titleStr
        },
        tooltip: {  // 提示框
            trigger: 'axis'  //坐标轴触发
        },
        legend:{
            data:['total', 'done', 'restart', 'rollback']
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
        series: [{
            name: '上线统计',
            type: 'line',
            data: []
        }]
    });

    myChart.hideLoading();  //隐藏加载图

    $.getJSON("source.json").done(function (data) {
        var rawData = handleData(data);  // 处理数据
        var dataInfo = splitData(rawData);  // 分拣数据
        console.log(dataInfo);
        myChart.setOption({
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
        });
        $("#main").resize(function () {
           $(myChart).resize();
        });
        window.onresize = myChart.resize;
    });
}