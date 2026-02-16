(function(){
  window.addEventListener('DOMContentLoaded',function(){
    var hero=document.querySelector('.hero');
    if(!hero)return;
    var title=hero.querySelector('.hero__title');
    if(title&&!title.querySelector('.line')){
      var html=title.innerHTML.trim();
      var emMatch=html.match(/<em[^>]*>.*?<\/em>/);
      if(emMatch){
        var idx=html.indexOf(emMatch[0]);
        var before=html.substring(0,idx).trim();
        var em=emMatch[0];
        var after=html.substring(idx+emMatch[0].length).trim();
        var lines=[];
        if(before)lines.push(before);
        if(em)lines.push(em);
        if(after)lines.push(after);
        title.innerHTML=lines.map(function(l){
          return'<span class="line" style="display:block;opacity:0;transform:translateY(32px);">'+l+'</span>';
        }).join('');
      }
    }
    requestAnimationFrame(function(){
      requestAnimationFrame(function(){
        hero.classList.add('hero--animated');
      });
    });
  });
  var nav=document.querySelector('.site-nav');
  if(nav){
    var onScroll=function(){nav.classList.toggle('scrolled',window.scrollY>40)};
    window.addEventListener('scroll',onScroll,{passive:true});
    onScroll();
  }
})();
