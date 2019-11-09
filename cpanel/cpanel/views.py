from django.shortcuts import render
from firebase import firebase

config = {
    'apiKey': "AIzaSyBDy-h8m4ED9U25mG2qbkh9BKjUIecvd4Q",
    'authDomain': "cpanel-83910.firebaseapp.com",
    'databaseURL': "https://cpanel-83910.firebaseio.com",
    'projectId': "cpanel-83910",
    'storageBucket': "cpanel-83910.appspot.com",
    'messagingSenderId': "361160647545",
    'appId': "1:361160647545:web:811b72a690576c23c505a8",
    'measurementId': "G-P9Q8LNJJ4Q"
}
firebase = firebase.initialize_app(config)
auth = firebase.auth()
def singIn(request):
    return render(request, "signIn.html")
def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"signIn.html",{"msg":message})
        print(user)
        return render(request, "welcome.html",{"e":email})
