import pandas as pd
from atlassian import Jira

jira = Jira(
    url='https://example.atlassian.net/',
    username='sebastian.viana@example.com',
    password='K2d5tCcXGq3gZQFm')

jql_request = 'project in (SOP, OB) AND issuetype in (Support, Problem) AND "Source[Dropdown]" = Support AND "Technology[Dropdown]" = "Veeam Backup & Replication" AND "Customer Request Type" in ("Operational task request (OB)", "Incident request (SOP)") AND created >= -1w'

df = pd.DataFrame(jql_request)
df.to_csv('Output2.csv')