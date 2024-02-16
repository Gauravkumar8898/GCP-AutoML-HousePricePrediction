from src.utils.constant import data_directory, data_gcs_path
import logging

logging.basicConfig(level=logging.INFO)


def manage_data():
    from src.utils.constant import categorical_cols
    import logging
    import pandas as pd

    import numpy as np
    dataset = pd.read_csv(data_gcs_path)
    logging.info("reading data.....")
    df = pd.get_dummies(dataset, columns=categorical_cols)

    # Replace NaNs with mean
    df = df.fillna(df.mean())

    # Separate features and labels
    X, y = df.drop(columns=['id', 'stroke']), df['stroke'].values

    # Split data into training set and test set
    logging.info("train test split ...!")

    logging.info("data prepare complete")
    np.save(f"{data_directory}/x.npy", X)
    np.save(f"{data_directory}/y.npy", y)


def decision_classifier():
    import logging
    import pickle
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    X = np.load(f"{data_directory}/x.npy", allow_pickle=True)
    y = np.load(f"{data_directory}/y.npy", allow_pickle=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
    model = DecisionTreeClassifier().fit(X_train, y_train)
    logging.info("model is trained ...")
    with open(f"{data_directory}/model.pkl", 'wb') as f:
        pickle.dump(model, f)
    logging.info("model saved")
