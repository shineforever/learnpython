/**
 * Created by qimi on 2016/8/19.
 */

// 自定义检查JS

$("#test_form").validate({
    rules: {
        module_select: "required",
        mode_select: "required",
        code1: {
            required: true,
            minlength: 5
        },
        data1: {
            required: true,
            minlength: 5
        },
        data2: {
            required: true,
            minlength: 5
        },
        radio_test: "required"
    },
    messages: {
        module_select: "请选择要上线的模块",
        mode_select: "请选择上线的模式",
        code1: {
            required: "请填写代码的路径",
            minlength: "代码地址不正确"
        },
        data1: {
            required: "请填写数据1",
            minlength: "请填写正确的数据1地址"
        },
        data2: {
            required: "请填写数据2",
            minlength: "请填写正确的数据2地址"
        },
        radio_test: {
            required: "请选择上线方式"
        }
    }
});
