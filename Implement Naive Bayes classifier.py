import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

breastcancer = datasets.load_breast_cancer()
print("\nFeatures of breastcancer dataset : ", breastcancer.feature_names)
print("\nLabels of breastcancer dataset : ", breastcancer.target_names)
print("\nShape of breastcancer dataset : ", breastcancer.data.shape)
print("\n")
R = breastcancer.data
T = breastcancer.target

Rtrain, Rtest, Ttrain, Ttest = train_test_split(R, T, test_size = 0.2, random_state = 0)
gauss = GaussianNB()
gauss.fit(Rtrain,Ttrain)
pred = gauss.predict(Rtest)

gcr = classification_report(Ttest,pred)
print("\nClassification Report gaussian : \n", gcr)

gcm = confusion_matrix(Ttest, pred)
print("\nConfusion matrix gaussian : \n", gcm)

accuracy = accuracy_score(Ttest, pred)
print("\nAccuracy : ", accuracy * 100)