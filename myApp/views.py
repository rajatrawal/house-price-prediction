from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import pickle 
import numpy as np
df = pd.read_csv('./model/clean_df.csv')
pipe = pickle.load(open('./model/pipe.pkl','rb'))

# Create your views here.

def index(request):
    global df
    locations = df['location'].unique()
    params = {
        'locations':locations
    }
    return render(request,'myApp/index.html',params)

def predict(request):
    if request.method == 'POST':
        # try :
            global pipe
            location =request.POST.get('location')
            area =int(request.POST.get('area'))
            bhk =int(request.POST.get('bhk'))
            bath =int(request.POST.get('bath'))
        
            df = pd.DataFrame([[location,area,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
            prediction = pipe.predict(df)
            return HttpResponse(np.round(prediction[0],3))
    #     except :
    #         return HttpResponse('error')
    # else:
    #     return HttpResponse('error')
        
        