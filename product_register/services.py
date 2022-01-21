from .models import Notification, ProductActionLog


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
