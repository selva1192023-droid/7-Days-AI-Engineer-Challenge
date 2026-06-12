from sklearn.linear_model import LinearRegression
import numpy as np

hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
scores = np.array([20, 40, 50, 70, 90])

model = LinearRegression()
model.fit(hours, scores)

prediction = model.predict([[6]])

print("Predicted Score for 6 Hours Study:")
print(prediction[0])
