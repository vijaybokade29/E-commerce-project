from django.shortcuts import render,redirect
from consumer_app.models import UserData,Product,Cart,CartHistory
import random
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from decimal import *
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from decimal import Decimal


# Create your views here.
def index(request):
    # #import ipdb;ipdb.set_trace()
    try:
        s_mail = request.session['email']
        if s_mail:
            # print('s_mail',s_mail)
            user_obj = UserData.objects.get(email = s_mail)
            return render(request,'index.html',{'user_data':user_obj })
        else:
            raise Exception('s_mail not found')
    except:
        return render(request, 'index.html')

def about(request):
    try:
        s_mail = request.session['email']
        print('s_mail',s_mail)
        user_obj = UserData.objects.get(email = s_mail)
        return render(request,'about.html',{'user_data':user_obj})
    except:
        return render(request,'about.html')

def products(request):
    try:
        # #import ipdb;ipdb.set_trace()
        
        if request.method =='GET':
            s_mail = request.session['email']
            print('s_mail',s_mail)
            user_obj = UserData.objects.get(email = s_mail)
            pro_list = Product.objects.all()
            paginator = Paginator(pro_list,3)
            page_number = request.GET.get('page')
            prod_final = paginator.get_page(page_number)
            # last_pg = prod_final.paginator.num_pages 
            return render(request,'products.html',{'user_data':user_obj,"pro_list":prod_final,'pg':page_number,'last':prod_final, })
        else:
            # #import ipdb;ipdb.set_trace()
            s_mail = request.session['email']
            user_obj = UserData.objects.get(email = s_mail)
            prod_name = request.POST.get('product_name')
            if prod_name:
                prod_list = Product.objects.filter(product_name__icontains = prod_name)
                return render(request,'products.html',{'pro_list':prod_list,'user_data':user_obj})
    except:
        return render(request,'products.html')
          
def otp_generator(user_dict):
    try:
        global otp
        otp = str(random.randint(999,10000))
        
        sub= 'Email Verification'
        from_mail=settings.EMAIL_HOST_USER 
        msg=f"<p>Hello <b>{user_dict['name']}</b>,<br>Your OTP is : <b>{otp}</b></p>"
        to = user_dict['email']
        final_st = EmailMultiAlternatives(sub,msg,from_mail,[to])
        final_st.content_subtype = 'html'
        final_st.send()
        return True
    except:
        return False
    
def signup(request):
    
    if request.method != "POST":
        return render(request,'signup.html')
    else:
        # this code saves forms data to database
        try:
            # #import ipdb
            # ipdb.set_trace()
            check_email = UserData.objects.all()
            email_list = [i.email for i in check_email]
            ver1 = request.POST['email'] in email_list
            if  ver1:
                print('pass')
                msg = '*Email is already Exist!'
                return render(request,'signup.html',{'msg': msg, })
            else:
                raise Exception('Just')
        except :#ObjectDoesNotExist:
            # #import ipdb
            # ipdb.set_trace()
            if request.POST['re_password'] == request.POST['password']:
                
                global user_dict
                user_dict = {
                "name" : request.POST.get('name'),
                "phone" : request.POST.get('phone'),
                "email" : request.POST.get('email'),
                "password" : request.POST.get('password'),
                }
                res = otp_generator(user_dict)
                if res:
                    print('sent')
                    return redirect('otp_page')
                    
            else:
                msg = '*Both passwords are not same'
                return render(request,'signup.html',{'msg': msg, })
                
        
        

def product_detail(request,prod_id):
    try:
        
            # cart detail_page
            s_mail = request.session['email']
            print('s_mail',s_mail)
            user_obj = UserData.objects.get(email = s_mail)
            print(prod_id)
            prod_dtl = Product.objects.get(id =prod_id)
            # all products
            prod_list = Product.objects.all()
            # filter(search bar)
            
                
            # pagination
            paginator = Paginator(prod_list,2)
            page_number = request.GET.get('page')
            prod_final = paginator.get_page(page_number)
            return render(request,'product_detail.html',{'user_data':user_obj,'prod_dtls': prod_dtl,"prod_list":prod_list ,'last':prod_final,})
        
    except:
        return render(request,'product_detail.html')

def contact(request):
    try:
        s_mail = request.session['email']
        print('s_mail',s_mail)
        user_obj = UserData.objects.get(email = s_mail)
        return render(request,'contact.html',{'user_data':user_obj })
    except:
        return render(request,'contact.html')

def profile(request):
    if request.method =='GET':
        try:
            s_mail = request.session['email']
            print('s_mail',s_mail)
            user_obj = UserData.objects.get(email = s_mail)
            
            return render(request,'profile.html',{'user_data':user_obj })
        except:
            return render(request,'profile.html')
    else:
        #import ipdb;ipdb.set_trace()
        user_obj = UserData.objects.get(email = request.session['email'])
        user_obj.name = request.POST['name']
        user_obj.phone = request.POST['phone']
        user_obj.pic = request.FILES['pic']
        user_obj.save()
        user_data = UserData.objects.get(email = request.session['email'])
        return render(request, 'profile.html', {'user_data': user_data,'msg':'*Profile Updated'})
    
