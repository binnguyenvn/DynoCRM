!function(){"use strict";var e=tinymce.util.Tools.resolve("tinymce.PluginManager"),n=tinymce.util.Tools.resolve("tinymce.dom.DOMUtils"),t=tinymce.util.Tools.resolve("tinymce.util.Tools"),o=function(e){return e.getParam("save_enablewhendirty",!0)},i=function(e){return!!e.getParam("save_onsavecallback")},a=function(e){return!!e.getParam("save_oncancelcallback")},r=function(e,n){e.notificationManager.open({text:n,type:"error"})},c=function(e){var t;if(t=n.DOM.getParent(e.id,"form"),!o(e)||e.isDirty()){if(e.save(),i(e))return e.execCallback("save_onsavecallback",e),void e.nodeChanged();t?(e.setDirty(!1),t.onsubmit&&!t.onsubmit()||("function"==typeof t.submit?t.submit():r(e,"Error: Form submit field collision.")),e.nodeChanged()):r(e,"Error: No form element found.")}},u=function(e){var n=t.trim(e.startContent);a(e)?e.execCallback("save_oncancelcallback",e):e.resetContent(n)},l={register:function(e){e.addCommand("mceSave",function(){c(e)}),e.addCommand("mceCancel",function(){u(e)})}},s=function(e){return function(n){var t=function(){n.setDisabled(o(e)&&!e.isDirty())};return e.on("NodeChange dirty",t),function(){return e.off("NodeChange dirty",t)}}},d={register:function(e){e.ui.registry.addButton("save",{icon:"save",tooltip:"Save",disabled:!0,onAction:function(){return e.execCommand("mceSave")},onSetup:s(e)}),e.ui.registry.addButton("cancel",{icon:"cancel",tooltip:"Cancel",disabled:!0,onAction:function(){return e.execCommand("mceCancel")},onSetup:s(e)}),e.addShortcut("Meta+S","","mceSave")}};e.add("save",function(e){d.register(e),l.register(e)})}();