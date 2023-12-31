from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import random



def home(request):
    # What you want the button to do.
    host = request.get_host()
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "30",
        "item_name": "name-" + str(random.randint(1000, 9999)),
        "invoice": "ORDER-" + str(random.randint(1000, 9999)),
        "currency_code": "USD",
        "notify_url": 'http://{}{}'.format(host, reverse("paypal-ipn")),
        "return": request.build_absolute_uri(reverse('payment-completed')),
        "cancel_return": request.build_absolute_uri(reverse('payment-failed')),
    }
    # Create the instance.
    paypal_payment_button = PayPalPaymentsForm(initial=paypal_dict)

    cart_data_obj = request.session.get('cart_data_obj', {})
    cart_total_amount = 0
    if cart_data_obj:
        for p_i, item in cart_data_obj.items():
            cart_total_amount += int(item['qty'] * float(item['price']))

    context = {"cart_data": cart_data_obj, 'totalcartitems': len(cart_data_obj), 'cart_total_amount': cart_total_amount, 'form': paypal_payment_button}
    return render(request, "payment.html", context)




def successful(request):
    print("i was here in success page")
    return render(request, "successful.html")




def cancelled(request):
    print("i was here in cancelled page")
    return render(request, "cancelled.html")