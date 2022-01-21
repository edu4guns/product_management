from .models import Notification, ProductActionLog
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_notification(action, user, product):
    message = f'Action {action} was applied to product {product.name} by {user.username}'
    notification = Notification(
        message=message, sent=False, read=False, user_id=user.id)
    notification.save()


def save_actions(action, product_id, user_id):
    log = ProductActionLog(
        action=action, product_id=product_id, user_id=user_id)
    log.save()


def disable_form_if_needed(form, user):
    if not user.has_perm('product_management.add_product'):
        form.fields["sku"].disabled = True
        form.fields["name"].disabled = True
        form.fields["price"].disabled = True
        form.fields["brand"].disabled = True


def send_email(user, product, form):
    mail = user.email
    new_price = form['price'].value()
    context = {'mail': mail, 'product': product.name,
               'price': product.price, 'new_price': new_price}
    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Updated Product',
        'Zebrands',
        settings.EMAIL_HOST_USER,
        [mail],
    )
    email.attach_alternative(content, 'text/html')
    email.send()
