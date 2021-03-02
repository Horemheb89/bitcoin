from BitcoinPrediction.data import get_data
from BitcoinPrediction.models import cross_val
from BitcoinPrediction.mlflow_base import MLFlowBase

from itertools import product
# from BitcoinPrediction.preprocessing import preprocessing_data, features_target
# from BitcoinPrediction.train_test_split import input_data
# from BitcoinPrediction.utils import select_date

# import joblib
# from termcolor import colored
# import mlflow
# from memoized_property import memoized_property
# from mlflow.tracking import MlflowClient
# from BitcoinPrediction.params_gcp import BUCKET_NAME, BUCKET_TRAIN_DATA_PATH, MODEL_NAME, MODEL_VERSION 


# MLFLOW_URI = "https://mlflow.lewagon.co/" # Valider qu'on ne doit pas utiliser un autre URI que celui du wagon
# EXPERIMENT_NAME = "bitcoin_hist_results"




class Trainer(MLFlowBase):

    def __init__(self):
        super().__init__(
            "[FR] [Paris] [nhuberde] bitcoin project",
            "https://mlflow.lewagon.co")
            
    # def train(self, trainer_params, hyper_params):
    def train(self, trainer_params):

        i = 0

        # step 1 : iterate on trainer params
        for param_combination in product(*trainer_params.values()):

            exp_params = dict(zip(trainer_params.keys(), param_combination))

            # print(exp_params)

            # step 2 : iterate on models
            # for model_name, model_hparams in hyper_params.items():

                # print(f"model name {model_name}")

                # step 3 : iterate on model hyperparams
                # for hparam_combi in product(*model_hparams.values()):

                #     hexp_params = dict(zip(model_hparams.keys(), hparam_combi))

                    # print(hexp_params)

                    # mais avec quoi je train ?
            i += 1
            print(f"\nexperiment #{i}:")
            print(exp_params)
            # print(f"model name {model_name}")
            # print(hexp_params)

            # TODO: train with trainer params + model + hyperparams

            # => appeler la crossval
            data = get_data()
            score = cross_val(data, **exp_params)

            # then log on mlflow

            # create a mlflow training
            self.mlflow_create_run()  # create one training

            # log trainer params
            for key, value in exp_params.items():
                self.mlflow_log_param(key, value)

            # log params
            # self.mlflow_log_param("model", model_name)

            # log model hyper params
            # for key, value in hexp_params.items():
            #     self.mlflow_log_param(key, value)

            # push metrics to mlflow
            self.mlflow_log_metric("mean_score", score['mean_score'])
            self.mlflow_log_metric("std", score['std'])
            self.mlflow_log_metric("score_min", score['score_min'])
            self.mlflow_log_metric("score_max", score['score_max'])


# if __name__ == "__main__":

