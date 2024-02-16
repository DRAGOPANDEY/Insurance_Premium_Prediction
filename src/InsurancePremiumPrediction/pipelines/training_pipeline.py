from src.InsurancePremiumPrediction.components.data_ingestion import DataIngestion
import os
import sys
from src.InsurancePremiumPrediction.logger import logging
from src.InsurancePremiumPrediction.exception import customexception
import pandas as pd


obj=DataIngestion()


obj.initiate_data_ingestion()
