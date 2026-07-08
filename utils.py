import pandas as pd

def validate_inputs(heart_rate, temperature, blood_pressure, respiratory_rate, spo2):
    if heart_rate < 40 or heart_rate > 200:
        return False, "Heart Rate should be between 40 and 200 bpm."

    if temperature < 30 or temperature > 45:
        return False, "Temperature should be between 30°C and 45°C."

    if blood_pressure < 50 or blood_pressure > 250:
        return False, "Blood Pressure should be between 50 and 250 mmHg."

    if respiratory_rate < 5 or respiratory_rate > 50:
        return False, "Respiratory Rate should be between 5 and 50 breaths/min."

    if spo2 < 50 or spo2 > 100:
        return False, "SpO₂ should be between 50% and 100%."

    return True, "Valid Input"


def risk_level(probability):
    if probability >= 80:
        return "High Risk"
    elif probability >= 50:
        return "Moderate Risk"
    else:
        return "Low Risk"


def patient_summary(heart_rate, temperature, blood_pressure, respiratory_rate, spo2):
    return pd.DataFrame({
        "Vital Sign": [
            "Heart Rate",
            "Temperature",
            "Blood Pressure",
            "Respiratory Rate",
            "SpO₂"
        ],
        "Value": [
            f"{heart_rate} bpm",
            f"{temperature} °C",
            f"{blood_pressure} mmHg",
            f"{respiratory_rate} breaths/min",
            f"{spo2} %"
        ]
    })
