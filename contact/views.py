from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from .forms import ContactForm
from .models import Contact

def success_view(request):
    return render(request, 'contact/success.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()
            
            sender_email = contact.email

            # Send an email
            subject = f"New Contact Submission: {contact.subject}"
            message = f"""
            You have received a new contact submission:

            Name: {contact.name}
            Email: {contact.email}
            Message: {contact.message}
            """
            admin_email = 'allenareworksheet@gmail.com'
            
            # send_mail(subject, message, sender_email, [admin_email])
            
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=sender_email,  # Fixed email used for sending
                to=[admin_email],
                headers={'Reply-To': sender_email}  # Dynamic "Reply-To" set for replies
            )

            # Send the email
            email.send()
            
            

            return render(request,'contact/sucess.html')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
