import os
from datetime import date

# MongoDB Constants
DATABASE_NAME = "vehicle_insurance"
COLLECTION_NAME = "vehicle_insurance_data"
MONGODB_URL_KEY = "MONGODB_URL"

# General Paths
PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

# File Names
FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
MODEL_FILE_NAME = "model.pkl"
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"

# Target
TARGET_COLUMN = "Response"
CURRENT_YEAR = date.today().year

# Wasabi (S3-Compatible) Access
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "ap-southeast-1"  # Singapore (Wasabi region)
WASABI_ENDPOINT_URL = "https://s3.ap-southeast-1.wasabisys.com"

# Data Ingestion
DATA_INGESTION_COLLECTION_NAME: str = "vehicle_insurance_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25

# Data Validation
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

# Data Transformation
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# Model Trainer
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")
MODEL_TRAINER_N_ESTIMATORS = 200
MODEL_TRAINER_MIN_SAMPLES_SPLIT: int = 7
MODEL_TRAINER_MIN_SAMPLES_LEAF: int = 6
MIN_SAMPLES_SPLIT_MAX_DEPTH: int = 10
MIN_SAMPLES_SPLIT_CRITERION: str = 'entropy'
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 101

# Model Evaluation
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"

# FastAPI or Flask App Config
APP_HOST = "0.0.0.0"
APP_PORT = 5000
