import os
import platform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from colorama import Fore, Style
from ipywidgets import interact
import ipywidgets as widgets


def clear_terminal():
    """Clears the terminal screen."""
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


######################################################################
# CORRELATIONS #
######################################################################
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

FILE_PATH = "automobileEDA.csv"
df = pd.read_csv(FILE_PATH, header=0)


def highest_lowest_correlations(source, top_n):
    """
    Calculates the highest and lowest correlations different from 1 and -1 in a DataFrame.

    Parameters:
    - source (pd.DataFrame): The source DataFrame.
    - top_n (int): Number of highest and lowest correlations to be returned.

    Returns:
    - highest_correlations_df (pd.DataFrame): DataFrame with the highest correlations.
    - lowest_correlations_df (pd.DataFrame): DataFrame with the lowest correlations.
    - highest_combinations_list (list): List of lists with the highest combinations.
    - lowest_combinations_list (list): List of lists with the lowest combinations.
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


highest, lowest, highest_combinations, lowest_combinations = highest_lowest_correlations(
    df, 99)

clear_terminal()

print_colored_title(
    '''
                                                                     
    ,o888888o.        ,o888888o.     8 888888888o.   8 888888888o.   
   8888     `88.   . 8888     `88.   8 8888    `88.  8 8888    `88.  
,8 8888       `8. ,8 8888       `8b  8 8888     `88  8 8888     `88  
88 8888           88 8888        `8b 8 8888     ,88  8 8888     ,88  
88 8888           88 8888         88 8 8888.   ,88'  8 8888.   ,88'  
88 8888           88 8888         88 8 888888888P'   8 888888888P'   
88 8888           88 8888        ,8P 8 8888`8b       8 8888`8b       
`8 8888       .8' `8 8888       ,8P  8 8888 `8b.     8 8888 `8b.     
   8888     ,88'   ` 8888     ,88'   8 8888   `8b.   8 8888   `8b.   
    `8888888P'        `8888888P'     8 8888     `88. 8 8888     `88. 


| Creator: Lorenzo Vaz Marzari
|
| Application: DataFrame AUTO-FINDER for corr() 
|                           & 
|              Regression Models Viz and Evaluation
|
| https://github.com/Lovama
|
| @2024
    ''')

print(
    f"\n\n{Fore.CYAN}Highest correlations (different from 1 and -1):{Style.RESET_ALL}")
print(highest)

print(f"\n\n{Fore.MAGENTA}Lowest correlations (different from 1 and -1):{Style.RESET_ALL}")
print(lowest)

print(f"\n\n{Fore.YELLOW}List of Highest Combinations:{Style.RESET_ALL}")
print(highest_combinations)

print(f"\n\n{Fore.RED}List of Lowest Combinations:{Style.RESET_ALL}")
print(lowest_combinations)

######################################################################
# MSE, R2 #
######################################################################


def plot_regression(predictor_variable, predicted_variable, polynomial_degree):
    """
    Plots the regression model for given predictor and predicted variables.

    Parameters:
    - predictor_variable (pd.DataFrame): The predictor variable DataFrame. One or more df.columns
    - predicted_variable (pd.Series): The predicted variable Series. Just one df.column
    - polynomial_degree (int): Degree of the polynomial for polynomial regression.
    """
    if len(predictor_variable.columns) > 1:
        model_name = 'Multiple Linear Regression'
    else:
        model_name = 'Simple Linear Regression'

    X_train, X_test, y_train, y_test = train_test_split(
        predictor_variable, predicted_variable, test_size=0.2, random_state=42
    )

    for degree in range(1, polynomial_degree + 1):
        poly = PolynomialFeatures(degree=degree)
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.transform(X_test)

        poly_model = LinearRegression()
        poly_model.fit(X_train_poly, y_train)

        y_pred_poly = poly_model.predict(X_test_poly)

        mse_poly = mean_squared_error(y_test, y_pred_poly)
        r2_poly = r2_score(y_test, y_pred_poly)

        if degree == 1:
            print(
                f"\n{Fore.BLUE}{model_name}{Style.RESET_ALL} - Mean Squared Error: {mse_poly:.4f}, R-squared: {r2_poly:.4f}\n")
        else:
            print(f"{Fore.GREEN}Polynomial Regression (Degree {degree}){Style.RESET_ALL} - Mean Squared Error: {mse_poly:.4f}, R-squared: {r2_poly:.4f}\n")

        plt.figure(figsize=(8, 6))
        sns.set(style="darkgrid", rc={
                "axes.facecolor": "#2E2E2E", "grid.color": "#404040"})

        x_label = ', '.join(predictor_variable.columns)

        sns.regplot(x=X_test.iloc[:, 0], y=y_test, scatter_kws={
                    's': 20, 'color': 'blue'}, order=degree, ci=None, line_kws={'color': 'chartreuse'})
        plt.title(f'{model_name} - Polynomial Degree {degree}')
        plt.xlabel(x_label)
        plt.ylabel(predicted_variable.name)
        plt.show()


degree_slider = widgets.IntSlider(
    value=2, min=1, max=10, step=1, description='Polynomial Degree')

interact(plot_regression, predictor_variable=widgets.fixed(df[['engine-size', 'length']]),
         predicted_variable=widgets.fixed(df['price']),
         polynomial_degree=degree_slider)
