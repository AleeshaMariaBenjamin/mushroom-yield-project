import joblib

model = joblib.load("models/champion.joblib")

print(type(model))

try:
    print("Feature importances:")
    print(model.feature_importances_)
except:
    print("No feature importances available")
    