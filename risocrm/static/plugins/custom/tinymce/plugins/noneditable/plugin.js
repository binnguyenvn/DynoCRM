!function(){"use strict";var t=tinymce.util.Tools.resolve("tinymce.PluginManager"),e=tinymce.util.Tools.resolve("tinymce.util.Tools"),n=function(t){return t.getParam("noneditable_noneditable_class","mceNonEditable")},r=function(t){return t.getParam("noneditable_editable_class","mceEditable")},a=function(t){var e=t.getParam("noneditable_regexp",[]);return e&&e.constructor===RegExp?[e]:e},i=function(t){return function(e){return-1!==(" "+e.attr("class")+" ").indexOf(t)}},o=function(t,e,n){return function(r){var a=arguments,i=a[a.length-2],o=i>0?e.charAt(i-1):"";if('"'===o)return r;if(">"===o){var c=e.lastIndexOf("<",i);if(-1!==c)if(-1!==e.substring(c,i).indexOf('contenteditable="false"'))return r}return'<span class="'+n+'" data-mce-content="'+t.dom.encode(a[0])+'">'+t.dom.encode("string"==typeof a[1]?a[1]:a[0])+"</span>"}},c={setup:function(t){var c,l;c=" "+e.trim(r(t))+" ",l=" "+e.trim(n(t))+" ";var u=i(c),f=i(l),s=a(t);t.on("PreInit",function(){s.length>0&&t.on("BeforeSetContent",function(e){!function(t,e,r){var a=e.length,i=r.content;if("raw"!==r.format){for(;a--;)i=i.replace(e[a],o(t,i,n(t)));r.content=i}}(t,s,e)}),t.parser.addAttributeFilter("class",function(t){for(var e,n=t.length;n--;)e=t[n],u(e)?e.attr("contenteditable","true"):f(e)&&e.attr("contenteditable","false")}),t.serializer.addAttributeFilter("contenteditable",function(t){for(var e,n=t.length;n--;)e=t[n],(u(e)||f(e))&&(s.length>0&&e.attr("data-mce-content")?(e.name="#text",e.type=3,e.raw=!0,e.value=e.attr("data-mce-content")):e.attr("contenteditable",null))})})}};t.add("noneditable",function(t){c.setup(t)})}();