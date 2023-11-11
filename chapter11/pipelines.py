import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
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
    MultinomialNB(),
)

model.fit(newgroups_training.data, newgroups_training.target)

predicted_targets = model.predict(newgroups_testing.data)

accuracy = accuracy_score(newgroups_testing.target, predicted_targets)
print(accuracy)

confusion = confusion_matrix(newgroups_testing.target, predicted_targets)
confusion_df = pd.DataFrame(confusion, 
                            index=pd.Index(newgroups_testing.target_names, name="True"),
                            columns=pd.Index(newgroups_testing.target_names, name="Predicted"),
                            )

print(confusion_df)