def faq(request):
    try:
        s_mail = request.session['email']
        print('s_mail',s_mail)
        user_obj = UserData.objects.get(email = s_mail)
        return render(request,'faq.html',{'user_data':user_obj })
    except:
        return render(request,'faq.html')

def otp_page(request):
    if request.method == 'POST':
        # #import ipdb
        # ipdb.set_trace()
        if request.POST.get('otp')== otp:
            data = UserData(name = user_dict['name'],phone = user_dict['phone'],email = user_dict['email'],password = user_dict['password'])
            data.save()
            print(user_dict)
            return redirect('signin')
        else:
            msg = '*Entered OTP is Incorrect'
            return render(request,'otp_page.html',{'msg': msg, })
    else:
        return render(request,'otp_page.html')

def resend_otp(request):
    # #import ipdb;
    # ipdb.set_trace()
    print('otp sent')
    if request.method == 'POST': 
        res = otp_generator(user_dict)
        if res:
            msg = '* A new OTP has been sent to your email.'
            return render(request, 'otp_page.html', {'msg': msg})
    return redirect('otp_page')

def signin(request):    
    if request.method != 'POST':
        return render(request,'signin.html')
    else:
        #import ipdb;ipdb.set_trace()
        try:
            user_obj = UserData.objects.get(email = request.POST['email'])
            print(user_obj)
            
            if user_obj.password == request.POST['password']:
                # request.session['user_id'] = user_obj.id
                request.session['email'] = user_obj.email
                print(request.session['email'])
                return redirect('index')
            else:
                msg = '*Incorrect Password'
                return render(request,'signin.html',{'msg': msg})
        except: 
            return render(request,'signin.html', {'msg': '*Email Does Not Exist!!'})        

def s_otp_page(request):
    if request.method == 'POST':
        #import ipdb;ipdb.set_trace()
        if request.POST.get('otp')== otp_:
            return render(request,'new_password.html')
        else:
            msg = '*Entered OTP is Incorrect'
            return render(request,'s_otp_page.html',{'msg': msg, })
    else:
        return render(request,'s_otp_page.html')

        
def reset_password(request):
    if request.method != "POST":
        return render(request,'reset_password.html')
    else:
        #import ipdb;ipdb.set_trace()
        
        global otp_,s_user_obj
        otp_ = str(random.randint(999,10000))
        s_user_obj = UserData.objects.get(email = request.POST['email'])
        sub= 'Get Your Password'
        from_mail=settings.EMAIL_HOST_USER 
        msg=f"<p>Hello <b>{s_user_obj.name}</b>,<br>Your OTP is : <b>{otp_}</b></p>"
        to = s_user_obj.email
        final_st = EmailMultiAlternatives(sub,msg,from_mail,[to])
        final_st.content_subtype = 'html'
        final_st.send()
        msg = '*Check Your mail-box'
        
        return render(request,'s_otp_page.html',{'msg':msg})
        
def signout(request):
    # #import ipdb;ipdb.set_trace()
    # print(s_mail)
    del request.session['email']
    return redirect('index')


def s_resend_otp(request):
    # #import ipdb;
    # ipdb.set_trace()
    print('otp sent')
    if request.method == 'POST':
        s_dict = {'name':s_user_obj.name,
                  'email':s_user_obj.email
                } 
        res = otp_generator(s_dict)
        if res:
            msg = '*A new OTP has been sent to your email.'
            return render(request, 's_otp_page.html', {'msg': msg})
    return redirect('s_otp_page')

   
def new_password(request):
    #import ipdb;ipdb.set_trace()
    if request.method != "GET":
        if request.POST['password'] == request.POST['re_password']:
            email_obj = UserData.objects.get(email = request.POST['email'])
            
            user_obj = UserData(password = request.POST['password'],email = request.POST['email'],name = email_obj.name,phone = email_obj.phone)
            user_obj.save()
            print('passwird updated')
            request.session['email'] = user_obj.email
            print(request.session['email'])
            return render(request,'index.html',{'user_data':user_obj })
        else:
            msg = '*Both passwords are not same'
            return render(request,'new_password.html',{'msg':msg})
    else:            
        return render(request,'new_password.html')


