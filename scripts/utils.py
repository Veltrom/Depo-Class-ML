import re
import pandas
import unidecode

def clean_text(row: pandas.Series):
    columns = [
        'Name', 'CashTradeId', 'FundId', 'TradeValue',
        'TradeDetails', 'AccountCode', 'Created', 'CounterPartyCode', 'GrossAmount',
        'Comment', 'Description', 'EntryDate', 'Date',
    ]

    rows = [row[column] for column in columns]
    
    # list of words
    description = ' '.join(rows)
    # convert all characters to lowercase
    description = description.lower()
    # removing accented characters
    description = unidecode.unidecode(description)
    # remove extra whitespaces
    description = re.sub(r'^\s*|\s\s*', ' ', description).strip()

    return description
