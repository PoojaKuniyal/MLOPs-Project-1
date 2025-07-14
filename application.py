import joblib
import numpy as np
from config.paths_config import MODEL_OUTPUT_PATH
from flask import Flask, render_template, request

app = Flask(__name__)

loaded_model = joblib.load(MODEL_OUTPUT_PATH)

@app.route('/', methods = ['GET', 'POST'])

def index():
    prediction = None
    confidence = None
    if request.method =='POST':
        try:
            lead_time = int(request.form['lead_time'])
            no_of_special_requests = int(request.form["no_of_special_requests"])
            avg_price_per_room = float(request.form["avg_price_per_room"])
            arrival_month = int(request.form["arrival_month"])
            arrival_date = int(request.form["arrival_date"])
            market_segment_type = int(request.form["market_segment_type"])
            no_of_week_nights = int(request.form["no_of_week_nights"])
            no_of_weekend_nights = int(request.form["no_of_weekend_nights"])
            type_of_meal_plan = int(request.form["type_of_meal_plan"])
            room_type_reserved = int(request.form["room_type_reserved"])

# when we give input to the model in ML we convert it to a numpy array or pandas df
# in the similar senese will need to convert it to numpy array
            features = np.array([[lead_time, no_of_special_requests, avg_price_per_room,
                        arrival_month, arrival_date, market_segment_type,
                        no_of_week_nights, no_of_weekend_nights,
                        type_of_meal_plan, room_type_reserved]])

        
            prediction = loaded_model.predict(features)[0]
            proba = loaded_model.predict_proba(features)[0]
            confidence = round(proba[prediction] * 100, 2)  # percentage

        except Exception as e:
            print(f"Error during prediction: {e}")

        return render_template('index.html', prediction=prediction, confidence=confidence)

    return render_template('index.html', prediction=None, confidence=None)

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8080) # for ci-cd deployment give port 8080
