import joblib

class RandomForestModel:

    model, ref_cols = joblib.load("rfc_student_classifier.pkl")

    def make_prediction(self, arr):
        return self.model.predict([arr])[0]

if __name__ == "__main__":

    # TEST
    model = RandomForestModel()
    print(model.ref_cols)
    print(model.make_prediction([1,2,3,4,5,5,3,3]))