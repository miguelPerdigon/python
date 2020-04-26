from utils.bigquery import Bigquery

query = """select filed_name from dataset.table_name"""

bigquery_manager = Bigquery('project_id')
result = bigquery_manager.do_query(query)

for row in result:
    print(row.field_name)
