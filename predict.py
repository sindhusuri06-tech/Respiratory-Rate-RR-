import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/sepsis_model.pkl")

print("=== SepsisSense AI ===")

# Get user input
heart_rate = float(input("Heart Rate (bpm): "))
temperature = float(input("Temperature (°C): "))
blood_pressure = float(input("Blood Pressure (mmHg): "))
resp_rate = float(input("Respiratory Rate (breaths/min): "))
spo2 = float(input("SpO2 (%): "))

# Create DataFrame
patient_data = pd.DataFrame({
    "HeartRate": [heart_rate],
    "Temperature": [temperature],
    "BloodPressure": [blood_pressure],
    "RespiratoryRate": [resp_rate],
    "SpO2": [spo2]
})

# Predict
prediction = model.predict(patient_data)[0]
probability = model.predict_proba(patient_data)[0][1] * 100

# Display result
print("\n===== Prediction Result =====")

if prediction == 1:
    print("⚠ HIGH RISK OF SEPSIS")
else:
    print("✅ LOW RISK OF SEPSIS")

print(f"Risk Score: {probability:.2f}%")