def cart(request,prod_id):
    
    #import ipdb;ipdb.set_trace()
    s_mail = request.session['email']
    user_obj = UserData.objects.get(email = s_mail)
    
    product = Product.objects.get(id = prod_id)
    # product_id = request.GET.get('product_id')
    check = product in [i.product for i in Cart.objects.all()]
    quantity = int(request.POST['quantity'])
    res = True
    
    try:
        cart_obj = Cart.objects.get(product = product)
    except Cart.DoesNotExist:
        # cart_obj = Cart.objects.get(product = product,email=s_mail)

        product_price = float(product.price)* quantity
        
        Cart.objects.create(
            email = s_mail,
            product = product,
            image = product.pic,
            quantity = int(quantity) ,
            price = Decimal(product_price),
        )
        res = False
        cart_obj = Cart.objects.get(product = product,email=s_mail)
        
            # exit()
    except:
        cart_obj = Cart.objects.get(product = product,email=s_mail)
    if res :
        if cart_obj.email == s_mail: 
            if check:
                cart_obj.quantity += quantity
                count_of_product =  cart_obj.quantity
                product_price = float(cart_obj.product.price)* count_of_product
                cart_obj.price = Decimal(product_price)
                cart_obj.save()
        else:    
            product_f = Product.objects.filter(id = prod_id)
            product_price = float(product.price)*quantity
            
            Cart.objects.create(
                email = s_mail,
                product = product,
                image = product.pic,
                quantity = int(quantity) ,
                price = Decimal(product_price),
                )
    cart_obj = Cart.objects.filter(email = s_mail)
    total_amount = 0
    for amt in cart_obj:
        total_amount += amt.price     
        
    print(cart_obj)
    return redirect('products') 
# render(request,'cart_table.html',{"cart_obj":cart_obj,'user_data':user_obj,'total_amt':total_amount})
        
    # return redirect('index')
@csrf_exempt
def cart_table(request):
    s_mail = request.session['email']
    print('s_mail',s_mail)
    user_obj = UserData.objects.get(email = s_mail)
    cart_obj = Cart.objects.filter(email = s_mail)
    if cart_obj:
        # global total_amount
        #import ipdb;ipdb.set_trace()
        total_amount = 0
        for amt in cart_obj:
            total_amount += amt.price     
        global client
        client = razorpay.Client(
                            auth=(
                                settings.RAZOR_KEY_ID,
                                settings.RAZOR_KEY_SECRET
                                )
                            )
        payment = client.order.create({'amount':float(total_amount*100),"currency":'INR','payment_capture':'1' })    
        print(payment)
        return render(request,'cart_table.html',{"cart_obj":cart_obj,'user_data':user_obj,'total_amt':total_amount,'payment':payment,"callback_url":'paymenthandler/'})
    else:
        return render(request,'cart_table.html',{"cart_obj":cart_obj,'user_data':user_obj})

@csrf_exempt
def paymenthandler(request):
    # import  ipdb ; ipdb.set_trace()
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')    
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
                }
            # global amount
            # amount = total_amount
            try:
                # client.payment.capture(payment_id, amount)
                session_user = UserData.objects.get(email = request.session['email'])
                c_objects_list = Cart.objects.filter(email= request.session['email'])
                total_amount = 0
                for i in c_objects_list:
                    CartHistory.objects.create(
                        email = i.email,
                        product = i.product,
                        image = i.product.pic,
                        quantity = int(i.quantity) ,
                        price = Decimal(i.price),
                    )
                    for amt in c_objects_list:
                        print(amt.price)
                        total_amount += amt.price
                        
                    i.delete()
                    
                sub= 'Thanks For your Order!'
                from_mail=settings.EMAIL_HOST_USER 
                msg=f"<p>Hello <b>{session_user.name},</b><br>Thank you! for Visiting <b>Little Fashion</b><br>Here is your eBill of Rs. {total_amount}<br><br>from Little Fashion.</p>"
                to = session_user.email
                final_st = EmailMultiAlternatives(sub,msg,from_mail,[to])
                final_st.content_subtype = 'html'
                final_st.send()
                return render(request, 'success.html',{"payment":razorpay_order_id})
            except:
                return render(request, 'paymentfail.html')
           
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()



def update_quauntity(request,prod_id):  
    if request.method == "POST":
        # #import ipdb;ipdb.set_trace()
        
        s_mail = request.session['email']
        # product = Product.objects.get(id = prod_id)
        cart_obj = Cart.objects.get(id = prod_id,email=s_mail)
        count_of_product =  cart_obj.quantity
        if 'plus' in request.POST:
            count_of_product+=1
        else:
            count_of_product-=1
        cart_obj.quantity = count_of_product
        pro_price = cart_obj.product.price
        pro_price *= count_of_product
        cart_obj.price = pro_price
        cart_obj.save()
            
    return redirect('cart_table')

def del_cart_row(request, prod_id):
    #import ipdb;ipdb.set_trace()
    s_mail = request.session['email']
    del_row = Cart.objects.get(id = prod_id,email=s_mail)
    del_row.delete()
    return redirect('cart_table')

def success(request):
    return render(request,'success.html')


def track(request):
    try:
        s_mail = request.session['email']
        prod_track_obj = CartHistory.objects.filter(email = s_mail)
        print('s_mail',s_mail)
        user_obj = UserData.objects.get(email = s_mail)
        return render(request,'track.html',{'user_data':user_obj,"track":prod_track_obj })
    except:
        return render(request,'track.html')
    
