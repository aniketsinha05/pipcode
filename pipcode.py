# ===================== Practical 1 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

print("Before:\n", df)
print("\nMissing:\n", df.isnull().sum())

num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

print("\nAfter:\n", df)
print("\nMissing After:\n", df.isnull().sum())


# ===================== Practical 2 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

print("Before:\n", df['Department'].value_counts())

df['Department'].fillna(df['Department'].mode()[0], inplace=True)

print("\nAfter:\n", df['Department'].value_counts())


# ===================== Practical 3 =====================
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("ml_practical_dataset.csv")

le = LabelEncoder()
df['Department'] = df['Department'].astype(str)

df['Department_Encoded'] = le.fit_transform(df['Department'])

print(df[['Department', 'Department_Encoded']])


# ===================== Practical 4 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

df = pd.get_dummies(df, columns=['Department', 'Education'])

print(df.head())


# ===================== Practical 5 =====================
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("ml_practical_dataset.csv")

num_cols = ['Age', 'Salary', 'Experience', 'PerformanceScore']

scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print(df[num_cols].head())


# ===================== Practical 6 =====================
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("ml_practical_dataset.csv")

num_cols = ['Age', 'Salary', 'Experience', 'PerformanceScore']

scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print(df[num_cols].mean())
print(df[num_cols].std())

# ===================== Practical 7 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

df['New_Feature'] = df['Experience'] * df['PerformanceScore']

print(df.head())


# ===================== Practical 8 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

print(df.describe())

print("\nMedian:\n", df.median(numeric_only=True))


# ===================== Practical 9 =====================
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ml_practical_dataset.csv")

df.hist()
plt.show()


# ===================== Practical 10 =====================
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ml_practical_dataset.csv")

df.boxplot()
plt.show()


# ===================== Practical 11 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

corr = df.corr(numeric_only=True)
print(corr)


# ===================== Practical 12 =====================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ml_practical_dataset.csv")

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
plt.show()


# ===================== Practical 13 =====================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ml_practical_dataset.csv")

sns.pairplot(df)
plt.show()


# ===================== Practical 14 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

print(df.skew(numeric_only=True))


# ===================== Practical 15 =====================
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("ml_practical_dataset.csv")

df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

model = LogisticRegression()
model.fit(X, y)


# ===================== Practical 16 =====================
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("ml_practical_dataset.csv")

df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)


# ===================== Practical 17 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("ml_practical_dataset.csv")

df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred)


# ===================== Practical 18 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("ml_practical_dataset.csv")

df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))


# ===================== Practical 19 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

df = pd.read_csv("ml_practical_dataset.csv")

df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))


# ===================== Practical 20 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv("ml_practical_dataset.csv")

df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

# ===================== Practical 21 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

# Without scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Without Scaling Accuracy:", accuracy_score(y_test, y_pred))

# With scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("With Scaling Accuracy:", accuracy_score(y_test, y_pred))


# ===================== Practical 22 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print(y_pred)


# ===================== Practical 23 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))


# ===================== Practical 24 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

for k in range(1, 11):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("k =", k, "Accuracy =", accuracy_score(y_test, pred))


# ===================== Practical 25 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

# Without scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Without Scaling:", accuracy_score(y_test, pred))

# With scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("With Scaling:", accuracy_score(y_test, pred))


# ===================== Practical 26 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)


# ===================== Practical 27 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

# ===================== Practical 28 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))


# ===================== Practical 29 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))


# ===================== Practical 30 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age']]   # single feature for simplicity
y = df['Target_Regression']

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))


# ===================== Practical 31 =====================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age']]
y = df['Target_Regression']

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

X_sorted = np.sort(X.values, axis=0)
y_poly = model.predict(poly.transform(X_sorted))

plt.scatter(X, y)
plt.plot(X_sorted, y_poly)
plt.show()


# ===================== Practical 32 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))


# ===================== Practical 33 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Ridge(alpha=0.1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Ridge MSE:", mean_squared_error(y_test, y_pred))


# ===================== Practical 34 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Lasso(alpha=0.1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Lasso MSE:", mean_squared_error(y_test, y_pred))


# ===================== Practical 35 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = LinearRegression()
ridge = Ridge(alpha=0.1)
lasso = Lasso(alpha=0.1)

lr.fit(X_train, y_train)
ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)

pred_lr = lr.predict(X_test)
pred_ridge = ridge.predict(X_test)
pred_lasso = lasso.predict(X_test)

print("Linear MSE:", mean_squared_error(y_test, pred_lr))
print("Ridge MSE:", mean_squared_error(y_test, pred_ridge))
print("Lasso MSE:", mean_squared_error(y_test, pred_lasso))


# ===================== Practical 36 =====================
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

model = LinearRegression()

scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')

print("Average MSE:", -scores.mean())


# ===================== Practical 37 =====================
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

# Validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Validation MSE:", mean_squared_error(y_test, pred))

# Cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
print("Cross-Validation MSE:", -scores.mean())


# ===================== Practical 38 =====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

models = {
    "Linear": LinearRegression(),
    "Ridge": Ridge(alpha=0.1),
    "Lasso": Lasso(alpha=0.1)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print(name, "MSE:", mean_squared_error(y_test, pred))


# ===================== Practical 39 =====================
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

model = Ridge()

params = {'alpha': [0.001, 0.01, 0.1, 1, 10]}

grid = GridSearchCV(model, params, cv=5, scoring='neg_mean_squared_error')
grid.fit(X, y)

print("Best Alpha:", grid.best_params_)


# ===================== Practical 40 =====================
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

df = pd.read_csv("ml_practical_dataset.csv")
df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Regression']

alphas = [0.001, 0.01, 0.1, 1, 10]
errors = []

for a in alphas:
    model = Ridge(alpha=a)
    scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    errors.append(-scores.mean())

plt.plot(alphas, errors)
plt.xscale('log')
plt.xlabel("Alpha")
plt.ylabel("MSE")
plt.show()

