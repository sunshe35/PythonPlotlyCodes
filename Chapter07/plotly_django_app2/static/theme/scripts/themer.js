function themerUpdateColors(primary)
{
	updatePrimaryColor(primary, true, true);
}

//Converts an RGB object to a hex string
function rgb2hex(rgb) 
{
	var hex = [
		rgb.r.toString(16),
		rgb.g.toString(16),
		rgb.b.toString(16)
	];
	$.each(hex, function(nr, val) {
		if (val.length === 1) hex[nr] = '0' + val;
	});
	return '#' + hex.join('');
}

// converts a string to RGB object
function rgbString2obj(string)
{
	var parts = string.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
	var rgbObj = { r: Number(parts[1]), g: Number(parts[2]), b: Number(parts[3]) };
	return rgbObj;
}

function updatePrimaryColor(hex, attach, charts)
{
	themerPrimaryColor = hex;
	$('#themer-primary-cp').val(themerPrimaryColor);
	$.minicolors.refresh();
	
	if (attach === true)
		attachStylesheet();
	
	if (charts === true)
		updateCharts();
	
	if (themerPrimaryColor != themerThemes[themerSelectedTheme].primaryColor)
		themerCustom[themerSelectedTheme].primaryColor = themerPrimaryColor;
	else
		themerCustom[themerSelectedTheme].primaryColor = null;
	
	$.cookie('themerCustom', JSON.stringify(themerCustom));
	
	toggleGetCode();
}

function toggleGetCode()
{
	var tcs = themerCustom[themerSelectedTheme];
	
	if (themerSelectedTheme != 0 || (themerSelectedTheme == 0 && tcs.primaryColor != null))
	{
		if ($('#themer-getcode').is(':hidden')) $('#themer-getcode').show();
	}
	else
	{
		if ($('#themer-getcode').is(':visible')) $('#themer-getcode').hide();
	}
}

var themerAdvanced = $.cookie('themerAdvanced') != null ? $.cookie('themerAdvanced') == true : false;
function themerAdvancedToggle()
{
	var cp = [$('#themer-primary-cp'), $('#themer-header-cp'), $('#themer-menu-cp')];
	
	if ($('#themer-advanced-toggle').is(':checked'))
	{
		$('#themer').addClass('themer-advanced');
		$.each(cp, function(k,v){ v.attr('data-textfield', true).removeClass('minicolors-hidden'); });
	}
	else
	{
		$('#themer').removeClass('themer-advanced');
		$.each(cp, function(k,v){ v.attr('data-textfield', false).addClass('minicolors-hidden'); });
	}
}

function generateCSS(basePath)
{
	if(!basePath)
		basePath = "";
		
	var css =
		"@primaryColor: " + themerPrimaryColor + ";\n" +
		
		primaryBgColorTargets.join(", \n") + "\n" + 
		"{\n" +
		"	background-color: @primaryColor;\n"+
		"}\n\n" +
		
		primaryTextColorTargets.join(", \n") + "\n" + 
		"{\n" +
		"	color: @primaryColor;\n"+
		"}\n\n" +
		
		primaryBorderColorTargets.join(", \n") + "\n" + 
		"{\n" +
		"	border-color: @primaryColor;\n"+
		"}\n\n";
		
	css += 
		".table-primary tbody td\n" +
		"{\n" +
		"	background-color: lighten(@primaryColor, 50%);\n" +
		"}\n\n" +
		".table-primary tbody tr.selected td, .table-primary tbody tr.selectable:hover td\n" +
		"{\n" +
		"	background-color: lighten(@primaryColor, 40%);\n" +
		"}\n\n" +
		".table-primary.table-bordered tbody td, .table-primary, .pagination ul > .disabled > a, .pagination ul > .disabled > span\n" +
		"{\n" +
		"	border-color: lighten(@primaryColor, 50%);\n" +
		"}\n\n" +
		
		".widget-activity ul.activities li.highlight\n" +
		"{\n" +
		"	background-color: fade(@primaryColor, 60%);\n" +
		"}\n\n" +
		
		".widget-stats .glyphicons i:before\n" +
		"{\n" +
		"	color: #fff;\n" +
		"}\n\n" +
		
		".pagination ul > .active > a, .pagination ul > .active > span\n" +
		"{\n" +
		"	background-color: fade(@primaryColor, 50%);\n" +
		"}\n\n" +
		
		".widget .widget-body.list.list-2 ul li\n" +
		"{\n" +
		"	&.active { border-color: lighten(@primaryColor, 20%); }\n" +
		"	a { color: lighten(@primaryColor, 20%); i:before { background: lighten(@primaryColor, 50%); color: lighten(@primaryColor, 10%); border-color: lighten(@primaryColor, 20%); } }\n" +
		"}";
		
	return css;
}

