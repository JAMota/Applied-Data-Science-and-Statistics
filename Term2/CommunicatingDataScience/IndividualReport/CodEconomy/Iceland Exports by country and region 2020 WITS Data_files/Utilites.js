var agentWidth;function Hash(){this.length=0;this.items=new Array();for(var b=0;b<arguments.length;b+=2){if(typeof(arguments[b+1])!="undefined"){this.items[arguments[b]]=arguments[b+1];this.length++}}this.removeItem=function(a){var d;if(typeof(this.items[a])!="undefined"){this.length--;var d=this.items[a];delete this.items[a]}return d};this.getKey4ItemText=function(a){for(var d in this.items){if(this.items[d]==a){return d}}return"0"};this.getItem=function(a){return this.items[a]};this.setItem=function(a,e){var f;if(typeof(e)!="undefined"){if(typeof(this.items[a])=="undefined"){this.length++}else{f=this.items[a]}this.items[a]=e}return f};this.hasItem=function(a){return typeof(this.items[a])!="undefined"};this.clear=function(){for(var a in this.items){delete this.items[a]}this.length=0};this.getAllKeys=function(a){var e;e="";for(var f in this.items){e+=this.items[f]+a}return e};this.getAllEntries=function(a){var e;e="";for(var f in this.items){e+=f+a}return e};this.getAllItems4JSON=function(a){var e;e="";for(var f in this.items){e+=f+"="+this.items[f]+a}return e};this.getAllItems4JSON=function(a,h){var f;f="";for(var g in this.items){f+=g+a+this.items[g]+h}return f}}function ShowCountryToolTip(l){var m=htPartner.getItem(SelectedReporter).replace(/ /g,"").replace(/,/g,"").replace(/\./g,"").replace(/\)/g,"").replace(/\(/g,"").replace(/\%/g,"").replace(/\$/g,"");if($(l).hasClass("active")){$(".toolTipContent").html("");$(l).removeClass("active")}else{$(".glyphicon-eye-open").removeClass("active");$(".toolTipContent").html("");var s="#"+$(l).attr("id");var n=($(s).offset().left-8)-$(window).scrollLeft();var p=($(s).offset().top+20)-$(window).scrollTop();var t=$(window).width();var r=t-n;var o="";var q="";if(htMetadata.hasItem(m.toLowerCase().replace("-and-","&"))){q="<table class='toolTipData'>";o=htMetadata.getItem(m.toLowerCase().replace("-and-","&")).split("`");for(i=0;i<o.length;i++){q=q+"<tr><td class='labels'>"+o[i].split("~")[0]+":</td><td>"+o[i].split("~")[1]+"</td></tr>"}q=q+"</table>"}else{q="<table class='toolTipData'><tr><td> No metadata available </td></tr></table>"}var u="<div class='toolTip'><a class='close' onclick='closeToolTip();' ><span class='glyphicon glyphicon-remove-circle'></span></a><div class='clearfix'></div><div class='toolTipBody'>"+q+"</div> </div> ";$(".toolTipContent").append(u);$(".toolTip").show();if(agentWidth>767){if(r>350){$(".toolTip").css({left:n+"px",top:p+"px",overflow:"visible"})}else{$(".toolTip").css({right:(r-30)+"px",top:p+"px",left:"auto",overflow:"visible"});$(".toolTip").addClass("rightAlign")}}else{$(".toolTip").css({left:"20px",top:p+"px",overflow:"visible"});$(".toolTip").addClass("centerAlign")}$(l).addClass("active")}}function showToolTip(k){if($(k).hasClass("active")){$(".toolTipContent").html("");$(k).removeClass("active")}else{$(".glyphicon-eye-open").removeClass("active");$(".toolTipContent").html("");var q="#"+$(k).attr("id");var l=($(q).offset().left-8)-$(window).scrollLeft();var n=($(q).offset().top+20)-$(window).scrollTop();var r=$(window).width();var p=r-l;var m="";var o="";if(htMetadata.hasItem($(k).attr("id").replace("-and-","&").split("-")[1].toLowerCase())){o="<table class='toolTipData'>";m=htMetadata.getItem($(k).attr("id").replace("-and-","&").split("-")[1].toLowerCase()).split("`");for(i=0;i<m.length;i++){o=o+"<tr><td class='labels'>"+m[i].split("~")[0]+":</td><td>"+m[i].split("~")[1]+"</td></tr>"}o=o+"</table>"}else{o="<table class='toolTipData'><tr><td> No metadata available </td></tr></table>"}var s="<div class='toolTip'><a class='close' onclick='closeToolTip();' ><span class='glyphicon glyphicon-remove-circle'></span></a><div class='clearfix'></div><div class='toolTipBody'>"+o+"</div> </div> ";$(".toolTipContent").append(s);$(".toolTip").show();if(agentWidth>767){if(p>350){$(".toolTip").css({left:l+"px",top:n+"px",overflow:"visible"})}else{$(".toolTip").css({right:(p-30)+"px",top:n+"px",left:"auto",overflow:"visible"});$(".toolTip").addClass("rightAlign")}}else{$(".toolTip").css({left:"20px",top:n+"px",overflow:"visible"});$(".toolTip").addClass("centerAlign")}$(k).addClass("active")}$(window).scroll(function(){$(".toolTipContent").html("");$(k).removeClass("active")})}function showNTMToolTip(k){if($(k).hasClass("active")){$(".toolTipContent").html("");$(k).removeClass("active")}else{$(".glyphicon-eye-open").removeClass("active");$(".toolTipContent").html("");var q="#"+$(k).attr("id");var l=($(q).offset().left-8)-$(window).scrollLeft();var n=($(q).offset().top+20)-$(window).scrollTop();var r=$(window).width();var p=r-l;$(".toolTipContent").html("");var m="";var o="";if(htMetadata.hasItem($(k).attr("id").split("_")[1].toLowerCase())){o="<table class='toolTipData'>";m=htMetadata.getItem($(k).attr("id").split("_")[1].toLowerCase()).split("`");for(i=0;i<m.length;i++){o=o+"<tr><td class='labels'>"+m[i].split("~")[0]+":</td><td>"+m[i].split("~")[1]+"</td></tr>"}o=o+"</table>"}else{o="<table class='toolTipData'><tr><td> No metadata available </td></tr></table>"}var s="<div class='toolTip'><a class='close' onclick='closeToolTip();' ><span class='glyphicon glyphicon-remove-circle'></span></a><div class='clearfix'></div><div class='toolTipBody'>"+o+"</div> </div> ";$(".toolTipContent").append(s);$(".toolTip").show();if(agentWidth>767){if(p>350){$(".toolTip").css({left:l+"px",top:n+"px",overflow:"visible"})}else{$(".toolTip").css({right:(p-30)+"px",top:n+"px",left:"auto",overflow:"visible"});$(".toolTip").addClass("rightAlign")}}else{$(".toolTip").css({left:"20px",top:n+"px",overflow:"visible"});$(".toolTip").addClass("centerAlign")}$(k).addClass("active")}$(window).scroll(function(){$(".toolTipContent").html("");$(k).removeClass("active")})}function showTextviewToolTip(k){if($(k).hasClass("active")){$(".toolTipContent").html("");$(k).removeClass("active")}else{$(".glyphicon-eye-open").removeClass("active");$(".toolTipContent").html("");var q="#"+$(k).attr("id");var l=($(q).offset().left-8)-$(window).scrollLeft();var n=($(q).offset().top+20)-$(window).scrollTop();var r=$(window).width();var p=r-l;var m="";var o="";if(htMetadata.hasItem($(k).attr("id").split("-")[1].toLowerCase())){o="<table class='toolTipData'>";m=htMetadata.getItem($(k).attr("id").split("-")[1].toLowerCase()).split("`");for(i=0;i<m.length;i++){o=o+"<tr><td class='labels'>"+m[i].split("~")[0]+":</td><td>"+m[i].split("~")[1]+"</td></tr>"}o=o+"</table>"}else{o="<table class='toolTipData'><tr><td> No metadata available </td></tr></table>"}var s="<div class='toolTip'><a class='close' onclick='closeToolTip();' ><span class='glyphicon glyphicon-remove-circle'></span></a><div class='clearfix'></div><div class='toolTipBody'>"+o+"</div> </div> ";$(".toolTipContent").append(s);$(".toolTip").show();if(agentWidth>767){if(p>350){$(".toolTip").css({left:l+"px",top:n+"px",overflow:"visible"})}else{$(".toolTip").css({right:(p-30)+"px",top:n+"px",left:"auto",overflow:"visible"});$(".toolTip").addClass("rightAlign")}}else{$(".toolTip").css({left:"20px",top:n+"px",overflow:"visible"});$(".toolTip").addClass("centerAlign")}$(k).addClass("active")}$(window).scroll(function(){$(".toolTipContent").html("");$(k).removeClass("active")})}function staticToolTip(l){if($(l).hasClass("active")){$(".toolTipContent").html("");$(l).removeClass("active")}else{$(".glyphicon-eye-open").removeClass("active");$(".toolTipContent").html("");var r="#"+$(l).attr("id");var m=($(r).offset().left-8)-$(window).scrollLeft();var n=($(r).offset().top+20)-$(window).scrollTop();var t=$(window).width();var o=$(window).height();var p=t-m;var q=o-n;var s=$(r).attr("title");tableMarkUp="<table class='toolTipData'><tr><td> "+s+" </td></tr></table>";var u="<div class='toolTip'><a class='close' onclick='closeToolTip();' ><span class='glyphicon glyphicon-remove-circle'></span></a><div class='clearfix'></div><div class='toolTipBody'>"+tableMarkUp+"</div> </div> ";$(".toolTipContent").append(u);$(".toolTip").show();if(agentWidth>767){if(p>350){$(".toolTip").css({left:m+"px",overflow:"visible"})}else{$(".toolTip").css({right:(p-30)+"px",left:"auto",overflow:"visible"});$(".toolTip").addClass("rightAlign")}}else{$(".toolTip").css({left:"20px",top:n+"px",overflow:"visible"});$(".toolTip").addClass("centerAlign")}if(q>220){$(".toolTip").css({top:n+"px",overflow:"visible"})}else{$(".toolTip").css({bottom:(q+30)+"px",overflow:"visible",top:"auto"});$(".toolTip").addClass("bottomAlign")}$(l).addClass("active")}$(window).scroll(function(){$(".toolTipContent").html("");$(l).removeClass("active")})}function closeToolTip(){$(".toolTipContent").html("");$(".ttIcon").removeClass("active")}function SetCookie(g,h){var e=new Date();var f=new Date();nDays=100;f.setTime(e.getTime()+3600000*24*nDays);document.cookie=g+"="+escape(h)+";expires="+f.toGMTString()+";path=/; secure"}function ReadCookie(g){var e=" "+document.cookie;var h=e.indexOf(" "+g+"=");if(h==-1){h=e.indexOf(";"+g+"=")}if(h==-1||g==""){return""}var f=e.indexOf(";",h+1);if(f==-1){f=e.length}return unescape(e.substring(h+g.length+2,f))}function deletecookie(b){document.cookie=b+"=; expires=Thu, 01 Jan 1970 00:00:01 GMT;"}function DataDownload(m,o,q,s,r,u){var l=m+"Download.aspx?";var p="Reporter="+o+"&Year="+q+"&Tradeflow="+s+"&Type="+u+"&Lang="+r;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<div id='file-loading-sv' class='loading'><img src='"+m+"/images/ajax-loader.gif' width='32' height='32'  alt='' /><br /><strong>Loading...</strong></div>");$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}var t=document.documentElement.clientWidth;var n=document.documentElement.clientHeight;$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=l+p;$("#file-loading-sv").fadeOut(500);return false}function DataDownloadPartnerTimeseries(o,r,s,u,x,z,t,w,A){var p=o+"Download.aspx?";var v="Reporter="+r+"&StartYear="+s+"&EndYear="+u+"&Tradeflow="+x+"&Indicator="+z.replace("~","(").replace("`",")").replace("%","`")+"&Partner="+t+"&Type="+A+"&Lang="+w;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<div id='file-loading-sv' class='loading'><img src='../../images/ajax-loader.gif' width='32' height='32'  alt='' /><br /><strong>Loading...</strong></div>");$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}var y=document.documentElement.clientWidth;var q=document.documentElement.clientHeight;$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=p+v;$("#file-loading-sv").fadeOut(500);return}function DataDownloadCountryTimeseries(n,p,q,r,w,t,v){var m=n+"Download.aspx?";var s="Reporter="+p+"&StartYear="+q+"&EndYear="+r+"&Indicator="+w.replace("~","(").replace("`",")").replace("%","`")+"&Type="+v+"&Lang="+t;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<div id='file-loading-sv' class='loading'><img src='../../images/ajax-loader.gif' width='32' height='32'  alt='' /><br /><strong>Loading...</strong></div>");$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}var u=document.documentElement.clientWidth;var o=document.documentElement.clientHeight;$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=m+s;$("#file-loading-sv").fadeOut(500);return}function DataDownloadProductTimeseries(p,s,u,v,z,B,t,x,y,C){var q=p+"Download.aspx?";var w="Reporter="+s+"&StartYear="+u+"&EndYear="+v+"&Tradeflow="+z+"&Indicator="+B.replace("~","(").replace("`",")").replace("%","`")+"&Partner="+t+"&Product="+x+"&Type="+C+"&Lang="+y;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<div id='file-loading-sv' class='loading'><img src='../../images/ajax-loader.gif' width='32' height='32'  alt='' /><br /><strong>Loading...</strong></div>");$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}var A=document.documentElement.clientWidth;var r=document.documentElement.clientHeight;$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=q+w;$("#file-loading-sv").fadeOut(500);return}function DataDownloadProduct(n,q,v,w,r,t,u,y){var o=n+"Download.aspx?";var s="Reporter="+q+"&Year="+v+"&Tradeflow="+w+"&Partner="+r+"&Product="+t+"&Type="+y+"&Lang="+u;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<div id='file-loading-sv' class='loading'><img src='../../images/ajax-loader.gif' width='32' height='32'  alt='' /><br /><strong>Loading...</strong></div>");$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}var x=document.documentElement.clientWidth;var p=document.documentElement.clientHeight;$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=o+s;$("#file-loading-sv").fadeOut(500);return}function DataDownloadCompareCountries(z,r,x,s,t,y,v,w,A,C){var p=z+"Download.aspx?";var u="Reporter="+r+"&SelectedYear="+x+"&Indicator="+s.replace("~","(").replace("`",")").replace("%","`")+"&Partner="+t+"&SelectedProductcode="+y+"&SelectedComparename="+v+"&Selectedwithcode="+w+"&Type="+C+"&Lang="+A;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<div id='file-loading-sv' class='loading'><img src='../../images/ajax-loader.gif' width='32' height='32'  alt='' /><br /><strong>Loading...</strong></div>");$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}var B=document.documentElement.clientWidth;var q=document.documentElement.clientHeight;$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=p+u;$("#file-loading-sv").fadeOut(500);return}function SummaryNTMDownloadMeasure(l,m,k,h){var g=l+"Download.aspx?";var j="Reporter="+m+"&Type="+h+"&Lang="+k;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=g+j;$("#file-loading-sv").fadeOut(500);return false}function SummaryNTMDownloadSector(l,m,k,h){var g=l+"Download.aspx?";var j="Reporter="+m+"&Type="+h+"&Lang="+k;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=g+j;$("#file-loading-sv").fadeOut(500);return false}function PrevalenceNTMDownloadSectorDetails(l,m,k,h){var g=l+"Download.aspx?";var j="Reporter="+m+"&Type="+h+"&Lang="+k;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=g+j;$("#file-loading-sv").fadeOut(500);return false}function NTMDownloadByMeasure(l,n,r,p,m,q,s){var k=l+"Download.aspx?";var o="NTMView="+n+"&NTMMeasure="+r+"&NTMSector="+p+"&Reporter="+m+"&Type="+s+"&Lang="+q;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=k+o;$("#file-loading-sv").fadeOut(500);return false}function navigate2CPSummaryURLFromByIndicator(){var b=ReadCookie("SelctedCountry");if(b==""){b="USA"}window.location.assign(Svrpath+"CountryProfile/Country/"+b+"/Year/"+GetLatestYear(b)+"/Summary")}function navigate2CPSummaryURL(){var b=ReadCookie("SelctedCountry");if(b==""){b="USA"}window.location.assign("CountryProfile/Country/"+b+"/Year/"+GetLatestYear(b)+"/Summary")}function navigate2CPSummaryURLFromHelp(){var b=ReadCookie("SelctedCountry");if(b==""){b="WLD"}window.location.assign("../CountryProfile/Country/"+b+"/Year/"+GetLatestYear(b)+"/Summary")}function navigate2CPTradeStatsFromHtmlPages(){window.location.assign("tradestats.aspx")}function navigate2CPSummaryURLFromCPSubmenu(){var b=ReadCookie("SelctedCountry");if(b==""){b="WLD"}window.location.assign("../../Country/"+b+"/Year/"+GetLatestYear(b)+"/Summary")}function navigate2CPSummaryURLFromDataAvailability(){var b=ReadCookie("SelctedCountry");if(b==""){b="WLD"}window.location.assign("../CountryProfile/Country/"+b+"/Year/"+GetLatestYear(b)+"/Summary")}function navigate2CPMetadataURL(){window.location.assign("CountryProfile/Metadata/Country/All")}function navigate2CPMetadataURLfromHelp(){window.location.assign("../CountryProfile/Metadata/Country/All")}function GetLatestYear(f){var h=htReporter.getItem(f);var g=null;g=h.split(",");var e="2010";e=htYearCode.getItem(g[0]);return e}function number_format(p,s,n,q){p=(p+"").replace(/[^0-9+\-Ee.]/g,"");var t=!isFinite(+p)?0:+p,u=!isFinite(+s)?0:Math.abs(s),l=(typeof q==="undefined")?",":q,r=(typeof n==="undefined")?".":n,m="",o=function(c,a){var b=Math.pow(10,a);return""+Math.round(c*b)/b};m=(u?o(t,u):""+Math.round(t)).split(".");if(m[0].length>3){m[0]=m[0].replace(/\B(?=(?:\d{3})+(?!\d))/g,l)}if((m[1]||"").length<u){m[1]=m[1]||"";m[1]+=new Array(u-m[1].length+1).join("0")}return m.join(r)}function buildShareURL(){}$(document).ready(function(){agentWidth=$(window).width();$(window).resize(function(){agentWidth=$(window).width()});$(document).click(function(b){if(!$(b.target).hasClass("glyphicon")){$(".toolTipContent").html("");$(".glyphicon-eye-open").removeClass("active")}});$(".ttIcon").click(function(b){b.stopPropagation()});$("section").on("click",".ttIcon,.toolTip",function(b){b.stopPropagation()});$(".toolTipContent").on("click",".toolTip",function(b){b.stopPropagation()});$("#varSelectorWrapper").on("click","#countryName1",function(b){b.stopPropagation()});$("#navList li").addClass("hovernav");$("#customQuery").click(function(){});$("#Help").click(function(){window.open(Svrpath+"Help/country-summary-help.aspx?lang="+strLanguage.toLowerCase(),"WITSHelp","toolbar=no,menubar=no,center=yes,scrollbars=yes,resizable=yes,status=no")});$("#SnapshotHelp").click(function(){window.open(Svrpath+"Help/country-snapshot-help.aspx?lang="+strLanguage.toLowerCase(),"WITSHelp","toolbar=no,menubar=no,center=yes,scrollbars=yes,resizable=yes,status=no")});$("#CountryHelp").click(function(){window.open(Svrpath+"Help/country-help.aspx?lang="+strLanguage.toLowerCase(),"WITSHelp","toolbar=no,menubar=no,center=yes,scrollbars=yes,resizable=yes,status=no")});$("#PartnerHelp").click(function(){window.open(Svrpath+"Help/by-partner-help.aspx?lang="+strLanguage.toLowerCase(),"WITSHelp","toolbar=no,menubar=no,center=yes,scrollbars=yes,resizable=yes,status=no")});$("#ProductHelp").click(function(){window.open(Svrpath+"Help/by-product-help.aspx","WITSHelp","toolbar=no,menubar=no,center=yes,scrollbars=yes,resizable=yes,status=no")});$("#topRightNav li").click(function(){if($(this).find("a").text().trim()=="Login"){}});$(".shareLinkList li").click(function(){var e="";if($(this).find("a").attr("title")=="Facebook"){e="http://www.facebook.com/sharer.php?u="+document.URL+"&t="+document.title+""}if($(this).find("a").attr("title")=="Twitter"){e="http://twitter.com/intent/tweet?text="+document.title.replace(/\%/g,"%25").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C")+"&url="+document.URL}if($(this).find("a").attr("title")=="Linkedin"){e="http://www.linkedin.com/shareArticle?mini=true&url="+document.URL+"&title="+document.title.replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C").replace("|","%7C")+"&summary=World%20Integrated%20Trade%20Solution%20(WITS)&source=World%20Bank"}if($(this).find("a").attr("title")=="Google Plus"){e="https://plus.google.com/share?url="+document.URL}if($(this).find("a").attr("title")=="Reddit"){e="http://reddit.com/submit?url="+document.URL+"&amp;title"+document.title}if($(this).find("a").attr("title")=="StumbleUpon"){e="http://www.stumbleupon.com/submit?url="+document.URL+"&amp;title="+document.title}if($(this).find("a").attr("title")=="Delicious"){e="http://del.icio.us/post?url"+document.URL+"&title="+document.title}if($(this).find("a").attr("title")=="Email"){e="mailto:?Subject="+document.title+"&body="+document.URL+""}if($(this).find("a").attr("title")!="Twitters"){window.open(e)}if($(this).find("a").attr("title")=="whatsapp"){var f=encodeURIComponent(document.URL);var d="whatsapp://send?text="+f;e=d}});$("#share").click(function(){$(this).toggleClass("open")})});function getTwitterURL(b){$.getJSON("http://api.bitly.com/v3/shorten?callback=?",{format:"json",apiKey:"R_b6ef9b17a47447fc9aba5bcd63b507c1",login:"wbwits",longUrl:b},function(d){var a="";a=d.data.url;return a})}function DataDownloadCountryTariffData(q,t,B,w,v,D,A,y,z,u,E){var r=q+"Download.aspx?";var x="Reporter="+t+"&selYear="+B+"&filt="+w+"&filtope="+v+"&filtval="+D+"&sor="+A+"&sortord="+y+"&pagtartIndex="+z+"&pagendIndex="+u+"&Type="+E;if(document.getElementById("file-loading-sv")==null){$("#gdp-meta-data").append("<div id='file-loading-sv' class='loading'><img src='../../images/ajax-loader.gif' width='32' height='32'  alt='' /><br /><strong>Loading...</strong></div>");$("#gdp-meta-data").append("<iframe id='dl-iframe-sv' style='display:none;'></iframe>")}var C=document.documentElement.clientWidth;var s=document.documentElement.clientHeight;$("#file-loading-sv").css({}).fadeIn(200);$("#dl-iframe-sv").get(0).src=r+x;$("#file-loading-sv").fadeOut(500);return}var downloadType="";var s_lang="English";var s_channel="";var s_hier1="";var s_prop1="";var s_prop10="";var s_prop13="";var s_prop16="";var s_prop17="";var s_pageName="";var s_prop1="";var s_account="";function OmnitureControlClick(x,n,s){var y=window.location.pathname;var p=y.lastIndexOf("/")+1;var u=y.length-5;var r=y.substring(p,u);var o=document.title;var q=o.split("-");var v="wbnispdecwits,wbglobalext";var t="DEC WITS EXT";var w="DEC,DEC WITS EXT";while(o.indexOf(",")>-1){o=o.replace(",","")}s_pageName=o+" download excel";s_prop1=o+" download excel";w+=", "+o+" download excel";s_prop10="Live";s_prop13="DEC";s_prop16=s_lang;s_prop17=s_lang;s_linkType="d";s_linkName=r+" page download";s_gs_WITS(v,s)}function s_gs_WITS(ak,al){return;ak=ak.toLowerCase();var aB=s_gg("dynamicAccountSelection"),ax=s_gg("dynamicAccountList"),ay=s_gg("dynamicAccountMatch");if(aB&&ax){ak=s_dyas(ak,ax,ay)}s_un=ak;var aA=1,am=new Date,aj=Math&&Math.random?Math.floor(Math.random()*10000000000000):am.getTime(),v="s"+Math.floor(am.getTime()/10800000)%10+aj,ar=am.getYear(),aw=am.getDate()+"/"+am.getMonth()+"/"+(ar<1900?ar+1900:ar)+" "+am.getHours()+":"+am.getMinutes()+":"+am.getSeconds()+" "+am.getDay()+" "+am.getTimezoneOffset(),aE=s_gtfs(),aw,aC="",q="",at="";if(!s_q){var aF=aE.location,s="",ap="",x="",p="",w="",aq="",j="1.0",k=s_c_w("s_cc","true",0)?"Y":"N",h="",an="",ai=s_gg("iePlugins"),au=0,az;if(s_apv>=4){s=screen.width+"x"+screen.height}if(s_isns||s_isopera){if(s_apv>=3){j="1.1";x=s_n.javaEnabled()?"Y":"N";if(s_apv>=4){j="1.2";ap=screen.pixelDepth;w=s_wd.innerWidth;aq=s_wd.innerHeight;if(s_apv>=4.06){j="1.3"}}}s_pl=s_n.plugins}else{if(s_isie){if(s_apv>=4){x=s_n.javaEnabled()?"Y":"N";j="1.2";ap=screen.colorDepth;if(s_apv>=5){w=s_d.documentElement.offsetWidth;aq=s_d.documentElement.offsetHeight;j="1.3";if(!s_ismac&&s_d.body){s_d.body.addBehavior("#default#homePage");h=s_d.body.isHomePage(aF)?"Y":"N";s_d.body.addBehavior("#default#clientCaps");an=s_d.body.connectionType;if(ai){s_pl=new Array;s_pt(ai,",",s_iepf,"")}}}}else{r=""}if(!s_pl&&ai){s_pl=s_n.plugins}}}if(s_pl){while(au<s_pl.length&&au<30){az=s_fl(s_pl[au].name,100)+";";if(p.indexOf(az)<0){p+=az}au++}}s_q=(s?"&s="+s_ape(s):"")+(ap?"&c="+s_ape(ap):"")+(j?"&j="+j:"")+(x?"&v="+x:"")+(k?"&k="+k:"")+(w?"&bw="+w:"")+(aq?"&bh="+aq:"")+(an?"&ct="+s_ape(an):"")+(h?"&hp="+h:"")+(s_vb?"&vb="+s_vb:"")+(p?"&p="+s_ape(p):"")}if(s_gg("usePlugins")){s_wd.s_doPlugins()}var l=s_wd.location,r=aE.document.referrer;if(!s_gg("pageURL")){s_wd.s_pageURL=s_fl(l?l:"",255)}if(!s_gg("referrer")){s_wd.s_referrer=s_fl(r?r:"",255)}if(s_lnk||s_eo){var o=s_eo?s_eo:s_lnk;if(!o){return""}var p=s_gv("pageName"),af=1,t=s_ot(o),n=s_oid(o),ag=o.s_oidt,av,l,c,ah;if(s_eo&&o==s_eo){while(o&&!n&&t!="BODY"){o=o.parentElement?o.parentElement:o.parentNode;if(!o){return""}t=s_ot(o);n=s_oid(o);ag=o.s_oidt}ah=o.onclick?o.onclick.toString():"";if(ah.indexOf("s_gs(")>=0){return""}}aC=o.target;av=o.href?o.href:"";c=av.indexOf("?");av=s_gg("linkLeaveQueryString")||c<0?av:av.substring(0,c);l=s_gg("linkName")?s_gg("linkName"):s_ln(av);t=s_gg("linkType")?s_gg("linkType").toLowerCase():s_lt(av);if(t&&(av||l)){q+="&pe=lnk_"+(t=="d"||t=="e"?s_ape(t):"o")+(av?"&pev1="+s_ape(av):"")+(l?"&pev2="+s_ape(l):"")}else{aA=0}if(s_gg("trackInlineStats")){if(!p){p=s_gv("pageURL");af=0}t=s_ot(o);c=o.sourceIndex;if(s_gg("objectID")){n=s_gg("objectID");ag=1;c=1}if(p&&n&&t){at="&pid="+s_ape(s_fl(p,255))+(af?"&pidt="+af:"")+"&oid="+s_ape(s_fl(n,100))+(ag?"&oidt="+ag:"")+"&ot="+s_ape(t)+(c?"&oi="+c:"")}}}if(!aA&&!at){return""}if(aA){q=(aw?"&t="+s_ape(aw):"")+s_hav()+q}s_wd.s_linkName=s_wd.s_linkType=s_wd.s_objectID=s_lnk=s_eo="";if(!s_wd.s_disableLegacyVars){s_wd.linkName=s_wd.linkType=s_wd.objectID=""}var aD="";if(ak){if(aA&&s_vs(ak,aj)){aD+=s_mr_WITS(ak,v,q+(at?at:s_rq(ak)),aC,al)}s_sq(ak,aA?"":at)}else{if(s_wd.s_unl){for(var ao=0;ao<s_wd.s_unl.length;ao++){ak=s_wd.s_unl[ao];if(aA&&s_vs(ak,aj)){aD+=s_mr_WITS(ak,v,q+(at?at:s_rq(ak)),aC,al)}s_sq(ak,aA?"":at)}}}return aD}function s_mr_WITS(x,e,C,y,z){x=x.toLowerCase();C=C+"&pe=lnk_d&pev1="+z+"&oid="+z+"&pid="+document.title+"&pidt=1";var b=x.indexOf(","),v=b<0?x:x.substring(0,b),q=s_rep(v,"_","-"),B="s_i_"+v,s=s_gg("visitorNamespace"),t,u,w,A="http"+(s_ssl?"s":"")+"://"+(s?s:(s_ssl?"102":q))+".112.2O7.net/b/ss/"+x+"/1/G.9p2/"+e+"?[AQB]&ndh=1"+(C?C:"")+(s_q?s_q:"")+"&[AQE]";if(s_ios){t=s_wd[B]?s_wd[B]:s_d.images[B];if(!t){t=s_wd[B]=new Image}t.src=A;if(A.indexOf("&pe=")>=0&&(!y||y=="_self"||y=="_top"||(s_wd.name&&y==s_wd.name))){u=w=new Date;while(w.getTime()-u.getTime()<500){w=new Date}}return""}return'<img src="'+A+'" width=1 height=1 border=0 alt="">'}function checkIsRegionByISO3(b){for(i=0;i<region.length;i++){if(region[i].value==b){return true}}return false}function checkIsRegionByName(b){b=b.trim();for(i=0;i<region.length;i++){if(region[i].label==b){return true}}return false}function searchProductIndicatorsArray(c){c=c.trim();for(i=0;i<ProductIndicators.length;i++){var d=ProductIndicators[i].label;if(d.trim()==c){return ProductIndicators[i].value.split("~")[1]}}return c}function searchPartnerIndicatorArray(c){c=c.trim();for(i=0;i<PartnerIndicators.length;i++){var d=PartnerIndicators[i].label;if(d.trim()==c){return PartnerIndicators[i].value.split("~")[1]}}return c}function GetCountryIndicatorCode(c){c=c.trim();for(i=0;i<indicator.length;i++){var d=indicator[i].label;if(d.toUpperCase().trim()==c.toUpperCase().trim()){return indicator[i].value}}return c}function getValue4LabelFromArray(g,f,h){var e=0;if(g.length>=0){for(e=0;e<g.length;e++){if(g[e].label.toUpperCase().trim()==f.toUpperCase().trim()){return(h===true?g[e].value.split("~")[1]:g[e].value)}}return f}}function displayTime(){var h="";var k=new Date();var g=k.getHours();var f=k.getMinutes();var j=k.getSeconds();if(f<10){f="0"+f}if(j<10){j="0"+j}h+=g+":"+f+":"+j+" ";if(g>11){h+="PM"}else{h+="AM"}return h}function arrayMin(d){var e=d.length,f=0;while(e--){alert(d[e].value);if(d[e].value<f){f=d[e].value}}return f}$(document).ready(function(){$("#customQuery").bind("click",function(){window.location.href="https://wits.worldbank.org/WITS/WITS/Restricted/Login.aspx"});$("ul#topRightLink li:nth-last-child(2)").bind("click",function(){window.location.href="https://wits.worldbank.org/WITS/WITS/Restricted/Login.aspx"})});function redirectToSpn(){var d=window.location.href;var e;if(d.toLowerCase().indexOf("/es/")>=0){}else{var f=d.lastIndexOf("/");e=d.substring(0,f)+"/es"+d.substring(f);window.location=e}return false}function redirectToEng(){var d=window.location.href;var e="";if(d.toLowerCase().indexOf("/es/")<=-1){}else{var f=d.toLowerCase().indexOf("/es/");d=d.substring(0,f)+d.substring(f+3);window.location=d}return false}function changeUrl(f){var d=getURLParameterByName("lang");if(strLanguage!=undefined){d=strLanguage}var e=$(f).attr("href");if(d=="es"){e="es/"+e}$(f).attr("href",e)}function getURLParameterByName(e){e=e.replace(/[\[]/,"\\[").replace(/[\]]/,"\\]");var f=new RegExp("[\\?&]"+e+"=([^&#]*)"),d=f.exec(location.search);return d===null?"":decodeURIComponent(d[1].replace(/\+/g," "))}function redirectForLang(f){var e=window.location.href;if($("footer").attr("class")!=="esfooter"){if((e.toLowerCase().indexOf(".aspx")<=-1)&&(e.toLowerCase().indexOf(".html")<=-1)){if(e.toLowerCase().indexOf("/es/")>=0){changeHrefSpanish(f,"/es")}else{if(e.toLowerCase().indexOf("/en/")>=0){}}}else{if((e.toLowerCase().indexOf(".html")>=0)){if(e.toLowerCase().indexOf("/es/")>=0){changeHrefSpanish(f,"/es/")}}else{if((e.toLowerCase().indexOf(".aspx")>=0)){var d=getURLParameterByName("lang");if(d=="es"){changeHrefSpanish(f,"/es")}}}}}}$(document).ready(function(){redirectForLang("ul#topRightLink li:last-child a");redirectForLang("#footerStrip ul:first-child a:eq(0)");redirectForLang("#footerStrip ul:first-child a:eq(1)");redirectForLang("#footerStrip ul:first-child a:eq(2)");redirectForLang("#footerStrip ul:first-child a:eq(4)")});function changeHrefSpanish(g,e){var f=$(g).attr("href");var h=f.lastIndexOf("/");f=f.substring(0,h)+e+f.substring(h);$(g).attr("href",f)}function LauncheLearning(){window.open("http://wits.worldbank.org/WITS/Training/player.html","eLearning","toolbar=no,menubar=no,center=yes,scrollbars=yes,resizable=yes,status=no")};
