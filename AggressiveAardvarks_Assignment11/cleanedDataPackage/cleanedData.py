#cleanedData.py


class CleanedData:
    def save_cleaned_data(self): 
        self.data.to_csv('Data/cleanedData.csv', index=False)
