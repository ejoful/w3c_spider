var AjaxDo = function () {

	//* END:CORE HANDLERS *//
	/*给a标签绑定 dialog事件 */
	function bindDialog(){
		$(this).unbind('click').click(function(event){
			var $this   = $(this);
			
			var predo = $this.attr("predo");
			var predofn;
			if(predo){
				predofn = eval('(' + predo + ')');
				predofn.call(this);
			}
			var title   = $this.attr("title") || $this.text();
			var rel     = $this.attr("rel") || "_blank";
			var data    = $this.attr("data") || "";
			var options = {};
			var w       = $this.attr("width");
			var h       = $this.attr("height");
			if (w) options.width = w;
			if (h) {
				if (h == 'window') {
					options.height = $(window).width();
				}else{
					options.height = h;
				}
			}
			options.max           = eval($this.attr("max") || "false");
			options.mask          = eval($this.attr("mask") || "false");
			options.maxable       = eval($this.attr("maxable") || "true");
			options.minable       = eval($this.attr("minable") || "true");
			options.fresh         = eval($this.attr("fresh") || "true");
			options.resizable     = eval($this.attr("resizable") || "true");
			options.drawable      = eval($this.attr("drawable") || "true");
			options.close         = eval($this.attr("close") || "");
			options.param         = $this.attr("param") || "";
			options.iframe        = eval($this.attr("iframe") || "false");
			options.fullH        = eval($this.attr("fullH") || "false");
			options.closecallback = $this.attr("closecallback") || "false";

			
			var url = unescape($this.attr("href")).replaceTmById($(event.target).parents(".unitBox:first"));
			AjaxDo.debug(url);
			if (!url.isFinishedTm()) {
				alertMsg.error($this.attr("warn") || AjaxDo.msg("alertSelectMsg"));
				return false;
			}
			//补充数据，采用get方式传递
			if (data != '') {
				url += '?' + data;
			};
			$.pdialog.open(url, rel, title, options);
			
			return false;
		});
	}

    return {
		eventType: {
			pageClear:"pageClear",	// 用于重新ajaxLoad、关闭nabTab, 关闭dialog时，去除xheditor等需要特殊处理的资源
			resizeGrid:"resizeGrid"	// 用于窗口或dialog大小调整
		},
		statusCode: {unlogin:100, ok:200, error:300, timeout:301},
		ui:{sbar:true},
		frag:{}, //page fragment
		_msg:{}, //alert message
		_set:{debug:false},
		ajaxbg:$("#background,#progressBar"),
		
		initUI: function(_box){
			//if($.isFunction(initUI)) initUI();
			var $p = $(_box || document);

			//tables
			//$("table.table", $p).jTable();

			//tabsPageHeader
			if($.fn.hoverClass){
				$("div.tabsHeader li, div.tabsPageHeader li, div.accordionHeader, div.accordion", $p).hoverClass("hover");
			}
			

			// navTab,通过ajax获取页面，并放置到多页面容器中
			$("a[target=navTab]", $p).each(function(){
				$(this).unbind('click').click(function(event){
					var $this    = $(this);
					var predo = $this.attr("predo");
					var predofn;
					if(predo){
						predofn = eval('(' + predo + ')');
						predofn.call(this);
					}
					var title    = $this.attr("title") || $this.text();
					var tabid    = $this.attr("rel") || "_blank";
					var data     = $this.attr("data") || "";
					var fresh    = eval($this.attr("fresh") || "true");
					var close    = eval($this.attr("close") || "false");
					var closebtn = eval($this.attr("close") || "false");
					var external = eval($this.attr("external") || "false");
					var header   = $this.attr("header") || "show";
					var footer   = $this.attr("footer") || "show";
					var animate  = $this.attr("data-animation") || 0;
					var url = unescape($this.attr("href")).replaceTmById($(event.target).parents(".unitBox:first"));
					AjaxDo.debug(url);
					
					if (!url.isFinishedTm()) {
						alertMsg.error($this.attr("warn") || AjaxDo.msg("alertSelectMsg"));
						return false;
					}
					//补充数据，采用get方式传递
					if (data != '') {
						url += '?' + data;
					};
					
					//打开页面
					navTab.openTab(tabid, url,{title:title, fresh:fresh, external:external,header:header,footer:footer,close:close,closebtn:closebtn,animate:animate});
					event.preventDefault();
				});
			});

			//dialogs，通过ajax获取页面，并放置到弹出窗口容器中
			$("a[target=dialog]", $p).each(function(){
				bindDialog.call(this);
			});

			//通过ajax方式获取页面，并加载到指定target标记的id页面容器中
			$("a[action=ajaxPage]", $p).each(function(){
				$(this).unbind('click').click(function(event){
					var $this   = $(this);
					var target  = $this.attr("target");
					var $target = $("#"+target);
					var fresh   = eval($this.attr("fresh") || "true");
					var view    = $this.attr("view") || "show";
					var iframe  = eval($this.attr("iframe") || "false");
					if (target) {
						if(iframe){
							var ih = $target.height() || "100px";
							var externalFrag = '<iframe src="{url}" style="width:100%;height:{height};" frameborder="no" border="0" marginwidth="0" marginheight="0"></iframe>';
							$target.html(externalFrag.replaceAll("{url}", $this.attr("href")).replaceAll("{height}", ih+"px"));
						}else{
							$target.loadUrl($this.attr("href"), {}, function(){
								$target.find("[layoutH]").layoutH();
							});
						}
					}

					if(view == 'hide'){
						$target.hide();
					}

					event.preventDefault();
				});
			});

			//日期选择器
			if ($.fn.datepicker){
				$('input.date', $p).each(function(){
					var $this = $(this);
					var opts = {};
					if ($this.attr("dateFmt")) opts.pattern = $this.attr("dateFmt");
					if ($this.attr("minDate")) opts.minDate = $this.attr("minDate");
					if ($this.attr("maxDate")) opts.maxDate = $this.attr("maxDate");
					if ($this.attr("mmStep")) opts.mmStep = $this.attr("mmStep");
					if ($this.attr("ssStep")) opts.ssStep = $this.attr("ssStep");
					$this.datepicker(opts);
				});
			};
			
			//tables
			//$("table.table", $p).jTable();
			// ajax方式调取数据
			if ($.fn.ajaxTodo) $("a[action=ajaxTodo]", $p).ajaxTodo();
			if ($.fn.ajaxTodo) $("a[action=ajaxData]", $p).ajaxTodo();
			// 这里放其他第三方jQuery插件...
			//App.initAjax();
			//App.refresh();
		},
		initEnv: function(){
			//if($.isFunction(initEnv)) initEnv();
			$.browser.msie = /msie/.test(navigator.userAgent.toLowerCase());
			if ( $.browser.msie && /6.0/.test(navigator.userAgent) ) {
				try {
					document.execCommand("BackgroundImageCache", false, true);
				}catch(e){}
			}
			//清理浏览器内存,只对IE起效
			if ($.browser.msie) {
				window.setInterval("CollectGarbage();", 10000);
			}
			
			var ajaxbg = $("#background,#progressBar");
			ajaxbg.hide();
			
			$(document).ajaxStart(function(){
				ajaxbg.show();
			}).ajaxStop(function(){
				ajaxbg.hide();
			});
			
			if($("#navTab").html() !== undefined){
				navTab.init();
			}
			
			setTimeout(function(){
				//App.initIScroll();
				//AjaxDo.initLayout();
				
				AjaxDo.initUI();
				// navTab styles
				var jTabsPH = $("div.tabsPageHeader");
				jTabsPH.find(".tabsLeft").hoverClass("tabsLeftHover");
				jTabsPH.find(".tabsRight").hoverClass("tabsRightHover");
				jTabsPH.find(".tabsMore").hoverClass("tabsMoreHover");
			
			}, 10);
		},
		initLayout: function(){
			var iContentW = $(window).width() - (AjaxDo.ui.sbar ? $("#sidebar").width() + 10 : 34) - 5;
			var iContentH = $(window).height() - $(".header").height() - 5;

			$(".page-container").height(iContentH);
			$(".sidebar-menu").height(iContentH-23);
			$(".page-content-body").height(iContentH);

			$("#container").width(iContentW);
			$("#container .tabsPageContent").height(iContentH - 34).find("[layoutH]").layoutH();
		},
		msg:function(key, args){
			var _format = function(str,args) {
				args = args || [];
				var result = str || "";
				for (var i = 0; i < args.length; i++){
					result = result.replace(new RegExp("\\{" + i + "\\}", "g"), args[i]);
				}
				return result;
			}
			return _format(this._msg[key], args);
		},
		debug:function(msg){
			if (this._set.debug) {
				if (typeof(console) != "undefined") console.log(msg);
				else alert(msg);
			}
		},
		alertMsg:function(msg,msgtype){
			var type = msgtype || 'error';
			//if (typeof(console) != "undefined") console.log(msg);
			if (type == 'error') {
				toastr.error(msg,'',{"positionClass":'toast-top-center'});
			}else{
				toastr.success(msg,'',{"positionClass":'toast-top-center'});
			}
		},
		reload:function(){
			setTimeout(function(){
				window.location.reload();
			},500);
		},
		/*
		 * json to string
		 */
		obj2str:function(o) {
			var r = [];
			if(typeof o =="string") return "\""+o.replace(/([\'\"\\])/g,"\\$1").replace(/(\n)/g,"\\n").replace(/(\r)/g,"\\r").replace(/(\t)/g,"\\t")+"\"";
			if(typeof o == "object"){
				if(!o.sort){
					for(var i in o)
						r.push(i+":"+AjaxDo.obj2str(o[i]));
					if(!!document.all && !/^\n?function\s*toString\(\)\s*\{\n?\s*\[native code\]\n?\s*\}\n?\s*$/.test(o.toString)){
						r.push("toString:"+o.toString.toString());
					}
					r="{"+r.join()+"}"
				}else{
					for(var i =0;i<o.length;i++) {
						r.push(AjaxDo.obj2str(o[i]));
					}
					r="["+r.join()+"]"
				}
				return r;
			}
			return o.toString();
		},
		jsonEval:function(data) {
			try{
				if ($.type(data) == 'string')
					return eval('(' + data + ')');
				else return data;
			} catch (e){
				return {};
			}
		},
		ajaxTodo:function(url, callback){
			var $callback = callback || AjaxDo.navTabAjaxDone;
			if (! $.isFunction($callback)) $callback = eval('(' + callback + ')');
			url = url + (/\?/.test(url) ? "&" : "?")+ "_hash=" + $.cookie("ypre_saltkey");
			$.ajax({
				type:'POST',
				url:url,
				dataType:"json",
				cache: false,
				success: $callback,
				error: AjaxDo.ajaxError
			});
		},
		ajaxError:function(xhr, ajaxOptions, thrownError){
			var msg = "Http status: " + xhr.status + " " + xhr.statusText + "\najaxOptions: " + ajaxOptions + "\n";
			if (toastr) {
				toastr.error(msg);
			} else {
				alert(msg);
			}
		},
		ajaxDone:function(json){
			if(json.statusCode == AjaxDo.statusCode.error) {
				if(json.message && AjaxDo.alertMsg) AjaxDo.alertMsg(json.message);
			} else if (json.statusCode == AjaxDo.statusCode.timeout) {
				if(AjaxDo.alertMsg) AjaxDo.alertMsg(json.message || AjaxDo.msg("sessionTimout"), {okCall:AjaxDo.loadLogin});
				else AjaxDo.loadLogin();
			} else {
				if(json.message && AjaxDo.alertMsg) AjaxDo.alertMsg(json.message,'success');
			};

		},
		/**
		 * 处理两种查询方式
		 * @param {Object} form
		 */
		search : function(form, targetType){
			if (targetType == "dialog") dialogSearch(form);
			else navTabSearch(form);
			return false;
		},
		/**
		 * 处理navTab上的查询, 会重新载入当前navTab
		 * @param {Object} form
		 */
		navTabSearch : function(form, navTabId){
			var $form = $(form);
			//if (form[AjaxDo.pageInfo.pageNum]) form[AjaxDo.pageInfo.pageNum].value = 1;
			navTab.reload($form.attr('action'), {data: $form.serializeArray(), navTabId:navTabId});
			return false;
		},
		/**
		 * 处理dialog弹出层上的查询, 会重新载入当前dialog
		 * @param {Object} form
		 */
		dialogSearch : function(form){
			var $form = $(form);
			//if (form[AjaxDo.pageInfo.pageNum]) form[AjaxDo.pageInfo.pageNum].value = 1;
			$.pdialog.reload($form.attr('action'), {data: $form.serializeArray()});
			return false;
		},
		/**
		 * 处理div上的局部查询, 会重新载入指定div
		 * @param {Object} form
		 */
		divSearch : function(form, rel){
			var $form = $(form);
			if (form[DWZ.pageInfo.pageNum]) form[DWZ.pageInfo.pageNum].value = 1;
			if (rel) {
				var $box = $("#" + rel);
				$box.ajaxUrl({
					type:"POST", url:$form.attr("action"), data: $form.serializeArray(), callback:function(){
						$box.find("[layoutH]").layoutH();
					}
				});
			}
			return false;
		},
		/**
		 * 普通ajax表单提交
		 * @param {Object} form
		 * @param {Object} callback
		 * @param {String} confirmMsg 提示确认信息
		 */
		formCallback : function(form, callback, confirmMsg) {
			var $form = $(form);
			var _hash = $.cookie("ypre_saltkey");
			$form.append('<input type="hidden" name="_hash" value="'+_hash+'" />');
			
			if (!$form.valid()) {
				return false;
			}
			//console.log(callback);
			var _submitFn = function(){
				$.ajax({
					type: form.method || 'POST',
					url:$form.attr("action"),
					data:$form.serializeArray(),
					dataType:"json",
					cache: false,
					success: callback || AjaxDo.ajaxDone,
					error: AjaxDo.ajaxError
				});
			}
			
			if (confirmMsg) {
				if(confirm(confirmMsg)) _submitFn();
			} else {
				_submitFn();
			}
			
			return false;
		},
		/**
		 * 带文件上传的ajax表单提交
		 * @param {Object} form
		 * @param {Object} callback
		 */
		iframeCallback : function(form, callback){
			var $form = $(form), $iframe = $("#callbackframe");
			if(!$form.valid()) {return false;}

			if ($iframe.size() == 0) {
				$iframe = $("<iframe id='callbackframe' name='callbackframe' src='about:blank' style='display:none'></iframe>").appendTo("body");
			}
			if(!form.ajax) {
				$form.append('<input type="hidden" name="ajax" value="1" />');
			}
			form.target = "callbackframe";
			
			AjaxDo._iframeResponse($iframe[0], callback || AjaxDo.ajaxDone);
		},
		_iframeResponse : function(iframe, callback){
			var $iframe = $(iframe), $document = $(document);
			
			$document.trigger("ajaxStart");
			
			$iframe.bind("load", function(event){
				$iframe.unbind("load");
				$document.trigger("ajaxStop");
				
				if (iframe.src == "javascript:'%3Chtml%3E%3C/html%3E';" || // For Safari
					iframe.src == "javascript:'<html></html>';") { // For FF, IE
					return;
				}

				var doc = iframe.contentDocument || iframe.document;

				// fixing Opera 9.26,10.00
				if (doc.readyState && doc.readyState != 'complete') return; 
				// fixing Opera 9.64
				if (doc.body && doc.body.innerHTML == "false") return;
			   
				var response;
				
				if (doc.XMLDocument) {
					// response is a xml document Internet Explorer property
					response = doc.XMLDocument;
				} else if (doc.body){
					try{
						response = $iframe.contents().find("body").text();
						response = jQuery.parseJSON(response);
					} catch (e){ // response is html document or plain text
						response = doc.body.innerHTML;
					}
				} else {
					// response is a xml document
					response = doc;
				}
				
				callback(response);
			});
		},
		/**
		 * navTabAjaxDone是AjaxDo框架中预定义的表单提交回调函数．
		 * 服务器转回navTabId可以把那个navTab标记为reloadFlag=1, 下次切换到那个navTab时会重新载入内容. 
		 * callbackType如果是closeCurrent就会关闭当前tab
		 * 只有callbackType="forward"时需要forwardUrl值
		 * navTabAjaxDone这个回调函数基本可以通用了，如果还有特殊需要也可以自定义回调函数.
		 * 如果表单提交只提示操作是否成功, 就可以不指定回调函数. 框架会默认调用AjaxDo.ajaxDone()
		 * <form action="/user.do?method=save" onsubmit="return formCallback(this, navTabAjaxDone)">
		 * 
		 * form提交后返回json数据结构statusCode=AjaxDo.statusCode.ok表示操作成功, 做页面跳转等操作. statusCode=AjaxDo.statusCode.error表示操作失败, 提示错误原因. 
		 * statusCode=AjaxDo.statusCode.timeout表示session超时，下次点击时跳转到AjaxDo.loginUrl
		 * {"statusCode":"200", "message":"操作成功", "navTabId":"navNewsLi", "forwardUrl":"", "callbackType":"closeCurrent", "rel"."xxxId"}
		 * {"statusCode":"300", "message":"操作失败"}
		 * {"statusCode":"301", "message":"会话超时"}
		 * 
		 */
		navTabAjaxDone: function(json){
			AjaxDo.ajaxDone(json);
			if (json.statusCode == AjaxDo.statusCode.ok){

				if (json.dotype.close == "current") {
					setTimeout(function(){navTab.closeCurrentTab(json.navTabId);}, 100);
				}
				if (json.dotype.openUrl != ''){
					navTab.openTab('nav_newtab', json.dotype.openUrl, {title:'=='});
				}
				
				if (json.dotype.reloadId != ''){ //把指定navTab页面标记为需要“重新载入”。注意navTabId不能是当前navTab页面的
					navTab.reloadFlag(json.dotype.reloadId);
				} 

				if(json.dotype.reload == 'currentTab') { //重新载入当前navTab页面
					navTab.reloadCurrentTab();
					var $pagerForm = $("#pagerForm", navTab.getCurrentPanel());
					var args = $pagerForm.size()>0 ? $pagerForm.serializeArray() : {}
					AjaxDo.PageReload({data:args, rel:json.rel});
				}else if (json.dotype.reload != '') {//在当前navTab页面载入新的其他页面
					navTab.reload(json.dotype.reload);
				} 
				if ("forwardConfirm" == callback) {
					if(confirm(json.confirmMsg || AjaxDo.msg("forwardConfirmMsg"))) {
						navTab.reload(json.forwardUrl);
					}else{
						navTab.closeCurrentTab(json.navTabId);
					};
				} else if (json.callback != ''){
					var callback = json.callback;
					if (! $.isFunction(callback)) callback = eval('(' + json.callback + ')');
					if (json.data != '') {
						//var returnJson = AjaxDo.jsonEval(json.json);
						callback(json.data);
					}else {
						callback();
					}
				};
			}
		},
		/**
		 * dialog上的表单提交回调函数
		 * 当前navTab页面有pagerForm就重新加载
		 * 服务器转回navTabId，可以重新载入指定的navTab. statusCode=AjaxDo.statusCode.ok表示操作成功, 自动关闭当前dialog
		 * 
		 * form提交后返回json数据结构,json格式和navTabAjaxDone一致
		 */
		dialogAjaxDone : function(json){
			AjaxDo.ajaxDone(json);
			if (json.statusCode == AjaxDo.statusCode.ok){
				if (json.dotype.openId != ''){
					navTab.reload(json.forwardUrl, {navTabId: json.dotype.openId});
				} 
				if(json.dotype.reload == 'currentTab' && json.data.reload != "false"){
					navTab.reloadCurrentTab();
					var $pagerForm = $("#pagerForm", navTab.getCurrentPanel());
					var args = $pagerForm.size()>0 ? $pagerForm.serializeArray() : {}
					AjaxDo.PageReload({data:args, rel:json.rel});
				}
				if (json.dotype.close == "current") {
					$.pdialog.closeCurrent();
				}
				if (json.dotype.openUrl != ''){
					navTab.openTab('dialog_newtab', json.dotype.openUrl, {title:'=='});
				}
				if (json.callback != ''){
					var callback = json.callback;
					if (! $.isFunction(callback)) callback = eval('(' + json.callback + ')');
					if (json.data != '') {
						//var returnJson = AjaxDo.jsonEval(json.json);
						callback(json.data);
					}else {
						callback();
					}
				};
			}
		},
		/**
		 * 处理navTab或dialog页面刷新 
		 * targetType: navTab 或 dialog
		 * rel: 可选 用于局部刷新div id号
		 * data: pagerForm参数 {pageNum:"n", numPerPage:"n", orderField:"xxx", orderDirection:""}
		 * callback: 加载完成回调函数
		 */
		PageReload : function(options){
			var op = $.extend({ targetType:"navTab", rel:"", data:{pageNum:"", numPerPage:"", orderField:"", orderDirection:""}, callback:null}, options);
			var $parent = op.targetType == "dialog" ? $.pdialog.getCurrent() : navTab.getCurrentPanel();

			if (op.rel) {
				var $box = $parent.find("#" + op.rel);
				var form = _getPagerForm($box, op.data);
				if (form) {
					$box.ajaxUrl({
						type:"POST", url:$(form).attr("action"), data: $(form).serializeArray(), callback:function(){
							$box.find("[layoutH]").layoutH();
						}
					});
				}
			} else if(false) {
				var form = _getPagerForm($parent, op.data);
				var params = $(form).serializeArray();
				alert($(form).attr("action"));
				if (op.targetType == "dialog") {
					if (form) $.pdialog.reload($(form).attr("action"), {data: params, callback: op.callback});
				} else {
					if (form) navTab.reload($(form).attr("action"), {data: params, callback: op.callback});
				}
				
			}
		},
		bindAjaxTodo:function(){
			if ($.fn.ajaxTodo) $("a[action=ajaxTodo]", document).ajaxTodo();
		},
		bindDialog:function(){
			$("a[target=dialog]").each(function(){
				bindDialog.call(this);
			});
		}

	}
}();

var navTab = {
	componentBox: null, // tab component. contain tabBox, prevBut, nextBut, panelBox
	_tabBox: null,
	_prevBut: null,
	_nextBut: null,
	_panelBox: null,
	_moreBut:null,
	_moreBox:null,
	_title:null,
	_currentIndex: 0,
	_isAnimating:false,
	_animation:0,
	
	_op: {stNavTab:"#navTab", stTabBox:"#navTab-tab", stPanelBox:"#navTab-panel",stTitle:"#navTab-title", mainTabId:"main", close$:"a.close", prevClass:".tabsLeft", nextClass:".tabsRight", stMore:".tabsMore", stMoreLi:"ul.tabsMoreList"},
	
	init: function(options){
		if ($.History) $.History.init("#navTab");
		var $this = this;
		$.extend(this._op, options);

		this.componentBox = $(this._op.stNavTab);
		this._title = this.componentBox.find(this._op.stTitle)
		this._tabBox = this.componentBox.find(this._op.stTabBox);
		this._panelBox = this.componentBox.find(this._op.stPanelBox);
		this._prevBut = this.componentBox.find(this._op.prevClass);
		this._nextBut = this.componentBox.find(this._op.nextClass);
		this._moreBut = this.componentBox.find(this._op.stMore);
		this._moreBox = this.componentBox.find(this._op.stMoreLi);

		this._prevBut.click(function(event) {$this._scrollPrev()});
		this._nextBut.click(function(event) {$this._scrollNext()});
		this._moreBut.click(function(){
			$this._moreBox.show();
			return false;
		});
		$(document).click(function(){$this._moreBox.hide()});
		
		this._contextmenu(this._tabBox);
		this._contextmenu(this._getTabs());
		
		this._init();
		this._ctrlScrollBut();
	},
	_init: function(initShow){
		var $this = this;
		var doSwitchTab = initShow || true;
		this._getTabs().each(function(iTabIndex){
			$(this).unbind("click").click(function(event){
				$this._switchTab(iTabIndex);
			});
			$(this).find(navTab._op.close$).unbind("click").click(function(){
				$this._closeTab(iTabIndex);
			});
		});
		this._getMoreLi().each(function(iTabIndex){
			$(this).find(">a").unbind("click").click(function(event){
				$this._switchTab(iTabIndex);
			});
		});

		this._switchTab(this._currentIndex);
	},
	_contextmenu:function($obj){ // navTab右键菜单
		var $this = this;
		$obj.contextMenu('navTabCM', {
			bindings:{
				reload:function(t,m){
					$this._reload(t, true);
				},
				closeCurrent:function(t,m){
					var tabId = t.attr("tabid");
					if (tabId) $this.closeTab(tabId);
					else $this.closeCurrentTab();
				},
				closeOther:function(t,m){
					var index = $this._indexTabId(t.attr("tabid"));
					$this._closeOtherTab(index > 0 ? index : $this._currentIndex);
				},
				closeAll:function(t,m){
					$this.closeAllTab();
				}
			},
			ctrSub:function(t,m){
				var mReload = m.find("[rel='reload']");
				var mCur = m.find("[rel='closeCurrent']");
				var mOther = m.find("[rel='closeOther']");
				var mAll = m.find("[rel='closeAll']");
				var $tabLi = $this._getTabs();
				if ($tabLi.size() < 2) {
					mCur.addClass("disabled");
					mOther.addClass("disabled");
					mAll.addClass("disabled");
				}
				if ($this._currentIndex == 0 || t.attr("tabid") == $this._op.mainTabId) {
					mCur.addClass("disabled");
					mReload.addClass("disabled");
				} else if ($tabLi.size() == 2) {
					mOther.addClass("disabled");
				}
				
			}
		});
	},
	
	_getTabs: function(){
		return this._tabBox.find("> li");
	},
	_getPanels: function(){
		return this._panelBox.find("> div");
	},
	_getMoreLi: function(){
		return this._moreBox.find("> li");
	},
	_getTab: function(tabid){
		var index = this._indexTabId(tabid);
		if (index >= 0) return this._getTabs().eq(index);
	},
	getPanel: function(tabid){
		var index = this._indexTabId(tabid);
		if (index >= 0) return this._getPanels().eq(index);
	},
	_getTabsW: function(iStart, iEnd){
		return this._tabsW(this._getTabs().slice(iStart, iEnd));
	},
	_tabsW:function($tabs){
		var iW = 0;
		$tabs.each(function(){
			iW += $(this).outerWidth(true);
		});
		return iW;
	},
	_indexTabId: function(tabid){
		if (!tabid) return -1;
		var iOpenIndex = -1;
		this._getTabs().each(function(index){
			if ($(this).attr("tabid") == tabid){iOpenIndex = index; return;}
		});
		return iOpenIndex;
	},
	_getLeft: function(){
		return this._tabBox.position().left;
	},
	_getScrollBarW: function(){
		return this.componentBox.width()-55;
	},
	
	_visibleStart: function(){
		var iLeft = this._getLeft(), iW = 0;
		var $tabs = this._getTabs();
		for (var i=0; i<$tabs.size(); i++){
			if (iW + iLeft >= 0) return i;
			iW += $tabs.eq(i).outerWidth(true);
		}
		return 0;
	},
	_visibleEnd: function(){
		var iLeft = this._getLeft(), iW = 0;
		var $tabs = this._getTabs();
		for (var i=0; i<$tabs.size(); i++){
			iW += $tabs.eq(i).outerWidth(true);
			if (iW + iLeft > this._getScrollBarW()) return i;
		}
		return $tabs.size();
	},
	_scrollPrev: function(){
		var iStart = this._visibleStart();
		if (iStart > 0){
			this._scrollTab(-this._getTabsW(0, iStart-1));
		}
	},
	_scrollNext: function(){
		var iEnd = this._visibleEnd();
		if (iEnd < this._getTabs().size()){
			this._scrollTab(-this._getTabsW(0, iEnd+1) + this._getScrollBarW());
		}	
	},
	_scrollTab: function(iLeft, isNext){
		var $this = this;
		this._tabBox.animate({ left: iLeft+'px' }, 200, function(){$this._ctrlScrollBut();});
	},
	_scrollCurrent: function(){ // auto scroll current tab
		var iW = this._tabsW(this._getTabs());
		if (iW <= this._getScrollBarW()){
			this._scrollTab(0);
		} else if (this._getLeft() < this._getScrollBarW() - iW){
			this._scrollTab(this._getScrollBarW()-iW);
		} else if (this._currentIndex < this._visibleStart()) {
			this._scrollTab(-this._getTabsW(0, this._currentIndex));
		} else if (this._currentIndex >= this._visibleEnd()) {
			this._scrollTab(this._getScrollBarW() - this._getTabs().eq(this._currentIndex).outerWidth(true) - this._getTabsW(0, this._currentIndex));
		}
	},
	_ctrlScrollBut: function(){
		var iW = this._tabsW(this._getTabs());
		if (this._getScrollBarW() > iW){
			this._prevBut.hide();
			this._nextBut.hide();
			this._tabBox.parent().removeClass("tabsPageHeaderMargin");
		} else {
			this._prevBut.show().removeClass("tabsLeftDisabled");
			this._nextBut.show().removeClass("tabsRightDisabled");
			this._tabBox.parent().addClass("tabsPageHeaderMargin");
			if (this._getLeft() >= 0){
				this._prevBut.addClass("tabsLeftDisabled");
			} else if (this._getLeft() <= this._getScrollBarW() - iW) {
				this._nextBut.addClass("tabsRightDisabled");
			} 
		}
	},

	switchTab: function(tabid) {
		var index = this._indexTabId(tabid);
		this._switchTab(index);
	},
	
	_switchTab: function(iTabIndex){
		var $tab = this._getTabs().removeClass("selected").eq(iTabIndex).addClass("selected");
		this._getPanels().hide().eq(iTabIndex).show();
		this._getMoreLi().removeClass("selected").eq(iTabIndex).addClass("selected");
		//切换效果
		if((this._animation > 0)&&(this._currentIndex != iTabIndex)){
			var $currPage = this._getPanels().eq(this._currentIndex);
			var $nextPage = this._getPanels().eq(iTabIndex);
			this._animate(this._animation,{currPage:$currPage, nextPage:$nextPage});
		}

		this._currentIndex = iTabIndex;
		
		this._scrollCurrent();
		this._reload($tab);
	},

	_resetPage: function( $currPage, $nextPage ) {
		$currPage.attr( 'class', "page unitBox" );
		$nextPage.attr( 'class', "page unitBox" );
		this._isAnimating = false;
		this._animation = 0;
	},

	_animate: function(animation,options){
		var op = $.extend({currPage:"", nextPage:""}, options);

		var animation = parseInt(animation);//切换的类型
		var $currPage=op.currPage,$nextPage = op.nextPage,
			outClass = '', inClass = '';

		//是否正在切换中
		if( this._isAnimating ) {
			return false;
		}
		this._isAnimating = true;

		switch( animation ) {

			case 1:
				outClass = 'pt-page-moveToLeft';
				inClass = 'pt-page-moveFromRight';
				break;
			case 2:
				outClass = 'pt-page-moveToRight';
				inClass = 'pt-page-moveFromLeft';
				break;
			case 3:
				outClass = 'pt-page-moveToTop';
				inClass = 'pt-page-moveFromBottom';
				break;
			case 4:
				outClass = 'pt-page-moveToBottom';
				inClass = 'pt-page-moveFromTop';
				break;
			case 5:
				outClass = 'pt-page-fade';
				inClass = 'pt-page-moveFromRight pt-page-ontop';
				break;
			case 6:
				outClass = 'pt-page-fade';
				inClass = 'pt-page-moveFromLeft pt-page-ontop';
				break;
			case 7:
				outClass = 'pt-page-fade';
				inClass = 'pt-page-moveFromBottom pt-page-ontop';
				break;
			case 8:
				outClass = 'pt-page-fade';
				inClass = 'pt-page-moveFromTop pt-page-ontop';
				break;
			case 9:
				outClass = 'pt-page-moveToLeftFade';
				inClass = 'pt-page-moveFromRightFade';
				break;
			case 10:
				outClass = 'pt-page-moveToRightFade';
				inClass = 'pt-page-moveFromLeftFade';
				break;
			case 11:
				outClass = 'pt-page-moveToTopFade';
				inClass = 'pt-page-moveFromBottomFade';
				break;
			case 12:
				outClass = 'pt-page-moveToBottomFade';
				inClass = 'pt-page-moveFromTopFade';
				break;
			case 13:
				outClass = 'pt-page-moveToLeftEasing pt-page-ontop';
				inClass = 'pt-page-moveFromRight';
				break;
			case 14:
				outClass = 'pt-page-moveToRightEasing pt-page-ontop';
				inClass = 'pt-page-moveFromLeft';
				break;
			case 15:
				outClass = 'pt-page-moveToTopEasing pt-page-ontop';
				inClass = 'pt-page-moveFromBottom';
				break;
			case 16:
				outClass = 'pt-page-moveToBottomEasing pt-page-ontop';
				inClass = 'pt-page-moveFromTop';
				break;
		}

		var support = true,
			animEndEventName = "animationend",
			endCurrPage = false,
            endNextPage = false;

		$currPage.addClass( outClass ).on( animEndEventName, function() {
			$currPage.off( animEndEventName );
			//console.log("do here");
			endCurrPage = true;
			if( endNextPage ) {
				this._resetPage( $currPage, $nextPage );
			}
		} );

		$nextPage.addClass( inClass ).on( animEndEventName, function() {
			$nextPage.off( animEndEventName );
			endNextPage = true;
			if( endCurrPage ) {
				this._resetPage( $currPage, $nextPage );
			}
		} );

		if( !support ) {
			this._resetPage( $currPage, $nextPage );
		}

	},
			
	_closeTab: function(index, openTabid){

		this._getTabs().eq(index).remove();
		this._getPanels().eq(index).trigger(AjaxDo.eventType.pageClear).remove();
		this._getMoreLi().eq(index).remove();
		if (this._currentIndex >= index) this._currentIndex--;
		
		if (openTabid) {
			var openIndex = this._indexTabId(openTabid);
			if (openIndex >= 0) this._currentIndex = openIndex;
		}
		
		this._init();
		this._scrollCurrent();
		this._reload(this._getTabs().eq(this._currentIndex));
	},
	closeTab: function(tabid, openTabid){
		var index = this._indexTabId(tabid);
		if (index > 0) { this._closeTab(index, openTabid); }
	},
	closeCurrentTab: function(openTabid){ //openTabid 可以为空，默认关闭当前tab后，打开最后一个tab
		if (this._currentIndex > 0) {this._closeTab(this._currentIndex, openTabid);}
	},
	closeAllTab: function(){
		this._getTabs().filter(":gt(0)").remove();
		this._getPanels().filter(":gt(0)").trigger(AjaxDo.eventType.pageClear).remove();
		this._getMoreLi().filter(":gt(0)").remove();
		this._currentIndex = 0;
		this._init();
		this._scrollCurrent();
	},
	_closeOtherTab: function(index){
		index = index || this._currentIndex;
		if (index > 0) {
			var str$ = ":eq("+index+")";
			this._getTabs().not(str$).filter(":gt(0)").remove();
			this._getPanels().not(str$).filter(":gt(0)").trigger(AjaxDo.eventType.pageClear).remove();
			this._getMoreLi().not(str$).filter(":gt(0)").remove();
			this._currentIndex = 1;
			this._init();
			this._scrollCurrent();
		} else {
			this.closeAllTab();
		}
	},

	_loadUrlCallback: function($panel){
		$panel.find("[layoutH]").layoutH();
		$panel.find(":button.closeTab").click(function(){
			navTab.closeCurrentTab();
		});
	},
	_reload: function($tab, flag){
		flag = flag || $tab.data("reloadFlag");
		var url = $tab.attr("url");
		if (flag && url) {
			$tab.data("reloadFlag", null);
			var $panel = this.getPanel($tab.attr("tabid"));
			
			if ($tab.hasClass("external")){
				navTab.openExternal(url, $panel);
			}else {
				//获取pagerForm参数
				var $pagerForm = $("#pagerForm", $panel);
				var args = $pagerForm.size()>0 ? $pagerForm.serializeArray() : {}
				$panel.loadUrl(url, args, function(){navTab._loadUrlCallback($panel);});
			}
		}
	},
	reloadFlag: function(tabid){
		var $tab = this._getTab(tabid);
		if ($tab){
			if (this._indexTabId(tabid) == this._currentIndex) this._reload($tab, true);
			else $tab.data("reloadFlag", 1);
		}
	},
	reloadCurrentTab: function(){
		var index = this._currentIndex;
		if (index >= 0) {
			$tab = this._getTabs().eq(index);
			this._reload($tab, true);
		}
	},
	reload: function(url, options){
		var op = $.extend({data:{}, navTabId:"", callback:null}, options);
		var $tab = op.navTabId ? this._getTab(op.navTabId) : this._getTabs().eq(this._currentIndex);
		var $panel =  op.navTabId ? this.getPanel(op.navTabId) : this._getPanels().eq(this._currentIndex);
		
		if ($panel){
			if (!url) {
				url = $tab.attr("url");
			}
			if (url) {
				if ($tab.hasClass("external")) {
					navTab.openExternal(url, $panel);
				} else {
					if ($.isEmptyObject(op.data)) { //获取pagerForm参数
						var $pagerForm = $("#pagerForm", $panel);
						op.data = $pagerForm.size()>0 ? $pagerForm.serializeArray() : {}
					}
					
					$panel.ajaxUrl({
						type:"POST", url:url, data:op.data, callback:function(response){
							navTab._loadUrlCallback($panel);
							if ($.isFunction(op.callback)) op.callback(response);
						}
					});
				}
			}
		}
	},
	getCurrentPanel: function() {
		return this._getPanels().eq(this._currentIndex);
	},
	checkTimeout:function(){
		var json = AjaxDo.jsonEval(this.getCurrentPanel().html());
		if (json && json.statusCode == AjaxDo.statusCode.timeout) this.closeCurrentTab();
	},
	openExternal:function(url, $panel){
		var ih = navTab.componentBox.height()- 5;
		var externalFrag = '<iframe src="{url}" style="width:100%;height:{height};" frameborder="no" border="0" marginwidth="0" marginheight="0"></iframe>';
		$panel.html(externalFrag.replaceAll("{url}", url).replaceAll("{height}", ih+"px"));
	},
	/**
	 * 
	 * @param {Object} tabid
	 * @param {Object} url
	 * @param {Object} params: title, data, fresh
	 */
	openTab: function(tabid, url, options){ //if found tabid replace tab, else create a new tab.
		var op = $.extend({title:"", data:{}, fresh:true, external:false, close:false,closebtn:false,animate:0, header:"show", footer:"show"}, options);

		var iOpenIndex = this._indexTabId(tabid);
		/*
		//是否显示头部导航
		if (op.header == "show"){
			App.showHeaderNavbar();
		}else if(op.header == "hide"){
			App.hideHeaderNavbar();
		}
		//是否关闭底部导航
		if (op.footer == "hide"){
			App.hideFooterBar();
		}else{
			App.showFooterBar();
		}
		*/
		//是否关闭当前页面，并回到tabid页面
		if (op.close){
			navTab.closeCurrentTab(tabid);
			return;
		}
		//是否使用页面切换效果
		if (op.animate > 0){
			this._animation = op.animate;
		}

		if (iOpenIndex >= 0){
			var $tab = this._getTabs().eq(iOpenIndex);
			var span$ = $tab.attr("tabid") == this._op.mainTabId ? "> span > span" : "> span";
			$tab.find(">a").attr("title", op.title).find(span$).html(op.title);
			this._title.text(op.title);
			var $panel = this._getPanels().eq(iOpenIndex);
			if(op.fresh || $tab.attr("url") != url) {
				$tab.attr("url", url);
				if (op.external) {
					$tab.addClass("external");
					navTab.openExternal(url, $panel);
				} else if(url.isExternalUrl()){
					$tab.removeClass("external");
					$panel.ajaxJson({
						type:"GET", url:url, datafor:"pageUI", data:op.data, callback:function(){
							if(op.callback != undefined){
								op.callback();
							}
							navTab._loadUrlCallback($panel);
						}
					});
				} else {
					$tab.removeClass("external");
					$panel.ajaxUrl({
						type:"GET", url:url, data:op.data, callback:function(){
							if(op.callback != undefined){
								op.callback();
							}
							navTab._loadUrlCallback($panel);
						}
					});
				}
			}
			this._currentIndex = iOpenIndex;
		} else {
			var closebtnClass = op.closebtn?'closebtn':'';
			var tabFrag = '<li tabid="#tabid#"><a href="javascript:" title="#title#" class="#tabid#"><span>#title#</span></a><a href="javascript:;" class="close navTabClose '+closebtnClass+'">close</a></li>';
			this._tabBox.append(tabFrag.replaceAll("#tabid#", tabid).replaceAll("#title#", op.title));
			this._panelBox.append('<div class="page unitBox"></div>');
			this._moreBox.append('<li><a href="javascript:" title="#title#">#title#</a></li>'.replaceAll("#title#", op.title));
			this._title.text(op.title);

			var $tabs = this._getTabs();
			var $tab = $tabs.filter(":last");
			var $panel = this._getPanels().filter(":last");
			
			if (op.external) {
				$tab.addClass("external");
				navTab.openExternal(url, $panel);
			} else if(url.isExternalUrl()){
				$tab.removeClass("external");
				$panel.ajaxJson({
					type:"GET", url:url, datafor:"pageUI", data:op.data, callback:function(){
						if(op.callback != undefined){
							op.callback();
						}
						navTab._loadUrlCallback($panel);
					}
				});
			} else {
				$tab.removeClass("external");
				$panel.ajaxUrl({
					type:"GET", url:url, data:op.data, callback:function(){
						if(op.callback != undefined){
							op.callback();
						}
						navTab._loadUrlCallback($panel);
					}
				});
			}
			
			if ($.History) {
				setTimeout(function(){
					$.History.addHistory(tabid, function(tabid){
						var i = navTab._indexTabId(tabid);
						if (i >= 0) navTab._switchTab(i);
					}, tabid);
				}, 10);
			}
				
			this._currentIndex = $tabs.size() - 1;
			this._contextmenu($tabs.filter(":last").hoverClass("hover"));
		}

		this._init();
		this._scrollCurrent();
		this._getTabs().eq(this._currentIndex).attr("url", url);
	}
};
//navTab右键菜单功能
(function($){
	var menu, shadow, hash;
	$.fn.extend({
		contextMenu: function(id, options){
			var op = $.extend({
				    shadow : true,
				    bindings:{},
					ctrSub:null
				}, options
			);
			
			if (!menu) {
				menu = $('<div id="contextmenu"></div>').appendTo('body').hide();
			}
			if (!shadow) {
				shadow = $('<div id="contextmenuShadow"></div>').appendTo('body').hide();
			}
			
			hash = hash || [];
			hash.push({
				id : id,
				shadow: op.shadow,
				bindings: op.bindings || {},
				ctrSub: op.ctrSub
			});
			
			var index = hash.length - 1;
			$(this).bind('contextmenu', function(e) {
				display(index, this, e, op);
				return false;
			});
			return this;
		}
	});
	
	function display(index, trigger, e, options) {
		var cur = hash[index];

		var content = $('<ul id="navTabCM"><li rel="reload">刷新标签页</li><li rel="closeCurrent">关闭标签页</li><li rel="closeOther">关闭其它标签页</li><li rel="closeAll">关闭全部标签页</li></ul>');
		content.find('li').hoverClass();
	
		// Send the content to the menu
		menu.html(content);
	
		$.each(cur.bindings, function(id, func) {
			$("[rel='"+id+"']", menu).bind('click', function(e) {
				hide();
				func($(trigger), $("#"+cur.id));
			});
		});
		
		var posX = e.pageX;
		var posY = e.pageY;
		if ($(window).width() < posX + menu.width()) posX -= menu.width();
		if ($(window).height() < posY + menu.height()) posY -= menu.height();

		menu.css({'left':posX,'top':posY}).show();
		if (cur.shadow) shadow.css({width:menu.width(),height:menu.height(),left:posX+3,top:posY+3}).show();
		$(document).one('click', hide);
		
		if ($.isFunction(cur.ctrSub)) {cur.ctrSub($(trigger), $("#"+cur.id));}
	}
	
	function hide() {
		menu.hide();
		shadow.hide();
	}
})(jQuery);

/**
 * jQuery ajax history plugins
 */
(function($){
	$.extend({
		browser: {},		
		History: {
			_hash: new Array(),
			_cont: undefined,
			_currentHash: "",
			_callback: undefined,
			init: function(cont, callback){
				$.History._cont = cont;
				$.History._callback = callback;
				var current_hash = location.hash.replace(/\?.*$/, '');
				$.History._currentHash = current_hash;
				if ($.browser.msie) {
					if ($.History._currentHash == '') {
						$.History._currentHash = '#';
					}
					$("body").append('<iframe id="jQuery_history" style="display: none;" src="about:blank"></iframe>');
					var ihistory = $("#jQuery_history")[0];
					var iframe = ihistory.contentDocument || ihistory.contentWindow.document;
					iframe.open();
					iframe.close();
					iframe.location.hash = current_hash;
				}
				if ($.isFunction(this._callback)) 
					$.History._callback(current_hash.skipChar("#"));
				setInterval($.History._historyCheck, 100);
			},
			_historyCheck: function(){
				var current_hash = "";
				if ($.browser.msie) {
					var ihistory = $("#jQuery_history")[0];
					var iframe = ihistory.contentWindow;
					current_hash = iframe.location.hash.skipChar("#").replace(/\?.*$/, '');
				} else {
					current_hash = location.hash.skipChar('#').replace(/\?.*$/, '');
				}
//				if (!current_hash) {
//					if (current_hash != $.History._currentHash) {
//						$.History._currentHash = current_hash;
//						//TODO
//					}
//				} else {
					if (current_hash != $.History._currentHash) {
						$.History._currentHash = current_hash;
						$.History.loadHistory(current_hash);
					}
//				}
				
			},
			addHistory: function(hash, fun, args){
				$.History._currentHash = hash;
				var history = [hash, fun, args];
				$.History._hash.push(history);
				if ($.browser.msie) {
					var ihistory = $("#jQuery_history")[0];
					var iframe = ihistory.contentDocument || ihistory.contentWindow.document;
					iframe.open();
					iframe.close();
					iframe.location.hash = hash.replace(/\?.*$/, '');
					location.hash = hash.replace(/\?.*$/, '');
				} else {
					location.hash = hash.replace(/\?.*$/, '');
				}
			},
			loadHistory: function(hash){
				if ($.browser.msie) {
					location.hash = hash;
				}
				for (var i = 0; i < $.History._hash.length; i += 1) {
					if ($.History._hash[i][0] == hash) {
						$.History._hash[i][1]($.History._hash[i][2]);
						return;
					}
				}
			}
		},
		ajaxdo:function(param){

			if(typeof param.type != 'undefined' && param.type.toLowerCase() == 'post'){
				if(typeof param.data == "undefined"){
					param.data = {};
				}
				if(typeof param.data == 'string'){ // 处理用序列化处理的post参数
					param.data += '&_hash='+$.cookie("ypre_saltkey");
				}else{
					param.data['_hash'] = $.cookie("ypre_saltkey");
				}
			}else{
				param.url = param.url + (/\?/.test(param.url) ? "&" : "?")+ "_hash=" + $.cookie("ypre_saltkey");
			}
			$.ajax(param);
		}
	});
})(jQuery);
/**
 * toast
 * @param  
 * toastr.options = {
		"closeButton": true,
		"debug": false,
		"positionClass": "toast-top-right",
		"onclick": null,
		"showDuration": "1000",
		"hideDuration": "1000",
		"timeOut": "5000",
		"extendedTimeOut": "1000",
		"showEasing": "swing",
		"hideEasing": "linear",
		"showMethod": "fadeIn",
		"hideMethod": "fadeOut"
    }
 * Command: toastr[toastType](message,title); 
 * toastType = {'info','success','warning','error'}
 */
(function (define) {
	define(['jquery'], function ($) {
		return (function () {
			var version = '2.0.1';
			var $container;
			var listener;
			var toastId = 0;
			var toastType = {
				error: 'error',
				info: 'info',
				success: 'success',
				warning: 'warning'
			};

			var toastr = {
				clear: clear,
				error: error,
				getContainer: getContainer,
				info: info,
				options: {},
				subscribe: subscribe,
				success: success,
				version: version,
				warning: warning
			};

			return toastr;

			//#region Accessible Methods
			function error(message, title, optionsOverride) {
				return notify({
					type: toastType.error,
					iconClass: getOptions().iconClasses.error,
					message: message,
					optionsOverride: optionsOverride,
					title: title
				});
			}

			function info(message, title, optionsOverride) {
				return notify({
					type: toastType.info,
					iconClass: getOptions().iconClasses.info,
					message: message,
					optionsOverride: optionsOverride,
					title: title
				});
			}

			function subscribe(callback) {
				listener = callback;
			}

			function success(message, title, optionsOverride) {
				return notify({
					type: toastType.success,
					iconClass: getOptions().iconClasses.success,
					message: message,
					optionsOverride: optionsOverride,
					title: title
				});
			}

			function warning(message, title, optionsOverride) {
				return notify({
					type: toastType.warning,
					iconClass: getOptions().iconClasses.warning,
					message: message,
					optionsOverride: optionsOverride,
					title: title
				});
			}

			function clear($toastElement) {
				var options = getOptions();
				if (!$container) { getContainer(options); }
				if ($toastElement && $(':focus', $toastElement).length === 0) {
					$toastElement[options.hideMethod]({
						duration: options.hideDuration,
						easing: options.hideEasing,
						complete: function () { removeToast($toastElement); }
					});
					return;
				}
				if ($container.children().length) {
					$container[options.hideMethod]({
						duration: options.hideDuration,
						easing: options.hideEasing,
						complete: function () { $container.remove(); }
					});
				}
			}
			//#endregion

			//#region Internal Methods

			function getDefaults() {
				return {
					tapToDismiss: true,
					toastClass: 'toast',
					containerId: 'toast-container',
					debug: false,

					showMethod: 'fadeIn', //fadeIn, slideDown, and show are built into jQuery
					showDuration: 300,
					showEasing: 'swing', //swing and linear are built into jQuery
					onShown: undefined,
					hideMethod: 'fadeOut',
					hideDuration: 1000,
					hideEasing: 'swing',
					onHidden: undefined,

					extendedTimeOut: 1000,
					iconClasses: {
						error: 'toast-error',
						info: 'toast-info',
						success: 'toast-success',
						warning: 'toast-warning'
					},
					iconClass: 'toast-info',
					positionClass: 'toast-top-right',
					timeOut: 5000, // Set timeOut and extendedTimeout to 0 to make it sticky
					titleClass: 'toast-title',
					messageClass: 'toast-message',
					target: 'body',
					closeHtml: '<button>&times;</button>',
					newestOnTop: true
				};
			}

			function publish(args) {
				if (!listener) {
					return;
				}
				listener(args);
			}

			function notify(map) {
				var
					options = getOptions(),
					iconClass = map.iconClass || options.iconClass;

				if (typeof (map.optionsOverride) !== 'undefined') {
					options = $.extend(options, map.optionsOverride);
					iconClass = map.optionsOverride.iconClass || iconClass;
				}

				toastId++;

				$container = getContainer(options);
				var
					intervalId = null,
					$toastElement = $('<div/>'),
					$titleElement = $('<div/>'),
					$messageElement = $('<div/>'),
					$closeElement = $(options.closeHtml),
					response = {
						toastId: toastId,
						state: 'visible',
						startTime: new Date(),
						options: options,
						map: map
					};

				if (map.iconClass) {
					$toastElement.addClass(options.toastClass).addClass(iconClass);
				}

				if (map.title) {
					$titleElement.append(map.title).addClass(options.titleClass);
					$toastElement.append($titleElement);
				}

				if (map.message) {
					$messageElement.append(map.message).addClass(options.messageClass);
					$toastElement.append($messageElement);
				}

				if (options.closeButton) {
					$closeElement.addClass('toast-close-button');
					$toastElement.prepend($closeElement);
				}

				$toastElement.hide();
				if (options.newestOnTop) {
					$container.prepend($toastElement);
				} else {
					$container.append($toastElement);
				}


				$toastElement[options.showMethod](
					{ duration: options.showDuration, easing: options.showEasing, complete: options.onShown }
				);
				if (options.timeOut > 0) {
					intervalId = setTimeout(hideToast, options.timeOut);
				}

				$toastElement.hover(stickAround, delayedhideToast);
				if (!options.onclick && options.tapToDismiss) {
					$toastElement.click(hideToast);
				}
				if (options.closeButton && $closeElement) {
					$closeElement.click(function (event) {
						event.stopPropagation();
						hideToast(true);
					});
				}

				if (options.onclick) {
					$toastElement.click(function () {
						options.onclick();
						hideToast();
					});
				}

				publish(response);

				if (options.debug && console) {
					console.log(response);
				}

				return $toastElement;

				function hideToast(override) {
					if ($(':focus', $toastElement).length && !override) {
						return;
					}
					return $toastElement[options.hideMethod]({
						duration: options.hideDuration,
						easing: options.hideEasing,
						complete: function () {
							removeToast($toastElement);
							if (options.onHidden) {
								options.onHidden();
							}
							response.state = 'hidden';
							response.endTime = new Date(),
							publish(response);
						}
					});
				}

				function delayedhideToast() {
					if (options.timeOut > 0 || options.extendedTimeOut > 0) {
						intervalId = setTimeout(hideToast, options.extendedTimeOut);
					}
				}

				function stickAround() {
					clearTimeout(intervalId);
					$toastElement.stop(true, true)[options.showMethod](
						{ duration: options.showDuration, easing: options.showEasing }
					);
				}
			}
			function getContainer(options) {
				if (!options) { options = getOptions(); }
				$container = $('#' + options.containerId);
				if ($container.length) {
					return $container;
				}
				$container = $('<div/>')
					.attr('id', options.containerId)
					.addClass(options.positionClass);
				$container.appendTo($(options.target));
				return $container;
			}

			function getOptions() {
				return $.extend({}, getDefaults(), toastr.options);
			}

			function removeToast($toastElement) {
				if (!$container) { $container = getContainer(); }
				if ($toastElement.is(':visible')) {
					return;
				}
				$toastElement.remove();
				$toastElement = null;
				if ($container.children().length === 0) {
					$container.remove();
				}
			}
			//#endregion

		})();
	});
}(typeof define === 'function' && define.amd ? define : function (deps, factory) {
	if (typeof module !== 'undefined' && module.exports) { //Node
		module.exports = factory(require(deps[0]));
	} else {
		window['toastr'] = factory(window['jQuery']);
	}
}));


(function($){
	// AjaxDo set regional
	$.setRegional = function(key, value){
		if (!$.regional) $.regional = {};
		$.regional[key] = value;
	};
	
	$.fn.extend({
		ajaxTodo: function(){
			return this.each(function(){
				var $this = $(this);
				$this.unbind('click').click(function(event){
					var predo = $this.attr("predo");
					var predofn;
					if(predo){
						predofn = eval('(' + predo + ')');
						predofn.call($this[0]);
					}
					var url = unescape($this.attr("href")).replaceTmById($(event.target).parents(".unitBox:first"));
					AjaxDo.debug(url);
					if (!url.isFinishedTm()) {
						AjaxDo.alertMsg($this.attr("warn") || AjaxDo.msg("alertSelectMsg"));
						return false;
					}
					var title = $this.attr("title");
					
					
					if (title) {
						if(confirm(title)){
							AjaxDo.ajaxTodo(url, $this.attr("callback"));
						};
					} else {
						
						AjaxDo.ajaxTodo(url, $this.attr("callback"));
					}
					event.preventDefault();
				});
			});
		},
		/**
		 * @param {Object} op: {type:GET/POST, url:ajax请求地址, data:ajax请求参数列表, callback:回调函数 }
		 */
		ajaxUrl: function(op){
			var $this = $(this);
			var ajaxError = op.error || AjaxDo.ajaxError;
			$this.trigger(AjaxDo.eventType.pageClear);
			
			$.ajax({
				type: op.type || 'GET',
				url: op.url,
				data: op.data,
				//dataType: "html",
				cache: false,
				success: function(response){
					var json = AjaxDo.jsonEval(response);
					AjaxDo.ajaxbg.hide();
					
					if (json.statusCode==AjaxDo.statusCode.unlogin){
						if (json.message) AjaxDo.alertMsg(json.message);
						AjaxDo.reload();
					}else if (json.statusCode==AjaxDo.statusCode.error){
						if (json.message) AjaxDo.alertMsg(json.message);
					} else {
						$this.html(response).initUI();
						if ($.isFunction(op.callback)) op.callback(response);
					}
					
					if (json.statusCode==AjaxDo.statusCode.timeout){
						if ($.pdialog) $.pdialog.checkTimeout();
						if (navTab) navTab.checkTimeout();
	
						AjaxDo.alertMsg(json.message || AjaxDo.msg("请求超时"), {okCall:function(){
							//AjaxDo.loadLogin();
							alert(AjaxDo.msg("请求超时") || thrownError);
						}});
					} 
					
				},
				error: ajaxError,
				statusCode: {
					503: function(xhr, ajaxOptions, thrownError) {
						alert(AjaxDo.msg("请求错误") || thrownError);
					}
				}
			});
		},
		/**
		 * 跨域获取页面
		 * @param {Object} op: {type:GET/POST, url:ajax请求地址, data:ajax请求参数列表, callback:回调函数 }
		 */
		ajaxJson:function(op){
			var $this = $(this);
			var ajaxError = op.error || AjaxDo.ajaxError;
			var datafor = op.datafor || "data";
			$this.trigger(AjaxDo.eventType.pageClear);

			$.ajax({
				type : "GET",
				async: false,
				url : op.url,
				data: op.data,
				dataType : "jsonp",
				jsonp: "jsoncallback",//服务端用于接收callback调用的function名的参数
				success : function(json){
					//console.log(json);
					var json = AjaxDo.jsonEval(json);
					if(datafor == "pageUI"){
						$this.html(json.html).initUI();
					}
					if ($.isFunction(op.callback)) op.callback(json);		
				},
				error: ajaxError,
				statusCode: {
					503: function(xhr, ajaxOptions, thrownError) {
						alert(AjaxDo.msg("statusCode_503") || thrownError);
					}
				}
			});
		},
		loadUrl: function(url,data,callback){
			$(this).ajaxUrl({url:url, data:data, callback:callback});
		},
		initUI: function(){
			return this.each(function(){
				AjaxDo.initUI(this);
			});
		},
		/**
		 * adjust component inner reference box height
		 * @param {Object} refBox: reference box jQuery Obj
		 */
		layoutH: function($refBox){
			return this.each(function(){
				var $this = $(this);
				if (! $refBox) $refBox = $this.parents("div.layoutBox:first");
				var iRefH = $refBox.height();
				var iLayoutH = parseInt($this.attr("layoutH"));
				var iH = iRefH - iLayoutH > 50 ? iRefH - iLayoutH : 50;
				
				if ($this.isTag("table")) {
					$this.removeAttr("layoutH").wrap('<div layoutH="'+iLayoutH+'" style="overflow:auto;height:'+iH+'px"></div>');
				} else {
					$this.height(iH).css("overflow","auto");
				}
			});
		},
		hoverClass: function(className, speed){
			var _className = className || "hover";
			return this.each(function(){
				var $this = $(this), mouseOutTimer;
				$this.hover(function(){
					if (mouseOutTimer) clearTimeout(mouseOutTimer);
					$this.addClass(_className);
				},function(){
					mouseOutTimer = setTimeout(function(){$this.removeClass(_className);}, speed||10);
				});
			});
		},
		focusClass: function(className){
			var _className = className || "textInputFocus";
			return this.each(function(){
				$(this).focus(function(){
					$(this).addClass(_className);
				}).blur(function(){
					$(this).removeClass(_className);
				});
			});
		},
		isTag:function(tn) {
			if(!tn) return false;
			return $(this)[0].tagName.toLowerCase() == tn?true:false;
		},
		/**
		 * 判断当前元素是否已经绑定某个事件
		 * @param {Object} type
		 */
		isBind:function(type) {
			var _events = $(this).data("events");
			return _events && type && _events[type];
		},
		/**
		 * 输出firebug日志
		 * @param {Object} msg
		 */
		log:function(msg){
			return this.each(function(){
				if (console) console.log("%s: %o", msg, this);
			});
		}
	});
	
	/**
	 * 扩展String方法
	 */
	$.extend(String.prototype, {
		isPositiveInteger:function(){
			return (new RegExp(/^[1-9]\d*$/).test(this));
		},
		isInteger:function(){
			return (new RegExp(/^\d+$/).test(this));
		},
		isNumber: function(value, element) {
			return (new RegExp(/^-?(?:\d+|\d{1,3}(?:,\d{3})+)(?:\.\d+)?$/).test(this));
		},
		trim:function(){
			return this.replace(/(^\s*)|(\s*$)|\r|\n/g, "");
		},
		startsWith:function (pattern){
			return this.indexOf(pattern) === 0;
		},
		endsWith:function(pattern) {
			var d = this.length - pattern.length;
			return d >= 0 && this.lastIndexOf(pattern) === d;
		},
		replaceSuffix:function(index){
			return this.replace(/\[[0-9]+\]/,'['+index+']').replace('#index#',index);
		},
		trans:function(){
			return this.replace(/&lt;/g, '<').replace(/&gt;/g,'>').replace(/&quot;/g, '"');
		},
		encodeTXT: function(){
			return (this).replaceAll('&', '&amp;').replaceAll("<","&lt;").replaceAll(">", "&gt;").replaceAll(" ", "&nbsp;");
		},
		replaceAll:function(os, ns){
			return this.replace(new RegExp(os,"gm"),ns);
		},
		replaceTm:function($data){
			if (!$data) return this;
			return this.replace(RegExp("({[A-Za-z_]+[A-Za-z0-9_]*})","g"), function($1){
				return $data[$1.replace(/[{}]+/g, "")];
			});
		},
		replaceTmById:function(_box){
			var $parent = _box || $(document);
			return this.replace(RegExp("({[A-Za-z_]+[A-Za-z0-9_]*})","g"), function($1){
				var $input = $parent.find("#"+$1.replace(/[{}]+/g, ""));
				return $input.val() ? $input.val() : $1;
			});
		},
		isFinishedTm:function(){
			return !(new RegExp("{[A-Za-z_]+[A-Za-z0-9_]*}").test(this)); 
		},
		skipChar:function(ch) {
			if (!this || this.length===0) {return '';}
			if (this.charAt(0)===ch) {return this.substring(1).skipChar(ch);}
			return this;
		},
		isValidPwd:function() {
			return (new RegExp(/^([_]|[a-zA-Z0-9]){6,32}$/).test(this)); 
		},
		isValidMail:function(){
			return(new RegExp(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/).test(this.trim()));
		},
		isSpaces:function() {
			for(var i=0; i<this.length; i+=1) {
				var ch = this.charAt(i);
				if (ch!=' '&& ch!="\n" && ch!="\t" && ch!="\r") {return false;}
			}
			return true;
		},
		isPhone:function() {
			return (new RegExp(/(^([0-9]{3,4}[-])?\d{3,8}(-\d{1,6})?$)|(^\([0-9]{3,4}\)\d{3,8}(\(\d{1,6}\))?$)|(^\d{3,8}$)/).test(this));
		},
		isUrl:function(){
			return (new RegExp(/^[a-zA-z]+:\/\/([a-zA-Z0-9\-\.]+)([-\w .\/?%&=:]*)$/).test(this));
		},
		isExternalUrl:function(){
			return this.isUrl() && this.indexOf("://"+document.domain) == -1;
		}
	});

})(jQuery);

/**
 * jQuery session(sessionStorage) & storage(localStorage) plugins
 */
(function($){
	$.extend({		
		storage: {
			handle: window.localStorage,
			data: window.localStorage,
			_cont: undefined,
			_currentHash: "",
			_callback: undefined,
			init: function(cont, callback){
				$.History._cont = cont;
				$.History._callback = callback;
				var current_hash = location.hash.replace(/\?.*$/, '');
				$.History._currentHash = current_hash;
			},
			jsonEval:function(data) {
				try{
					if ($.type(data) == 'string')
						return eval('(' + data + ')');
					else return data;
				} catch (e){
					return data;
				}
			},
			set: function(key, value){
				if(typeof value == "object"){
					value = JSON.stringify(value); //将JSON对象转化为JSON字符
				}
				$.storage.handle.setItem(key,value);
			},
			get: function(key){
				return $.storage.jsonEval($.storage.handle.getItem(key)); //将JSON字符串转化为JSON对象
			},
			setItem : function(key,value){
				$.storage.handle.setItem(key,value);
			},
			getItem: function(key){
				return $.storage.handle.getItem(key);
			},
			getkey: function(index){
				return $.storage.handle.key(index);
			},
			remove : function(key){
				$.storage.handle.removeItem(key);
			},
			clear: function(){
				$.storage.handle.clear();
			}
		},
		session : {
			handle: window.sessionStorage,
			data: window.sessionStorage,
			jsonEval:function(data) {
				try{
					if ($.type(data) == 'string')
						return eval('(' + data + ')');
					else return data;
				} catch (e){
					return data;
				}
			},
			set: function(key, value){
				if(typeof value == "object"){
					value = JSON.stringify(value); //将JSON对象转化为JSON字符
				}
				$.storage.handle.setItem(key,value);
			},
			get: function(key){
				return $.storage.jsonEval($.storage.handle.getItem(key)); //将JSON字符串转化为JSON对象
			},
			setItem : function(key,value){
				$.storage.handle.setItem(key,value);
			},
			getItem: function(key){
				return $.storage.handle.getItem(key);
			},
			getkey: function(index){
				return $.storage.handle.key(index);
			},
			remove : function(key){
				$.storage.handle.removeItem(key);
			},
			clear: function(){
				$.storage.handle.clear();
			}
		}
	});
})(jQuery);