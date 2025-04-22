import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import plotly.express as px

df = pd.read_csv("cric.csv")
df = df.drop(columns=['Unnamed: 0', 'Player', 'Span'])
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna()


model = LinearRegression()

x = df[['Ave']]
y = df['Runs']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=50)


model.fit(x_train, y_train)

print(f'Intercept={model.intercept_}')
print(f'Coefficient={model.coef_}')

y_pred = model.predict(x_test)
print(f'Mean squared error={mean_squared_error(y_test, y_pred)}')
print(f'Mean squared error={mean_absolute_error(y_test, y_pred)}')
plt.xlabel("Actual Runs")
plt.ylabel("Predicted Runs")
plt.scatter(y_test, y_pred)
plt.show()
