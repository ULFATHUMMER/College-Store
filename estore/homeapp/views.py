from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views import View
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import format_html
from . models import Category, Product,Profile
from .forms import ProfileCreationForm
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

class ProfileView(View):
    def get(self,request):
        form = ProfileCreationForm()
        return render(request,'form.html',{'form':form})
    def post(self,request):
        form = ProfileCreationForm(request.POST)
        print("before post")
        if form.is_valid():
            print("form is valid")
            if request.user.is_authenticated():
                #user=self.request.user.id
                ##profile_user=Profile(user=user)
                profile = form.save(commit=False)
                print("profile assigned")

                profile.user = self.request.user.id
                print("user is", profile.user)
                profile.save()
                print("profile saved")
                form.save()
                print("form saved")
                return redirect('index')
            else:
                print("not authenticated")

        else:
            print(" else here",form.errors)
            form = ProfileCreationForm()

        args = {'form': form}
        return render(request, 'form.html', args)
def index(request):
    return render(request,'index.html')
def is_number(value):
    try:
        float_value = float(value)
        # If converting to a float is successful, it's a number
        return True
    except ValueError:
        # If converting to a float raises a ValueError, it's a string
        return False

#class MyDataForm(forms.ModelForm):
 #   class Meta:
 #       model = Profile
 #       fields = '__all__'

def profile(request,user):
    print("user in profile",user)
    if request.method == "POST":
        print("PSOT WORKED")
        name = request.POST['name']
        user = request.POST['user']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        purpose = request.POST['purpose']
        print("start here")
        profile = Profile(
            name=name,dob=dob, age=age,
            user=user,
            gender=gender, phone=phone,
            mailid=email, address=address,
            department=department, purpose=purpose)
        print('end here')
        print("name is", profile)
        profile.save()
        print("SAVED USER PRFILE")
        return redirect('homeapp:allProdCat', user.id)
    else:
        print("Request.method ", request.method)
        return render(request, 'profile.html', {"user": user})

            #try:
            #    print("Is Number : ",is_number(user))
            #    print("type ",type(user))
             #   if is_number(user):
             #       user = User.objects.get(id=user)
             #   else:
             #       user = User.objects.get(id=user)

            #    print("User===>",user)
           # except User.DoesNotExist:
           #     print("User Not fountd")
            #    raise Http404("User not found")

            #print('user under post')

            #data = {
             #   "gender":gender,
             #   "phone":phone,
              #  "email":email,
              #  "address":address,
              #  "department":department,
               # "purpose":purpose,
               # "user":user
           # }

            # form = MyDataForm(data)
            # if form.is_valid():
            #     form.save()
            #     return  render(request,"success.html")
            # else:
            #
            #     return  render(request,"error.html",{"str":"Not Saved - "+form.errors})









    #except Exception as e:
     #   print("EXCEPCTION ; ",str(e))
     #   return render(request,'error.html',{"str":str(e)})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username is taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print("registered user is",user)
                return redirect('homeapp:login')
        else:
            messages.info(request, "password do not match")
            return redirect('register')

        return redirect('/')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            user_obj=User.objects.get(username=username)
            return redirect('homeapp:allProdCat',user_obj.id)
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return  redirect('homeapp:index')
def payment(request):
    text1="your order is confirmed"
    text2="Back to home"
    messages.info(request, format_html(" {} <a href='/index'>{}</a>",text1 , text2))
    return  redirect('cartapp:cart_detail')

def allProdCat(request,user,c_slug=None,):
    print("Request ",request)
    print("user ",user)
    user=User.objects.filter(id=user)
    print("User ",user)

    c_page = None
    products_list=None
    if c_slug!=None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Product.objects.all().filter(available=True)
    paginator = Paginator(products_list,12)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    digits_list = [1, 2, 3, 4, 5]

    return render(request,'store.html',{"category":c_page,"products":products,
                                        'user':user.first().id
                                        })
"""
<!--                    <a class="btn btn-primary btn-lg " href="{% url 'homeapp:profile' {{user}} %}" style="margin-left: 500px;">Profile</a>-->

"""
def proDetails(request,c_slug,p_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{"product":product})
