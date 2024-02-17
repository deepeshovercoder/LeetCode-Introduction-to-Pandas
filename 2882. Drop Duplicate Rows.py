import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
   

   # Use the .drop_duplicates() method to keep only the first occurrence of each email
   unique_customers = customers.drop_duplicates(subset=['email'], keep='first')

   return unique_customers

# Example usage
customers = pd.DataFrame({'customer_id': [1, 2, 3, 4, 5, 6],
                         'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
                         'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']})

unique_customers = dropDuplicateEmails(customers)

print(unique_customers)
