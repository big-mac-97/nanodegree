# import libraries
import pandas as pd
from sqlalchemy import create_engine
import sys


def load_data(messages_filepath, categories_filepath):
    """
    Imports and merges messages and categories data from 2 separate .csv filepaths.

    Parameters:
    messages_filepath: path of messages csv file
    categories_filepath: path of categories csv file

    Returns:
    df: dataframe of merged messages and categories files

    """

    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories, on = 'id')
    print("Imported datasets.")

    return df

def clean_data(df):
    """
    Cleans the merged messages/categories dataframe.

    Parameters:
    df: dataframe (generated from load_data())

    Returns:
    df: Cleaned dataframe with column headers corresponding to categories and values of 1 or 0

    """
    #creates a dataframe of the column categories and selects the first row to extract column names
    categories = df['categories'].str.split(pat=";", expand=True)
    row = categories.iloc[0]

    #generate a Series containing the category names, and rename the df column labels
    category_colnames = row.apply(lambda x: x[0:(len(x) - 2)])
    categories.columns = category_colnames

    #extracts last character of each string (the category indicator) and converts to a numeric value
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]

        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])

    #remove now-redundant categories column and append the new cleaned data
    df.drop(columns="categories", inplace=True)
    df = df.join(categories)
    print("Cleaned data.")

    #remove any duplicated messages.
    df.drop_duplicates(subset="message", inplace=True)
    print("Removed duplicate messages from dataset.")

    return df

def save_data(df, database_filename):
    """Loads cleaned df into a SQLite database."""
    engine = create_engine(f'sqlite:///{database_filename}')
    df.to_sql('messages_database', engine, index=False, if_exists='replace')
    


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()