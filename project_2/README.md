# Data Science Nanodegree Project 2 - Disaster Response Machine Learning Pipeline

### Project Description and Motivation
As part of the Data Science Nanodegree I learned about Extract, Transform, Load and Machine Learning Pipelines. I developed a solid understanding of the processes required and applied them to templates provided by Udacity to build a web app and machine learning pipeline that analyses disaster message data to sort messages into 36 categories. This process has significant real-world applications to help with allocation of resources during disaster relief efforts. The web app also contains functionality to categorise a new message using the ML model, and displays visualisations of the dataset provided.

### Using the model:
1. Download the files from this repository.

2. Install the required Python packages:
    - pandas 1.2.4
    - sqlalchemy 1.4.7
    - numpy 1.20.1
    - sqlite 3.35.4
    - matplotlib 3.3.4
    - nltk 3.6.1
    - scikit-learn 0.24.1
    - plotly 5.4.0
    - flask 1.1.2

3. Execture the following commands in the project root directory:

    - ETL Pipeline (imports data from .csv files, cleans it, and stores it in an SQL database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/disaster_message_database.db`
    - ML Pipeline (trains ML classifier and outputs model as a pickle file)
        `python models/train_classifier.py data/disaster_message_database.db models/classifier.pkl`

4. To run the web app, navigate to the app directory and execute `python run.py`

5. The web app can be viewed locally at http://localhost:3000/ when it is running.

### File Descriptions
app    

| - template    
| |- master.html `web app main page`
| |- go.html `web app custom message classification page`  
|- run.py `web app Flask file`   


data    

|- disaster_categories.csv `categories data to process`    
|- disaster_messages.csv `message data to process`    
|- process_data.py `ETL pipeline`    
|- disaster_message_database.db `cleaned data database - custom name can be passed as argument to process_data.py`


models   

|- train_classifier.py `ML pipeline`     
|- classifier.pkl `pickled model`     


README.md    

ETL Pipeline Preparation.ipynb `Jupyter notebook of ETL pipeline pre-work provided by Udacity`
ML Pipeline Preparation.ipynb `Jupyter notebook of ML pipeline pre-work provided by Udacity`



#### Acknowledgements
Massive thanks to Udacity for a great project, very informative lessons, and providing robust templates to help build this ML Pipeline!