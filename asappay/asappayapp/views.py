import csv
from django.shortcuts import render,HttpResponse, redirect
from .models import Account
from .models import Transaction
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 

# Create your views here.

def index(req):
    if req.method == "GET":
        print(req.method) # GET
        return render(req,"index.html")
    else:
        uname=req.POST["uname"]
        uemail=req.POST["uemail"]
        upass=req.POST["upass"]
        print(upass,uname)
        # userdata=User.objects.filter(email=uemail,password=upass)
        userdata = authenticate(username=uname,email=uemail,password=upass)
        print(userdata)
        if userdata is not None:
            login(req,userdata)
            # return render(req, "dashboard.html")
            return redirect("dashboard")
        else:
            context = {}
            context["errmsg"] = "Invalid email or password"
            return render(req,"index.html",context)
        

def singup(req):    
    if req.method == "GET":
        print(req.method) # GET
        return render(req,"regester.html")
    else:
        print(req.method) # POST
        uname=req.POST["uname"]
        uemail=req.POST["uemail"]
        upass=req.POST["upass"]
        ucpass=req.POST["ucpass"]
        print(uname,upass,ucpass,uemail)
        if upass != ucpass:
            errmsg="Password and Confirm password nust be same"
            context = {"errmsg":errmsg}
            return render(req,"regester.html",context)
        elif uname == upass:
            errmsg="Password should not be same as email id"
            context = {"errmsg":errmsg}
            return render(req,"regester.html",context)
        else:
            try:
                userdata=User.objects.create(username=uname,email=uemail,password=upass)
                userdata.set_password(upass)
                userdata.save()
                print(User.objects.all())
                return redirect("index")
            except:
                errmsg="User already exist. Try with different username"
                context = {"errmsg":errmsg}
                return render(req,"regester.html",context)


def dashboard(req):
    print(req.user)
    username = req.user
    return render(req, "home.html",{"username": username,})

def profile(req):
    print(req.user)
    username = req.user
    return render(req, "profile.html",{"username": username,})

def account(req):
    message = ""
    username = req.user
    if req.method == "GET":
        print(req.method) # GET
        return render(req,"Account.html",{"username": username,})
    else:
        if 'submit_manual' in req.POST:
            name = req.POST.get('aname')
            email = req.POST.get('aemail')
            phone = req.POST.get('aphone')
            pan = req.POST.get('apannu')
            gst = req.POST.get('agstnu')

            Account.objects.create(
                userid=req.user if req.user.is_authenticated else None,
                accountid=Account.objects.count() + 1,
                accountname=name,
                accountemailid=email,
                accountphone=phone,
                accountpan=pan,
                accountgst=gst
            )
            message = "Account added successfully!"
            return render(req, "Account.html",{"username": username,"message": message,})

        elif 'submit_csv' in req.POST and 'csvfile' in req.FILES:
            csv_file = req.FILES['csvfile']
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)

                user = req.user if req.user.is_authenticated else None
                created_count = 0
                errors = []

                for i, row in enumerate(reader, start=1):
                    try:
                        if not row.get('name'):
                            continue

                        Account.objects.create(
                            userid=user,
                            accountid=Account.objects.count() + 1,
                            accountname=row.get('name').strip(),
                            accountemailid=row.get('email').strip(),
                            accountphone=row.get('phone').strip(),
                            accountpan=row.get('pan_number').strip(),
                            accountgst=row.get('gst_number').strip()
                        )
                        created_count += 1
                    except Exception as e:
                        errors.append(f"Row {i}: {e}")

                if errors:
                    message = f"Imported {created_count} rows with {len(errors)} errors:\n" + "\n".join(errors)
                    return render(req, "Account.html",{"username": username,"message": message,})
                else:
                    message = f"Successfully imported {created_count} accounts."
                    return render(req, "Account.html",{"username": username,"message": message,})
                    
            except Exception as e:
                message = f"Error processing CSV: {e}"
                return render(req, "Account.html",{"username": username,"message": message,})
       
def transaction(req):
    print(req.user)
    username = req.user
    return render(req, "receive.html",{"username": username,})

def userlogout(req):
    logout(req)
    return redirect('/')
