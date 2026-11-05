// Minimal, dependency-free. External year in footer, and nothing else that could break if blocked.
document.addEventListener('DOMContentLoaded',function(){
  var y=document.querySelector('[data-year]'); if(y){y.textContent=new Date().getFullYear();}
});
