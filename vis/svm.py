import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score , classification_report , confusion_matrix

df = pd.read_csv("diabetes.csv")

x = df.drop(columns = ["Outcome"])
y = df["Outcome"]

scaler = StandardScaler()
xScaled = scaler.fit_transform(x)

xTrain , xTest , yTrain , yTest = train_test_split(xScaled , y , test_size = 0.2 , random_state= 42)

model = SVC(kernel = "rbf" , C =1.0 , gamma = "scale")
model.fit(xTrain , yTrain)

yPred = model.predict(xTest)

accuracy = accuracy_score(yTest , yPred)
classR = classification_report(yTest , yPred)
cm = confusion_matrix(yTest , yPred)

print("Accuracy is: " , accuracy)
print("\n Classification report \n :" , classR)

plt.figure(figsize = (6 , 4))
sns.heatmap(cm , cmap = "coolwarm" , fmt = ".3f" , annot=True ,  xticklabels=["No Diabetes", "Diabetes"], yticklabels=["NoDiabetes", "Diabetes"])
plt.title("Confusion Matrix - SVM on Diabetes Dataset")
plt.show()