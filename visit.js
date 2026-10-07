(function(){
  var h=location.hostname;
  if(!/(^|\.)theworthguide\.com$/.test(h)) return;
  var id="";
  document.cookie.split(";").forEach(function(p){var x=p.trim().split("="); if(x[0]==="wgid") id=x[1];});
  if(!id){ id=Math.random().toString(36).slice(2)+Date.now().toString(36); document.cookie="wgid="+id+"; domain=.theworthguide.com; path=/; max-age=31536000; secure; samesite=lax"; }
  var page=h+location.pathname;
  var seen={};
  try{ seen=JSON.parse(localStorage.getItem("wgpages")||"{}"); }catch(e){}
  if(seen[page]) return;
  seen[page]=1; try{ localStorage.setItem("wgpages", JSON.stringify(seen)); }catch(e){}
  var u="https://dash.theworthguide.com/visit?host="+encodeURIComponent(h)+"&path="+encodeURIComponent(location.pathname)+"&id="+encodeURIComponent(id);
  if(navigator.sendBeacon) navigator.sendBeacon(u); else fetch(u,{method:"POST",mode:"no-cors",keepalive:true}).catch(function(){});
})();
