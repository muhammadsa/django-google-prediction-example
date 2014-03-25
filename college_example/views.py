from django.http import HttpResponse
from google_prediction.models import TrainedModel
from django.shortcuts import render
from college_example.forms import CollegeForm

def index(request):
	result = ''

	if request.method == 'POST':
		form = CollegeForm(request.POST)
		if form.is_valid():
			sat = form.cleaned_data['SAT']
			gpa = float(form.cleaned_data['GPA'])
			others = form.cleaned_data['others']

			m = TrainedModel("sat-example", "stanford-model")
			result = m.predict([sat, gpa, others])['outputLabel']
	else:
		form = CollegeForm()

	return render(request, 'index.html', {
			'form':form,
			'result':result,
		})

def generate_model(request):
	model = TrainedModel("sat-example", "stanford-model")

	try: # Checks if the model has already been created
		model.get()
		return HttpResponse("Model already exists.")
	except:
		model.insert("sat-example/dataset.csv")
		return HttpResponse("Model created.")