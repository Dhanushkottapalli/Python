# Logical_Operator
# if applicant has high income AND good credit Eligible for loan
has_high_income=True
has_high_credit=True
if has_high_income and has_high_credit: #There are two condition, If we want to print out put when the two conditions are true then we will use "and" operator.
    print("Eligible for loan")

has_high_income=False
has_high_credit=True
if has_high_income or has_high_credit: #There are two condition, If we want to print out put when the one conditions are true then we will use "or" operator.
    print("Eligible for loan")

# if applicant has good credit And doesn't have a criminal record
has_high_income=True
has_criminal_record=True
if has_high_income and not has_criminal_record: #And not operator is wsed to revers the boolian value.
    print("Eligible for loan")
