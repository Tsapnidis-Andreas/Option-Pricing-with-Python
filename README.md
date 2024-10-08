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
![Στιγμιότυπο οθόνης 2024-09-11 174654](https://github.com/user-attachments/assets/12b97beb-7b0a-45dd-8081-e4d9ec480766)

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
![Στιγμιότυπο οθόνης 2024-09-11 174717](https://github.com/user-attachments/assets/fb3908c4-72fa-4a95-82e2-3b6b5ef62797)


