import pandas as pd
import core

# Establish connection
core.connect()

# Main code
response = core.run_query("SELECT * FROM chatbot")
print(response)
