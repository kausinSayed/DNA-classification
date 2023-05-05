import sqlite3
def add():
    con = sqlite3.connect('chimp_data.txt','human_data.txt')
    cur = con.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS data1_(id INTEGER PRIMARY KEY AUTOINCREMENT ,bid TEXT,Bti TEXT)")
    con.commit()
    con.close()
def accuracy():
    from sklearn.model_selection import train_test_split
    X_train_human, X_test_human, y_train_human, y_test_human = train_test_split(X_human,y_human,test_size =                                                                         0.25,random_state=42)
    from sklearn.tree import DecisionTreeClassifier #importing the decisiontreeclassifier algorithm from sklearn
    dtree_human = DecisionTreeClassifier() 
    dtree_human.fit(X_train_human,y_train_human)
    dtree_human_pred = dtree_human.predict(X_test_human) 
    print("Accuracy for human data using  DecisionTree Classifier : ",accuracy_score(dtree_human_pred,y_test_human)) 