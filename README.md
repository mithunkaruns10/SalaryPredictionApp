# SalaryPredictionApp
A web application that predicts the average salary in a particular country based on the educational qualifications and year of experience of an individual.
# Note

###Please unzip survey_results_public.csv.zip in the project for the dataset 

# Steps to follow:

1. First download the directory.

2. Inside the directory path, create new environment by 

  ``` conda create -n ml python=3.9 ```

3. Activate that environment by

  ```conda activate ml```

4. Install all needed modules

  ```pip install streamlit```
    
  ```pip install numpy pandas```

  ```pip install matplotlib scikit-learn```

5. Install kernel for virtual environment

  ```ipython kernel install --user --name=ml```

6. Finally, run this command

  ```streamlit run app.py```
