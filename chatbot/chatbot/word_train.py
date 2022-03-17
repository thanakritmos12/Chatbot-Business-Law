import nltk
import pprint
import word_utils
import pickle
import pandas

# prepare data
dfs = pandas.read_excel("train.xlsx")

questions = []
for df in dfs.to_dict("records"):
    questions.append((df["question"], df["tag"]))

print(questions)

train_data = []
for question, tag in questions:
    data = word_utils.get_features(question)
    train_data.append((data, tag))

pprint.pprint(train_data)

# train
classifier = nltk.NaiveBayesClassifier.train(train_data)

# print("Accuracy:", nltk.classify.accuracy(classifier, test_data) * 100)

# To save:
f = open("my_classifier.pickle", "wb")
pickle.dump(classifier, f)
f.close()
