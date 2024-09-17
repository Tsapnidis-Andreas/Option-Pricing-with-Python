# Project Title
## Option Pricing with Python <br>
# Contents
[Info](#Info)<br>
[Black Scholes Model for Option Pricing](#Black-Scholes-Model-for-Option-Pricing)<br>
[Monte Carlo Simulation for Option Pricing](#Monte-Carlo-Simulation-for-Option-Pricing)<br>
[Disclaimer](#Disclaimer)
# Info
## Programming Language: 
Python <br>
## Libraries used:
[Pandas](https://pandas.pydata.org/#:~:text=pandas%20is%20a%20fast,%20powerful,%20flexible)<br>
[Numpy](https://numpy.org/)<br>
[Matplotlib](https://matplotlib.org/)<br>
[Yfinance](https://pypi.org/project/yfinance/)<br>
[Datetime](https://docs.python.org/3/library/datetime.html)<br>
[Scipy](https://scipy.org/)<br>
[Openpyxl](https://pypi.org/project/openpyxl/#:~:text=openpyxl%20is%20a%20Python%20library%20to)<br>
[Xlsxwriter](https://pypi.org/project/XlsxWriter/#:~:text=XlsxWriter%20is%20a%20Python%20module%20for)<br>
# Black Scholes Model for Option Pricing
## How to use
Install the libraries mentioned above<br>
Initialize:<br>
The variable ‘stock’ with the ticker symbol of the stock<br>
The variable ‘days’ with the number of days left<br>
Tthe variable ‘path’ with the directory where the excel and png files will be saved<br>


## How it works
### The code entails:
Pulling the 13 week treasury bill yield rate(^IRX) and setting the risk free rate to be equal to it<br>
Pulling the stock’s last closing price from yahoo finance<br>
Pulling the closing prices of the last 365 days to calculate the standard deviation<br>
Using the Black Scholes formulas to price the call and put options for a range of strike prices<br>
Saving the table in an excel file<br>
Plotting the results and saving the graph as a png file<br>
## Example
![1](https://github.com/user-attachments/assets/83efd1c7-3dbc-4597-96bc-59680aafe168)
![2](https://github.com/user-attachments/assets/e954830b-7483-4df7-8493-c9045343964a)

# Monte Carlo Simulation for Option Pricing

## How to use
Install the libraries mentioned above<br>
Initialize:<br>
The variable ‘stock’ with the ticker symbol of the stock<br>
The variable ‘days’ with the number of days left<br>
Tthe variable ‘path’ with the directory where the excel and png files will be saved<br>

## How it works
### The code entails:
Pulling the 13 week treasury bill yield rate(^IRX) and setting the risk free rate to be equal to it<br>
Pulling the stock’s last closing price from yahoo finance<br>
Pulling the closing prices of the last 365 days to calculate the standard deviation
Creating a range of strike prices<br>
Running 1000 Monte Carlo simulations for each strike price, based on the Brownian motion to create different scenarios regarding the stock’s future returns<br>
Calculating the option’s Net Present Value for each strike price<br>
Saving the table in an excel file<br>
Plotting 10 different 10 Monte Carlo simulations and saving the graph as a png file<br>


## Example
![3](https://github.com/user-attachments/assets/b0ec0804-e9fa-4dfa-996c-e01c163844a4)
![4](https://github.com/user-attachments/assets/ad3d5d6a-49c4-4fc9-bb36-d23b1850f5ac)
