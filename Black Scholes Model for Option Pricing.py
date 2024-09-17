import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader
from scipy.stats import norm
import yfinance as yf
import datetime as dt
from datetime import datetime



def get_price_and_volatility(i):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.strptime(end_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')
    stock_data = yf.download(i, start=start_date, end=end_date)
    stock_data.index=range(0,len(stock_data))
    price=stock_data.loc[len(stock_data['Close'])-1,'Close']
    volatility=stock_data['Close'].std()
    return(round(price,2),round(volatility,1)/100)

def d1(S,K,r,stdev,T):
    return(np.log(S/K)+(r+stdev**2/2)*T)/(stdev*np.sqrt(T))

def d2(S,K,r,stdev,T):
    return(np.log(S/K)+(r-stdev**2/2)*T)/(stdev*np.sqrt(T))


def BSM(Spot,K,r,stdev,T,a):
    if a=='call':
        return (Spot*norm.cdf(d1(Spot,K,r,stdev,T)))-(K*np.exp(-r*T)*norm.cdf(d2(Spot,K,r,stdev,T)))
    else:
        return(np.exp(-r*T)*K*norm.cdf(-d2(Spot,K,r,stdev,T))-Spot*norm.cdf(-d1(Spot,K,r,stdev,T)))


def saving(df):
    global path
    writer = pd.ExcelWriter(path + 'Option prices.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False, header=True, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    for i, col in enumerate(df.columns):
        width = max(df[col].apply(lambda x: len(str(x))).max(), len(df[col]))
        worksheet.set_column(i, i, width)
    writer.close()

def plotting(df,x):
    plt.plot(x, df['call'], 'r')
    plt.plot(x, df['put'], 'g')
    plt.ylabel('Option price')
    plt.xlabel('Strike price')
    plt.savefig(path + 'Option price in realtion to strike price.png')


#INITIALIZE
stock='aapl'
global path
path=""
days=65



risk_free_rate,a=get_price_and_volatility('^IRX')
risk_free_rate=risk_free_rate/100
r=(1+risk_free_rate)**(days/365)-1
Spot,vol=get_price_and_volatility(stock)

s=round(Spot/100,1)
start=round(s*100-90)
end=round(s*100+40)
int=round((end-start)/10)

x=range(start,end+1,10)
df=pd.DataFrame({'strike price':x})
df['call']=df['strike price'].apply(lambda i:BSM(Spot,i,r,vol,days/360,'call'))
df['put']=df['strike price'].apply(lambda i:BSM(Spot,i,r,vol,days/360,'put'))

df=round(df,2)
print(df)

plotting(df,x)
saving(df)
