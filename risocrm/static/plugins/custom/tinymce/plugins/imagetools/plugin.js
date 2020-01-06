!function(e){"use strict";var n,t,r,o,i=function(e){var n=e,t=function(){return n};return{get:t,set:function(e){n=e},clone:function(){return i(t())}}},u=tinymce.util.Tools.resolve("tinymce.PluginManager"),a=tinymce.util.Tools.resolve("tinymce.util.Tools"),c=function(){},s=function(e){return function(){return e}},f=s(!1),l=s(!0),d=function(){return m},m=(n=function(e){return e.isNone()},o={fold:function(e,n){return e()},is:f,isSome:f,isNone:l,getOr:r=function(e){return e},getOrThunk:t=function(e){return e()},getOrDie:function(e){throw new Error(e||"error: getOrDie called on none.")},getOrNull:s(null),getOrUndefined:s(void 0),or:r,orThunk:t,map:d,each:c,bind:d,exists:f,forall:l,filter:d,equals:n,equals_:n,toArray:function(){return[]},toString:s("none()")},Object.freeze&&Object.freeze(o),o),g=function(e){var n=s(e),t=function(){return o},r=function(n){return n(e)},o={fold:function(n,t){return t(e)},is:function(n){return e===n},isSome:l,isNone:f,getOr:n,getOrThunk:n,getOrDie:n,getOrNull:n,getOrUndefined:n,or:t,orThunk:t,map:function(n){return g(n(e))},each:function(n){n(e)},bind:r,exists:r,forall:r,filter:function(n){return n(e)?o:m},toArray:function(){return[e]},toString:function(){return"some("+e+")"},equals:function(n){return n.is(e)},equals_:function(n,t){return n.fold(f,function(n){return t(e,n)})}};return o},h={some:g,none:d,from:function(e){return null==e?m:g(e)}};function v(n,t){return y(e.document.createElement("canvas"),n,t)}function p(e){var n=v(e.width,e.height);return w(n).drawImage(e,0,0),n}function w(e){return e.getContext("2d")}function y(e,n,t){return e.width=n,e.height=t,e}var b=window.Promise?window.Promise:function(){var n=function(e){if("object"!=typeof this)throw new TypeError("Promises must be constructed via new");if("function"!=typeof e)throw new TypeError("not a function");this._state=null,this._value=null,this._deferreds=[],f(e,r(u,this),r(a,this))},t=n.immediateFn||"function"==typeof window.setImmediate&&window.setImmediate||function(n){e.setTimeout(n,1)};function r(e,n){return function(){return e.apply(n,arguments)}}var o=Array.isArray||function(e){return"[object Array]"===Object.prototype.toString.call(e)};function i(e){var n=this;null!==this._state?t(function(){var t=n._state?e.onFulfilled:e.onRejected;if(null!==t){var r;try{r=t(n._value)}catch(n){return void e.reject(n)}e.resolve(r)}else(n._state?e.resolve:e.reject)(n._value)}):this._deferreds.push(e)}function u(e){try{if(e===this)throw new TypeError("A promise cannot be resolved with itself.");if(e&&("object"==typeof e||"function"==typeof e)){var n=e.then;if("function"==typeof n)return void f(r(n,e),r(u,this),r(a,this))}this._state=!0,this._value=e,c.call(this)}catch(e){a.call(this,e)}}function a(e){this._state=!1,this._value=e,c.call(this)}function c(){for(var e=0,n=this._deferreds;e<n.length;e++){var t=n[e];i.call(this,t)}this._deferreds=[]}function s(e,n,t,r){this.onFulfilled="function"==typeof e?e:null,this.onRejected="function"==typeof n?n:null,this.resolve=t,this.reject=r}function f(e,n,t){var r=!1;try{e(function(e){r||(r=!0,n(e))},function(e){r||(r=!0,t(e))})}catch(e){if(r)return;r=!0,t(e)}}return n.prototype.catch=function(e){return this.then(null,e)},n.prototype.then=function(e,t){var r=this;return new n(function(n,o){i.call(r,new s(e,t,n,o))})},n.all=function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t];var r=Array.prototype.slice.call(1===e.length&&o(e[0])?e[0]:e);return new n(function(e,n){if(0===r.length)return e([]);var t=r.length;function o(i,u){try{if(u&&("object"==typeof u||"function"==typeof u)){var a=u.then;if("function"==typeof a)return void a.call(u,function(e){o(i,e)},n)}r[i]=u,0==--t&&e(r)}catch(e){n(e)}}for(var i=0;i<r.length;i++)o(i,r[i])})},n.resolve=function(e){return e&&"object"==typeof e&&e.constructor===n?e:new n(function(n){n(e)})},n.reject=function(e){return new n(function(n,t){t(e)})},n.race=function(e){return new n(function(n,t){for(var r=0,o=e;r<o.length;r++)o[r].then(n,t)})},n}();function E(n){var t,r=n.src;return 0===r.indexOf("data:")?S(r):(t=r,new b(function(n,r){var o=new e.XMLHttpRequest;o.open("GET",t,!0),o.responseType="blob",o.onload=function(){200===this.status&&n(this.response)},o.onerror=function(){var e,n=this;r(0===this.status?((e=new Error("No access to download image")).code=18,e.name="SecurityError",e):new Error("Error "+n.status+" downloading image"))},o.send()}))}function I(n){return new b(function(t,r){var o=e.URL.createObjectURL(n),i=new e.Image,u=function(){i.removeEventListener("load",a),i.removeEventListener("error",c)};function a(){u(),t(i)}function c(){u(),r("Unable to load data of type "+n.type+": "+o)}i.addEventListener("load",a),i.addEventListener("error",c),i.src=o,i.complete&&a()})}function S(n){return new b(function(t,r){(function(n){var t=n.split(","),r=/data:([^;]+)/.exec(t[0]);if(!r)return h.none();for(var o=r[1],i=t[1],u=e.atob(i),a=u.length,c=Math.ceil(a/1024),s=new Array(c),f=0;f<c;++f){for(var l=1024*f,d=Math.min(l+1024,a),m=new Array(d-l),g=l,v=0;g<d;++v,++g)m[v]=u[g].charCodeAt(0);s[f]=new Uint8Array(m)}return h.some(new e.Blob(s,{type:o}))})(n).fold(function(){r("uri is not base64: "+n)},t)})}function O(n,t,r){return t=t||"image/png",e.HTMLCanvasElement.prototype.toBlob?new b(function(e,o){n.toBlob(function(n){n?e(n):o()},t,r)}):S(n.toDataURL(t,r))}function T(n){return I(n).then(function(n){!function(n){e.URL.revokeObjectURL(n.src)}(n);var t=v(function(e){return e.naturalWidth||e.width}(n),function(e){return e.naturalHeight||e.height}(n));return w(t).drawImage(n,0,0),t})}function N(e,n,t){var r=n.type;function o(n,t){return e.then(function(e){return function(e,n,t){return n=n||"image/png",e.toDataURL(n,t)}(e,n,t)})}return{getType:s(r),toBlob:function(){return b.resolve(n)},toDataURL:function(){return t},toBase64:function(){return t.split(",")[1]},toAdjustedBlob:function(n,t){return e.then(function(e){return O(e,n,t)})},toAdjustedDataURL:o,toAdjustedBase64:function(e,n){return o(e,n).then(function(e){return e.split(",")[1]})},toCanvas:function(){return e.then(p)}}}function _(n){return function(n){return new b(function(t){var r=new e.FileReader;r.onloadend=function(){t(r.result)},r.readAsDataURL(n)})}(n).then(function(e){return N(T(n),n,e)})}function x(e,n){return O(e,n).then(function(n){return N(b.resolve(e),n,e.toDataURL())})}function R(e,n){return e.toCanvas().then(function(t){return function(e,n,t){var r=v(e.width,e.height),o=w(r),i=0,u=0;90!==(t=t<0?360+t:t)&&270!==t||y(r,r.height,r.width);90!==t&&180!==t||(i=r.width);270!==t&&180!==t||(u=r.height);return o.translate(i,u),o.rotate(t*Math.PI/180),o.drawImage(e,0,0),x(r,n)}(t,e.getType(),n)})}function A(e,n){return e.toCanvas().then(function(t){return function(e,n,t){var r=v(e.width,e.height),o=w(r);"v"===t?(o.scale(1,-1),o.drawImage(e,0,-r.height)):(o.scale(-1,1),o.drawImage(e,-r.width,0));return x(r,n)}(t,e.getType(),n)})}var U=function(e){return _(e)},D=tinymce.util.Tools.resolve("tinymce.util.Delay"),C=tinymce.util.Tools.resolve("tinymce.util.Promise"),B=tinymce.util.Tools.resolve("tinymce.util.URI"),L=function(e){return e.getParam("imagetools_toolbar","rotateleft rotateright flipv fliph editimage imageoptions")};var k,j={getImageSize:function(e){var n,t;function r(e){return/^[0-9\.]+px$/.test(e)}return n=e.style.width,t=e.style.height,n||t?r(n)&&r(t)?{w:parseInt(n,10),h:parseInt(t,10)}:null:(n=e.width,t=e.height,n&&t?{w:parseInt(n,10),h:parseInt(t,10)}:null)},setImageSize:function(e,n){var t,r;n&&(t=e.style.width,r=e.style.height,(t||r)&&(e.style.width=n.w+"px",e.style.height=n.h+"px",e.removeAttribute("data-mce-style")),t=e.width,r=e.height,(t||r)&&(e.setAttribute("width",n.w),e.setAttribute("height",n.h)))},getNaturalImageSize:function(e){return{w:e.naturalWidth,h:e.naturalHeight}}},P=(k="function",function(e){return function(e){if(null===e)return"null";var n=typeof e;return"object"===n&&(Array.prototype.isPrototypeOf(e)||e.constructor&&"Array"===e.constructor.name)?"array":"object"===n&&(String.prototype.isPrototypeOf(e)||e.constructor&&"String"===e.constructor.name)?"string":n}(e)===k}),M=Array.prototype.slice,F=function(e,n){for(var t=0,r=e.length;t<r;t++){var o=e[t];if(n(o,t))return h.some(o)}return h.none()},z=(P(Array.from)&&Array.from,function(e){return null!=e}),H={traverse:function(e,n){var t;return t=n.reduce(function(e,n){return z(e)?e[n]:void 0},e),z(t)?t:null},readBlob:function(n){return new C(function(t){var r=new e.FileReader;r.onload=function(e){var n=e.target;t(n.result)},r.readAsText(n)})},requestUrlAsBlob:function(n,t,r){return new C(function(o){var i;(i=new e.XMLHttpRequest).onreadystatechange=function(){4===i.readyState&&o({status:i.status,blob:this.response})},i.open("GET",n,!0),i.withCredentials=r,a.each(t,function(e,n){i.setRequestHeader(n,e)}),i.responseType="blob",i.send()})},parseJson:function(e){var n;try{n=JSON.parse(e)}catch(e){}return n}},q=[{code:404,message:"Could not find Image Proxy"},{code:403,message:"Rejected request"},{code:0,message:"Incorrect Image Proxy URL"}],$=[{type:"key_missing",message:"The request did not include an api key."},{type:"key_not_found",message:"The provided api key could not be found."},{type:"domain_not_trusted",message:"The api key is not valid for the request origins."}],W=function(e){return"ImageProxy HTTP error: "+F(q,function(n){return e===n.code}).fold(s("Unknown ImageProxy error"),function(e){return e.message})},X=function(e){var n=W(e);return C.reject(n)},G=function(e){return F($,function(n){return n.type===e}).fold(s("Unknown service error"),function(e){return e.message})},J=function(e,n){return H.readBlob(n).then(function(e){var n=function(e){var n=H.parseJson(e),t=H.traverse(n,["error","type"]);return"ImageProxy Service error: "+(t?G(t):"Invalid JSON in service error message")}(e);return C.reject(n)})},Y={handleServiceErrorResponse:function(e,n){return 400===(t=e)||403===t||500===t?J(0,n):X(e);var t},handleHttpError:X,getHttpErrorMsg:W,getServiceErrorMsg:G},V=function(e,n){var t={"Content-Type":"application/json;charset=UTF-8","tiny-api-key":n};return H.requestUrlAsBlob(function(e,n){var t=-1===e.indexOf("?")?"?":"&";return/[?&]apiKey=/.test(e)||!n?e:e+t+"apiKey="+encodeURIComponent(n)}(e,n),t,!1).then(function(e){return e.status<200||e.status>=300?Y.handleServiceErrorResponse(e.status,e.blob):C.resolve(e.blob)})};var K=function(e,n,t){return n?V(e,n):function(e,n){return H.requestUrlAsBlob(e,{},n).then(function(e){return e.status<200||e.status>=300?Y.handleHttpError(e.status):C.resolve(e.blob)})}(e,t)},Q=function(e,n,t){return 0!=(e.compareDocumentPosition(n)&t)},Z=function(n,t){return Q(n,t,e.Node.DOCUMENT_POSITION_CONTAINED_BY)},ee=function(){return ne(0,0)},ne=function(e,n){return{major:e,minor:n}},te={nu:ne,detect:function(e,n){var t=String(n).toLowerCase();return 0===e.length?ee():function(e,n){var t=function(e,n){for(var t=0;t<e.length;t++){var r=e[t];if(r.test(n))return r}}(e,n);if(!t)return{major:0,minor:0};var r=function(e){return Number(n.replace(t,"$"+e))};return ne(r(1),r(2))}(e,t)},unknown:ee},re=function(e,n){return function(){return n===e}},oe=function(e){var n=e.current;return{current:n,version:e.version,isEdge:re("Edge",n),isChrome:re("Chrome",n),isIE:re("IE",n),isOpera:re("Opera",n),isFirefox:re("Firefox",n),isSafari:re("Safari",n)}},ie={unknown:function(){return oe({current:void 0,version:te.unknown()})},nu:oe,edge:s("Edge"),chrome:s("Chrome"),ie:s("IE"),opera:s("Opera"),firefox:s("Firefox"),safari:s("Safari")},ue=function(e,n){return function(){return n===e}},ae=function(e){var n=e.current;return{current:n,version:e.version,isWindows:ue("Windows",n),isiOS:ue("iOS",n),isAndroid:ue("Android",n),isOSX:ue("OSX",n),isLinux:ue("Linux",n),isSolaris:ue("Solaris",n),isFreeBSD:ue("FreeBSD",n)}},ce={unknown:function(){return ae({current:void 0,version:te.unknown()})},nu:ae,windows:s("Windows"),ios:s("iOS"),android:s("Android"),linux:s("Linux"),osx:s("OSX"),solaris:s("Solaris"),freebsd:s("FreeBSD")},se=function(e,n){var t=String(n).toLowerCase();return F(e,function(e){return e.search(t)})},fe=function(e,n){return se(e,n).map(function(e){var t=te.detect(e.versionRegexes,n);return{current:e.name,version:t}})},le=function(e,n){return se(e,n).map(function(e){var t=te.detect(e.versionRegexes,n);return{current:e.name,version:t}})},de=function(e,n){return-1!==e.indexOf(n)},me=/.*?version\/\ ?([0-9]+)\.([0-9]+).*/,ge=function(e){return function(n){return de(n,e)}},he=[{name:"Edge",versionRegexes:[/.*?edge\/ ?([0-9]+)\.([0-9]+)$/],search:function(e){return de(e,"edge/")&&de(e,"chrome")&&de(e,"safari")&&de(e,"applewebkit")}},{name:"Chrome",versionRegexes:[/.*?chrome\/([0-9]+)\.([0-9]+).*/,me],search:function(e){return de(e,"chrome")&&!de(e,"chromeframe")}},{name:"IE",versionRegexes:[/.*?msie\ ?([0-9]+)\.([0-9]+).*/,/.*?rv:([0-9]+)\.([0-9]+).*/],search:function(e){return de(e,"msie")||de(e,"trident")}},{name:"Opera",versionRegexes:[me,/.*?opera\/([0-9]+)\.([0-9]+).*/],search:ge("opera")},{name:"Firefox",versionRegexes:[/.*?firefox\/\ ?([0-9]+)\.([0-9]+).*/],search:ge("firefox")},{name:"Safari",versionRegexes:[me,/.*?cpu os ([0-9]+)_([0-9]+).*/],search:function(e){return(de(e,"safari")||de(e,"mobile/"))&&de(e,"applewebkit")}}],ve=[{name:"Windows",search:ge("win"),versionRegexes:[/.*?windows\ nt\ ?([0-9]+)\.([0-9]+).*/]},{name:"iOS",search:function(e){return de(e,"iphone")||de(e,"ipad")},versionRegexes:[/.*?version\/\ ?([0-9]+)\.([0-9]+).*/,/.*cpu os ([0-9]+)_([0-9]+).*/,/.*cpu iphone os ([0-9]+)_([0-9]+).*/]},{name:"Android",search:ge("android"),versionRegexes:[/.*?android\ ?([0-9]+)\.([0-9]+).*/]},{name:"OSX",search:ge("os x"),versionRegexes:[/.*?os\ x\ ?([0-9]+)_([0-9]+).*/]},{name:"Linux",search:ge("linux"),versionRegexes:[]},{name:"Solaris",search:ge("sunos"),versionRegexes:[]},{name:"FreeBSD",search:ge("freebsd"),versionRegexes:[]}],pe={browsers:s(he),oses:s(ve)},we=function(e,n){var t=pe.browsers(),r=pe.oses(),o=fe(t,e).fold(ie.unknown,ie.nu),i=le(r,e).fold(ce.unknown,ce.nu),u=function(e,n,t,r){var o=e.isiOS()&&!0===/ipad/i.test(t),i=e.isiOS()&&!o,u=e.isiOS()||e.isAndroid(),a=u||r("(pointer:coarse)"),c=o||!i&&u&&r("(min-device-width:768px)"),f=i||u&&!c,l=n.isSafari()&&e.isiOS()&&!1===/safari/i.test(t),d=!f&&!c&&!l;return{isiPad:s(o),isiPhone:s(i),isTablet:s(c),isPhone:s(f),isTouch:s(a),isAndroid:e.isAndroid,isiOS:e.isiOS,isWebView:s(l),isDesktop:s(d)}}(i,o,e,n);return{browser:o,os:i,deviceType:u}},ye=i(we(e.navigator.userAgent,function(n){return e.window.matchMedia(n).matches})),be=function(e){if(null==e)throw new Error("Node cannot be null or undefined");return{dom:s(e)}},Ee={fromHtml:function(n,t){var r=(t||e.document).createElement("div");if(r.innerHTML=n,!r.hasChildNodes()||r.childNodes.length>1)throw e.console.error("HTML does not have a single root node",n),new Error("HTML must have a single root node");return be(r.childNodes[0])},fromTag:function(n,t){var r=(t||e.document).createElement(n);return be(r)},fromText:function(n,t){var r=(t||e.document).createTextNode(n);return be(r)},fromDom:be,fromPoint:function(e,n,t){var r=e.dom();return h.from(r.elementFromPoint(n,t)).map(be)}},Ie=(e.Node.ATTRIBUTE_NODE,e.Node.CDATA_SECTION_NODE,e.Node.COMMENT_NODE,e.Node.DOCUMENT_NODE,e.Node.DOCUMENT_TYPE_NODE,e.Node.DOCUMENT_FRAGMENT_NODE,e.Node.ELEMENT_NODE),Se=(e.Node.TEXT_NODE,e.Node.PROCESSING_INSTRUCTION_NODE,e.Node.ENTITY_REFERENCE_NODE,e.Node.ENTITY_NODE,e.Node.NOTATION_NODE,Ie),Oe=(ye.get().browser.isIE(),void 0!==e.window?e.window:Function("return this;")(),function(e,n){return function(e,n){return F(e.dom().childNodes,function(e){return n(Ee.fromDom(e))}).map(Ee.fromDom)}(e,function(e){return function(e,n){var t=e.dom();if(t.nodeType!==Se)return!1;var r=t;if(void 0!==r.matches)return r.matches(n);if(void 0!==r.msMatchesSelector)return r.msMatchesSelector(n);if(void 0!==r.webkitMatchesSelector)return r.webkitMatchesSelector(n);if(void 0!==r.mozMatchesSelector)return r.mozMatchesSelector(n);throw new Error("Browser lacks native selectors")}(e,n)})}),Te=0,Ne=function(e){return Oe(Ee.fromDom(e),"img")},_e=function(e,n){return e.dom.is(n,"figure")},xe=function(e,n){e.notificationManager.open({text:n,type:"error"})},Re=function(e){var n=e.selection.getNode();return _e(e,n)?Ne(n):h.some(Ee.fromDom(n))},Ae=function(e,n){var t=n.src;return 0===t.indexOf("data:")||0===t.indexOf("blob:")||new B(t).host===e.documentBaseURI.host},Ue=function(e,n){return-1!==a.inArray(function(e){return e.getParam("imagetools_cors_hosts",[],"string[]")}(e),new B(n.src).host)},De=function(e,n){var t,r=n.src;return Ue(e,n)?K(n.src,null,function(e,n){return-1!==a.inArray(function(e){return e.getParam("imagetools_credentials_hosts",[],"string[]")}(e),new B(n.src).host)}(e,n)):Ae(e,n)?E(n):(r=function(e){return e.getParam("imagetools_proxy")}(e),r+=(-1===r.indexOf("?")?"?":"&")+"url="+encodeURIComponent(n.src),t=function(e){return e.getParam("api_key",e.getParam("imagetools_api_key","","string"),"string")}(e),K(r,t,!1))},Ce=function(e,n){return function(e){return h.from(e.getParam("imagetools_fetch_image",null,"function"))}(e).fold(function(){return De(e,n)},function(e){return e(n)})},Be=function(e,n){var t;return(t=e.editorUpload.blobCache.getByUri(n.src))?C.resolve(t.blob()):Ce(e,n)},Le=function(e,n){var t=D.setEditorTimeout(e,function(){e.editorUpload.uploadImagesAuto()},function(e){return e.getParam("images_upload_timeout",3e4,"number")}(e));n.set(t)},ke=function(e){D.clearTimeout(e.get())},je=function(e,n,t,r,o,i){return n.toBlob().then(function(u){var a,c,s,f;return s=e.editorUpload.blobCache,a=o.src,function(e){return e.getParam("images_reuse_filename",!1,"boolean")}(e)&&((f=s.getByUri(a))?(a=f.uri(),c=f.name()):c=function(e,n){var t=n.match(/\/([^\/\?]+)?\.(?:jpeg|jpg|png|gif)(?:\?|$)/i);return t?e.dom.encode(t[1]):null}(e,a)),f=s.create({id:"imagetools"+Te++,blob:u,base64:n.toBase64(),uri:a,name:c}),s.add(f),e.undoManager.transact(function(){e.$(o).on("load",function n(){e.$(o).off("load",n),e.nodeChanged(),t?e.editorUpload.uploadImagesAuto():(ke(r),Le(e,r))}),i&&e.$(o).attr({width:i.w,height:i.h}),e.$(o).attr({src:f.blobUri()}).removeAttr("data-mce-src")}),f})},Pe=function(e,n,t,r){return function(){return Re(e).fold(function(){xe(e,"Could not find selected image")},function(o){return e._scanForImages().then(function(){return Be(e,o.dom())}).then(U).then(t).then(function(t){return je(e,t,!1,n,o.dom(),r)},function(n){xe(e,n)})})}},Me={rotate:function(e,n,t){return function(){var r=Re(e).fold(function(){return null},function(e){var n=j.getImageSize(e.dom());return n?{w:n.h,h:n.w}:null});return Pe(e,n,function(e){return function(e,n){return R(e,n)}(e,t)},r)()}},flip:function(e,n,t){return function(){return Pe(e,n,function(e){return function(e,n){return A(e,n)}(e,t)})()}},getEditableImage:function(e,n){var t=function(n){return function(n){return e.dom.is(n,"img:not([data-mce-object],[data-mce-placeholder])")}(n)&&(Ae(e,n)||Ue(e,n)||e.settings.imagetools_proxy)};return _e(e,n)?Ne(n).map(function(e){return t(e.dom())?h.some(e.dom()):h.none()}):t(n)?h.some(n):h.none()},cancelTimedUpload:ke,findBlob:Be,getSelectedImage:Re,handleDialogBlob:function(n,t,r,o,i){return new C(function(u){(function(e){return I(e)})(i).then(function(n){var t=j.getNaturalImageSize(n);return o.w===t.w&&o.h===t.h||j.getImageSize(r)&&j.setImageSize(r,t),e.URL.revokeObjectURL(n.src),i}).then(U).then(function(e){return je(n,e,!0,t,r)},function(){})})}},Fe=s("save-state"),ze=s("disable"),He=s("enable"),qe=function(n,t){return function(){var r=Me.getSelectedImage(n),o=r.map(function(e){return j.getNaturalImageSize(e.dom())});Me.getSelectedImage(n).each(function(i){Me.getEditableImage(n,i.dom()).each(function(u){Me.findBlob(n,i.dom()).then(function(i){var u=function(n){return{blob:n,url:e.URL.createObjectURL(n)}}(i);n.windowManager.open({title:"Edit Image",size:"large",body:{type:"panel",items:[{type:"imagetools",name:"imagetools",label:"Edit Image",currentState:u}]},buttons:[{type:"cancel",name:"cancel",text:"Cancel"},{type:"submit",name:"save",text:"Save",primary:!0,disabled:!0}],onSubmit:function(e){var i=e.getData().imagetools.blob;r.each(function(e){o.each(function(r){Me.handleDialogBlob(n,t,e.dom(),r,i)})}),e.close()},onCancel:function(){},onAction:function(e,n){switch(n.name){case Fe():n.value?e.enable("save"):e.disable("save");break;case ze():e.disable("save"),e.disable("cancel");break;case He():e.enable("cancel")}}})})})})}},$e={register:function(e,n){a.each({mceImageRotateLeft:Me.rotate(e,n,-90),mceImageRotateRight:Me.rotate(e,n,90),mceImageFlipVertical:Me.flip(e,n,"v"),mceImageFlipHorizontal:Me.flip(e,n,"h"),mceEditImage:qe(e,n)},function(n,t){e.addCommand(t,n)})}},We={setup:function(e,n,t){e.on("NodeChange",function(r){var o=t.get();o&&o.src!==r.element.src&&(Me.cancelTimedUpload(n),e.editorUpload.uploadImagesAuto(),t.set(null)),Me.getEditableImage(e,r.element).each(t.set)})}},Xe={register:function(e){var n=function(n){return function(){return e.execCommand(n)}};e.ui.registry.addButton("rotateleft",{tooltip:"Rotate counterclockwise",icon:"rotate-left",onAction:n("mceImageRotateLeft")}),e.ui.registry.addButton("rotateright",{tooltip:"Rotate clockwise",icon:"rotate-right",onAction:n("mceImageRotateRight")}),e.ui.registry.addButton("flipv",{tooltip:"Flip vertically",icon:"flip-vertically",onAction:n("mceImageFlipVertical")}),e.ui.registry.addButton("fliph",{tooltip:"Flip horizontally",icon:"flip-horizontally",onAction:n("mceImageFlipHorizontal")}),e.ui.registry.addButton("editimage",{tooltip:"Edit image",icon:"edit-image",onAction:n("mceEditImage"),onSetup:function(n){var t=function(){Me.getSelectedImage(e).each(function(t){var r=Me.getEditableImage(e,t.dom()).isNone();n.setDisabled(r)})};return e.on("NodeChange",t),function(){e.off("NodeChange",t)}}}),e.ui.registry.addButton("imageoptions",{tooltip:"Image options",icon:"image-options",onAction:n("mceImage")}),e.ui.registry.addContextMenu("imagetools",{update:function(t){return Me.getEditableImage(e,t).fold(function(){return[]},function(e){return[{text:"Edit image",icon:"edit-image",onAction:n("mceEditImage")}]})}})}},Ge={register:function(e){e.ui.registry.addContextToolbar("imagetools",{items:L(e),predicate:function(n){return Me.getEditableImage(e,n).isSome()},position:"node",scope:"node"})}};u.add("imagetools",function(e){var n=i(0),t=i(null);$e.register(e,n),Xe.register(e),Ge.register(e),We.setup(e,n,t)})}(window);