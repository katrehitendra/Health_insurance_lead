import pickle
import json
import config
import numpy as np

class HealthInsuranceLead():
    def __init__(self, City_Code, Accomodation_Type, Reco_Insurance_Type, Married, Health_Indicator, Holding_Policy_Duration,
                 Holding_Policy_Type, Reco_Policy_Cat, Reco_Policy_Premium, Avg_Age):
        self.City_Code               = City_Code
        self.Accomodation_Type       = Accomodation_Type
        self.Reco_Insurance_Type     = Reco_Insurance_Type 
        self.Married                 = Married
        self.Health_Indicator        = Health_Indicator
        self.Holding_Policy_Duration = Holding_Policy_Duration
        self.Holding_Policy_Type     = Holding_Policy_Type
        self.Reco_Policy_Cat         = Reco_Policy_Cat
        self.Reco_Policy_Premium     = Reco_Policy_Premium
        self.Avg_Age                 = Avg_Age
    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f :
            self.model = pickle.load(f)
        with open(config.JSON_FILE_PATH,"r") as f :
            self.json_data  = json.load(f)
    def get_insurance_lead(self):
        self.load_model()
        test_array    = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.json_data['City_Code'][self.City_Code]
        test_array[1] = self.json_data['Reco_Insurance_Type'][self.Reco_Insurance_Type]
        test_array[3] = self.json_data['Married'][self.Married]
        test_array[4] = self.json_data["Health_Indicator"][self.Health_Indicator]
        test_array[5] = self.Holding_Policy_Duration
        test_array[6] = self.Holding_Policy_Type
        test_array[7] = self.Reco_Policy_Cat
        test_array[8] = self.Reco_Policy_Premium
        test_array[9] = self.Avg_Age
        print("Test Array",test_array)
        array = test_array.reshape(1,10)
        lead_predict  = self.model.predict(array)
        if lead_predict == 0 :
            print("Negative ")
        else :
            print("Positive")
        return lead_predict

            