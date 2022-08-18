# SalaryPredictionApp


# Note
*** Please unzip survey_results_public.csv.zip in the project for the dataset 

# Steps to follow:
_1) First download the directory.

2) Inside the directory path, create new environment by 

conda create -n ml python=3.9

Activate that environment by
conda activate ml

Install all needed modules
pip install streamlit
pip install numpy pandas
pip install matplotlib scikit-learn

Install kernel for virtual environment
ipython kernel install --user --name=ml

At last run this command
streamlit run app.py
