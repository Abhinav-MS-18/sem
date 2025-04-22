import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, confusion_matrix, accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("cric.csv")
df = df.drop(columns=['Unnamed: 0', 'Player', 'Span'])
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna()
df = df.fillna(df['Runs'].sum())

median = df['Runs'].median()
df['Runs-Category'] = (df['Runs'] > median).astype(int)

x = df[['Ave']]
y = df['Runs-Category']

model = LogisticRegression()
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=40)
model.fit(x_train, y_train)

print(f'intercept={model.intercept_}')
print(f'coefficient={model.coef_}')
y_pred = model.predict_proba(x_test)

print(f'Mean squared error={mean_squared_error(y_test, y_pred)}')
print(f'Mean squared error={mean_absolute_error(y_test, y_pred)}')

acc = accuracy_score(y_test, y_pred)
mat = confusion_matrix(y_test, y_pred)
print(f'classification report={classification_report(y_test, y_pred)}')

print(f'accuracy={acc}')
print(f'confusion matrix={mat}')

# plt.figure(figsize=(7,9))
# plt.scatter(y_pred,y_test)
sns.heatmap(mat,annot=True)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()