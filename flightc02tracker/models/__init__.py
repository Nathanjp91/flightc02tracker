"""
This file is the common initialization routines for the Models Sub library
"""
import os

import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client[os.environ["ENVIRONMENT"]]
