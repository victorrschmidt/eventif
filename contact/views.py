from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings

def contact(request):
    return render(request, 'contact/contact_form.html', {'form': SubscriptionForm()})
