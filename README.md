# DF.CORR() and REGRESSION MODELING EVALUATION

This repository contains a Python script for **automatically** conducting correlation analysis and regression modeling evaluation using pandas DataFrames (`DF`). The scripts include functions for calculating correlations between variables in a DataFrame and evaluating various regression models for predictive analysis.

## For FAST READERS!!!

- Simply execute the file and go to the last line of the code.


## Features:

- **Correlation Analysis:** Explore relationships between variables in a DataFrame using the `corr()` function.
- **Regression Modeling Evaluation:** Evaluate the performance of regression models using metrics such as Mean Squared Error (`MSE`) and R-squared (`R2`).
- **Easy to use output lists:** Gives meaningful insights of data correlations and an easy to iterate list.


## Key Components:

- `correlations_and_regression_widgets.ipynb`: Jupyter Notebook with the previous module + widget to adjust the degree of polynomial regression model + charts.
- `requirements.txt`: Text file with libraries needed.


## How to Use:

1. Clone the repository to your local machine.
2. Install the required dependencies listed in `requirements.txt` using `pip freeze`.
3. Run the Python script using your preferred IDE or command line interface.
4. Customize the scripts to analyze your own datasets and modify the models as needed.
- In the `correlation_and_regression.py` go to LINE 24 and LAST LINE for more information.


## DOUBTS?

- In the `correlations_and_regression_widgets.ipynb`, when it's displayed <em>Multiple Linear Regression</em>, it means that there's a list of predictors variables, <strong>but</strong> you can set just one predictor variable. In this case it's a <em>Simple Linear Regression</em> displayed as <em>Multiple Linear Regression</em>.

## Console Output:

