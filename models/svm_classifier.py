from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


class SVMClassifier():
    """ Initialize a support vector machine, with class_weight='balanced' because 
    our training set has roughly an equal amount of positive and negative 
    sentiment sentences"""
    def __init__(self, embed_train_data, test_data) -> None:
        self.embed_train_data = embed_train_data
        self.test_data = test_data

    def classification_model(self):
        svm_classifier = make_pipeline(StandardScaler(), SVC(class_weight='balanced')) 
        # fit the support vector machine
        svm_classifier.fit(self.embed_train_data, self.test_data)
        return svm_classifier