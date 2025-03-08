from django.shortcuts import render
from joblib import load
import pickle
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sklearn.preprocessing import StandardScaler
import os
import json
from django.conf import settings
from pathlib import Path
from App.models import Reports

MODEL_PATH = Path(settings.BASE_DIR) / "App/model/log_reg_model.pkl"
SCALER_PATH = Path(settings.BASE_DIR) / "App/model/scaler.pkl"

crime_data = {
    "area": {
        1: "Central",
        3: "Southwest",
        15: "N Hollywood",
        19: "Mission",
        14: "Pacific",
        2: "Rampart",
        4: "Hollenbeck",
        18: "Southeast",
        13: "Newton",
        20: "Olympic",
    },
    "crime_type": {
        624: "Battery - Simple Assault",
        745: "Vandalism - Misdemeanor ($399 or Under)",
        740: "Vandalism - Felony ($400 & Over, All Church Vandalisms)",
        625: "Battery Police (Simple Assault)",
        886: "Child Abandonment",
        761: "Vehicle - Attempt Stolen (Others)",
        845: "Sex Offender Registrant Out of Compliance",
        756: "Vehicle - Stolen (Others)",
        121: "Rape, Forcible",
        860: "Violation of Court Order",
    },
    "victim_sex": {
        1: "Female (F)",
        2: "Hispanic (H)",
        3: "Male (M)",
        4: "Unknown",
        5: "Non-Binary/Other (X)",
    },
    "victim_descent": {
        2: "Black (B)",
        7: "Hispanic (H)",
        19: "Other (X)",
        18: "White (W)",
        1: "Asian (A)",
        12: "Other (O)",
        16: "Unknown",
        3: "Chinese (C)",
        5: "Filipino (F)",
        10: "Korean (K)",
    },
    "weapon_used": {
        61: "Strong-Arm (Hands, Fist, Feet or Bodily Force)",
        62: "Unknown Weapon/Other Weapon",
        79: "Unknown",
        54: "Rock/Thrown Object",
        73: "Verbal Threat",
        30: "Handgun",
        40: "Knife with Blade Over 6 Inches",
        20: "Heckler & Koch 91 Semiautomatic Assault Rifle",
        23: "M-14 Semiautomatic Assault Rifle",
        17: "Uzi Semiautomatic Assault Rifle",
    },
}

# Create your views here.
def index(request):
    context = {}
    return render(request,'App/index.html',context)

@csrf_exempt  
def crime_predict(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request
            data = json.loads(request.body)

            # Extract input features
            features = [
                float(data.get('area', 0)),
                float(data.get('crimeType', 0)),
                float(data.get('victimSex', 0)),
                float(data.get('victimDescent', 0)),
                float(data.get('weaponUsed', 0)),
                float(data.get('timeOfCrime', 0)),
                float(data.get('reportedDelay', 0)),
                float(data.get('daysAfterReported', 0)),
            ]
            # Loading the model and scaler
            with open(MODEL_PATH, 'rb') as model_file:
                model = load(model_file)

            with open(SCALER_PATH, 'rb') as scl_model:
                scl_model = load(scl_model)
                
            # Converting the features to numpy array
            features = np.array(features).reshape(1, -1)
            # Predicting the Resulting using model and converting to int
            scaled_features = scl_model.transform(features)
            results_predict = int(model.predict(scaled_features)[0])

            confidence_score = model.predict_proba(scaled_features).max() * 100

            print("predict",results_predict)
            print("confidence",data.get('area', 0),type(data.get('area', 0)))
            create_report = Reports(
                area=int(data.get('area', 0)),
                area_name=crime_data['area'].get(int(data.get('area', 0)), "Unknown"),
                crime_type=int(data.get('crimeType', 0)),
                crime_type_name=crime_data['crime_type'].get(int(data.get('crimeType', 0)), "Unknown"),
                victim_sex=int(data.get('victimSex', 0)),
                victim_sex_label=crime_data['victim_sex'].get(int(data.get('victimSex', 0)), "Unknown"),
                victim_descent=int(data.get('victimDescent', 0)),
                victim_descent_label=crime_data['victim_descent'].get(int(data.get('victimDescent', 0)), "Unknown"),
                weapon_used=int(data.get('weaponUsed', 0)),
                weapon_used_label=crime_data['weapon_used'].get(int(data.get('weaponUsed', 0)), "Unknown"),
                time_of_crime=int(data.get('timeOfCrime', 0)),
                reported_delay=int(data.get('reportedDelay', 0)),
                days_after_reported=int(data.get('daysAfterReported', 0)),
                prediction=results_predict,
                confidence=confidence_score
            )
            create_report.save()
            # According to results redirecting to results page
            if results_predict == 1:
                prediction = "The crime is likely to happen"
            else:
                prediction = "The crime is not likely to happen"

            # Retrieve the last 12 reports
            last_reports = Reports.objects.order_by('-id')[:12]

            # Prepare area data
            area_counts = {}
            for report in last_reports:
                area_counts[report.area_name] = area_counts.get(report.area_name, 0) + 1
            areas_chart = {
                "labels": list(area_counts.keys()),
                "data": list(area_counts.values())
            }

            # Prepare time_of_crime data
            time_counts = [0] * 24
            for report in last_reports:
                time_counts[report.time_of_crime] += 1
            time_chart = {
                "labels": list(range(24)),
                "data": time_counts
            }

            # Prepare crime type data
            crime_type_counts = {}
            for report in last_reports:
                crime_type_counts[report.crime_type_name] = crime_type_counts.get(report.crime_type_name, 0) + 1
            crime_types_chart = {
                "labels": list(crime_type_counts.keys()),
                "data": list(crime_type_counts.values())
            }

            # Send response
            return JsonResponse({
                'success': True,
                'prediction': prediction,
                'confidence_score': confidence_score,
                'areas': areas_chart,
                'time_of_crime': time_chart,
                'crimeTypes': crime_types_chart
            })

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

