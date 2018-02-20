from datetime import datetime, timedelta
import time
from collections import namedtuple
import pandas as pd
import requests
import matplotlib.pyplot as plt

API_KEY = "ef504af496da69c7"
BASE_URL = "http://api.wunderground.com/api/API_KEY/history_20180221/q/NE/Lincoln.json"

