!function(t){"use strict";var e=function(t){var n=t,r=function(){return n};return{get:r,set:function(t){n=t},clone:function(){return e(r())}}},n=tinymce.util.Tools.resolve("tinymce.PluginManager"),r=tinymce.util.Tools.resolve("tinymce.util.Delay"),o=tinymce.util.Tools.resolve("tinymce.util.LocalStorage"),a=tinymce.util.Tools.resolve("tinymce.util.Tools"),i=function(t,e){var n=t||e,r=/^(\d+)([ms]?)$/.exec(""+n);return(r[2]?{s:1e3,m:6e4}[r[2]]:1)*parseInt(n,10)},u=function(e){var n=e.getParam("autosave_prefix","tinymce-autosave-{path}{query}{hash}-{id}-");return n=(n=(n=(n=n.replace(/\{path\}/g,t.document.location.pathname)).replace(/\{query\}/g,t.document.location.search)).replace(/\{hash\}/g,t.document.location.hash)).replace(/\{id\}/g,e.id)},s=function(t){return t.getParam("autosave_restore_when_empty",!1)},c=function(t,e){var n=t.settings.forced_root_block;return""===(e=a.trim(void 0===e?t.getBody().innerHTML:e))||new RegExp("^<"+n+"[^>]*>(( |&nbsp;|[ \t]|<br[^>]*>)+?|)</"+n+">|<br>$","i").test(e)},f=function(t){var e=parseInt(o.getItem(u(t)+"time"),10)||0;return!((new Date).getTime()-e>function(t){return i(t.settings.autosave_retention,"20m")}(t))||(l(t,!1),!1)},l=function(t,e){var n=u(t);o.removeItem(n+"draft"),o.removeItem(n+"time"),!1!==e&&function(t){t.fire("RemoveDraft")}(t)},m=function(t){var e=u(t);!c(t)&&t.isDirty()&&(o.setItem(e+"draft",t.getContent({format:"raw",no_events:!0})),o.setItem(e+"time",(new Date).getTime().toString()),function(t){t.fire("StoreDraft")}(t))},v=function(t){var e=u(t);f(t)&&(t.setContent(o.getItem(e+"draft"),{format:"raw"}),function(t){t.fire("RestoreDraft")}(t))},d=function(t,e){var n=function(t){return i(t.settings.autosave_interval,"30s")}(t);e.get()||(r.setInterval(function(){t.removed||m(t)},n),e.set(!0))},g=function(t){t.undoManager.transact(function(){v(t),l(t)}),t.focus()};function y(t){for(var e=[],n=1;n<arguments.length;n++)e[n-1]=arguments[n];return function(){for(var n=[],r=0;r<arguments.length;r++)n[r]=arguments[r];var o=e.concat(n);return t.apply(null,o)}}var p=function(t){return{hasDraft:y(f,t),storeDraft:y(m,t),restoreDraft:y(v,t),removeDraft:y(l,t),isEmpty:y(c,t)}},D=tinymce.util.Tools.resolve("tinymce.EditorManager"),h=function(t){t.editorManager.on("BeforeUnload",function(t){var e;a.each(D.get(),function(t){t.plugins.autosave&&t.plugins.autosave.storeDraft(),!e&&t.isDirty()&&function(t){return t.getParam("autosave_ask_before_unload",!0)}(t)&&(e=t.translate("You have unsaved changes are you sure you want to navigate away?"))}),e&&(t.preventDefault(),t.returnValue=e)})},_=function(t,e){return function(e){e.setDisabled(!f(t));var n=function(){return e.setDisabled(!f(t))};return t.on("StoreDraft RestoreDraft RemoveDraft",n),function(){return t.off("StoreDraft RestoreDraft RemoveDraft",n)}}},w=function(t,e){d(t,e),t.ui.registry.addButton("restoredraft",{tooltip:"Restore last draft",icon:"restore-draft",onAction:function(){g(t)},onSetup:_(t)}),t.ui.registry.addMenuItem("restoredraft",{text:"Restore last draft",icon:"restore-draft",onAction:function(){g(t)},onSetup:_(t)})};n.add("autosave",function(t){var n=e(!1);return h(t),w(t,n),t.on("init",function(){s(t)&&t.dom.isEmpty(t.getBody())&&v(t)}),p(t)})}(window);