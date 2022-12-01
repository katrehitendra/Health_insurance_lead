from flask import Flask, render_template,jsonify,request
import config
from Project_data.utils import HealthInsuranceLead

app = Flask(__name__)
@app.route("/")
def Morning_class():
    # return "Success"
    return render_template("index.html")


@app.route("/predict_lead")
def get_ins_lead_pred():
    data = request.form
    City_Code             = data["City_Code"]
    Accomodation_Type     = data["Accomodation_Type"]
    Reco_Insurance_Type   = data["Reco_Insurance_Type"]
    Married               = data["Married"]
    Health_Indicator      = data["Health_Indicator"]
    Holding_Policy_Duration = int(data["Holding_Policy_Duration"])
    Holding_Policy_Type   = int(data["Holding_Policy_Type"])
    Reco_Policy_Cat       = int(data["Reco_Policy_Cat"])
    Reco_Policy_Premium   = int(data["Reco_Policy_Premium"])
    Avg_Age               = int(data["Avg_Age"])
    lead_pred = HealthInsuranceLead(City_Code,Accomodation_Type,Reco_Insurance_Type,Married,Health_Indicator,Holding_Policy_Duration,
                Holding_Policy_Type,Reco_Policy_Cat,Reco_Policy_Premium,Avg_Age)
    lead = lead_pred.get_insurance_lead()
    return jsonify({"Result":f"Predicted lead {lead}"})
        



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)
