import os
import sys
from datetime import datetime

# Get the current timestamp in the format 'yymmddhm'.
timestamp = datetime.now().strftime("%y%m%d%H%M%S")

# Run Behave with the HTML formatter and specify the output directory.
report_path = os.path.join('reports', f'smoke-test-results-{timestamp}.html')
os.system(f'behave --tags=smoke --format html -o {report_path}')