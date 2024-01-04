import pandas as pd
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Load CSV data
df = pd.read_csv("include/dynamic_csv/dag_data.csv")

def execute_dynamic_dag(input_value, **kwargs):
    print(f"Executing DAG with input: {input_value}")
    dag_id = kwargs['dag'].dag_id
    result = input_value['input_1'] + input_value['input_2']
    print(f"DAG {dag_id} - Result: {result}")
    # You can perform additional processing or use the result as needed

# Update the result in the CSV file
    df.loc[df['dag_id'] == int(dag_id.split('_')[-1]), 'result'] = result
    df.to_csv("include/dynamic_csv/dag_data.csv", index=False)


    # You can define your dynamic DAG logic here

# Iterate over rows in the CSV and generate a DAG for each row
for index, row in df.iterrows():
    dag_id = f"dynamic_CSV_{row['dag_id']}"
    schedule_interval = timedelta(days=1) if row['schedule_interval'] == 'daily' else timedelta(weeks=1)

    default_args = {
        'owner': 'airflow',
        'start_date': datetime(2023, 1, 1),
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    }

    dag = DAG(
        dag_id,
        schedule_interval=schedule_interval,
        default_args=default_args,
        catchup=False,
    )

    with dag:
        task = PythonOperator(
            task_id=f"task_{row['dag_id']}",
            python_callable=execute_dynamic_dag,
            op_kwargs={'input_value': row},
            provide_context=True,
        )

# Note: You can add more operators/tasks, dependencies, etc., based on your requirements

# Now, you need to save this script and run it to dynamically generate your DAGs.
