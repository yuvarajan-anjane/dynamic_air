from jinja2 import Environment, FileSystemLoader
import yaml
import os

print("Current Working Directory:", os.getcwd())


file_dir = os.path.dirname(os.path.abspath(f"{__file__}/--/"))
env = Environment(loader=FileSystemLoader(file_dir))
template = env.get_template('include/dynamic/dag_template.jinja2')

# template_path = os.path.join(os.path.dirname(__file__), 'templates', 'dag_template.jinja2')
# template = env.get_template(template_path)


for filename in os.listdir(f"{file_dir}/dynamic"):
    print(filename)
    if filename.endswith('.yaml'):
        with open(f"{file_dir}/dynamic/{filename}", "r") as input_file:
            inputs = yaml.safe_load(input_file)
            with open(f"dags/get_price{inputs['dag_id']}.py", "w") as f:
                f.write(template.render(inputs))