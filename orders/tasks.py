from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    try:
        # Fetch the order using the order_id
        order = Order.objects.get(id=order_id)

        # Prepare the subject and message for the email
        subject = f'Order nr. {order.id} Confirmation'
        message = (
            f'Dear {order.first_name},\n\n'
            f'You have successfully placed an order.\n'
            f'Your order ID is {order.id}.\n\n'
            f'Thank you for shopping with us!'
        )
        
        # Send the email
        mail_sent = send_mail(
            subject,  # Subject
            message,  # Message body
            'gaurabchoudhary482@gmail.com',  # From email
            [order.email],  # Recipient (order email)
            fail_silently=False  # If sending fails, raise an error
        )

        return mail_sent  # Return the number of emails sent (should be 1 if successful)

    except Order.DoesNotExist:
        # Handle the case when the order is not found (in case of invalid order_id)
        return f"Order with ID {order_id} does not exist."
