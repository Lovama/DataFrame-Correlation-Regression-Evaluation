# DF.CORR() and REGRESSION MODELING EVALUATION

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)

This repository contains a Python script for **automatically** conducting correlation analysis and regression modeling evaluation using pandas DataFrames (`DF`). The scripts include functions for calculating correlations between variables in a DataFrame and evaluating various regression models for predictive analysis.

## 🚀 Quick Start

1. **Set FILE_PATH.**
2. **Go to the end of the code to select "df.columns".**


🖼️ Gallery


![GIF](gif_demo.gif)


## ✨ Features

- **Correlation Analysis:** Explore relationships between variables in a DataFrame using the `corr()` function.
- **Regression Modeling Evaluation:** Evaluate the performance of regression models using metrics such as Mean Squared Error (`MSE`) and R-squared (`R2`).
- **Easy to use output lists:** Provides meaningful insights of data correlations and an easy-to-iterate list.

## 📂 Key Components

- `correlations_and_regression_widgets.ipynb`: Jupyter Notebook with the previous module + widget to adjust the degree of polynomial regression model + charts.
- `requirements.txt`: Text file with libraries needed.

## 🛠️ How to Use

1. **Clone the repository to your local machine.**
2. **Install the required dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.**
3. **Run the Python script using your preferred IDE or command line interface.**
4. **Customize the scripts to analyze your own datasets and modify the models as needed.**
   - In the `correlation_and_regression.py`, go to LINE 24 and the LAST LINE for more information.

## ❓ FAQs

- **Multiple Linear Regression:** In the `correlations_and_regression_widgets.ipynb`, when it's displayed as <em>Multiple Linear Regression</em>, it means that there's a list of predictor variables, but you can set just one predictor variable. In this case, it's a <em>Simple Linear Regression</em> displayed as <em>Multiple Linear Regression</em>.

## 📊 Console Output

```plaintext
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
| Application: DataFrame AUTO-FINDER for corr() & Regression Models Viz and Evaluation
| https://github.com/Lovama
| @2024

Highest correlations (different from 1 and -1):
           Predictor1         Predictor2  Correlation
0   compression-ratio             diesel     0.985231
1            city-mpg        highway-mpg     0.972044
2          horsepower       city-L/100km     0.889488
3              length        curb-weight     0.880665
4          wheel-base             length     0.876024
5         engine-size              price     0.872335
...
49           city-mpg             diesel     0.265676

Lowest correlations (different from 1 and -1):
           Predictor1         Predictor2  Correlation
0   compression-ratio                gas    -0.985231
1            city-mpg       city-L/100km    -0.949713
2         highway-mpg       city-L/100km    -0.930028
3          horsepower           city-mpg    -0.822214
4          horsepower        highway-mpg    -0.804575
...
49         horsepower             diesel    -0.169053

Multiple Linear Regression - Mean Squared Error: 34539979.2350, R-squared: 0.7177
Polynomial Regression (Degree 2) - Mean Squared Error: 33359585.1014, R-squared: 0.7273
```


🤝 Contributions
- Contributions to improve the code, add new features, or fix bugs are welcome! Please fork the repository, make your changes, and submit a pull request.


📜 License
- This project is licensed under the MIT License - see the LICENSE file for details.
