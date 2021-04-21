from catboost import CatBoostClassifier

def CatBoost_Prediction():
    boost = CatBoostClassifier(iterations=1000, depth=5, learning_rate=0.1)
    boost.load_model('catboost.pkl')
    pred = boost.predict(X_test)
    return pred