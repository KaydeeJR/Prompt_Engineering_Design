from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import mlflow
import mlflow.sklearn
import numpy as np
import logging
import sys

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)
alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

with mlflow.start_run():
    svm_classifier = make_pipeline(StandardScaler(), SV(class_weight='balanced')) 
    # fit the support vector machine
    svm_classifier.fit(embed_train_data, test_data)
    predicted_qualities = lr.predict(test_x)

    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)
    mlflow.log_metric("mae", mae)

    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

    # Model registry does not work with file store
    if tracking_url_type_store != "file":

    # Register the model
    # There are other ways to use the Model Registry, which depends  the use case,
    # please refer to the doc for more information:
    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
        mlflow.sklearn.log_model(lr, "model", registered_model_name="ElasticnetWineModel")
    else:
        mlflow.sklearn.log_model(lr, "model")


class SVMClassifier():
    """ Initialize a support vector machine, with class_weight='balanced' because 
    our training set has roughly an equal amount of positive and negative sentiment sentences"""
    def __init__(self, embed_train_data, test_data) -> None:
        self.embed_train_data = embed_train_data
        self.test_data = test_data

    def classification_model(self):
        svm_classifier = make_pipeline(StandardScaler(), SVC(class_weight='balanced')) 
        # fit the support vector machine
        svm_classifier.fit(self.embed_train_data, self.test_data)
        return svm_classifier