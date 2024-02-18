from src.InsurancePremiumPrediction.pipelines.prediction_pipeline import CustomData

custdataobj=CustomData(23,"female",34.9,0,"no","northeast")

data=custdataobj.get_data_as_dataframe()
print(data)