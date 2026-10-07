(function(){
  var h=location.hostname;
  if(!/(^|\.)theworthguide\.com$/.test(h)) return;
  var k="wgv:"+h;
  try{ if(sessionStorage.getItem(k)) return; sessionStorage.setItem(k,"1"); }catch(e){}
  var u="https://dash.theworthguide.com/visit?host="+encodeURIComponent(h);
  if(navigator.sendBeacon) navigator.sendBeacon(u);
  else fetch(u,{method:"POST",mode:"no-cors",keepalive:true}).catch(function(){});
})();
