import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import datetime
import joblib

date = datetime.datetime.today().date()
year = datetime.datetime.today().year
regressao = LinearRegression()

df = pd.read_csv('producao.csv')
#df.head()

x = df.drop('Production (kWh)', axis=1)
x = x.drop('Date', axis=1)
x = x.drop('Plate Price (R$)', axis=1)
y = df['Production (kWh)']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=18, shuffle=False)
regressao.fit(X_train,y_train)

# Serializa modelo
joblib.dump(regressao, 'model.pkl')

predicao = regressao.predict(X_train)

plt.scatter(predicao,y_train)
plt.xlabel('Producao real')
plt.ylabel('Producao estimada')
plt.title('Producao real vs Producao estimada')

print('r2:', metrics.r2_score(y_train, predicao))
print('MAE:', metrics.mean_absolute_error(y_train, predicao))
print('MSE:', metrics.mean_squared_error(y_train, predicao))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_train, predicao)))