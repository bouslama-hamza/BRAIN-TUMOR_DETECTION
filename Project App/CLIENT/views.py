from django.shortcuts import render , redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .predict import Predict , BioGpt

model = Predict('CLIENT/static/model/unet_brain_mri_seg.hdf5')

# Create your views here.
def client_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-login')
    else:
        form = UserRegisterForm()
    return render(request, 'create-account.html', {'form': form})

@login_required
def client_dashboard(request):
    if request.method == 'POST':
        message = model.predict('CLIENT/static/images/'+str(request.POST.get('file_upload')))
        if message == 'Tumor':
            message = 'To Save yourSelf From brain tumor you need  to be aware of different manifestations of various diseases such as head injury, infection, migraine, epilepsy, and finally in our everyday practice we have to be well versed in these benign neurological conditions as well as in malignancies, which can also cause disastrous consequences after a delay.'
            return render(request, 'client_dashboard.html', {'message': message})
        else:
            message = 'No Tumor Detected in your Brain MRI Scan'
            return render(request, 'client_dashboard.html', {'message': message})
    return render(request, 'client_dashboard.html')