from predict import predict_yield

result = predict_yield(
    temperature=25,
    humidity=80,
    CO2=1000
)

print(
    f"Predicted Yield: {result}"
)