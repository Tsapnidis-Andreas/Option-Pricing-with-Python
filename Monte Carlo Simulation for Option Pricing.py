import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader
from scipy.stats import norm
import yfinance as yf
import datetime as dt
from datetime import datetime
import openpyxl
import xlsxwriter
from xlsxwriter import Workbook



def get_price_and_volatility(i):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.strptime(end_date, '%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')
    stock_data = yf.download(i, start=start_date, end=end_date)
    stock_data.index=range(0,len(stock_data))
    price=stock_data.loc[len(stock_data['Close'])-1,'Close']
    volatility=stock_data['Close'].std()
    return(round(price,2),round(volatility,1)/100)
def GBM(S,r,var,days):
    drift = r - 0.5 * var  # u=average
    stdev = np.sqrt(var)
    T = 1
    N = days
    dt = T / N
    z = np.random.standard_normal(N)
    # print(z)
    St = np.zeros(N)
    St[0] = Spot
    for j in np.arange(1, N):
        St[j] = St[j - 1] * np.exp((drift - stdev ** 2 / 2) * dt + stdev * np.sqrt(dt) * z[j])

    return(St)

def GBM_pricing(S,K,r_annual,var,days):
    prices=[]
    pr=[]
    x=np.linspace(1,days,days)
    r = (1 + r_annual) ** (days / 365) - 1
    for i in range(1,1000):
        St=GBM(S,r,var,days)
        prices.append(St[-1])
        if St[-1]>K:
            pr.append(St[-1]-K)
        else:
            pr.append(0)

    avg=np.mean(pr)
    c=avg*np.exp(-days/365*r_annual)
    return(c)

def saving(df):
    writer = pd.ExcelWriter(path + 'Call prices.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False, header=True, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    for i, col in enumerate(df.columns):
        width = max(df[col].apply(lambda x: len(str(x))).max(), len(df[col]))
        worksheet.set_column(i, i, width)
    writer.close()





def plotting(Spot,r,vol,days):
    global path
    x = np.linspace(1, days, days)
    for i in range(1, 11):
        y = GBM(Spot, r, vol ** 2, days)
        plt.plot(x, y)
    plt.xlabel('Day')
    plt.ylabel('Stock Price')
    plt.title('Monte Carlo Simulations')
    plt.savefig(path + 'Monte Carlo Simulations.png')


#INITIALIZE
global path
path=""
stock='aapl'
days=65




risk_free_rate,a=get_price_and_volatility('^IRX')
risk_free_rate=risk_free_rate/100
r=(1+risk_free_rate)**(days/365)-1
Spot,vol=get_price_and_volatility(stock)

s=round(Spot/100,1)
start=round(s*100-90)
end=round(s*100+40)
int=round((end-start)/10)
print(start,end)

x=range(start,end+1,10)
df=pd.DataFrame({'strike price':x})
df['call price']=df['strike price'].apply(lambda i:GBM_pricing(Spot,i,risk_free_rate,vol**2,days))
df['call price']=round(df['call price'],2)
print(df)
saving(df)

plotting(Spot,r,vol,days)