count=2

function add(){
    newdiv=document.createElement('div');
    document.getElementById('mainform').appendChild(newdiv);
    count=count+1;
    newdiv.innerHTML=`Option${count}
                    <br>
                    <input type="text" name="o${count}" id="o${count}" required>`;
}

function remove(){
    mainform=document.getElementById('mainform');
    if(count-1>=2)
    {
        count=count-1;
        mainform.removeChild(mainform.lastElementChild);
    }
    else 
    {
        alert("Minimum 2 options!");
    }
}

function rules(){
    rules="1. Start Time and End Time Should be in YYYY/MM/DD HH:MM:SS format only \n";
    rules=rules+"2. If entered Start Time < Current Time, Start Time will automatically be set to Current Time (according to UTC Timezone)\n";
    rules=rules+"3. If entered Start Time > Current Time, the poll will be not be visible on home until the Start Time = Current Time. This can be used to Schedule Polls \n";
    rules=rules+"4. Enter time in 24 hours format \n";
    rules=rules+"5.End Time cannot be less than Start Time. End Time should be atleast 300 seconds more than Start Time"
    alert(rules);
}