!function(e){"use strict";var t=tinymce.util.Tools.resolve("tinymce.PluginManager"),n=tinymce.util.Tools.resolve("tinymce.dom.DOMUtils"),a={},r=a,i=void 0!==a?a:"undefined"!=typeof WorkerGlobalScope&&e.self instanceof WorkerGlobalScope?e.self:{},o=function(){var t=/\blang(?:uage)?-(?!\*)(\w+)\b/i,n=i.Prism={util:{encode:function(e){return e instanceof a?new a(e.type,n.util.encode(e.content),e.alias):"Array"===n.util.type(e)?e.map(n.util.encode):e.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/\u00a0/g," ")},type:function(e){return Object.prototype.toString.call(e).match(/\[object (\w+)\]/)[1]},clone:function(e){switch(n.util.type(e)){case"Object":var t={};for(var a in e)e.hasOwnProperty(a)&&(t[a]=n.util.clone(e[a]));return t;case"Array":return e.map&&e.map(function(e){return n.util.clone(e)})}return e}},languages:{extend:function(e,t){var a=n.util.clone(n.languages[e]);for(var r in t)a[r]=t[r];return a},insertBefore:function(e,t,a,r){var i=(r=r||n.languages)[e];if(2===arguments.length){for(var o in a=arguments[1])a.hasOwnProperty(o)&&(i[o]=a[o]);return i}var s={};for(var l in i)if(i.hasOwnProperty(l)){if(l===t)for(var o in a)a.hasOwnProperty(o)&&(s[o]=a[o]);s[l]=i[l]}return n.languages.DFS(n.languages,function(t,n){n===r[e]&&t!==e&&(this[t]=s)}),r[e]=s},DFS:function(e,t,a){for(var r in e)e.hasOwnProperty(r)&&(t.call(e,r,e[r],a||r),"Object"===n.util.type(e[r])?n.languages.DFS(e[r],t):"Array"===n.util.type(e[r])&&n.languages.DFS(e[r],t,r))}},plugins:{},highlightAll:function(t,a){for(var r=e.document.querySelectorAll('code[class*="language-"], [class*="language-"] code, code[class*="lang-"], [class*="lang-"] code'),i=0,o=void 0;o=r[i++];)n.highlightElement(o,!0===t,a)},highlightElement:function(a,r,o){for(var s,l,u=a;u&&!t.test(u.className);)u=u.parentNode;u&&(s=(u.className.match(t)||[,""])[1],l=n.languages[s]),a.className=a.className.replace(t,"").replace(/\s+/g," ")+" language-"+s,u=a.parentNode,/pre/i.test(u.nodeName)&&(u.className=u.className.replace(t,"").replace(/\s+/g," ")+" language-"+s);var c=a.textContent,g={element:a,language:s,grammar:l,code:c};if(c&&l)if(n.hooks.run("before-highlight",g),r&&i.Worker){var p=new e.Worker(n.filename);p.onmessage=function(e){g.highlightedCode=e.data,n.hooks.run("before-insert",g),g.element.innerHTML=g.highlightedCode,o&&o.call(g.element),n.hooks.run("after-highlight",g),n.hooks.run("complete",g)},p.postMessage(JSON.stringify({language:g.language,code:g.code,immediateClose:!0}))}else g.highlightedCode=n.highlight(g.code,g.grammar,g.language),n.hooks.run("before-insert",g),g.element.innerHTML=g.highlightedCode,o&&o.call(a),n.hooks.run("after-highlight",g),n.hooks.run("complete",g);else n.hooks.run("complete",g)},highlight:function(e,t,r){var i=n.tokenize(e,t);return a.stringify(n.util.encode(i),r)},tokenize:function(e,t,a){var r=n.Token,i=[e],o=t.rest;if(o){for(var s in o)t[s]=o[s];delete t.rest}e:for(var s in t)if(t.hasOwnProperty(s)&&t[s]){var l=t[s];l="Array"===n.util.type(l)?l:[l];for(var u=0;u<l.length;++u){var c=l[u],g=c.inside,p=!!c.lookbehind,d=0,f=c.alias;c=c.pattern||c;for(var h=0;h<i.length;h++){var m=i[h];if(i.length>e.length)break e;if(!(m instanceof r)){c.lastIndex=0;var b=c.exec(m);if(b){p&&(d=b[1].length);var y=b.index-1+d,v=y+(b=b[0].slice(d)).length,k=m.slice(0,y+1),w=m.slice(v+1),x=[h,1];k&&x.push(k);var S=new r(s,g?n.tokenize(b,g):b,f);x.push(S),w&&x.push(w),Array.prototype.splice.apply(i,x)}}}}}return i},hooks:{all:{},add:function(e,t){var a=n.hooks.all;a[e]=a[e]||[],a[e].push(t)},run:function(e,t){var a=n.hooks.all[e];if(a&&a.length)for(var r=0,i=void 0;i=a[r++];)i(t)}}},a=n.Token=function(e,t,n){this.type=e,this.content=t,this.alias=n};if(a.stringify=function(e,t,r){if("string"==typeof e)return e;if("Array"===n.util.type(e))return e.map(function(n){return a.stringify(n,t,e)}).join("");var i={type:e.type,content:a.stringify(e.content,t,r),tag:"span",classes:["token",e.type],attributes:{},language:t,parent:r};if("comment"===i.type&&(i.attributes.spellcheck="true"),e.alias){var o="Array"===n.util.type(e.alias)?e.alias:[e.alias];Array.prototype.push.apply(i.classes,o)}n.hooks.run("wrap",i);var s="";for(var l in i.attributes)s+=(s?" ":"")+l+'="'+(i.attributes[l]||"")+'"';return"<"+i.tag+' class="'+i.classes.join(" ")+'" '+s+">"+i.content+"</"+i.tag+">"},!i.document)return i.addEventListener?(i.addEventListener("message",function(e){var t=JSON.parse(e.data),a=t.language,r=t.code,o=t.immediateClose;i.postMessage(n.highlight(r,n.languages[a],a)),o&&i.close()},!1),i.Prism):i.Prism}();void 0!==r&&(r.Prism=o),o.languages.markup={comment:/<!--[\w\W]*?-->/,prolog:/<\?[\w\W]+?\?>/,doctype:/<!DOCTYPE[\w\W]+?>/,cdata:/<!\[CDATA\[[\w\W]*?]]>/i,tag:{pattern:/<\/?[^\s>\/=.]+(?:\s+[^\s>\/=]+(?:=(?:("|')(?:\\\1|\\?(?!\1)[\w\W])*\1|[^\s'">=]+))?)*\s*\/?>/i,inside:{tag:{pattern:/^<\/?[^\s>\/]+/i,inside:{punctuation:/^<\/?/,namespace:/^[^\s>\/:]+:/}},"attr-value":{pattern:/=(?:('|")[\w\W]*?(\1)|[^\s>]+)/i,inside:{punctuation:/[=>"']/}},punctuation:/\/?>/,"attr-name":{pattern:/[^\s>\/]+/,inside:{namespace:/^[^\s>\/:]+:/}}}},entity:/&#?[\da-z]{1,8};/i},o.hooks.add("wrap",function(e){"entity"===e.type&&(e.attributes.title=e.content.replace(/&amp;/,"&"))}),o.languages.xml=o.languages.markup,o.languages.html=o.languages.markup,o.languages.mathml=o.languages.markup,o.languages.svg=o.languages.markup,o.languages.css={comment:/\/\*[\w\W]*?\*\//,atrule:{pattern:/@[\w-]+?.*?(;|(?=\s*\{))/i,inside:{rule:/@[\w-]+/}},url:/url\((?:(["'])(\\(?:\r\n|[\w\W])|(?!\1)[^\\\r\n])*\1|.*?)\)/i,selector:/[^\{\}\s][^\{\};]*?(?=\s*\{)/,string:/("|')(\\(?:\r\n|[\w\W])|(?!\1)[^\\\r\n])*\1/,property:/(\b|\B)[\w-]+(?=\s*:)/i,important:/\B!important\b/i,function:/[-a-z0-9]+(?=\()/i,punctuation:/[(){};:]/},o.languages.css.atrule.inside.rest=o.util.clone(o.languages.css),o.languages.markup&&(o.languages.insertBefore("markup","tag",{style:{pattern:/<style[\w\W]*?>[\w\W]*?<\/style>/i,inside:{tag:{pattern:/<style[\w\W]*?>|<\/style>/i,inside:o.languages.markup.tag.inside},rest:o.languages.css},alias:"language-css"}}),o.languages.insertBefore("inside","attr-value",{"style-attr":{pattern:/\s*style=("|').*?\1/i,inside:{"attr-name":{pattern:/^\s*style/i,inside:o.languages.markup.tag.inside},punctuation:/^\s*=\s*['"]|['"]\s*$/,"attr-value":{pattern:/.+/i,inside:o.languages.css}},alias:"language-css"}},o.languages.markup.tag)),o.languages.clike={comment:[{pattern:/(^|[^\\])\/\*[\w\W]*?\*\//,lookbehind:!0},{pattern:/(^|[^\\:])\/\/.*/,lookbehind:!0}],string:/(["'])(\\(?:\r\n|[\s\S])|(?!\1)[^\\\r\n])*\1/,"class-name":{pattern:/((?:\b(?:class|interface|extends|implements|trait|instanceof|new)\s+)|(?:catch\s+\())[a-z0-9_\.\\]+/i,lookbehind:!0,inside:{punctuation:/(\.|\\)/}},keyword:/\b(if|else|while|do|for|return|in|instanceof|function|new|try|throw|catch|finally|null|break|continue)\b/,boolean:/\b(true|false)\b/,function:/[a-z0-9_]+(?=\()/i,number:/\b-?(?:0x[\da-f]+|\d*\.?\d+(?:e[+-]?\d+)?)\b/i,operator:/--?|\+\+?|!=?=?|<=?|>=?|==?=?|&&?|\|\|?|\?|\*|\/|~|\^|%/,punctuation:/[{}[\];(),.:]/},o.languages.javascript=o.languages.extend("clike",{keyword:/\b(as|async|await|break|case|catch|class|const|continue|debugger|default|delete|do|else|enum|export|extends|false|finally|for|from|function|get|if|implements|import|in|instanceof|interface|let|new|null|of|package|private|protected|public|return|set|static|super|switch|this|throw|true|try|typeof|var|void|while|with|yield)\b/,number:/\b-?(0x[\dA-Fa-f]+|0b[01]+|0o[0-7]+|\d*\.?\d+([Ee][+-]?\d+)?|NaN|Infinity)\b/,function:/[_$a-zA-Z\xA0-\uFFFF][_$a-zA-Z0-9\xA0-\uFFFF]*(?=\()/i}),o.languages.insertBefore("javascript","keyword",{regex:{pattern:/(^|[^\/])\/(?!\/)(\[.+?]|\\.|[^\/\\\r\n])+\/[gimyu]{0,5}(?=\s*($|[\r\n,.;})]))/,lookbehind:!0}}),o.languages.insertBefore("javascript","class-name",{"template-string":{pattern:/`(?:\\`|\\?[^`])*`/,inside:{interpolation:{pattern:/\$\{[^}]+\}/,inside:{"interpolation-punctuation":{pattern:/^\$\{|\}$/,alias:"punctuation"},rest:o.languages.javascript}},string:/[\s\S]+/}}}),o.languages.markup&&o.languages.insertBefore("markup","tag",{script:{pattern:/<script[\w\W]*?>[\w\W]*?<\/script>/i,inside:{tag:{pattern:/<script[\w\W]*?>|<\/script>/i,inside:o.languages.markup.tag.inside},rest:o.languages.javascript},alias:"language-javascript"}}),o.languages.js=o.languages.javascript,o.languages.c=o.languages.extend("clike",{keyword:/\b(asm|typeof|inline|auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b/,operator:/\-[>-]?|\+\+?|!=?|<<?=?|>>?=?|==?|&&?|\|?\||[~^%?*\/]/,number:/\b-?(?:0x[\da-f]+|\d*\.?\d+(?:e[+-]?\d+)?)[ful]*\b/i}),o.languages.insertBefore("c","string",{macro:{pattern:/(^\s*)#\s*[a-z]+([^\r\n\\]|\\.|\\(?:\r\n?|\n))*/im,lookbehind:!0,alias:"property",inside:{string:{pattern:/(#\s*include\s*)(<.+?>|("|')(\\?.)+?\3)/,lookbehind:!0}}}}),delete o.languages.c["class-name"],delete o.languages.c.boolean,o.languages.csharp=o.languages.extend("clike",{keyword:/\b(abstract|as|async|await|base|bool|break|byte|case|catch|char|checked|class|const|continue|decimal|default|delegate|do|double|else|enum|event|explicit|extern|false|finally|fixed|float|for|foreach|goto|if|implicit|in|int|interface|internal|is|lock|long|namespace|new|null|object|operator|out|override|params|private|protected|public|readonly|ref|return|sbyte|sealed|short|sizeof|stackalloc|static|string|struct|switch|this|throw|true|try|typeof|uint|ulong|unchecked|unsafe|ushort|using|virtual|void|volatile|while|add|alias|ascending|async|await|descending|dynamic|from|get|global|group|into|join|let|orderby|partial|remove|select|set|value|var|where|yield)\b/,string:[/@("|')(\1\1|\\\1|\\?(?!\1)[\s\S])*\1/,/("|')(\\?.)*?\1/],number:/\b-?(0x[\da-f]+|\d*\.?\d+)\b/i}),o.languages.insertBefore("csharp","keyword",{preprocessor:{pattern:/(^\s*)#.*/m,lookbehind:!0}}),o.languages.cpp=o.languages.extend("c",{keyword:/\b(alignas|alignof|asm|auto|bool|break|case|catch|char|char16_t|char32_t|class|compl|const|constexpr|const_cast|continue|decltype|default|delete|do|double|dynamic_cast|else|enum|explicit|export|extern|float|for|friend|goto|if|inline|int|long|mutable|namespace|new|noexcept|nullptr|operator|private|protected|public|register|reinterpret_cast|return|short|signed|sizeof|static|static_assert|static_cast|struct|switch|template|this|thread_local|throw|try|typedef|typeid|typename|union|unsigned|using|virtual|void|volatile|wchar_t|while)\b/,boolean:/\b(true|false)\b/,operator:/[-+]{1,2}|!=?|<{1,2}=?|>{1,2}=?|\->|:{1,2}|={1,2}|\^|~|%|&{1,2}|\|?\||\?|\*|\/|\b(and|and_eq|bitand|bitor|not|not_eq|or|or_eq|xor|xor_eq)\b/}),o.languages.insertBefore("cpp","keyword",{"class-name":{pattern:/(class\s+)[a-z0-9_]+/i,lookbehind:!0}}),o.languages.java=o.languages.extend("clike",{keyword:/\b(abstract|continue|for|new|switch|assert|default|goto|package|synchronized|boolean|do|if|private|this|break|double|implements|protected|throw|byte|else|import|public|throws|case|enum|instanceof|return|transient|catch|extends|int|short|try|char|final|interface|static|void|class|finally|long|strictfp|volatile|const|float|native|super|while)\b/,number:/\b0b[01]+\b|\b0x[\da-f]*\.?[\da-fp\-]+\b|\b\d*\.?\d+(?:e[+-]?\d+)?[df]?\b/i,operator:{pattern:/(^|[^.])(?:\+[+=]?|-[-=]?|!=?|<<?=?|>>?>?=?|==?|&[&=]?|\|[|=]?|\*=?|\/=?|%=?|\^=?|[?:~])/m,lookbehind:!0}}),o.languages.php=o.languages.extend("clike",{keyword:/\b(and|or|xor|array|as|break|case|cfunction|class|const|continue|declare|default|die|do|else|elseif|enddeclare|endfor|endforeach|endif|endswitch|endwhile|extends|for|foreach|function|include|include_once|global|if|new|return|static|switch|use|require|require_once|var|while|abstract|interface|public|implements|private|protected|parent|throw|null|echo|print|trait|namespace|final|yield|goto|instanceof|finally|try|catch)\b/i,constant:/\b[A-Z0-9_]{2,}\b/,comment:{pattern:/(^|[^\\])(?:\/\*[\w\W]*?\*\/|\/\/.*)/,lookbehind:!0}}),o.languages.insertBefore("php","class-name",{"shell-comment":{pattern:/(^|[^\\])#.*/,lookbehind:!0,alias:"comment"}}),o.languages.insertBefore("php","keyword",{delimiter:/\?>|<\?(?:php)?/i,variable:/\$\w+\b/i,package:{pattern:/(\\|namespace\s+|use\s+)[\w\\]+/,lookbehind:!0,inside:{punctuation:/\\/}}}),o.languages.insertBefore("php","operator",{property:{pattern:/(->)[\w]+/,lookbehind:!0}}),o.languages.markup&&(o.hooks.add("before-highlight",function(e){"php"===e.language&&(e.tokenStack=[],e.backupCode=e.code,e.code=e.code.replace(/(?:<\?php|<\?)[\w\W]*?(?:\?>)/gi,function(t){return e.tokenStack.push(t),"{{{PHP"+e.tokenStack.length+"}}}"}))}),o.hooks.add("before-insert",function(e){"php"===e.language&&(e.code=e.backupCode,delete e.backupCode)}),o.hooks.add("after-highlight",function(e){if("php"===e.language){for(var t=0,n=void 0;n=e.tokenStack[t];t++)e.highlightedCode=e.highlightedCode.replace("{{{PHP"+(t+1)+"}}}",o.highlight(n,e.grammar,"php").replace(/\$/g,"$$$$"));e.element.innerHTML=e.highlightedCode}}),o.hooks.add("wrap",function(e){"php"===e.language&&"markup"===e.type&&(e.content=e.content.replace(/(\{\{\{PHP[0-9]+\}\}\})/g,'<span class="token php">$1</span>'))}),o.languages.insertBefore("php","comment",{markup:{pattern:/<[^?]\/?(.*?)>/,inside:o.languages.markup},php:/\{\{\{PHP[0-9]+\}\}\}/})),o.languages.python={comment:{pattern:/(^|[^\\])#.*/,lookbehind:!0},string:/"""[\s\S]+?"""|'''[\s\S]+?'''|("|')(?:\\?.)*?\1/,function:{pattern:/((?:^|\s)def[ \t]+)[a-zA-Z_][a-zA-Z0-9_]*(?=\()/g,lookbehind:!0},"class-name":{pattern:/(\bclass\s+)[a-z0-9_]+/i,lookbehind:!0},keyword:/\b(?:as|assert|async|await|break|class|continue|def|del|elif|else|except|exec|finally|for|from|global|if|import|in|is|lambda|pass|print|raise|return|try|while|with|yield)\b/,boolean:/\b(?:True|False)\b/,number:/\b-?(?:0[bo])?(?:(?:\d|0x[\da-f])[\da-f]*\.?\d*|\.\d+)(?:e[+-]?\d+)?j?\b/i,operator:/[-+%=]=?|!=|\*\*?=?|\/\/?=?|<[<=>]?|>[=>]?|[&|^~]|\b(?:or|and|not)\b/,punctuation:/[{}[\];(),.:]/},function(e){e.languages.ruby=e.languages.extend("clike",{comment:/#(?!\{[^\r\n]*?\}).*/,keyword:/\b(alias|and|BEGIN|begin|break|case|class|def|define_method|defined|do|each|else|elsif|END|end|ensure|false|for|if|in|module|new|next|nil|not|or|raise|redo|require|rescue|retry|return|self|super|then|throw|true|undef|unless|until|when|while|yield)\b/});var t={pattern:/#\{[^}]+\}/,inside:{delimiter:{pattern:/^#\{|\}$/,alias:"tag"},rest:e.util.clone(e.languages.ruby)}};e.languages.insertBefore("ruby","keyword",{regex:[{pattern:/%r([^a-zA-Z0-9\s\{\(\[<])(?:[^\\]|\\[\s\S])*?\1[gim]{0,3}/,inside:{interpolation:t}},{pattern:/%r\((?:[^()\\]|\\[\s\S])*\)[gim]{0,3}/,inside:{interpolation:t}},{pattern:/%r\{(?:[^#{}\\]|#(?:\{[^}]+\})?|\\[\s\S])*\}[gim]{0,3}/,inside:{interpolation:t}},{pattern:/%r\[(?:[^\[\]\\]|\\[\s\S])*\][gim]{0,3}/,inside:{interpolation:t}},{pattern:/%r<(?:[^<>\\]|\\[\s\S])*>[gim]{0,3}/,inside:{interpolation:t}},{pattern:/(^|[^\/])\/(?!\/)(\[.+?]|\\.|[^\/\r\n])+\/[gim]{0,3}(?=\s*($|[\r\n,.;})]))/,lookbehind:!0}],variable:/[@$]+[a-zA-Z_][a-zA-Z_0-9]*(?:[?!]|\b)/,symbol:/:[a-zA-Z_][a-zA-Z_0-9]*(?:[?!]|\b)/}),e.languages.insertBefore("ruby","number",{builtin:/\b(Array|Bignum|Binding|Class|Continuation|Dir|Exception|FalseClass|File|Stat|File|Fixnum|Fload|Hash|Integer|IO|MatchData|Method|Module|NilClass|Numeric|Object|Proc|Range|Regexp|String|Struct|TMS|Symbol|ThreadGroup|Thread|Time|TrueClass)\b/,constant:/\b[A-Z][a-zA-Z_0-9]*(?:[?!]|\b)/}),e.languages.ruby.string=[{pattern:/%[qQiIwWxs]?([^a-zA-Z0-9\s\{\(\[<])(?:[^\\]|\\[\s\S])*?\1/,inside:{interpolation:t}},{pattern:/%[qQiIwWxs]?\((?:[^()\\]|\\[\s\S])*\)/,inside:{interpolation:t}},{pattern:/%[qQiIwWxs]?\{(?:[^#{}\\]|#(?:\{[^}]+\})?|\\[\s\S])*\}/,inside:{interpolation:t}},{pattern:/%[qQiIwWxs]?\[(?:[^\[\]\\]|\\[\s\S])*\]/,inside:{interpolation:t}},{pattern:/%[qQiIwWxs]?<(?:[^<>\\]|\\[\s\S])*>/,inside:{interpolation:t}},{pattern:/("|')(#\{[^}]+\}|\\(?:\r?\n|\r)|\\?.)*?\1/,inside:{interpolation:t}}]}(o);var s,l,u,c,g,p={isCodeSample:function(e){return e&&"PRE"===e.nodeName&&-1!==e.className.indexOf("language-")},trimArg:function(e){return function(t,n){return e(n)}}},d=function(){},f=function(e){return function(){return e}},h=f(!1),m=f(!0),b=function(){return y},y=(s=function(e){return e.isNone()},c={fold:function(e,t){return e()},is:h,isSome:h,isNone:m,getOr:u=function(e){return e},getOrThunk:l=function(e){return e()},getOrDie:function(e){throw new Error(e||"error: getOrDie called on none.")},getOrNull:f(null),getOrUndefined:f(void 0),or:u,orThunk:l,map:b,each:d,bind:b,exists:h,forall:m,filter:b,equals:s,equals_:s,toArray:function(){return[]},toString:f("none()")},Object.freeze&&Object.freeze(c),c),v=function(e){var t=f(e),n=function(){return r},a=function(t){return t(e)},r={fold:function(t,n){return n(e)},is:function(t){return e===t},isSome:m,isNone:h,getOr:t,getOrThunk:t,getOrDie:t,getOrNull:t,getOrUndefined:t,or:n,orThunk:n,map:function(t){return v(t(e))},each:function(t){t(e)},bind:a,exists:a,forall:a,filter:function(t){return t(e)?r:y},toArray:function(){return[e]},toString:function(){return"some("+e+")"},equals:function(t){return t.is(e)},equals_:function(t,n){return t.fold(h,function(t){return n(e,t)})}};return r},k={some:v,none:b,from:function(e){return null==e?y:v(e)}},w=function(e){var t=e.selection?e.selection.getNode():null;return p.isCodeSample(t)?k.some(t):k.none()},x=w,S=function(e,t,a){e.undoManager.transact(function(){var r=w(e);return a=n.DOM.encode(a),r.fold(function(){e.insertContent('<pre id="__new" class="language-'+t+'">'+a+"</pre>"),e.selection.select(e.$("#__new").removeAttr("id")[0])},function(n){e.dom.setAttrib(n,"class","language-"+t),n.innerHTML=a,o.highlightElement(n),e.selection.select(n)})})},A=function(e){return w(e).fold(function(){return""},function(e){return e.textContent})},C=function(e){return e.settings.codesample_languages},_=function(e){var t=C(e);return t||[{text:"HTML/XML",value:"markup"},{text:"JavaScript",value:"javascript"},{text:"CSS",value:"css"},{text:"PHP",value:"php"},{text:"Ruby",value:"ruby"},{text:"Python",value:"python"},{text:"Java",value:"java"},{text:"C",value:"c"},{text:"C#",value:"csharp"},{text:"C++",value:"cpp"}]},N=function(e,t){return x(e).fold(function(){return t},function(e){var n=e.className.match(/language-(\w+)/);return n?n[1]:t})},O=(g="function",function(e){return function(e){if(null===e)return"null";var t=typeof e;return"object"===t&&(Array.prototype.isPrototypeOf(e)||e.constructor&&"Array"===e.constructor.name)?"array":"object"===t&&(String.prototype.isPrototypeOf(e)||e.constructor&&"String"===e.constructor.name)?"string":t}(e)===g}),P=Array.prototype.slice,z=(O(Array.from)&&Array.from,{open:function(e){var t,n=_(e),a=(t=n,0===t.length?k.none():k.some(t[0])).fold(function(){return""},function(e){return e.value}),r=N(e,a),i=A(e);e.windowManager.open({title:"Insert/Edit Code Sample",size:"large",body:{type:"panel",items:[{type:"selectbox",name:"language",label:"Language",items:n},{type:"textarea",name:"code",label:"Code view"}]},buttons:[{type:"cancel",name:"cancel",text:"Cancel"},{type:"submit",name:"save",text:"Save",primary:!0}],initialData:{language:r,code:i},onSubmit:function(t){var n=t.getData();S(e,n.language,n.code),t.close()}})}}),W={register:function(e){e.addCommand("codesample",function(){var t=e.selection.getNode();e.selection.isCollapsed()||p.isCodeSample(t)?z.open(e):e.formatter.toggle("code")})}},j={setup:function(e){var t=e.$;e.on("PreProcess",function(e){t("pre[contenteditable=false]",e.node).filter(p.trimArg(p.isCodeSample)).each(function(e,n){var a=t(n),r=n.textContent;a.attr("class",t.trim(a.attr("class"))),a.removeAttr("contentEditable"),a.empty().append(t("<code></code>").each(function(){this.textContent=r}))})}),e.on("SetContent",function(){var n=t("pre").filter(p.trimArg(p.isCodeSample)).filter(function(e,t){return"false"!==t.contentEditable});n.length&&e.undoManager.transact(function(){n.each(function(n,a){t(a).find("br").each(function(t,n){n.parentNode.replaceChild(e.getDoc().createTextNode("\n"),n)}),a.contentEditable="false",a.innerHTML=e.dom.encode(a.textContent),o.highlightElement(a),a.className=t.trim(a.className)})})})}},T={register:function(e){e.ui.registry.addToggleButton("codesample",{icon:"code-sample",tooltip:"Insert/edit code sample",onAction:function(){return z.open(e)},onSetup:function(t){var n=function(){t.setActive(function(e){var t=e.selection.getStart();return e.dom.is(t,"pre.language-markup")}(e))};return e.on("NodeChange",n),function(){return e.off("NodeChange",n)}}}),e.ui.registry.addMenuItem("codesample",{text:"Code sample...",icon:"code-sample",onAction:function(){return z.open(e)}})}};t.add("codesample",function(e){j.setup(e),T.register(e),W.register(e),e.on("dblclick",function(t){p.isCodeSample(t.target)&&z.open(e)})})}(window);