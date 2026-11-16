import re
class UserInputError(Exception):
    pass

def validate_text_entries(entries: list):
    # entries is a list of tuples where each tuple is (variable_name, variable_value)
    for entry_name, entry_value in entries:
        if not entry_value:
            raise UserInputError(f"{entry_name} must be at least 1 letter")
        if len(entry_value) > 50:
            raise UserInputError(f"{entry_name} must be under 50 characters long")
        
def validate_year_entry(year):
    if not re.search("^[1-2][0-9]{3}$", year):
        raise UserInputError("Year must be an integer between 1000 and 2999")
