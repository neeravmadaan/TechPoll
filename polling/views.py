from django.shortcuts import render
import pyrebase
from django.contrib import auth 
import datetime
from datetime import timezone
import time
import uuid
from django.template.defaulttags import register

@register.filter
def get_type(a):
    return isinstance(a,int)

#ADD FIREBASE CONFIG HERE
config={
}

firebase=pyrebase.initialize_app(config)
authh=firebase.auth()
database=firebase.database()

def index(request):
    poll=database.child('poll').get().val()
    if poll:
        poll=dict(poll)
    else:
        poll={}
    return render(request,'index.html',{"flag":0,"database":poll,"curr_time":int(time.time())})

def login(request):
    return render(request,'login.html')

def postsign(request):
    email=request.POST.get('email')
    pw=request.POST.get('password')
    try:
        user=authh.sign_in_with_email_and_password(email,pw)
    except:
        return render(request,'login.html',{"message":"Invalid Access, Make sure Email and PW are correct!"})
    session_id=user['localId']
    request.session['uid']=str(session_id)
    poll=database.child('poll').get().val()
    if poll:
        poll=dict(poll)
    else:
        poll={}
    return render(request,'index.html',{"flag":1,"database":poll,"curr_time":int(time.time())})

def logout(request):
    auth.logout(request)
    poll=database.child('poll').get().val()
    if poll:
        poll=dict(poll)
    else:
        poll={}
    return render(request,'index.html',{"flag":0,"database":poll,"curr_time":int(time.time())})

def signup(request):
    return render(request,'signup.html')

def postsignup(request):
    uname=request.POST.get('uname')
    email=request.POST.get('email')
    pw=request.POST.get('pw')
    cpw=request.POST.get('cpw')
    try:
        if pw!=cpw:
            return render(request,'signup.html',{"message":"Passwords do not match!"})
        user=authh.create_user_with_email_and_password(email,pw)
        uid=user['localId']
        data={"uname":uname}
        database.child("users").child(uid).child("details").set(data)
    except:
        return render(request,'signup.html',{"message":"PW should have atleast 6 char. If you already have an account, please login instead!"})
    poll=database.child('poll').get().val()
    if poll:
        poll=dict(poll)
    else:
        poll={}
    return render(request,'index.html',{"message":"Congrats, Signup success! Login to access account!","flag":0,"database":poll,"curr_time":int(time.time())})

def profile(request):
    tokenid=request.session['uid']
    poll=database.child('poll').get().val()
    if poll:
        poll=dict(poll)
    else:
        poll={}
    user=database.child('users').child(tokenid).child('cpoll').get().val()
    if user:
        user=dict(user)
    else:
        user={}
    return render(request,'profile.html',{"database":poll,"user":user,"curr_time":int(time.time())})

def poll(request):
    return render(request,'poll.html')

def postpoll(request):
    #overall polls table
    #user table with username,created polls, voted polls
    data={}
    data['question']=request.POST.get('question')
    data['tag']=request.POST.get('tag')
    data['stime']=request.POST.get('stime')
    data['etime']=request.POST.get('etime')

    #endtime
    endt=[]
    temp=''
    for i in range(len(data['etime'])):
        if data['etime'][i]=='/' or data['etime'][i]==' ' or data['etime'][i]==':':
            try:
                endt.append(int(temp))
                temp=''
            except:
                return render(request,'poll.html',{"message":"Enter in YYYY/MM/DD HH:MM:SS format only"})
        else:
            temp=temp+data['etime'][i]
    endt.append(int(temp))
    try:
        dt=datetime.datetime(endt[0],endt[1],endt[2],endt[3],endt[4],endt[5])
    except:
        return render(request,'poll.html',{"message":"Enter in YYYY/MM/DD HH:MM:SS format only"})
    timestamp=int(dt.replace(tzinfo=timezone.utc).timestamp())
    data['etimeu']=timestamp

    #starttime
    startt=[]
    temp=''
    for i in range(len(data['stime'])):
        if data['stime'][i]=='/' or data['stime'][i]==' ' or data['stime'][i]==':':
            try:
                startt.append(int(temp))
                temp=''
            except:
                 return render(request,'poll.html',{"message":"Enter in YYYY/MM/DD HH:MM:SS format only"})
        else:
            temp=temp+data['stime'][i]
    startt.append(int(temp))
    try:
        dt=datetime.datetime(startt[0],startt[1],startt[2],startt[3],startt[4],startt[5])
    except:
        return render(request,'poll.html',{"message":"Enter in YYYY/MM/DD HH:MM:SS format only"})
    timestamp=int(dt.replace(tzinfo=timezone.utc).timestamp())
    if timestamp<time.time():
        timestamp=int(time.time())
        data['stime']=datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y/%m/%d %H:%M:%S')
    data['stimeu']=timestamp

    if data['etimeu']-data['stimeu']<300:
        return render(request,'poll.html',{"message":"Enter valid Start and End Time"})

    for i in range(4,len(request.POST)-1):
        data['o'+str(i-3)]=request.POST.get('o'+str(i-3))
        data['o'+str(i-3)+'c']=0
    idtoken=request.session['uid']
    data['uname']=database.child('users').child(idtoken).child("details").child('uname').get().val()
    
    #overall poll
    pollid=str(uuid.uuid1())
    database.child('poll').child(pollid).set(data)
    #user 
    database.child('users').child(idtoken).child('cpoll').child(pollid).set(1)
    tokenid=request.session['uid']
    poll=database.child('poll').get().val()
    if poll:
        poll=dict(poll)
    else:
        poll={}
    user=database.child('users').child(tokenid).child('cpoll').get().val()
    if user:
        user=dict(user)
    else:
        user={}
    return render(request,'profile.html',{"database":poll,"user":user,"curr_time":int(time.time())})

def upddata(request):
    for i in request.POST:
        if i=="csrfmiddlewaretoken" or i=="flag":
            continue
        else:
            prev=database.child('poll').child(i).child(str(request.POST.get(i))+'c').get().val()
            database.child('poll').child(i).child(str(request.POST.get(i))+'c').set(prev+1)
    poll=database.child('poll').get().val()
    if poll:
        poll=dict(poll)
    else:
        poll={}
    return render(request,'index.html',{"flag":request.POST.get('flag'),"database":poll,"curr_time":int(time.time())})

def deletep(request):
    pollid=request.POST.get("pollid")
    tokenid=request.session['uid']
    #remove from overall poll
    database.child('poll').child(pollid).remove()
    #remove from user also
    database.child('users').child(tokenid).child('cpoll').child(pollid).remove()
    poll=database.child('poll').get().val()
    if poll:
        poll=dict(poll)
    else:
        poll={}
    user=database.child('users').child(tokenid).child('cpoll').get().val()
    if user:
        user=dict(user)
    else:
        user={}
    return render(request,'profile.html',{"database":poll,"user":user,"curr_time":int(time.time())})

def tohome(request):
    poll=database.child('poll').get().val()
    if poll:
        poll=dict(poll)
    else:
        poll={}
    return render(request,'index.html',{"flag":1,"database":poll,"curr_time":int(time.time())})