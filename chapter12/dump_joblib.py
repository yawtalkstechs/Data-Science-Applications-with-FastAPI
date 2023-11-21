import joblib
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

categories = [
    "soc.religion.christian",
    "talk.religion.misc",
    "comp.sys.mac.hardware",
    "sci.crypt",
]

newgroups_training = fetch_20newsgroups(
    subset="train", categories=categories, random_state=0
)

newgroups_testing = fetch_20newsgroups(
    subset="test", categories=categories, random_state=0
)

model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

model.fit(newgroups_training.data, newgroups_training.target)

model_file = "newgroups_model.joblib"
model_targets_tuple = (model, newgroups_training.target_names)
joblib.dump(model_targets_tuple, model_file)