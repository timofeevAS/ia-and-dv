# Python script which go through a checklist and prints out the items that are not completed.
# Original checklist from TASK.md file:
#  [ ] Python 3.9–3.12; 
#  [ ] Poetry; 
#  [ ] VS Code + расширения; 
#  [ ] `poetry install` без ошибок; 
#  [ ] проверка импортов вернула «OK».


# Step 1. Python 3.9-3.12:
import sys
if sys.version_info > (3, 8) and sys.version_info < (3, 13):
    print(f"Python version is {sys.version_info.major}.{sys.version_info.minor}")
    print("[+] Python 3.9–3.12")
else:
    print("Python version is not in the range 3.9-3.12")
    raise Exception("Checklist step 1: [ ] Python 3.9–3.12 is not completed.")

# Step 2. Poetry:
# To install poetry, run the following command in your terminal:
#   curl -sSL https://install.python-poetry.org | python3 -
#   poetry install


import shutil
print("[+] Poetry is installed.")
poetry_path = shutil.which("poetry")
if poetry_path is None:
    print("Poetry is not installed.")
    print("Try to use:\t\tcurl -sSL https://install.python-poetry.org | python3 -")
    print("Then run:\t\tpoetry install")
    raise Exception("Checklist step 2: [ ] Poetry is not completed.")

# Step 3. VS Code + extensions:
# To install VS Code, visit https://code.visualstudio.com/ and download the installer.
# 
# Follow .vscode/extensions.json file to install the recommended extensions.
# Or use:
#   code --install-extension ms-python.python
#   code --install-extension ms-toolsai.jupyter
# Check it manually.