import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:

    first_three_rows = employees.head(3)

    # Return the selected rows as a new DataFrame
    return first_three_rows

# Example usage
employees = pd.DataFrame({'employee_id': [3, 90, 9, 60, 49, 43],
                          'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
                          'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
                          'salary': [48675, 11096, 33805, 37678, 23793, 40454]})

selected_rows = selectFirstRows(employees)

print(selected_rows)

