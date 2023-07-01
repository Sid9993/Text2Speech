@echo on

REM Step 1: Upgrade pip
python -m pip install --upgrade pip

REM Step 2: Create a virtual environment
python -m venv myenv
call myenv\Scripts\activate

REM Step 3: Install virtualenv package (if not already installed)
python -m pip install virtualenv

REM Step 4: Install dependencies from requirements.txt
pip install -r requirements.txt

REM Step 5: Run your Python file
python Text-to-Speech.py

REM Step 6: Deactivate the virtual environment
deactivate
