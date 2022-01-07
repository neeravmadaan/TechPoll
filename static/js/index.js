function active(){
    act=document.getElementById("act");
    inact=document.getElementById("inact");
    actpoll=document.getElementsByClassName("activepoll")
    inactpoll=document.getElementsByClassName("inactivepoll")
    for(let i=0;i<actpoll.length;i=i+1){
        actpoll[i].style.display="block";
    }
    for(let i=0;i<inactpoll.length;i=i+1){
        inactpoll[i].style.display="none";
    }
    if(!act.classList.contains("active")){
        act.classList.add("active");
    }
    if(act.classList.contains("inactive")){
        act.classList.remove("inactive");
    }
    if(!inact.classList.contains("inactive")){
        inact.classList.add("inactive");
    }
    if(inact.classList.contains("active")){
        inact.classList.remove("active");
    }
}
function inactive(){
    act=document.getElementById("act");
    inact=document.getElementById("inact");
    actpoll=document.getElementsByClassName("activepoll")
    inactpoll=document.getElementsByClassName("inactivepoll")
    for(let i=0;i<actpoll.length;i=i+1){
        actpoll[i].style.display="none";
    }
    for(let i=0;i<inactpoll.length;i=i+1){
        inactpoll[i].style.display="block";
    }
    if(act.classList.contains("active")){
        act.classList.remove("active");
    }
    if(!act.classList.contains("inactive")){
        act.classList.add("inactive");
    }
    if(inact.classList.contains("inactive")){
        inact.classList.remove("inactive");
    }
    if(!inact.classList.contains("active")){
        inact.classList.add("active");
    }
}