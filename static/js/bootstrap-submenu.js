/*!
 * Bootstrap-submenu v2.0.4 (https://vsn4ik.github.io/bootstrap-submenu/)
 * Copyright 2014-2017 Vasily A. (https://github.com/vsn4ik)
 * Licensed under the MIT license
 */

"use strict";
! function(a) {
    "function" == typeof define && define.amd ? define(["jquery"], a) : "object" == typeof exports ? module.exports = a(require("jquery")) : a(jQuery)
}(function(a) {
    function b(b) {
        this.$element = a(b), this.$menu = this.$element.closest(".dropdown-menu"), this.$main = this.$menu.parent(), this.$items = this.$menu.children(".dropdown-submenu"), this.init()
    }

    function c(b) {
        this.$element = a(b), this.$main = this.$element.parent(), this.$menu = this.$main.children(".dropdown-menu"), this.$subs = this.$main.siblings(".dropdown-submenu"), this.$items = this.$menu.children(".dropdown-submenu"), this.init()
    }

    function d(b) {
        this.$element = a(b), this.$main = this.$element.parent(), this.$menu = this.$main.children(".dropdown-menu"), this.$items = this.$menu.children(".dropdown-submenu"), this.init()
    }
    b.prototype = {
        init: function() {
            this.$element.on("keydown", a.proxy(this, "keydown"))
        },
        close: function() {
            this.$main.removeClass("open"), this.$items.trigger("hide.bs.submenu")
        },
        keydown: function(a) {
            27 == a.keyCode && (a.stopPropagation(), this.close(), this.$main.children("a, button").trigger("focus"))
        }
    }, a.extend(c.prototype, b.prototype, {
        init: function() {
            this.$element.on({
                click: a.proxy(this, "click"),
                keydown: a.proxy(this, "keydown")
            }), this.$main.on("hide.bs.submenu", a.proxy(this, "hide"))
        },
        click: function(a) {
            a.preventDefault(), a.stopPropagation(), this.toggle()
        },
        hide: function(a) {
            a.stopPropagation(), this.close()
        },
        open: function() {
            this.$main.addClass("open"), this.$subs.trigger("hide.bs.submenu")
        },
        toggle: function() {
            this.$main.hasClass("open") ? this.close() : this.open()
        },
        keydown: function(b) {
            32 == b.keyCode && b.preventDefault(), a.inArray(b.keyCode, [13, 32]) != -1 && this.toggle()
        }
    }), d.prototype = {
        init: function() {
            this.$menu.off("keydown.bs.dropdown.data-api"), this.$menu.on("keydown", a.proxy(this, "itemKeydown")), this.$menu.find("li > a").each(function() {
                new b(this)
            }), this.$menu.find(".dropdown-submenu > a").each(function() {
                new c(this)
            }), this.$main.on("hidden.bs.dropdown", a.proxy(this, "hidden"))
        },
        hidden: function() {
            this.$items.trigger("hide.bs.submenu")
        },
        itemKeydown: function(b) {
            if (a.inArray(b.keyCode, [38, 40]) != -1) {
                b.preventDefault(), b.stopPropagation();
                var c = this.$menu.find("li:not(.disabled):visible > a"),
                    d = c.index(b.target);
                if (38 == b.keyCode && 0 !== d) d--;
                else {
                    if (40 != b.keyCode || d === c.length - 1) return;
                    d++
                }
                c.eq(d).trigger("focus")
            }
        }
    };
    var e = a.fn.submenupicker;
    return a.fn.submenupicker = function(b) {
        var c = this instanceof a ? this : a(b);
        return c.each(function() {
            var b = a.data(this, "bs.submenu");
            b || (b = new d(this), a.data(this, "bs.submenu", b))
        })
    }, a.fn.submenupicker.Constructor = d, a.fn.submenupicker.noConflict = function() {
        return a.fn.submenupicker = e, this
    }, a.fn.submenupicker
});