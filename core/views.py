from django.shortcuts import render
from .models import Member, Event, Donation

def home(request):
    return render(request, 'core/home.html')

def members_list(request):
    members = Member.objects.all()
    return render(request, 'core/members_list.html', {'members': members})

def events_list(request):
    events = Event.objects.all()
    return render(request, 'core/events_list.html', {'events': events})

def donations_list(request):
    donations = Donation.objects.all()
    return render(request, 'core/donations_list.html', {'donations': donations})



from django.shortcuts import render, redirect
from .forms import MemberForm

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = MemberForm()
    return render(request, 'core/add_member.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .forms import MemberForm

def home(request):
    return render(request, 'core/home.html')

def member_list(request):
    members = Member.objects.all()
    return render(request, 'core/member_list.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'core/member_detail.html', {'member': member})

def member_new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect('member_detail', pk=member.pk)
    else:
        form = MemberForm()
    return render(request, 'core/member_edit.html', {'form': form})

def member_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            member = form.save()
            return redirect('member_detail', pk=member.pk)
    else:
        form = MemberForm(instance=member)
    return render(request, 'core/member_edit.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm

# Listar eventos
def event_list(request):
    events = Event.objects.all()
    return render(request, 'core/event_list.html', {'events': events})

# Criar evento
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'core/event_form.html', {'form': form})

# Editar evento
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'core/event_form.html', {'form': form})

# Deletar evento
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'core/event_confirm_delete.html', {'event': event})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Donation
from .forms import DonationForm

# Listar doações
def donation_list(request):
    donations = Donation.objects.all()
    return render(request, 'core/donation_list.html', {'donations': donations})

# Criar doação
def donation_create(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()
    return render(request, 'core/donation_form.html', {'form': form})

# Editar doação
def donation_update(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    if request.method == "POST":
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm(instance=donation)
    return render(request, 'core/donation_form.html', {'form': form})

# Deletar doação
def donation_delete(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    if request.method == "POST":
        donation.delete()
        return redirect('donation_list')
    return render(request, 'core/donation_confirm_delete.html', {'donation': donation})
