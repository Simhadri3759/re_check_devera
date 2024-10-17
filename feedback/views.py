from django.shortcuts import render,redirect
from feedback.models import feedbackform

def writefeedback(request):
  if request.method=="POST":
    name=request.POST.get('name')
    feedback=request.POST.get('feedback')
    user=feedbackform.objects.create(name=name,feedback=feedback)
    user.save()
    return redirect('sucessfully')
  return render(request,'feedback/feedbackform.html')


def veiwfeedback(request):
  retrive=feedbackform.objects.all()
  return render(request,'feedback/viewfeedback.html',{'retrive':retrive})

def succesfully(request):
  return render(request,'feedback/succesfully.html')
 