- Given a Data Set, the console output should look like this:
```


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
    


Highest correlations (different from 1 and -1):
           Predictor1         Predictor2  Correlation
0   compression-ratio             diesel     0.985231
1            city-mpg        highway-mpg     0.972044
2          horsepower       city-L/100km     0.889488
3              length        curb-weight     0.880665
4          wheel-base             length     0.876024
5         engine-size              price     0.872335
6               width        curb-weight     0.866201
7              length              width     0.857170
8         curb-weight        engine-size     0.849072
9         curb-weight              price     0.834415
10        engine-size         horsepower     0.822676
11         wheel-base              width     0.814507
12         horsepower              price     0.809575
13              price       city-L/100km     0.789898
14        curb-weight       city-L/100km     0.785353
15         wheel-base        curb-weight     0.782097
16        curb-weight         horsepower     0.757976
17              width              price     0.751265
18        engine-size       city-L/100km     0.745059
19              width        engine-size     0.729436
20             length              price     0.690628
21             length        engine-size     0.685025
22              width       city-L/100km     0.673363
23             length       city-L/100km     0.657373
24        curb-weight               bore     0.644060
25              width         horsepower     0.615077
26             length               bore     0.608971
27         wheel-base             height     0.590742
28         wheel-base              price     0.584642
29             length         horsepower     0.579821
30        engine-size               bore     0.572609
31         wheel-base        engine-size     0.572027
32               bore         horsepower     0.566936
33               bore       city-L/100km     0.554610
34              width               bore     0.544885
35               bore              price     0.543155
36         wheel-base               bore     0.493244
37             length             height     0.492063
38         wheel-base       city-L/100km     0.476153
39           peak-rpm                gas     0.475812
40          symboling  normalized-losses     0.466264
41         wheel-base         horsepower     0.371147
42  compression-ratio           city-mpg     0.331425
43             height        curb-weight     0.307581
44         wheel-base             diesel     0.307237
45              width             height     0.306002
46             height             diesel     0.281578
47          symboling           peak-rpm     0.279740
48  compression-ratio        highway-mpg     0.268465
49           city-mpg             diesel     0.265676


Lowest correlations (different from 1 and -1):
           Predictor1         Predictor2  Correlation
0   compression-ratio                gas    -0.985231
1            city-mpg       city-L/100km    -0.949713
2         highway-mpg       city-L/100km    -0.930028
3          horsepower           city-mpg    -0.822214
4          horsepower        highway-mpg    -0.804575
5         curb-weight        highway-mpg    -0.794889
6         curb-weight           city-mpg    -0.749543
7         highway-mpg              price    -0.704692
8              length        highway-mpg    -0.698142
9            city-mpg              price    -0.686571
10              width        highway-mpg    -0.680635
11        engine-size        highway-mpg    -0.679571
12             length           city-mpg    -0.665192
13        engine-size           city-mpg    -0.650546
14              width           city-mpg    -0.633531
15               bore        highway-mpg    -0.591309
16               bore           city-mpg    -0.582027
17          symboling             height    -0.550160
18         wheel-base        highway-mpg    -0.543304
19          symboling         wheel-base    -0.535987
20           peak-rpm             diesel    -0.475812
21         wheel-base           city-mpg    -0.470606
22  compression-ratio           peak-rpm    -0.435780
23  normalized-losses             height    -0.373737
24          symboling             length    -0.365404
25         wheel-base           peak-rpm    -0.360305
26             height           peak-rpm    -0.309974
27         wheel-base                gas    -0.307237
28  compression-ratio       city-L/100km    -0.299372
29             length           peak-rpm    -0.285970
30             height                gas    -0.281578
31        curb-weight           peak-rpm    -0.279361
32               bore           peak-rpm    -0.267392
33           city-mpg                gas    -0.265676
34        engine-size           peak-rpm    -0.256733
35              width           peak-rpm    -0.245800
36              width                gas    -0.244356
37          symboling              width    -0.242423
38             stroke                gas    -0.241303
39       city-L/100km             diesel    -0.241282
40          symboling        curb-weight    -0.233118
41  normalized-losses           city-mpg    -0.225016
42        curb-weight                gas    -0.221046
43  compression-ratio         horsepower    -0.214514
44             length                gas    -0.211187
45        highway-mpg                gas    -0.198690
46          symboling             diesel    -0.196735
47          symboling  compression-ratio    -0.182196
48  normalized-losses        highway-mpg    -0.181877
49         horsepower             diesel    -0.169053


List of Highest Combinations:
[['compression-ratio', 'diesel', 0.9852311290083917], ['city-mpg', 'highway-mpg', 0.9720437058960102], ['horsepower', 'city-L/100km', 0.8894882601555544], ['length', 'curb-weight', 0.8806647862654423], ['wheel-base', 'length', 0.8760238919618005], ['engine-size', 'price', 0.8723351674455182], ['width', 'curb-weight', 0.8662010980938418], ['length', 'width', 0.8571703218913005], ['curb-weight', 'engine-size', 0.8490716606415313], ['curb-weight', 'price', 0.834414525770285], ['engine-size', 'horsepower', 0.8226756460813216], ['wheel-base', 'width', 0.8145066522681035], ['horsepower', 'price', 0.8095745670036568], ['price', 'city-L/100km', 0.7898975136626947], ['curb-weight', 'city-L/100km', 0.7853533294476132], ['wheel-base', 'curb-weight', 0.782097244415664], ['curb-weight', 'horsepower', 0.7579756117015163], ['width', 'price', 0.7512653440522677], ['engine-size', 'city-L/100km', 0.7450588874770459], ['width', 'engine-size', 0.7294356383711981], ['length', 'price', 0.6906283804483649], ['length', 'engine-size', 0.6850247620753405], ['width', 'city-L/100km', 0.6733628497672186], ['length', 'city-L/100km', 0.6573726074789643], ['curb-weight', 'bore', 0.6440604789083982], ['width', 'horsepower', 0.6150767382953459], ['length', 'bore', 0.6089709700250034], ['wheel-base', 'height', 0.5907416748215092], ['wheel-base', 'price', 0.5846418222655075], ['length', 'horsepower', 0.5798214549142009], ['engine-size', 'bore', 0.5726093256553538], ['wheel-base', 'engine-size', 0.5720266928058414], ['bore', 'horsepower', 0.5669355262876099], ['bore', 'city-L/100km', 0.5546103635074106], ['width', 'bore', 0.5448854634757401], ['bore', 'price', 0.5431553832626603], ['wheel-base', 'bore', 0.49324418602960135], ['length', 'height', 0.4920625494156024], ['wheel-base', 'city-L/100km', 0.4761528741935937], ['peak-rpm', 'gas', 0.4758119321728285], ['symboling', 'normalized-losses', 0.46626375799151326], ['wheel-base', 'horsepower', 0.37114668276650403], ['compression-ratio', 'city-mpg', 0.33142483884243595], ['height', 'curb-weight', 0.30758081972622253], ['wheel-base', 'diesel', 0.30723721845928237], ['width', 'height', 0.3060021617034482], ['height', 'diesel', 0.2815784474718142], ['symboling', 'peak-rpm', 0.27973965896374103], ['compression-ratio', 'highway-mpg', 0.2684648475460542], ['city-mpg', 'diesel', 0.26567569646153183]]


List of Lowest Combinations:
[['compression-ratio', 'gas', -0.9852311290083914], ['city-mpg', 'city-L/100km', -0.949712910616761], ['highway-mpg', 'city-L/100km', -0.9300278818761628], ['horsepower', 'city-mpg', -0.8222143251628639], ['horsepower', 'highway-mpg', -0.8045747816033887], ['curb-weight', 'highway-mpg', -0.7948889423035673], ['curb-weight', 'city-mpg', -0.7495430863216357], ['highway-mpg', 'price', -0.7046922650589531], ['length', 'highway-mpg', -0.6981418469786207], ['city-mpg', 'price', -0.6865710067844684], ['width', 'highway-mpg', -0.6806352140910513], ['engine-size', 'highway-mpg', -0.6795712591220742], ['length', 'city-mpg', -0.6651923947142154], ['engine-size', 'city-mpg', -0.6505459759740386], ['width', 'city-mpg', -0.633530639341753], ['bore', 'highway-mpg', -0.5913092391650802], ['bore', 'city-mpg', -0.5820270499536312], ['symboling', 'height', -0.5501598641343745], ['wheel-base', 'highway-mpg', -0.5433044680377366], ['symboling', 'wheel-base', -0.5359868030343233], ['peak-rpm', 'diesel', -0.4758119321728286], ['wheel-base', 'city-mpg', -0.4706064088423566], ['compression-ratio', 'peak-rpm', -0.435779763301587], ['normalized-losses', 'height', -0.3737369502352739], ['symboling', 'length', -0.3654043627907566], ['wheel-base', 'peak-rpm', -0.3603045279169449], ['height', 'peak-rpm', -0.30997400245174694], ['wheel-base', 'gas', -0.3072372184592825], ['compression-ratio', 'city-L/100km', -0.2993715132652865], ['length', 'peak-rpm', -0.2859695997007056], ['height', 'gas', -0.2815784474718143], ['curb-weight', 'peak-rpm', -0.27936061978835147], ['bore', 'peak-rpm', -0.2673915985169951], ['city-mpg', 'gas', -0.26567569646153183], ['engine-size', 'peak-rpm', -0.2567329744707591], ['width', 'peak-rpm', -0.24580014375355738], ['width', 'gas', -0.24435576670039616], ['symboling', 'width', -0.2424226038916475], ['stroke', 'gas', -0.2413034454482311], ['city-L/100km', 'diesel', -0.2412823477404384], ['symboling', 'curb-weight', -0.2331184853695864], ['normalized-losses', 'city-mpg', -0.22501572863445693], ['curb-weight', 'gas', -0.22104562326657237], ['compression-ratio', 'horsepower', -0.21451413568333663], ['length', 'gas', -0.211186943726097], ['highway-mpg', 'gas', -0.19869018404293334], ['symboling', 'diesel', -0.1967352925088923], ['symboling', 'compression-ratio', -0.18219615797610494], ['normalized-losses', 'highway-mpg', -0.18187718191761093], ['horsepower', 'diesel', -0.16905251875871052]]

Multiple Linear Regression - Mean Squared Error: 34539979.2350, R-squared: 0.7177

Polynomial Regression (Degree 2) - Mean Squared Error: 33359585.1014, R-squared: 0.7273
```

