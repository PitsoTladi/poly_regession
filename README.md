Polynomial Regression Model

Overview
This repository contains code for implementing polynomial regression, a special case of multiple linear regression used to capture non-linear relationships between variables. In this project, we demonstrate the application of polynomial regression to predict pizza prices based on their diameters.

Requirements
Python 3
NumPy
Matplotlib
scikit-learn
Installation

Description
Polynomial regression extends the concept of linear regression by incorporating polynomial terms to model non-linear relationships between variables. In this project, we model the relationship between pizza prices and diameters using polynomial regression.

Implementation Details
The code uses scikit-learn to train both a simple linear regression model and a polynomial regression model.
The training and testing data consist of pizza diameters and their corresponding prices.
The degree of the polynomial regression model is set to 2.
The code plots the regression lines for both the simple linear regression model and the quadratic regression model.
Results
Upon executing the code, you will observe two regression lines plotted:

The solid line represents the simple linear regression model.
The dashed line represents the quadratic regression model.
The quadratic regression model demonstrates a better fit to the training data compared to the simple linear regression model, highlighting the effectiveness of polynomial regression in capturing non-linear relationships.
