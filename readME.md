# Breast Cancer Detection App

The breast cancer detection app is a machine learning application that utilizes Scikit-learn to train a predictive model. The model is trained on a dataset of tabular data containing various features associated with breast cancer. The features are used to train the model to predict whether a given case is benign or malignant .The machine  application is designed to be user-friendly and accessible to healthcare professionals, allowing them to quickly and accurately diagnose breast cancer using this powerful predictive tool. It has a performance of  97% accuracy on a hold-out test set.


## Data Collection 
The UCI Machine Learning Breast Cancer dataset is a widely used benchmark dataset for binary classification tasks. It contains information about breast cancer tumors, including attributes such as size, shape, and texture. There are a total of 569 instances in the dataset, with 212 malignant and 357 benign cases

[DOWNLOAD ON KAGGLE](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)

## Features

* radius_mean: the mean distance from the center to points on the perimeter of the tumor
* perimeter_mean: the perimeter (total length of the boundary) of the tumor
* area_mean: the area enclosed by the perimeter of the tumor
* concavity_mean: a measure of the severity of concave portions of the contour of the tumor
* concave points_mean: the number of concave portions of the contour of the tumor
* radius_worst: the largest distance from the center to points on the perimeter of the tumor
* perimeter_worst: the largest perimeter (total length of the boundary) of the tumor
* area_worst: the largest area enclosed by the perimeter of the tumor
* concavity_worst: the largest measure of the severity of concave portions of the contour of the tumor
* concave points_worst: the largest number of concave portions of the contour of the tumor.

## Training / Testing
The model was trained on 80% of the dataset, and was evaluated on the remaining 20% of the data.

![classification report](./images/report.png)


