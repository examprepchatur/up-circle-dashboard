
import pandas as pd

FILE_PATH = "uploads/latest_master_file.xlsx"

class DataLoader:

    def load_sheet(self, sheet_name):
        return pd.read_excel(FILE_PATH, sheet_name=sheet_name)

    def total_score(self):
        return self.load_sheet("Total Score")

    def mail_growth(self):
        return self.load_sheet("% growth in mail traffic")

    def parcel_growth(self):
        return self.load_sheet("% growth in Parcel traffic")

    def digital_cod_daily(self):
        return self.load_sheet("Digital COD Transactions  (Daily position)")

    def digital_cod_monthly(self):
        return self.load_sheet("% Digital Transactions for CoD Parcels (for which payment through Digital Mode) (6)")
