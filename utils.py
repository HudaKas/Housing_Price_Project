import seaborn as sns

def plot(df, col):
    """
    This function combines the matplotlib hist function with the seaborn kdeplot() and rugplot() functions.
    
    Parameters
    ----------
    df: pandas dataframe
      df containing column/s with numeric values
     
    col: numeric
      numeric column either integer or float
    
    Returns
    -------
    plot
     Returns the Axes object with the plot
     
     
    
    """
    return sns.distplot(df[col])


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def evaluate_model(y_train, y_test, y_train_preds, y_test_preds):
    """
    Evaluates a model, based on training and testing predictions
    In terms of R2, Mean Absolute Error, and Root Mean Squared Error
    --
    Inputs:
     - y_train - true target for training set (output of train/test split)
     - y_test - true target for test set
     - y_train_preds - predicted target for training set (output of model.predict)
     - y_test_preds - predicted target for test set
    """
    print(f"Train R2: {r2_score(y_train, y_train_preds):.3f}")
    print(f"Test R2: {r2_score(y_test, y_test_preds):.3f}")
    print("---")
    print(f"Train MAE: {mean_absolute_error(y_train, y_train_preds):.3f}")
    print(f"Test MAE: {mean_absolute_error(y_test, y_test_preds):.3f}")
    print("---")
    print(f"Train RMSE: {mean_squared_error(y_train, y_train_preds, squared=False):.3f}")
    print(f"Test RMSE: {mean_squared_error(y_test, y_test_preds, squared=False):.3f}")