from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import Account
from .serializer import AccountSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def upload_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        csv_file = request.FILES['file']
        df = pd.read_csv(csv_file)
         # Initialize an empty list to store deserialized data
        deserialized_data = []

        # Iterate through CSV rows and validate using serializer
        for index, row in df.iterrows():
            serializer = AccountSerializer(data=row.to_dict())
            if serializer.is_valid():
                # Save valid data to database
                serializer.save()
                deserialized_data.append(serializer.data)
            else:
                # Handle serializer validation errors
                return JsonResponse({'error': serializer.errors}, status=400)

        return JsonResponse({'message': 'CSV Uploaded Successfully', 'data': deserialized_data})

    return JsonResponse({'error': 'POST request required'}, status = 400)