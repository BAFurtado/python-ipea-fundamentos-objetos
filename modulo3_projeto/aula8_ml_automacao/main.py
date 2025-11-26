import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import machines  


def main(with_sample=False):
    df = pd.read_excel('data/default_data_uci.xls', header=1)  
    # sometimes the file is .xls — convert or use pandas.read_excel

    # target variable (default next month)
    y = df["default payment next month"]
    # drop target + ID
    X = df.drop(["ID", "default payment next month"], axis=1)

    if with_sample:
        df = df.sample(frac=0.1, random_state=0)

    # if there are categorical variables, do one-hot encoding
    X = pd.get_dummies(X, drop_first=True)

    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    models = machines.run_classifiers(x_train, x_test, y_train, y_test)

if __name__ == "__main__":
    main()
