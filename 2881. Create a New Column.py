import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a new column named 'bonus' that contains the doubled values of the 'salary' column.

    Args:
        employees: The DataFrame containing employee data.

    Returns:
        The modified DataFrame with the new 'bonus' column.
    """

    # Create a new column 'bonus' and assign the doubled value of 'salary' to it
    employees['bonus'] = employees['salary'] * 2

    return employees

# Example usage
employees = pd.DataFrame({'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
                          'salary': [4548, 28150, 1103, 6593, 74576, 24433]})

employees_with_bonus = createBonusColumn(employees.copy())  # create a copy to avoid modifying the original DataFrame

print(employees_with_bonus)