function attachStylesheet(basePath, reset)
{
	/*if(!$("#themer-stylesheet").length) $('body').append('<div id="themer-stylesheet"></div>');
	$("#themer-stylesheet").html($('<style type="text/less">' + generateCSS(basePath) + '</style>'));*/
	
	if (themerSelectedTheme == 0)
	{
		$('#themer-stylesheet').empty();
		less.refreshStyles();
		if (reset === true) return false;
	}
	
	if(!$("#themer-stylesheet").length) 
		$('head').append('<style id="themer-stylesheet"></style>');
	
	var code = generateCSS(basePath);
	latestCode.less = code;
	
	$('#themer-stylesheet').attr('type', 'text/x-less').text(code);
	less.refreshStyles();
}

function updateCharts()
{
	if (typeof charts == 'undefined')
		return false;
	
	//console.log('before: ' + charts.utility.chartColors);
	
	// apply styling
	charts.utility.chartColors.shift();
	charts.utility.chartColors.unshift(themerPrimaryColor);
	
	//console.log('after: ' + charts.utility.chartColors);
	
	if (typeof charts.website_traffic_graph != 'undefined' && charts.website_traffic_graph.plot != null)
		charts.website_traffic_graph.init();
	
	if (typeof charts.website_traffic_overview != 'undefined' && charts.website_traffic_overview.plot != null)
		charts.website_traffic_overview.init();
	
	if (typeof charts.traffic_sources_pie != 'undefined' && charts.traffic_sources_pie.plot != null)
		charts.traffic_sources_pie.init();
	
	if (typeof charts.chart_simple != 'undefined' && charts.chart_simple.plot != null)
		charts.chart_simple.init();
	
	if (typeof charts.chart_lines_fill_nopoints != 'undefined' && charts.chart_lines_fill_nopoints.plot != null)
		charts.chart_lines_fill_nopoints.init();
	
	if (typeof charts.chart_ordered_bars != 'undefined' && charts.chart_ordered_bars.plot != null)
		charts.chart_ordered_bars.init();
	
	if (typeof charts.chart_donut != 'undefined' && charts.chart_donut.plot != null)
		charts.chart_donut.init();
	
	if (typeof charts.chart_stacked_bars != 'undefined' && charts.chart_stacked_bars.plot != null)
		charts.chart_stacked_bars.init();
	
	if (typeof charts.chart_pie != 'undefined' && charts.chart_pie.plot != null)
		charts.chart_pie.init();
	
	if (typeof charts.chart_horizontal_bars != 'undefined' && charts.chart_horizontal_bars.plot != null)
		charts.chart_horizontal_bars.init();
	
	if (typeof charts.chart_live != 'undefined' && charts.chart_live.plot != null)
		charts.chart_live.init();
	
	if (typeof genSparklines != 'undefined') 
		genSparklines();
}

function updateTheme(themeSelect)
{
	if ($('#themer-theme').val() != themeSelect) $('#themer-theme').val(themeSelect);
	
	themerSelectedTheme = themeSelect; // index
	$.cookie('themerSelectedTheme', themerSelectedTheme);
	
	var uPrimaryColor = themerCustom[themeSelect].primaryColor != null ? themerCustom[themeSelect].primaryColor : themerThemes[themeSelect].primaryColor;
	
	updatePrimaryColor(uPrimaryColor, false, true);
	
	if (themeSelect == 0 && themerCustom[themeSelect].primaryColor == null)
		attachStylesheet('', true); // reset
	else
		attachStylesheet();
}

function themerGetCode(less)
{
	var tlc;
	if (less === true)
		tlc = latestCode.less;
	else
		tlc = latestCode.css();
		
	//bootbox.alert($('<textarea class="input-block-level" rows="10"></textarea>').val(tlc));
	bootbox.alert($('<pre class="prettyprint lang-html" id="themer-pretty"></pre>').html(tlc));
}

var primaryBgColorTargets = 
[
	".widget .widget-head",
	".btn-primary",
	".widget-stats",
	"#flotTip",
	".btn-group.open .btn-primary.dropdown-toggle, .btn-primary.disabled, .btn-primary[disabled], .btn-primary:hover",
	".filter-bar div.lbl",
	".widget.widget-2.primary .widget-head",
	".widget .widget-body.list.list-2 ul li.active a i:before",
	".label-important",
	".table-primary thead th",
	".gallery ul li .thumb",
	".widget-activity ul.filters li.glyphicons.active i",
	"#menu ul li.active:after",
	".ui-slider-wrap .slider-primary .ui-slider-range",
	".ui-slider-wrap .slider-primary .ui-slider-handle",
	".accordion-heading .accordion-toggle",
	".ui-widget-header",
	".ui-state-active, .ui-widget-content .ui-state-active, .ui-widget-header .ui-state-active",
	"#external-events li",
	".widget.widget-tabs-2 .widget-head ul li.active",
	".pagination ul > li > a:hover",
	".pagination ul > li > a, .pagination ul > li > span",
	".fc-event-skin"
];
var primaryTextColorTargets = 
[
 	"a, a:hover, a:focus",
	"#menu ul li.glyphicons a i:before", 
	".breadcrumb .glyphicons i:before",
	".widget .widget-body.list ul li .count",
	".breadcrumb .glyphicons i:before",
	"#menu > li.active > a",
	"#menu .menu li.active > a, #menu .menu ul li.active > a",
	"#menu .menu li a:hover, #menu .menu ul li a:hover",
	".glyphicons.single i:before",
	".glyphicons.single",
	".table-primary tbody td.important",
	".widget.widget-3 .widget-body.large.cancellations span span:first-child",
	".widget-stats.line .txt strong",
	".widget-stats.line .glyphicons i:before",
	"#docs_icons .glyphicons i:before",
	".widget.widget-3 .widget-footer a:hover, .widget.widget-3 .widget-footer a:hover i:before"
];
var primaryBorderColorTargets = 
[
	".col.main-left ul li.active",
	".widget .widget-head",
	".btn-primary",
	".ui-slider-wrap .slider-primary .ui-slider-handle",
	"#flotTip",
	".widget.widget-2.primary .widget-head",
	".widget .widget-body.list.list-2 ul li.active a i:before",
	".table-primary thead th",
	".pagination ul > .active > a, .pagination ul > .active > span",
	".widget.widget-4 .widget-head .heading",
	".ui-widget-header",
	".navbar.main .profile .img",
	".widget.widget-tabs-2 .widget-head",
	".widget-stats.line",
	".fc-event-skin"
];

