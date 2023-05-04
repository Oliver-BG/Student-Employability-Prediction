import joblib

model, ref_cols = joblib.load("rfc_student_classifier.pkl")

if __name__ == "__main__":
    print(ref_cols)
    print(model.predict([[1,2,3,4,5,5,3,3]]))