from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDClassifier


def run_classifiers(x, x_test, y, y_test):

    models = ['Tree', 'MLP', 'SGD', 'Voting']

    m1 = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=0)
    m3 = SGDClassifier(loss="log_loss", max_iter=2000)
    m4 = MLPClassifier(hidden_layer_sizes=(32,), max_iter=500)

    voting = VotingClassifier(estimators=[('rf', m1), ('sgd', m3), ('neural', m4)], voting='soft')

    cls = [m1, m3, m4, voting]

    for each in cls:
        each.fit(x, y)

    models = dict(zip(models, cls))

    for key in models:
        yhat = models[key].predict(x_test)
        acc = accuracy_score(y_test, yhat)
        cm = confusion_matrix(y_test, yhat)

        print(f"\n=== {key} ===")
        print(f"Accuracy: {acc:.4f}")
        print("Confusion matrix:")
        print(cm)
        print("\nClassification report:")
        print(classification_report(y_test, yhat))

    return models

