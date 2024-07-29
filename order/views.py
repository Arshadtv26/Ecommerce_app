from django.shortcuts import render, redirect
from .models import Order, OrderedItem
from product.models import Product
from django.contrib import messages


# Create your views here.

def show_cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context = {'cart': cart_obj}
    return render(request, 'cart.html', context)


def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        cart_obj, order_create = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        ordered_item, created = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if created:
            ordered_item.quantity = quantity
            ordered_item.save()
        else:
            ordered_item.quantity += quantity
            ordered_item.save()

        return redirect('cart')


def remove_from_cart(request, pk):
    item = OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')


def checkout(request):
    if request.POST:
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            order_obj = Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                status_message = 'Your order is confirmed'
                messages.success(request, status_message)
            else:
                status_message = 'Something went wrong'
                messages.error(request, status_message)
        except Exception as e:
            status_message = 'Something went wrong'
            messages.error(request, status_message)

    return redirect('cart')


def orders(request):
    user = request.user
    customer = user.customer_profile
    orders = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context = {'orders': orders}
    return render(request, 'orders.html', context)
