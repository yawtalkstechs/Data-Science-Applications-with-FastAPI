import joblib
import os

from sklearn.pipeline import Pipeline

model_file = os.path.join(os.path.dirname(__file__), "newgroups_model.joblib")
loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)
model, targets = loaded_model

p = model.predict(["computer cpu memory ram"])
print(targets[p[0]])