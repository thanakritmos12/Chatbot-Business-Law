import nltk
import pprint
import word_utils
import pickle
import pandas

import pathlib

def train(input, output):
    path = pathlib.Path(__file__).parent.parent

    # prepare data
    dfs = pandas.read_excel(path/input)

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
    f = open(path/output, "wb")
    pickle.dump(classifier, f)
    f.close()

if __name__ == '__main__':
    train('data/train1.xlsx', 'data/my_classifier.pickle')