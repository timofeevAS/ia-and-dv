# Python script which go through a checklist and prints out the items that are not completed.
# Original checklist from TASK.md file:
#  [ x ] Python 3.9–3.13; 
#  [ ] Poetry; 
#  [ ] VS Code + расширения; 
#  [ ] `poetry install` без ошибок; 
#  [ ] проверка импортов вернула «OK».


# Step 1. Python 3.9-3.13:
import sys
if sys.version_info > (3, 8) and sys.version_info < (3, 14):
    print(f"Python version is {sys.version_info.major}.{sys.version_info.minor}")
    print("[+] Python 3.9–3.13")
else:
    print("Python version is not in the range 3.9-3.13")
    raise Exception("Checklist step 1: [ ] Python 3.9–3.13 is not completed.")

    