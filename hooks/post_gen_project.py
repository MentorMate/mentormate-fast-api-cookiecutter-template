import os
import platform
import shutil
import subprocess


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def empty_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.write('')
        print(f"Content of {file_path} has been emptied.")
    except Exception as e:
        print(f"An error occurred while emptying {file_path}: {str(e)}")


def create_virtual_environment():
    # Create a virtual environment using the current Python version
    subprocess.run(["python", "-m", "venv", "env"])

    # Upgrade pip version
    subprocess.run(
        ["./env/bin/python3", "-m", "pip", "install", "--upgrade", "pip"])


def install_requirements():
    # Determine the requirements file based on the environment parameter
    requirements_file = f'requirements/local.txt'

    # Execute the pip command to install the requirements
    # TODO: set correct windows venv python path
    if platform.system() == 'Windows':
        subprocess.run(["./env/bin/python3", "-m", "pip", "install", "-r",
                        requirements_file], shell=True)
    else:
        subprocess.run(["./env/bin/python3", "-m", "pip", "install", "-r",
                        requirements_file])


def remove_example_api():
    if "{{ cookiecutter.add_example_apps }}" == "False":
        remove(os.path.join(os.getcwd(), 'src', 'users'))
        remove(os.path.join(os.getcwd(), 'src', 'auth'))


# Call the initial setup functions
create_virtual_environment()
install_requirements()
remove_example_api()
