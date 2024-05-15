"""
| Creator: Lorenzo Vaz Marzari                  
|
| Application: DataFrame AUTO-FINDER for corr()
|
| https://github.com/HappyCoderBr
|
| @2024
L_______________________________________________

Module to analyze data correlations and perform regression modeling evaluation.
Go to LINE 24 and LAST LINE for more information
"""

import os
import platform
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd
from colorama import Fore, Style

FILE_PATH = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"


def clear_terminal():
    """
    Clears the terminal based on the operating system.
    """
    system = platform.system().lower()
    if system.startswith('win'):
        os.system('cls')
    elif system.startswith('linux') or system.startswith('darwin'):
        os.system('clear')
    else:
        print("Unsupported operating system for terminal clearing.")


def print_colored_title(title):
    """
    Prints a colored and styled title.

    Args:
        title (str): The title to be printed.
    """
    print(f"{Style.BRIGHT}{Fore.YELLOW}{title}{Style.RESET_ALL}")

############################################################L#########
# CORR #
######################################################################


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

DF = pd.read_csv(FILE_PATH, header=0)


def highest_lowest_correlations(source, top_n):
    """
    Calculates the highest and lowest correlations different from 1 and -1 in a DataFrame.

    Args:
        source (pd.DataFrame): The source DataFrame.
        top_n (int): Number of highest and lowest correlations to be returned.

    Returns:
        pd.DataFrame: DataFrame with the highest correlations.
        pd.DataFrame: DataFrame with the lowest correlations.
        list: List of lists with the highest combinations.
        list: List of lists with the lowest combinations.
    """
    correlation_matrix = source.corr()
    correlation_matrix = correlation_matrix.where(
        ~((correlation_matrix == 1) | (correlation_matrix == -1)))
    flattened_correlations = correlation_matrix.unstack().dropna()
    added_combinations = set()

    highest_correlations = []
    lowest_correlations = []

    for index, value in flattened_correlations.nlargest(top_n).iteritems():
        predictor1, predictor2 = index
        if (predictor1, predictor2) not in added_combinations and (predictor2, predictor1) not in added_combinations:
            highest_correlations.append([predictor1, predictor2, value])
            added_combinations.add((predictor1, predictor2))

    for index, value in flattened_correlations.nsmallest(top_n).iteritems():
        predictor1, predictor2 = index
        if (predictor1, predictor2) not in added_combinations and (predictor2, predictor1) not in added_combinations:
            lowest_correlations.append([predictor1, predictor2, value])
            added_combinations.add((predictor1, predictor2))

    highest_correlations_df = pd.DataFrame(highest_correlations, columns=[
                                           'Predictor1', 'Predictor2', 'Correlation'])
    lowest_correlations_df = pd.DataFrame(lowest_correlations, columns=[
                                          'Predictor1', 'Predictor2', 'Correlation'])

    highest_combinations_list = highest_correlations_df.values.tolist()
    lowest_combinations_list = lowest_correlations_df.values.tolist()

    return highest_correlations_df, lowest_correlations_df, highest_combinations_list, lowest_combinations_list


HIGHEST, LOWEST, HIGHEST_COMBINATIONS, LOWEST_COMBINATIONS = highest_lowest_correlations(
    DF, 99)

clear_terminal()

print_colored_title(
    '''
| Creator: Lorenzo Vaz Marzari 
|
| Application: DataFrame AUTO-FINDER for corr()
|
| https://github.com/HappyCoderBr
|
| @2024
    ''')

print(f"\n\n{Fore.GREEN}Highest correlations (different from 1 and -1):{Style.RESET_ALL}")
print(HIGHEST)

print(f"\n\n{Fore.RED}Lowest correlations (different from 1 and -1):{Style.RESET_ALL}")
print(LOWEST)

print(f"\n\n{Fore.CYAN}List of Highest Combinations:{Style.RESET_ALL}")
print(HIGHEST_COMBINATIONS)

print(f"\n\n{Fore.MAGENTA}List of Lowest Combinations:{Style.RESET_ALL}")
print(LOWEST_COMBINATIONS)

############################################################V#########
# Mean Squared Error and R-Rquared #
######################################################################


def regression_model_evaluation(predictor_variable, predicted_variable, polynomial_degree=2):
    """
    Performs regression modeling and evaluates the model.

    Args:
        predictor_variable (pd.Series): The variable to be predicted.
        predicted_variable (pd.DataFrame): The list of predictor variables.
        polynomial_degree (int): Degree of polynomial features. Default -> 2

    Returns:
        None
    """
    model = LinearRegression()
    model_name = 'Multiple Linear Regression' if len(
        predictor_variable.columns) > 1 else 'Simple Linear Regression'

    x_train, x_test, y_train, y_test = train_test_split(
        predictor_variable, predicted_variable, test_size=0.2, random_state=42)

    model.fit(x_train, y_train)

    for degree in range(1, polynomial_degree + 1):
        if degree == 1:
            x_train_poly = x_train.values.reshape(-1, 1)
            x_test_poly = x_test.values.reshape(-1, 1)
        else:
            poly = PolynomialFeatures(degree=degree)
            x_train_poly = poly.fit_transform(x_train)
            x_test_poly = poly.transform(x_test)

        poly_model = LinearRegression()
        poly_model.fit(x_train_poly, y_train)
        y_pred_poly = poly_model.predict(x_test_poly)

        mse_poly = mean_squared_error(y_test, y_pred_poly)
        r2_poly = r2_score(y_test, y_pred_poly)

        if degree == 1:
            print(
                f"\n{Fore.BLUE}{model_name}{Style.RESET_ALL} - Mean Squared Error: {mse_poly:.4f}, R-squared: {r2_poly:.4f}\n")
        else:
            print(f"{Fore.GREEN}Polynomial Regression (Degree {degree}){Style.RESET_ALL} - Mean Squared Error: {mse_poly:.4f}, R-squared: {r2_poly:.4f}\n")


regression_model_evaluation(
    DF[['engine-size']], DF['price'], polynomial_degree=3)
