/**
 * Created by liwenzhou on 2016/9/6.
 */

//Toast弹窗提醒

function myToast(msgType, msg) {
    if (typeof msg === "undefined") {
        msg = msgType;
        msgType = "success";
    }
    var title = "提示信息";
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "positionClass": "toast-top-center",
        "onclick": null,
        "showDuration": "1000",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    };
    toastr[msgType](msg, title);
}