# from pendulum import datetime
# from airflow import DAG
# from airflow.models import Variable
# from airflow.operators.python import PythonOperator


# def create_dag(dag_id, schedule, dag_number, default_args):
#     def hello_world_py():
#         print("Hello World")
#         print("This is DAG: {}".format(str(dag_number)))

#     generated_dag = DAG(dag_id, schedule=schedule, default_args=default_args)

#     with generated_dag:
#         PythonOperator(task_id="hello_world", python_callable=hello_world_py)

#     return generated_dag


# number_of_dags = Variable.get("dag_number", default_var=3)
# number_of_dags = int(number_of_dags)

# for n in range(1, number_of_dags):
#     dag_id = "hello_world_{}".format(str(n))

#     default_args = {"owner": "airflow", "start_date": datetime(2023, 7, 1)}

#     schedule = "@daily"
#     dag_number = n
#     globals()[dag_id] = create_dag(dag_id, schedule, dag_number, default_args)