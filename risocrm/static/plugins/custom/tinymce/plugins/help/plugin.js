!function(){"use strict";var e=function(t){var n=t,o=function(){return n};return{get:o,set:function(e){n=e},clone:function(){return e(o())}}},t=tinymce.util.Tools.resolve("tinymce.PluginManager"),n=function(e){return{addTab:function(t){var n=e.get();n[t.name]=t,e.set(n)}}},o={register:function(e,t){e.addCommand("mceHelp",t)}},a={register:function(e,t){e.ui.registry.addButton("help",{icon:"help",tooltip:"Help",onAction:t}),e.ui.registry.addMenuItem("help",{text:"Help",icon:"help",shortcut:"Alt+0",onAction:t})}},r=function(){return(r=Object.assign||function(e){for(var t,n=1,o=arguments.length;n<o;n++)for(var a in t=arguments[n])Object.prototype.hasOwnProperty.call(t,a)&&(e[a]=t[a]);return e}).apply(this,arguments)},i=function(){},s=function(e){return function(){return e}};function c(e){for(var t=[],n=1;n<arguments.length;n++)t[n-1]=arguments[n];return function(){for(var n=[],o=0;o<arguments.length;o++)n[o]=arguments[o];var a=t.concat(n);return e.apply(null,a)}}var l,u,h,m,p,d=s(!1),f=s(!0),g=function(){return b},b=(l=function(e){return e.isNone()},m={fold:function(e,t){return e()},is:d,isSome:d,isNone:f,getOr:h=function(e){return e},getOrThunk:u=function(e){return e()},getOrDie:function(e){throw new Error(e||"error: getOrDie called on none.")},getOrNull:s(null),getOrUndefined:s(void 0),or:h,orThunk:u,map:g,each:i,bind:g,exists:d,forall:f,filter:g,equals:l,equals_:l,toArray:function(){return[]},toString:s("none()")},Object.freeze&&Object.freeze(m),m),y=function(e){var t=s(e),n=function(){return a},o=function(t){return t(e)},a={fold:function(t,n){return n(e)},is:function(t){return e===t},isSome:f,isNone:d,getOr:t,getOrThunk:t,getOrDie:t,getOrNull:t,getOrUndefined:t,or:n,orThunk:n,map:function(t){return y(t(e))},each:function(t){t(e)},bind:o,exists:o,forall:o,filter:function(t){return t(e)?a:b},toArray:function(){return[e]},toString:function(){return"some("+e+")"},equals:function(t){return t.is(e)},equals_:function(t,n){return t.fold(d,function(t){return n(e,t)})}};return a},k={some:y,none:g,from:function(e){return null==e?b:y(e)}},v=(p="function",function(e){return function(e){if(null===e)return"null";var t=typeof e;return"object"===t&&(Array.prototype.isPrototypeOf(e)||e.constructor&&"Array"===e.constructor.name)?"array":"object"===t&&(String.prototype.isPrototypeOf(e)||e.constructor&&"String"===e.constructor.name)?"string":t}(e)===p}),w=Array.prototype.slice,A=Array.prototype.indexOf,C=function(e,t){return A.call(e,t)},T=function(e,t){return C(e,t)>-1},x=function(e,t){for(var n=e.length,o=new Array(n),a=0;a<n;a++){var r=e[a];o[a]=t(r,a)}return o},P=(v(Array.from)&&Array.from,Object.keys),M=Object.hasOwnProperty,O=function(e,t){return M.call(e,t)},F=[{shortcuts:["Meta + B"],action:"Bold"},{shortcuts:["Meta + I"],action:"Italic"},{shortcuts:["Meta + U"],action:"Underline"},{shortcuts:["Meta + A"],action:"Select all"},{shortcuts:["Meta + Y","Meta + Shift + Z"],action:"Redo"},{shortcuts:["Meta + Z"],action:"Undo"},{shortcuts:["Access + 1"],action:"Header 1"},{shortcuts:["Access + 2"],action:"Header 2"},{shortcuts:["Access + 3"],action:"Header 3"},{shortcuts:["Access + 4"],action:"Header 4"},{shortcuts:["Access + 5"],action:"Header 5"},{shortcuts:["Access + 6"],action:"Header 6"},{shortcuts:["Access + 7"],action:"Paragraph"},{shortcuts:["Access + 8"],action:"Div"},{shortcuts:["Access + 9"],action:"Address"},{shortcuts:["Alt + 0"],action:"Open help dialog"},{shortcuts:["Alt + F9"],action:"Focus to menubar"},{shortcuts:["Alt + F10"],action:"Focus to toolbar"},{shortcuts:["Alt + F11"],action:"Focus to element path"},{shortcuts:["Ctrl + F9"],action:"Focus to contextual toolbar"},{shortcuts:["Shift + Enter"],action:"Open popup menu for split buttons"},{shortcuts:["Meta + K"],action:"Insert link (if link plugin activated)"},{shortcuts:["Meta + S"],action:"Save (if save plugin activated)"},{shortcuts:["Meta + F"],action:"Find (if searchreplace plugin activated)"},{shortcuts:["Meta + Shift + F"],action:"Switch to or from fullscreen mode"}],S=tinymce.util.Tools.resolve("tinymce.Env"),E=function(e){var t=S.mac?{alt:"&#x2325;",ctrl:"&#x2303;",shift:"&#x21E7;",meta:"&#x2318;",access:"&#x2303;&#x2325;"}:{meta:"Ctrl ",access:"Shift + Alt "},n=e.split("+"),o=x(n,function(e){var n=e.toLowerCase().trim();return O(t,n)?t[n]:e});return S.mac?o.join("").replace(/\s/,""):o.join("+")},I=function(){return{name:"shortcuts",title:"Handy Shortcuts",items:[{type:"table",header:["Action","Shortcut"],cells:x(F,function(e){var t=x(e.shortcuts,E).join(" or ");return[e.action,t]})}]}},_=function(e,t){return e.replace(/\$\{([^{}]*)\}/g,function(e,n){var o,a=t[n];return"string"===(o=typeof a)||"number"===o?a.toString():e})},j=tinymce.util.Tools.resolve("tinymce.util.I18n"),H=[{key:"advlist",name:"Advanced List"},{key:"anchor",name:"Anchor"},{key:"autolink",name:"Autolink"},{key:"autoresize",name:"Autoresize"},{key:"autosave",name:"Autosave"},{key:"bbcode",name:"BBCode"},{key:"charmap",name:"Character Map"},{key:"code",name:"Code"},{key:"codesample",name:"Code Sample"},{key:"colorpicker",name:"Color Picker"},{key:"directionality",name:"Directionality"},{key:"emoticons",name:"Emoticons"},{key:"fullpage",name:"Full Page"},{key:"fullscreen",name:"Full Screen"},{key:"help",name:"Help"},{key:"hr",name:"Horizontal Rule"},{key:"image",name:"Image"},{key:"imagetools",name:"Image Tools"},{key:"importcss",name:"Import CSS"},{key:"insertdatetime",name:"Insert Date/Time"},{key:"legacyoutput",name:"Legacy Output"},{key:"link",name:"Link"},{key:"lists",name:"Lists"},{key:"media",name:"Media"},{key:"nonbreaking",name:"Nonbreaking"},{key:"noneditable",name:"Noneditable"},{key:"pagebreak",name:"Page Break"},{key:"paste",name:"Paste"},{key:"preview",name:"Preview"},{key:"print",name:"Print"},{key:"save",name:"Save"},{key:"searchreplace",name:"Search and Replace"},{key:"spellchecker",name:"Spell Checker"},{key:"tabfocus",name:"Tab Focus"},{key:"table",name:"Table"},{key:"template",name:"Template"},{key:"textcolor",name:"Text Color"},{key:"textpattern",name:"Text Pattern"},{key:"toc",name:"Table of Contents"},{key:"visualblocks",name:"Visual Blocks"},{key:"visualchars",name:"Visual Characters"},{key:"wordcount",name:"Word Count"},{key:"advcode",name:"Advanced Code Editor*"},{key:"formatpainter",name:"Format Painter*"},{key:"powerpaste",name:"PowerPaste*"},{key:"tinydrive",name:"Tiny Drive*"},{key:"tinymcespellchecker",name:"Spell Checker Pro*"},{key:"a11ychecker",name:"Accessibility Checker*"},{key:"linkchecker",name:"Link Checker*"},{key:"mentions",name:"Mentions*"},{key:"mediaembed",name:"Enhanced Media Embed*"},{key:"checklist",name:"Checklist*"},{key:"casechange",name:"Case Change*"},{key:"permanentpen",name:"Permanent Pen*"},{key:"pageembed",name:"Page Embed*"},{key:"tinycomments",name:"Tiny Comments*"},{key:"advtable",name:"Advanced Tables*"},{key:"autocorrect",name:"Autocorrect*"}],U=function(e){var t,n=c(_,'<a href="${url}" target="_blank" rel="noopener">${name}</a>'),o=function(e,t){return function(e,t){for(var n=0,o=e.length;n<o;n++){var a=e[n];if(t(a,n))return k.some(a)}return k.none()}(H,function(e){return e.key===t}).fold(function(){var o=e.plugins[t].getMetadata;return"function"==typeof o?n(o()):t},function(e){return n({name:e.name,url:"https://www.tiny.cloud/docs/plugins/"+e.key})})},a=function(e){var t=function(e){var t,n=P(e.plugins);return void 0===e.settings.forced_plugins?n:function(e,t){for(var n=[],o=0,a=e.length;o<a;o++){var r=e[o];t(r,o)&&n.push(r)}return n}(n,(t=c(T,e.settings.forced_plugins),function(){for(var e=[],n=0;n<arguments.length;n++)e[n]=arguments[n];return!t.apply(null,e)}))}(e),n=x(t,function(t){return"<li>"+o(e,t)+"</li>"}),a=n.length,r=n.join("");return"<p><b>"+j.translate(["Plugins installed ({0}):",a])+"</b></p><ul>"+r+"</ul>"};return{name:"plugins",title:"Plugins",items:[{type:"htmlpanel",presets:"document",html:[function(e){return null==e?"":'<div data-mce-tabstop="1" tabindex="-1">'+a(e)+"</div>"}(e),(t=x(["Accessibility Checker","Advanced Code Editor","Advanced Tables","Case Change","Checklist","Tiny Comments","Tiny Drive","Enhanced Media Embed","Format Painter","Link Checker","Mentions","MoxieManager","Page Embed","Permanent Pen","PowerPaste","Spell Checker Pro"],function(e){return"<li>"+j.translate(e)+"</li>"}).join(""),'<div data-mce-tabstop="1" tabindex="-1"><p><b>'+j.translate("Premium plugins:")+"</b></p><ul>"+t+'<li style="list-style: none; margin-top: 1em;"><a href="https://www.tiny.cloud/pricing/?utm_campaign=editor_referral&utm_medium=help_dialog&utm_source=tinymce" target="_blank">'+j.translate("Learn more...")+"</a></li></ul></div>")].join("")}]}},W=tinymce.util.Tools.resolve("tinymce.EditorManager"),D=function(){var e,t,n='<a href="https://www.tinymce.com/docs/changelog/?utm_campaign=editor_referral&utm_medium=help_dialog&utm_source=tinymce" target="_blank">TinyMCE '+(e=W.majorVersion,t=W.minorVersion,0===e.indexOf("@")?"X.X.X":e+"."+t)+"</a>";return{name:"versions",title:"Version",items:[{type:"htmlpanel",html:"<p>"+j.translate(["You are using {0}",n])+"</p>",presets:"document"}]}},N=function(){return{name:"keyboardnav",title:"Keyboard Navigation",items:[{type:"htmlpanel",html:"<h1>Editor UI keyboard navigation</h1>\n\n<h2>Activating keyboard navigation</h2>\n\n<p>The sections of the outer UI of the editor - the menubar, toolbar, sidebar and footer - are all keyboard navigable. As such, there are multiple ways to activate keyboard navigation:</p>\n<ul>\n  <li>Focus the menubar: Alt + F9 (Windows) or &#x2325;F9 (MacOS)</li>\n  <li>Focus the toolbar: Alt + F10 (Windows) or &#x2325;F10 (MacOS)</li>\n  <li>Focus the footer: Alt + F11 (Windows) or &#x2325;F11 (MacOS)</li>\n</ul>\n\n<p>Focusing the menubar or toolbar will start keyboard navigation at the first item in the menubar or toolbar, which will be highlighted with a gray background. Focusing the footer will start keyboard navigation at the first item in the element path, which will be highlighted with an underline. </p>\n\n<h2>Moving between UI sections</h2>\n\n<p>When keyboard navigation is active, pressing tab will move the focus to the next major section of the UI, where applicable. These sections are:</p>\n<ul>\n  <li>the menubar</li>\n  <li>each group of the toolbar </li>\n  <li>the sidebar</li>\n  <li>the element path in the footer </li>\n  <li>the wordcount toggle button in the footer </li>\n  <li>the branding link in the footer </li>\n</ul>\n\n<p>Pressing shift + tab will move backwards through the same sections, except when moving from the footer to the toolbar. Focusing the element path then pressing shift + tab will move focus to the first toolbar group, not the last.</p>\n\n<h2>Moving within UI sections</h2>\n\n<p>Keyboard navigation within UI sections can usually be achieved using the left and right arrow keys. This includes:</p>\n<ul>\n  <li>moving between menus in the menubar</li>\n  <li>moving between buttons in a toolbar group</li>\n  <li>moving between items in the element path</li>\n</ul>\n\n<p>In all these UI sections, keyboard navigation will cycle within the section. For example, focusing the last button in a toolbar group then pressing right arrow will move focus to the first item in the same toolbar group. </p>\n\n<h1>Executing buttons</h1>\n\n<p>To execute a button, navigate the selection to the desired button and hit space or enter.</p>\n\n<h1>Opening, navigating and closing menus</h1>\n\n<p>When focusing a menubar button or a toolbar button with a menu, pressing space, enter or down arrow will open the menu. When the menu opens the first item will be selected. To move up or down the menu, press the up or down arrow key respectively. This is the same for submenus, which can also be opened and closed using the left and right arrow keys.</p>\n\n<p>To close any active menu, hit the escape key. When a menu is closed the selection will be restored to its previous selection. This also works for closing submenus.</p>\n\n<h1>Context toolbars and menus</h1>\n\n<p>To focus an open context toolbar such as the table context toolbar, press Ctrl + F9 (Windows) or &#x2303;F9 (MacOS).</p>\n\n<p>Context toolbar navigation is the same as toolbar navigation, and context menu navigation is the same as standard menu navigation.</p>\n\n<h1>Dialog navigation</h1>\n\n<p>There are two types of dialog UIs in TinyMCE: tabbed dialogs and non-tabbed dialogs.</p>\n\n<p>When a non-tabbed dialog is opened, the first interactive component in the dialog will be focused. Users can navigate between interactive components by pressing tab. This includes any footer buttons. Navigation will cycle back to the first dialog component if tab is pressed while focusing the last component in the dialog. Pressing shift + tab will navigate backwards.</p>\n\n<p>When a tabbed dialog is opened, the first button in the tab menu is focused. Pressing tab will navigate to the first interactive component in that tab, and will cycle through the tab’s components, the footer buttons, then back to the tab button. To switch to another tab, focus the tab button for the current tab, then use the arrow keys to cycle through the tab buttons.</p>"}]}},L=function(e){var t,n=P(e);return(-1===(t=C(n,"versions"))?k.none():k.some(t)).each(function(e){n.splice(e,1),n.push("versions")}),{tabs:e,names:n}},B=function(e,t){var n,o=I(),a=N(),i=U(e),s=D(),c=r(((n={})[o.name]=o,n[a.name]=a,n[i.name]=i,n[s.name]=s,n),t.get());return function(e){return k.from(e.getParam("help_tabs"))}(e).fold(function(){return L(c)},function(e){return function(e,t){var n={},o=x(e,function(e){return"string"==typeof e?(O(t,e)&&(n[e]=t[e]),e):(n[e.name]=e,e.name)});return{tabs:n,names:o}}(e,c)})},z=function(e,t){return function(){var n=B(e,t),o=n.tabs,a=n.names,r={type:"tabpanel",tabs:function(e){for(var t=[],n=function(e){t.push(e)},o=0;o<e.length;o++)e[o].each(n);return t}(x(a,function(e){return O(t=o,n=e)?k.from(t[n]):k.none();var t,n}))};e.windowManager.open({title:"Help",size:"medium",body:r,buttons:[{type:"cancel",name:"close",text:"Close",primary:!0}],initialData:{}})}};t.add("help",function(t){var r=e({}),i=n(r),s=z(t,r);return a.register(t,s),o.register(t,s),t.shortcuts.add("Alt+0","Open help dialog","mceHelp"),i})}();