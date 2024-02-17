import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:

   # Filter the DataFrame to only include the student with the desired student_id
   filtered_students = students[students["student_id"] == 101]

   # Select the desired columns (name and age)
   selected_data = filtered_students[["name", "age"]]

   return selected_data

# Example usage
students = pd.DataFrame({'student_id': [101, 53, 128, 3],
                        'name': ['Ulysses', 'William', 'Henry', 'Henry'],
                        'age': [13, 10, 6, 11]})

selected_data = selectData(students)

print(selected_data)
