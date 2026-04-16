# ===================== Practical Printer Library =====================

def practical_1():
    print("""# ===================== Practical 1 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

print("Before:\\n", df)
print("\\nMissing:\\n", df.isnull().sum())

num_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

print("\\nAfter:\\n", df)
print("\\nMissing After:\\n", df.isnull().sum())
""")


def practical_2():
    print("""# ===================== Practical 2 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

print("Before:\\n", df['Department'].value_counts())

df['Department'].fillna(df['Department'].mode()[0], inplace=True)

print("\\nAfter:\\n", df['Department'].value_counts())
""")


def practical_3():
    print("""# ===================== Practical 3 =====================
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("ml_practical_dataset.csv")

le = LabelEncoder()
df['Department'] = df['Department'].astype(str)

df['Department_Encoded'] = le.fit_transform(df['Department'])

print(df[['Department', 'Department_Encoded']])
""")


def practical_4():
    print("""# ===================== Practical 4 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

df = pd.get_dummies(df, columns=['Department', 'Education'])

print(df.head())
""")


def practical_5():
    print("""# ===================== Practical 5 =====================
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("ml_practical_dataset.csv")

num_cols = ['Age', 'Salary', 'Experience', 'PerformanceScore']

scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print(df[num_cols].head())
""")
    
def practical_6():
    print("""# ===================== Practical 6 =====================
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("ml_practical_dataset.csv")

num_cols = ['Age', 'Salary', 'Experience', 'PerformanceScore']

scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print(df[num_cols].mean())
print(df[num_cols].std())
""")


def practical_7():
    print("""# ===================== Practical 7 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

df['New_Feature'] = df['Experience'] * df['PerformanceScore']

print(df.head())
""")


def practical_8():
    print("""# ===================== Practical 8 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

print(df.describe())

print("\\nMedian:\\n", df.median(numeric_only=True))
""")


def practical_9():
    print("""# ===================== Practical 9 =====================
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ml_practical_dataset.csv")

df.hist()
plt.show()
""")


def practical_10():
    print("""# ===================== Practical 10 =====================
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ml_practical_dataset.csv")

df.boxplot()
plt.show()
""")


def practical_11():
    print("""# ===================== Practical 11 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

corr = df.corr(numeric_only=True)
print(corr)
""")


def practical_12():
    print("""# ===================== Practical 12 =====================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ml_practical_dataset.csv")

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
plt.show()
""")


def practical_13():
    print("""# ===================== Practical 13 =====================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("ml_practical_dataset.csv")

sns.pairplot(df)
plt.show()
""")


def practical_14():
    print("""# ===================== Practical 14 =====================
import pandas as pd

df = pd.read_csv("ml_practical_dataset.csv")

print(df.skew(numeric_only=True))
""")


def practical_15():
    print("""# ===================== Practical 15 =====================
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("ml_practical_dataset.csv")

df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

model = LogisticRegression()
model.fit(X, y)
""")


def practical_16():
    print("""# ===================== Practical 16 =====================
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("ml_practical_dataset.csv")

df = df.dropna()

X = df[['Age', 'Salary', 'Experience', 'PerformanceScore']]
y = df['Target_Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
""")


def practical_17():
    print("""# ===================== Practical 17 =====================
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
""")


def practical_18():
    print("""# ===================== Practical 18 =====================
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
""")


def practical_19():
    print("""# ===================== Practical 19 =====================
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
""")


def practical_20():
    print("""# ===================== Practical 20 =====================
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
""")


def practical_21():
    print("""# ===================== Practical 21 =====================
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
""")


def practical_22():
    print("""# ===================== Practical 22 =====================
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
""")


def practical_23():
    print("""# ===================== Practical 23 =====================
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
""")


def practical_24():
    print("""# ===================== Practical 24 =====================
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
""")


def practical_25():
    print("""# ===================== Practical 25 =====================
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
""")
    

def practical_31():
    print("""# ===================== Practical 31 =====================
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
""")


def practical_32():
    print("""# ===================== Practical 32 =====================
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
""")


def practical_33():
    print("""# ===================== Practical 33 =====================
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
""")


def practical_34():
    print("""# ===================== Practical 34 =====================
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
""")


def practical_35():
    print("""# ===================== Practical 35 =====================
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
""")


def practical_36():
    print("""# ===================== Practical 36 =====================
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
""")


def practical_37():
    print("""# ===================== Practical 37 =====================
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
""")


def practical_38():
    print("""# ===================== Practical 38 =====================
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
""")


def practical_39():
    print("""# ===================== Practical 39 =====================
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
""")


