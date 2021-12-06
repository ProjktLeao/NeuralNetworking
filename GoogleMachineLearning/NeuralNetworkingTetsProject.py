from sklearn import tree

features = [[140,1],[130,1],[150,0],[170,0]] #[[weight in grams,Bumpy(0) or Smooth(1)]]
labels = [ 0, 0, 1, 1] #[Apples(0) or Oranges(1)]

clf = tree.DecisionTreeClassifier() #defines what classifier method is used
clf  = clf.fit(features, labels)#Trains/ finds patern usiing the features and their respective outputs
print (clf.predict([[150, 0]]))#prints what the algorithm predicts (one of the labels) 