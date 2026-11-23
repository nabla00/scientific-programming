import polars as pl
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression

def open_data_file(file_name):
    data_file = pl.read_csv(file_name)
    return data_file

def preprocess_data(data_file, drop_duplicates):
    clean_data_file = data_file.drop_nulls().drop_nans()
    if drop_duplicates:
        clean_data_file = clean_data_file.unique(maintain_order=True)
    
    return clean_data_file

# Assuming the file is already preprocessed.
def split_data(data_file, random_state):
    features = data_file.drop("PE")
    target = data_file["PE"]

    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=random_state)
    return (features_train, features_test, target_train, target_test)

def create_datasets(raw_file_name, random_state):
    data_file = open_data_file(raw_file_name)
    clean_data_file = preprocess_data(data_file, True)
    clean_data_file.write_csv("datasets/clean_ccpp.csv")
    (features_train, features_test, target_train, target_test) = split_data(clean_data_file, random_state)
    features_train.write_csv("datasets/features_training.csv")
    features_test.write_csv("datasets/features_test.csv")
    target_train.to_frame().write_csv("datasets/target_training.csv")
    target_test.to_frame().write_csv("datasets/target_test.csv")

def create_datasets_keep_duplicates(raw_file_name, random_state):
    data_file = open_data_file(raw_file_name)
    clean_data_file = preprocess_data(data_file, False)
    clean_data_file.write_csv("datasets/full/clean_ccpp.csv")
    (features_train, features_test, target_train, target_test) = split_data(clean_data_file, random_state)
    features_train.write_csv("datasets/full/features_training.csv")
    features_test.write_csv("datasets/full/features_test.csv")
    target_train.to_frame().write_csv("datasets/full/target_training.csv")
    target_test.to_frame().write_csv("datasets/full/target_test.csv")

def fit_linear_line(feature):
    features_train = pl.read_csv("datasets/features_training.csv")
    features_test = pl.read_csv("datasets/features_test.csv")
    target_train = pl.read_csv("datasets/target_training.csv")
    target_test = pl.read_csv("datasets/target_test.csv")

    model = LinearRegression()
    model.fit(features_train.select(feature), target_train)
    slope = model.coef_[0]
    intercept = model.intercept_
    prediction = model.predict(features_test.select(feature))
    mae = mean_absolute_error(target_test, prediction)

    return (slope, intercept, prediction, mae)

def fit_linear_line_full(feature):
    features_train = pl.read_csv("datasets/full/features_training.csv")
    features_test = pl.read_csv("datasets/full/features_test.csv")
    target_train = pl.read_csv("datasets/full/target_training.csv")
    target_test = pl.read_csv("datasets/full/target_test.csv")

    model = LinearRegression()
    model.fit(features_train.select(feature), target_train)
    slope = model.coef_[0]
    intercept = model.intercept_
    prediction = model.predict(features_test.select(feature))
    mae = mean_absolute_error(target_test, prediction)

    return (slope, intercept, prediction, mae)

def hand_calculation():
    # Running the Calculation by Hand; Code is purely for checking.
    # Slope = -1.1681030017072855
    # Intercept = 517.8163439501609
    # V = 48.06
    # Prediction = Slope * V + Intercept = -1.1681030017072855 * 48.06 + 517.8163439501609 = 461.677313688
    # True PE = 455.27
    # Error = |Prediction - True PE| = |461.677313688 - 455.27| = 6.40731368811
    
    features_test = pl.read_csv("datasets/full/features_test.csv")
    target_test = pl.read_csv("datasets/full/target_test.csv")["PE"]
    
    (slope, intercept, _prediction, _mae) = fit_linear_line_full("V")
    slope, intercept = slope[0], intercept[0]

    i = 0
    line_number = i + 2 # 2 -> The header line is 1.
    
    vaccuum = features_test["V"][i]
    true_pe = target_test[i]
    prediction = slope * vaccuum + intercept
    error = abs(prediction - true_pe)

    print("Row Number:", line_number)
    print("V:", vaccuum)
    print("Predicted:", round(prediction, 8))
    print("True PE:", true_pe)
    print("Absolute Error:", round(error, 8))
    

# ### Requirements ###
# The project requires the folders 'dataset' and 'dataset/full' to exist.
# Inside 'dataset', the 'ccpp.csv' file must exist and be named as such.
# Inside 'dataset/full', the 'ccpp.csv' file must exist and be named as such.
# Everything else should be produced by the project.

# These only need to run once in order to create the splitted databases. Re-runs are not required, so they may be commented.
create_datasets("datasets/ccpp.csv", 42)
create_datasets_keep_duplicates("datasets/full/ccpp.csv", 42)

(slope, intercept, prediction, mae) = fit_linear_line("V")
(slope_full, intercept_full, prediction_full, mae_full) = fit_linear_line_full("V")
slope, intercept = slope[0], intercept[0]
slope_full, intercept_full = slope_full[0], intercept_full[0]

print("## Linear Regression - Duplicates Removed ##")
print("Model Slope:", slope)
print("Model Intercept:", intercept)
print("Model MAE:", mae)

print()
print()

print("## Linear Regression - Duplicates Kept ##")
print("Model Slope:", slope)
print("Model Intercept:", intercept)
print("Model MAE:", mae)

print()
print()

print("## Hand Calculation Check Run ##")
hand_calculation()

