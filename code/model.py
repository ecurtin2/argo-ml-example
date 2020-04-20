from typing import Dict, List

import joblib
import pandas as pd
from loguru import logger
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

from schema import FEAT_COLUMNS, TARGET_COLUMNS


def train(data: List[Dict], test_size: float, random_state: int):
    logger.info(
        f"Training a model with test size: {test_size} and random state: {random_state}"
    )

    df = pd.DataFrame(data)
    X, y = df[FEAT_COLUMNS], df[TARGET_COLUMNS]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    model = tree.DecisionTreeClassifier()
    model.fit(X_train, y_train)
    logger.info(f"Done training model")
    return model


def save(m, path):
    logger.info(f"Saving model to {path}")
    joblib.dump(m, path)
    logger.info("Saving complete.")


def load(path):
    logger.info(f"Loading model from {path}")
    m = joblib.load(path)
    logger.info("Successfully loaded model")
    return m
