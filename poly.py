import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# games played
x_train = [[3], [5], [7], [10], [12]]

# avg goals per game
y_train = [[2], [5], [8], [11], [12]]

# games played
x_test = [[5], [6], [7], [8]]
# avg goals per game
y_test = [[6], [7], [8], [9]]


# create linear regression object
reg = LinearRegression()

# create line of best fit
reg.fit(x_train, y_train)
x = np.linspace(0, 26, 100)
y = reg.predict(x.reshape(x.shape[0], 1))
plt.plot(x, y)

# create degree  for regression
quad_form = PolynomialFeatures(degree=2)


X_train_quadratic = quad_form.fit_transform(x_train)
X_test_quadratic = quad_form.transform(x_test)

#train and test data
quad_reg = LinearRegression()
quad_reg.fit(X_train_quadratic, y_train)

xx_quadratic = quad_form.transform(x.reshape(x.shape[0], 1))
# predict the data
# plot the points
plt.plot(x, quad_reg.predict(xx_quadratic), c='b', linestyle='-')

# create title for the graph
plt.title('number of games played and goals scored for a football player')

# write x label
plt.xlabel('games played')

# write ylabel
plt.ylabel('number of assists')

# create vertical and horizontal scale
plt.axis([0, 25, 0, 25])

# create grid
plt.grid(True)

plt.scatter(x_train, y_train)
plt.show()
