/**
 * Copyright (c) 2016 by Jamie Peabody, http://www.mergely.com
 * All rights reserved.
 * Version: 3.4.2 2016-08-13
 */
$(document).ready(function() {
    function a() {
        var a = {};
        return window.location.search.substr(1).split("&").forEach(function(b) {
            if ("" !== b) {
                var c = b.split("=");
                2 === c.length && c[1].search(/^(true|1)$/i) >= 0 ? a[c[0]] = !0 : 2 === c.length && c[1].search(/^(false|0)$/i) >= 0 ? a[c[0]] = !1 : a[c[0]] = c[1] && decodeURIComponent(c[1].replace(/\+/g, " "))
            }
        }),
        {
            get: function(b, c) {
                return a.hasOwnProperty(b) ? a[b] : c
            }
        }
    }
    function f(a) {
        if (!a.length)
            return !1;
        var b = $("#mergely")
          , c = a.find(".find")
          , d = c.find('input[type="text"]')
          , e = a.attr("id").indexOf("-lhs") > 0 ? "lhs" : "rhs"
          , f = b.mergely("options").autoupdate;
        c.slideDown("fast", function() {
            d.focus(),
            b.mergely("options", {
                autoupdate: !1
            }),
            b.mergely("unmarkup")
        }),
        c.find(".find-prev").click(function() {
            b.mergely("search", e, d.val(), "prev")
        }),
        c.find(".find-next").click(function() {
            b.mergely("search", e, d.val(), "next")
        }),
        c.find(".find-close").click(function() {
            c.css("display", "none"),
            b.mergely("options", {
                autoupdate: f
            })
        }),
        d.keydown(function(a) {
            return 13 != a.which && 27 != a.which ? !0 : (27 == a.which && (c.css("display", "none"),
            b.mergely("options", {
                autoupdate: f
            })),
            b.mergely("search", e, d.val()),
            !1)
        })
    }
    function u(a) {
        if ("file-new" == a)
            window.location = "/editor";
        else if ("file-save" == a) {
            var b = g.mergely("diff");
            if (-1 === navigator.userAgent.toLowerCase().indexOf("msie")) {
                "" == key && (key = "".random(8));
                var c = jQuery("<a />", {
                    href: "data:application/stream;base64," + window.btoa(unescape(encodeURIComponent(b))),
                    target: "_blank",
                    text: "clickme",
                    id: key
                });
                c.attr("download", key + ".diff"),
                jQuery("body").append(c);
                var d = $("a#" + key);
                d[0].click(),
                d.remove()
            } else {
                var e = new Blob([b]);
                window.navigator.msSaveOrOpenBlob(e, key + ".diff")
            }
        } else if ("file-share" == a)
            v(g);
        else if ("file-import" == a)
            x(g);
        else if ("edit-left-undo" == a)
            g.mergely("cm", "lhs").getDoc().undo();
        else if ("edit-left-redo" == a)
            g.mergely("cm", "lhs").getDoc().redo();
        else if ("edit-right-undo" == a)
            g.mergely("cm", "rhs").getDoc().undo();
        else if ("edit-right-redo" == a)
            g.mergely("cm", "rhs").getDoc().redo();
        else if ("edit-left-find" == a)
            f(g.find("#mergely-editor-lhs"));
        else if ("edit-left-merge-right" == a)
            g.mergely("mergeCurrentChange", "rhs");
        else if ("edit-left-merge-right-file" == a)
            g.mergely("merge", "rhs");
        else if (["edit-left-readonly", "edit-right-readonly", "options-autodiff", "options-sidebars", "options-swapmargin", "options-viewport", "options-ignorews", "options-wrap", "options-linenumbers"].indexOf(a) >= 0)
            s[a].set(!s[a].get()),
            h.wickedmenu("update", a);
        else if ("edit-left-clear" == a)
            g.mergely("clear", "lhs");
        else if ("edit-right-find" == a)
            f(g.find("#mergely-editor-rhs"));
        else if ("edit-right-merge-left" == a)
            g.mergely("mergeCurrentChange", "lhs");
        else if ("edit-right-merge-left-file" == a)
            g.mergely("merge", "lhs");
        else if ("edit-right-clear" == a)
            g.mergely("clear", "rhs");
        else if ("options-colors" == a)
            y(g);
        else if ("view-swap" == a)
            g.mergely("swap");
        else if ("view-refresh" == a)
            g.mergely("update");
        else if ("view-change-next" == a)
            g.mergely("scrollToDiff", "next");
        else if ("view-change-prev" == a)
            g.mergely("scrollToDiff", "prev");
        else if ("view-clear" == a)
            g.mergely("unmarkup");
        else if (0 == a.indexOf("examples-")) {
            var i = {
                test1: {
                    lhs: "one\ntwo\nthree",
                    rhs: "two\nthree"
                },
                test2: {
                    lhs: "two\nthree",
                    rhs: "one\ntwo\nthree"
                },
                test3: {
                    lhs: "one\nthree",
                    rhs: "one\ntwo\nthree"
                },
                test4: {
                    lhs: "one\ntwo\nthree",
                    rhs: "one\nthree"
                },
                test5: {
                    lhs: "to bee, or not to be",
                    rhs: "to be, or not to bee"
                },
                test6: {
                    lhs: "to be, or not to be z",
                    rhs: "to be, to be"
                },
                test7: {
                    lhs: "remained, & to assume",
                    rhs: "and to assume"
                },
                test8: {
                    lhs: "to be, or not to be",
                    rhs: "to  be,  or  not  to  be"
                }
            }
              , j = a.split("examples-")[1];
            g.mergely("lhs", i[j].lhs),
            g.mergely("rhs", i[j].rhs)
        }
        return !1
    }
    function v(a) {
        function d(a, d) {
            $.ajax({
                type: "POST",
                async: !0,
                dataType: "text",
                url: "/ajax/handle_file.php",
                data: {
                    key: key,
                    name: a,
                    content: d
                },
                success: function(a) {
                    if (++c,
                    2 == c) {
                        var d = "/ajax/handle_save.php?key=" + key;
                        b && (d += "&nkey=" + "".random(8)),
                        $.ajax({
                            type: "GET",
                            async: !1,
                            dataType: "text",
                            url: d,
                            success: function(a) {
                                a.length && (window.location.href = "/" + $.trim(a) + "/")
                            },
                            error: function(a, b, c) {}
                        })
                    }
                },
                error: function(a, b, c) {
                    alert(c)
                }
            })
        }
        function e() {
            var b = a.mergely("get", "lhs")
              , c = a.mergely("get", "rhs");
            d("lhs", b),
            d("rhs", c)
        }
        var b = "fork" == $(this).attr("id");
        "" == key && (key = "".random(8));
        var c = 0;
        $("#dialog-confirm").dialog({
            resizable: !1,
            width: 350,
            modal: !0,
            buttons: {
                "Save for Sharing": function() {
                    $(this).dialog("close"),
                    e()
                },
                Cancel: function() {
                    $(this).dialog("close")
                }
            }
        })
    }
    function w(a, b, c) {
        $.ajax({
            type: "GET",
            dataType: "text",
            data: {
                url: c
            },
            url: "/ajax/handle_crossdomain.php",
            contentType: "text/plain",
            success: function(c) {
                a.mergely(b, c)
            },
            error: function(a, b, c) {
                console.error("error", a, b, c)
            }
        })
    }
    function x(a) {
        function b(a, b) {
            function f(a, b) {
                e.trigger(a, b)
            }
            var c = a.files[0]
              , d = new FileReader
              , e = $(a);
            d.onloadstart = function(a) {
                f("start")
            }
            ,
            d.onprogress = function(a) {
                f("progress", a)
            }
            ,
            d.onload = function(a) {
                f("loaded", a.target.result)
            }
            ,
            d.onerror = function(a) {
                alert(a.target.error.name)
            }
            ;
            try {
                d.readAsText(c, "UTF-8")
            } catch (g) {
                console.error(g),
                alert(g)
            }
        }
        var c = {};
        $("#file-lhs, #file-rhs").change(function(a) {
            var d = new RegExp(".*[\\\\/](.*)$")
              , e = d.exec($(this).val())
              , f = e ? e[1] : "unknown"
              , g = $("#" + a.target.id + "-progress");
            b(a.target),
            $(a.target).bind("start", function(b) {
                $(a.target).css("display", "none"),
                g.css("display", "inline-block")
            }),
            $(a.target).bind("progress", function(a, b) {
                var c = b.loaded / b.total * 100;
                g.find("> .progress-label").text(c + "%"),
                g.progressbar("value", c)
            }),
            $(a.target).bind("loaded", function(b, d) {
                g.progressbar("value", 100),
                g.find("> .progress-label").text(f),
                c[a.target.id] = d
            })
        }),
        $("#file-lhs-progress").progressbar({
            value: 0
        }),
        $("#file-rhs-progress").progressbar({
            value: 0
        }),
        $("#dialog-upload .tabs").tabs(),
        $("#dialog-upload").dialog({
            dialogClass: "no-title",
            resizable: !1,
            width: "450px",
            modal: !0,
            buttons: {
                Import: function() {
                    $(this).dialog("close");
                    var b = {
                        lhs: $("#url-lhs").val(),
                        rhs: $("#url-rhs").val()
                    };
                    for (var d in b) {
                        var e = b[d];
                        e && w(a, d, e)
                    }
                    c.hasOwnProperty("file-lhs") && a.mergely("lhs", c["file-lhs"]),
                    c.hasOwnProperty("file-rhs") && a.mergely("rhs", c["file-rhs"])
                },
                Cancel: function() {
                    $(this).dialog("close")
                }
            }
        })
    }
    function y(a) {
        var b = $('<span style="display:none" class="mergely ch d lhs start end">C</span>')
          , c = $('<span style="display:none" class="mergely bg a rhs start end">C</span>')
          , d = $('<span style="display:none" class="mergely c rhs start end">C</span>');
        $("body").append(b),
        $("body").append(c),
        $("body").append(d);
        var e = {
            "c-border": {
                id: "#c-border",
                getColor: function() {
                    return d.css("border-top-color")
                },
                setColor: function(a) {
                    $("#" + this.id).val(a)
                }
            },
            "c-bg": {
                id: "#c-bg",
                getColor: function() {
                    return d.css("background-color")
                },
                setColor: function(a) {
                    $("#" + this.id).val(a)
                }
            },
            "a-border": {
                id: "#a-border",
                getColor: function() {
                    return c.css("border-top-color")
                },
                setColor: function(a) {
                    $("#" + this.id).val(a)
                }
            },
            "a-bg": {
                id: "#a-bg",
                getColor: function() {
                    return c.css("background-color")
                },
                setColor: function(a) {
                    $("#" + this.id).val(a)
                }
            },
            "d-border": {
                id: "#d-border",
                getColor: function() {
                    return b.css("border-top-color")
                },
                setColor: function(a) {
                    $("#" + this.id).val(a)
                }
            },
            "d-bg": {
                id: "#d-bg",
                getColor: function() {
                    return b.css("background-color")
                },
                setColor: function(a) {
                    $("#" + this.id).val(a)
                }
            }
        };
        $.each(e, function(a, b) {
            $(b.id).val(b.getColor())
        });
        var f = $.farbtastic("#picker");
        $(".colorwell").each(function() {
            f.linkTo(this)
        }).focus(function() {
            var a = $(this);
            f.linkTo(this);
            var b = e[a.attr("id")];
            f.setColor(b.getColor())
        }),
        $("#dialog-colors").dialog({
            width: 490,
            modal: !0,
            buttons: {
                Apply: function() {
                    var a = $("#c-border").val()
                      , b = $("#a-border").val()
                      , c = $("#d-border").val()
                      , d = $("#a-bg").val()
                      , e = $("#d-bg").val()
                      , f = $("#c-bg").val()
                      , g = z(a, f, b, d, c, e);
                    B(g, a, f, b, d, c, e, !0)
                },
                Reset: function() {},
                Close: function() {
                    $(this).dialog("close")
                }
            }
        })
    }
    function z(a, b, c, d, e, f) {
        var g = ".mergely.a.rhs.start{border-top-color:" + c + ";}\n			.mergely.a.lhs.start.end,\n			.mergely.a.rhs.end{border-bottom-color:" + c + ";}\n			.mergely.a.rhs{background-color:" + d + ";}\n			.mergely.d.lhs{background-color:" + f + ";}\n			.mergely.d.lhs.end,\n			.mergely.d.rhs.start.end{border-bottom-color:" + e + ";}\n			.mergely.d.rhs.start.end.first{border-top-color:" + e + ";}\n			.mergely.d.lhs.start{border-top-color:" + e + ";}\n			.mergely.c.lhs,\n			.mergely.c.rhs{background-color:" + b + ";}\n			.mergely.c.lhs.start,\n			.mergely.c.rhs.start{border-top-color:" + a + ";}\n			.mergely.c.lhs.end,\n			.mergely.c.rhs.end{border-bottom-color:" + a + ";}\n			.mergely.ch.a.rhs{background-color:" + d + ";}\n			.mergely.ch.d.lhs{background-color:" + f + ";color: #888;}";
        return g
    }
    function A(a) {
        var c = "#" + b.get("cb", o.cb)
          , d = "#" + b.get("cg", o.cg)
          , e = "#" + b.get("ab", o.ab)
          , f = "#" + b.get("ag", o.ag)
          , g = "#" + b.get("db", o.db)
          , h = "#" + b.get("dg", o.dg);
        B(z(c, d, e, f, g, h), c, d, e, f, g, h, a)
    }
    function B(a, b, c, d, e, f, h, i) {
        $('<style type="text/css">' + a + "</style>").appendTo("head"),
        g.mergely("options", {
            fgcolor: {
                a: d,
                c: b,
                d: f
            }
        });
        var j = D("cb", b.replace(/#/g, ""), o.cb);
        j = D("cg", c.replace(/#/g, ""), o.cg, j),
        j = D("ab", d.replace(/#/g, ""), o.ab, j),
        j = D("ag", e.replace(/#/g, ""), o.ag, j),
        j = D("db", f.replace(/#/g, ""), o.db, j),
        j = D("dg", h.replace(/#/g, ""), o.dg, j),
        i && C(j)
    }
    function C(a) {
        var b = [location.protocol, "//", location.host, location.pathname].join("");
        window.history.pushState({}, null , b + a)
    }
    function D(a, b, c, d) {
        d = d || document.location.search;
        var e = d.replace(/^\?/, "").split(/&/)
          , f = !1;
        for (var g in e) {
            if (e[g].startsWith(a + "=")) {
                f = !0,
                b === c ? e.splice(g, 1) : e[g] = a + "=" + b;
                break
            }
            if (0 === e[g].length) {
                e.splice(g, 1);
                break
            }
        }
        return f || e.push(a + "=" + b),
        e.length ? "?" + e.join("&") : ""
    }
    var b = a();
    if (b.get("test", !1)) {
        for (var c = $("<li>Tests</li>"), d = $("<ul>"), e = 1; 8 >= e; ++e)
            d.append($('<li id="examples-test' + e + '">Test ' + e + "</li>"));
        c.append(d),
        $("#main-menu").append(c)
    }
    $(document).keydown(function(a) {
        if ("f" != String.fromCharCode(a.which).toLowerCase() || !a.ctrlKey)
            return !0;
        a.preventDefault();
        var b = window.getSelection().getRangeAt(0)
          , c = $(b.commonAncestorContainer).parents(".mergely-column");
        return f(c),
        !1
    }),
    String.prototype.random = function(a) {
        for (var b = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz", c = "", d = 0; a > d; d++) {
            var e = Math.floor(Math.random() * b.length);
            c += b.substring(e, e + 1)
        }
        return c
    }
    ,
    $("body").css("visibility", "");
    var g = $("#mergely")
      , h = $("#main-menu")
      , i = $("#toolbar");
    if (g.mergely({
        width: "auto",
        height: "auto",
        cmsettings: {
            lineNumbers: !0,
            readOnly: isSample
        }
    }),
    b.get("lhs", null )) {
        var j = b.get("lhs");
        w(g, "lhs", j)
    }
    if (b.get("rhs", null )) {
        var j = b.get("rhs");
        w(g, "rhs", j)
    }
    var k = {}
      , l = {
        au: "autoupdate",
        ws: "ignorews",
        sb: "sidebar",
        vp: "viewport",
        wl: "wrap_lines",
        ln: "line_numbers"
    }
      , m = !1;
    for (var n in l)
        l.hasOwnProperty(n) && null !== b.get(n, null ) && (k[l[n]] = b.get(n),
        m = !0);
    null !== b.get("rm", null ) && (k.rhs_margin = b.get("rm") ? "left" : "right"),
    m && g.mergely("options", k);
    var o = {
        cb: "cccccc",
        cg: "fafafa",
        ab: "a3d1ff",
        ag: "ddeeff",
        db: "ff7f7f",
        dg: "ffe9e9"
    };
    A(!1),
    window.addEventListener("popstate", function(c) {
        c.state && (b = a(),
        A(!1))
    }),
    8 == key.length && $.when($.ajax({
        type: "GET",
        async: !0,
        dataType: "text",
        data: {
            key: key,
            name: "lhs"
        },
        url: "/ajax/handle_get.php",
        success: function(a) {
            g.mergely("lhs", a)
        },
        error: function(a, b, c) {}
    }), $.ajax({
        type: "GET",
        async: !0,
        dataType: "text",
        data: {
            key: key,
            name: "rhs"
        },
        url: "/ajax/handle_get.php",
        success: function(a) {
            g.mergely("rhs", a)
        },
        error: function(a, b, c) {}
    })).done(function() {
        var a = window.location.hash.substring(1);
        if (a) {
            var b = a.match(/([lr]hs)([0-9]+)/);
            b && 3 == b.length && (console.log(b),
            g.mergely("scrollTo", b[1], parseInt(b[2], 10)))
        }
    });
    var p = $(".find")
      , q = p.clone().attr("id", "mergely-editor-lhs-find")
      , r = p.clone().attr("id", "mergely-editor-rhs-find");
    $("#mergely-editor-lhs").append(q),
    $("#mergely-editor-rhs").append(r),
    p.remove();
    var s = {
        "options-autodiff": {
            get: function() {
                return g.mergely("options").autoupdate
            },
            set: function(a) {
                var b = !g.mergely("options").autoupdate;
                g.mergely("options", {
                    autoupdate: b
                });
                var c = D("au", b ? 1 : 0, 1);
                C(c)
            }
        },
        "options-ignorews": {
            get: function() {
                return g.mergely("options").ignorews
            },
            set: function(a) {
                var b = !g.mergely("options").ignorews;
                g.mergely("options", {
                    ignorews: b
                });
                var c = D("ws", b ? 1 : 0, 0);
                C(c)
            }
        },
        "options-sidebars": {
            get: function() {
                return console.log("sidebar", this),
                g.mergely("options").sidebar
            },
            set: function(a) {
                var b = !g.mergely("options").sidebar;
                g.mergely("options", {
                    sidebar: b
                });
                var c = D("sb", b ? 1 : 0, 1);
                C(c)
            }
        },
        "options-viewport": {
            get: function() {
                return console.log("viewport", this),
                g.mergely("options").viewport
            },
            set: function(a) {
                var b = !g.mergely("options").viewport;
                g.mergely("options", {
                    viewport: b
                });
                var c = D("vp", b ? 1 : 0, 0);
                C(c)
            }
        },
        "options-swapmargin": {
            get: function() {
                return "left" == g.mergely("options").rhs_margin
            },
            set: function(a) {
                var b = "left" == g.mergely("options").rhs_margin ? "right" : "left";
                g.mergely("options", {
                    rhs_margin: b
                });
                var c = D("rm", "left" == b ? 1 : 0, 0);
                C(c)
            }
        },
        "options-linenumbers": {
            get: function() {
                return console.log("wrap", this),
                g.mergely("options").line_numbers
            },
            set: function(a) {
                var b = !g.mergely("options").line_numbers;
                g.mergely("options", {
                    line_numbers: b
                });
                var c = D("ln", b ? 1 : 0, 1);
                C(c)
            }
        },
        "options-wrap": {
            get: function() {
                return console.log("wrap", this),
                g.mergely("options").wrap_lines
            },
            set: function(a) {
                var b = !g.mergely("options").wrap_lines;
                g.mergely("options", {
                    wrap_lines: b
                });
                var c = D("wl", b ? 1 : 0, 0);
                C(c)
            }
        },
        "edit-left-readonly": {
            get: function() {
                return g.mergely("cm", "lhs").getOption("readOnly")
            },
            set: function(a) {
                g.mergely("cm", "lhs").setOption("readOnly", a)
            }
        },
        "edit-right-readonly": {
            get: function() {
                return g.mergely("cm", "rhs").getOption("readOnly")
            },
            set: function(a) {
                g.mergely("cm", "rhs").setOption("readOnly", a)
            }
        }
    }
      , t = {
        hasIcon: function(a) {
            return s.hasOwnProperty(a)
        },
        getIcon: function(a) {
            return s[a].get() ? "icon-check" : void 0
        }
    };
    h.wickedmenu(t).bind("selected", function(a, b) {
        return u(b)
    }),
    i.wickedtoolbar({}).bind("selected", function(a, b) {
        return b ? u(b.replace(/^tb-/, "")) : !1
    }),
    i.find("li[title]").tipsy({
        opacity: 1
    }),
    h.find("li[title]").tipsy({
        opacity: 1,
        delayIn: 1e3,
        gravity: "w"
    })
});