## Gallery:
![Screenshot 2024-03-25 151906](https://github.com/HappyCoderBr/DF-CORR-and-REGRESSION-MODELING-EVALUATION/assets/48333433/2a45744d-5c19-4066-b58c-5e2b6901c095)
![Screenshot 2024-03-25 151918](https://github.com/HappyCoderBr/DF-CORR-and-REGRESSION-MODELING-EVALUATION/assets/48333433/0f418771-2ba7-4060-a2df-364e3e4991b4)
![Screenshot 2024-03-25 151931](https://github.com/HappyCoderBr/DF-CORR-and-REGRESSION-MODELING-EVALUATION/assets/48333433/f21bb4bf-6018-43f6-81eb-c7b5eea98d50)
![Screenshot 2024-03-25 152020](https://github.com/HappyCoderBr/DF-CORR-and-REGRESSION-MODELING-EVALUATION/assets/48333433/cded6502-bcff-4ece-8158-a8d3ad98b65a)

![Screenshot 2024-03-25 145513](https://github.com/HappyCoderBr/DF-CORR-and-REGRESSION-MODELING-EVALUATION/assets/48333433/31d42f73-b51b-4cbd-9787-f62c492057c3)
![Screenshot 2024-03-25 145524](https://github.com/HappyCoderBr/DF-CORR-and-REGRESSION-MODELING-EVALUATION/assets/48333433/6fd6ec7d-488a-44a7-9dc6-91e99276b29a)
![Screenshot 2024-03-25 145535](https://github.com/HappyCoderBr/DF-CORR-and-REGRESSION-MODELING-EVALUATION/assets/48333433/b6ac4592-800e-4497-8941-07f748df8fbf)
![Screenshot 2024-03-25 145554](https://github.com/HappyCoderBr/DF-CORR-and-REGRESSION-MODELING-EVALUATION/assets/48333433/e3595464-1df0-4a4f-81fd-783ee4c5f4a0)


## Contributions:

Contributions to improve the code, add new features, or fix bugs are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

