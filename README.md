# diabetes-mellitus-classification
Building Classification model to predict Diabetes condition

Diabetes is a medical condition that is caused due to insufficient production and secretion of insulin from the pancreas in case of Type-1 diabetes and defective response of insulin Type-2 diabetes. Diabetes is one of the most prevalent medical conditions in people today. Hospital readmission for diabetic patients is a major concern in the United States. Over $250 million dollars was spent on treatment of readmitted diabetic inpatients in 2011 alone.

# Objective
Hospital readmission rates for certain conditions are now considered an indicator of hospital quality, and also affect the cost of care adversely. Hospital readmissions of diabetic patients are expensive as hospitals face penalties if their readmission rate is higher than expected and reflects the inadequacies in health care system. For these reasons, it is important for the hospitals to improve focus on reducing readmission rates.

# Data Origin
The data used in this project was downloaded from Kaggle. The DataSet contains certain diagnostic measurements with 8 attributes, 768 samples. This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases.

# Handling missing values
* ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI'] columns are found to have 0 values for some samples and they are considered as missing values.
* These missing values are replaced with medians of respective columns grouped by the Outcome.

![](/images/missing_data.PNG)

Correlation map of cleaned data looks as below 

![](/images/correlation.PNG)

# Handling Data Imbalance
* There exists imbalance in data with target column having 500-0's and 268-1's

![](/images/count_plot.PNG)

* Since dataset is small, we choose to perform oversampling on the imbalance data.
* Data is split into train and test data prior handling data imbalance, so test data is not leaked and real.
* ADASYN algorithm is applied on train data to generate synthetic samples balancing the data.

![](/images/adasyn.PNG)

# Data preprocessing
* StandardScaler is applied to scale the data

# Model Building
Various models of Logistic Regression, KNN, Naive Bayes, support vector, Decision tree and Random Forest classification algorithms are builded.
On comparing the performances of all the models, its concluded that Random Forest Classification performs well with the problem.

![](/images/comparison.PNG)

# Results
* ##### F1-Score: 88.49557522123894 %
* ##### Recall: 92.5925925925926 %
* ##### Precision: 84.7457627118644 %

![](/images/confusion_matrix.PNG)

![](/images/feature_imp.PNG)

# API 

* The model is dumped as pickle file.
* Created an api- /y_predict using Flask, to take the input values of diagnostic measurements and return json data with prediction.

# Limitations
* Gathering more data can yield more robust predictions. 
