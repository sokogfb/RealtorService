from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail

from django.contrib import messages
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id    = request.POST['listing_id']
        listing       = request.POST['listing']
        name          = request.POST['name']
        email         = request.POST['email']
        phone         = request.POST['phone']
        message       = request.POST['message']
        user_id       = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made inquery already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquery for this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)
        contact.save()

        # send mail

        send_mail(
            'Property listing insquiry',
            'There has been an inquiry for ' + listing + '. Sign inti the admin panel',
            'grucushun90@gmail.com',
            [realtor_email, 'kateryna.yershova.2001@gmail.com'],
            fail_silently = False
        )

        messages.success(request, 'Your request has been submitted, realtor will come back soon')
        return redirect('/listings/' + listing_id)