/*
 * Persistent Selected Theme
 */
var themerSelectedTheme = $.cookie('themerSelectedTheme') != null ? $.cookie('themerSelectedTheme') : 0;

/*
 * Holds the latest CSS/LESS
 */
var latestCode = {
	css: function(){ return $('#themer-stylesheet').text(); },
	less: null
};

var themerThemes = [
	{
		name: "Default",
		primaryColor: "#71c39a",
		visible: true
	},
	{
		name: "Brown",
		primaryColor: "#ba5d32",
		visible: true
	},
	{
		name: "Purple-Gray",
		primaryColor: "#86618f",
		visible: true
	},
	{
		name: "Purple-Wine",
		primaryColor: "#b94b6f",
		visible: true
	},
	{
		name: "Blue-Gray",
		primaryColor: "#496cad",
		visible: true
	},
	{
		name: "Green Army",
		primaryColor: "#6f8745",
		visible: true
	},
	{
		name: "Black & White",
		primaryColor: "#575757",
		visible: true
	},
	{
		name: "Army",
		primaryColor: "#7a7a3a",
		visible: false
	},
	{
		name: "Evil Army",
		primaryColor: "#567a3a",
		visible: false
	},
	{
		name: "Forest",
		primaryColor: "#947131",
		visible: false
	},
	{
		name: "Cold Blue",
		primaryColor: "#676d8a",
		visible: false
	},
	{
		name: "Warm Blue",
		primaryColor: "#cc5470",
		visible: false
	},
	{
		name: "Experiment #2",
		primaryColor: "#438080",
		visible: false
	}
];

/*
 * Persistent Custom Theme Colors
 */
var themerCustomDefault = [];
$.each(themerThemes, function(k,v) { themerCustomDefault[k] = { primaryColor: null }; });
var themerCustom = $.cookie('themerCustom') != null ? $.parseJSON($.cookie('themerCustom')) : themerCustomDefault;

if (themerThemes.length != themerCustom.length)
{
	$.each(themerThemes, function(k,v){ if (typeof themerCustom[k] == 'undefined') themerCustom[k] = v; });
	$.cookie('themerCustom', JSON.stringify(themerCustom));
}

$(function()
{
	if ($('#themer').length)
	{
		var themerOpened = $.cookie('themerOpened') ? $.cookie('themerOpened') : 0;
		
		$('#themer')
			.on('shown', function(){ $.cookie('themerOpened', 1); })
			.on('hidden', function(){ $.cookie('themerOpened', 0); });
		
		$('#themer .close2').on('click', function(){
			$('#themer').collapse('hide');
		});
		
		if (themerOpened == 1)
			$('#themer').collapse('show');
		
		$("#themer-primary-cp")
			.attr('data-default', themerPrimaryColor)
			.on('change', function(){
				var input = $(this),
				hex = input.val();
				if (hex) updatePrimaryColor(hex, true, true);
			});
		
		var themeSelect = $('#themer-theme');
		$.each(themerThemes, function( i, p ) {
			if (p.visible === true)
			{
				var option = $("<option></option>").text(p.name).val(i);
				themeSelect.append(option);
			}
		});
		themeSelect.on('change', function(e) 
		{
			e.preventDefault();
			updateTheme(themeSelect.val());
		});
		
		$('#themer-getcode-less').click(function(e){
			e.preventDefault();
			themerGetCode(true);
		});
		
		$('#themer-getcode-css').click(function(e){
			e.preventDefault();
			themerGetCode();
		});
		
		$('#themer-custom-reset').click(function()
		{
			themerCustom[themerSelectedTheme].primaryColor = null;
			
			$.cookie('themerCustom', JSON.stringify(themerCustom));
			updateTheme(themerSelectedTheme);
		});
		
		$('#themer-advanced-toggle').on('change', function()
		{
			$.cookie('themerAdvanced', $(this).is(':checked') ? "1" : "0");
			themerAdvancedToggle();
		});
		
		if (themerAdvanced)
			$('#themer-advanced-toggle').prop('checked', true).trigger('change');
		
		updateTheme(themerSelectedTheme);
	}
});