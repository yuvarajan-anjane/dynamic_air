from airflow.models import DAG, Pool
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'airflow_pool',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# Create two pools - one for each database
pool_names = ['db_a_pool', 'db_b_pool']
for pool_name in pool_names:
    # Check if the pool already exists
    pool = Pool.get_pool(pool_name)
    
    # If the pool doesn't exist, create it
    if not pool:
        pool = Pool()
        pool.pool = pool_name
        pool.slots = 2


def process_data_from_db_a():
    print("Processing data from DB_A")

def process_data_from_db_b():
    print("Processing data from DB_B")

# Tasks that use resources from DB_A
task_db_a_1 = PythonOperator(
    task_id='task_db_a_1',
    python_callable=process_data_from_db_a,
    pool='db_a_pool',
    dag=dag,
)

task_db_a_2 = PythonOperator(
    task_id='task_db_a_2',
    python_callable=process_data_from_db_a,
    pool='db_a_pool',
    dag=dag,
)

# Tasks that use resources from DB_B
task_db_b_1 = PythonOperator(
    task_id='task_db_b_1',
    python_callable=process_data_from_db_b,
    pool='db_b_pool',
    dag=dag,
)

# Tasks that use resources from DB_B
task_db_b_2 = PythonOperator(
    task_id='task_db_b_2',
    python_callable=process_data_from_db_b,
    pool='db_b_pool',
    dag=dag,
)

# Tasks that use resources from DB_B
task_db_b_3 = PythonOperator(
    task_id='task_db_b_3',
    python_callable=process_data_from_db_b,
    pool='db_b_pool',
    dag=dag,
)

# Tasks that use resources from DB_B
task_db_b_4 = PythonOperator(
    task_id='task_db_b_4',
    python_callable=process_data_from_db_b,
    pool='db_b_pool',
    dag=dag,
)

# Define your workflow
task_db_a_1 >> task_db_a_2
task_db_a_1 >> task_db_b_1 >> task_db_b_2 >> task_db_b_3 >> task_db_b_4


# import logging
# import random
# from datetime import datetime, timedelta

# from airflow import AirflowException
# from airflow.decorators import dag, task

# @dag("xcom_guess", start_date=datetime(2023, 2, 27), schedule=timedelta(minutes=5))
# def taskflow():
#     @task
#     def generate_random_number():
#         number = random.randint(1, 10)
#         return number
#     @task
#     def guess_number(number: int):
#         guess = random.randint(1, 10)
#         if guess == number:
#             logging.info(
#                 f"Congratulations, your guess was right!\n;
#                 Number: {number}, guess: {guess}"
#             )
#         else:
#             raise AirflowException(f"Wrong guess! Number: {number}, guess: {guess}")
#     guess_number(generate_random_number())
# dag = taskflow()