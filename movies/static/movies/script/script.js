let menuslide=document.getElementById('menu-slide');
let closebtn=document.getElementById('close');
let menubtn=document.getElementById('menubtn');
menuslide.style.display="none";
console.log(closebtn);
closebtn.addEventListener("click",()=>{
        menuslide.style.display="none";
})  
menubtn.addEventListener("click",()=>{
    menuslide.style.display="flex";
})  


