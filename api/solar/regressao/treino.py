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



client_data = pd.read_csv('producao.csv')

teste_data = client_data['Production (kWh)']

client_data = client_data.drop('Date', axis=1)
client_data = client_data.drop('Plant ID', axis=1)
client_data = client_data.drop('Production (kWh)', axis=1)
client_data = client_data.drop('Primavera', axis=1)
client_data = client_data.drop('Verão', axis=1)
client_data = client_data.drop('Outono', axis=1)
client_data = client_data.drop('Inverno', axis=1)
client_data = client_data.drop('Plate Price (R$)', axis=1)


X_train, X_test, y_train, y_test = train_test_split(client_data, teste_data, test_size=0.3, random_state=18, shuffle=False)
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