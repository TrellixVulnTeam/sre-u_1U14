# Red Hat SRE-U Self Assessment

An application-based assessment around the topics from the SRE course defined in the syllabus. It can be used as a pre-test and post-test to gauge learning. 

# Setup Guide (MacOS)

* Clone repo in terminal `git clone https...`
* Install pip `python3 -m pip install --user --upgrade pip`
* Verify installation `python3 -m pip --version`
* Install virtual environment (allows us to download python packages) `python3 -m pip install --users virtualenv`
* Create virtual environment on machine ` python3 -m venv env`. This step is optional if `env` is present in directory.
* Start virtualenv `source env/bin/activate`
* Install all packages from requirements.txt `pip install -r requirements.txt`
* Start streamlit application on terminal `streamlit run main.py`