def practical_40():
    print("""# ===================== Practical 40 =====================
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
""")
    

def show_all_questions():
    print("""===================== ALL PRACTICAL QUESTIONS =====================

1. Load the given dataset and identify missing values in numerical columns, then replace them using mean imputation and display the dataset before and after preprocessing.

2. Using the given dataset, identify missing values in categorical columns and replace them using mode, then compare frequency distribution before and after.

3. Using the given dataset, apply Label Encoding on a categorical column and display the transformed values.

4. Using the given dataset, apply One-Hot Encoding on categorical features and show the increase in number of columns.

5. Using the given dataset, perform Min-Max scaling on numerical features and verify that all values lie between 0 and 1.

6. Using the given dataset, apply StandardScaler and verify mean is approximately 0 and standard deviation is 1.

7. Using the given dataset, create a new feature using existing columns and display the updated dataset.

8. Using the given dataset, display summary statistics including mean, median, minimum, maximum, and standard deviation.

9. Using the given dataset, plot histograms for numerical features and describe the distribution.

10. Using the given dataset, draw boxplots for selected features and identify outliers.

11. Using the given dataset, compute the correlation matrix and identify highly correlated features.

12. Using the given dataset, plot a heatmap for correlation matrix and interpret relationships.

13. Using the given dataset, generate a pairplot and analyze relationships between variables.

14. Using the given dataset, calculate skewness of features and identify skewed variables.

15. Using the given dataset, implement a Logistic Regression model for binary classification.

16. Using the given dataset, split the data into training and testing sets in 75:25 ratio.

17. Using the given dataset, train the Logistic Regression model and predict class labels.

18. Using the given dataset, calculate accuracy score of the Logistic Regression model.

19. Using the given dataset, generate a confusion matrix and interpret results.

20. Using the given dataset, print classification report including precision, recall, and F1-score.

21. Using the given dataset, train Logistic Regression with and without scaling and compare results.

22. Using the given dataset, implement k-NN classifier with k = 3.

23. Using the given dataset, evaluate accuracy of k-NN model.

24. Using the given dataset, train k-NN model for k values from 1 to 10.

25. Using the given dataset, apply feature scaling and observe its effect on k-NN.

26. Using the given dataset, implement Multiple Linear Regression.

27. Using the given dataset, predict target values using regression model.

28. Using the given dataset, calculate Mean Squared Error (MSE).

29. Using the given dataset, calculate R² score and interpret performance.

30. Using the given dataset, compare linear and polynomial regression results.

31. Using the given dataset, plot regression curve for visualization.

32. Using the given dataset, implement Linear Regression and compute MSE.

33. Using the given dataset, implement Ridge Regression with given alpha value.

34. Using the given dataset, implement Lasso Regression with given alpha value.

35. Using the given dataset, compare MSE of Linear, Ridge, and Lasso models.

36. Using the given dataset, calculate average MSE using cross-validation.

37. Using the given dataset, compare validation and cross-validation results.

38. Using the given dataset, select best model based on minimum error.

39. Using the given dataset, tune alpha parameter using cross-validation.

40. Using the given dataset, plot error versus alpha values.

41. Using the given dataset, compare coefficients of Ridge and Lasso models.

42. Using the given dataset, compare linear and polynomial regression results.

====================================================================
""")
    

def practical_26():
    print("""# Practical 26
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("ml_practical_dataset.csv").dropna()

X = df[['Age','Salary','Experience','PerformanceScore']]
y = df['Target_Regression']

model = LinearRegression()
model.fit(X, y)
""")


def practical_27():
    print("""# Practical 27
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("ml_practical_dataset.csv").dropna()

X = df[['Age','Salary','Experience','PerformanceScore']]
y = df['Target_Regression']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
print(y_pred)
""")


def practical_28():
    print("""# Practical 28
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("ml_practical_dataset.csv").dropna()

X = df[['Age','Salary','Experience','PerformanceScore']]
y = df['Target_Regression']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print(mean_squared_error(y, y_pred))
""")


def practical_29():
    print("""# Practical 29
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("ml_practical_dataset.csv").dropna()

X = df[['Age','Salary','Experience','PerformanceScore']]
y = df['Target_Regression']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print(r2_score(y, y_pred))
""")


def practical_30():
    print("""# Practical 30
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("ml_practical_dataset.csv").dropna()

X = df[['Age']]
y = df['Target_Regression']

poly = PolynomialFeatures(2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

print(mean_squared_error(y, y_pred))
print(r2_score(y, y_pred))
""")