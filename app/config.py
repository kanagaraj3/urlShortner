import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://default:Z4Qo2WtBFwDN@ep-nameless-water-a4whe7o1.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
