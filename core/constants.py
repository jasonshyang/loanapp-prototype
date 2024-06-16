# users constants
ACCOUNT_TYPE = [
    ('BORROWER', 'Borrower'),
    ('LENDER', 'Lender'),
]

RISK_LEVEL = [
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
]

OCCUPATION = [
    ('ST', 'Student'),
    ('EM', 'Employed'),
    ('SE', 'Self Employed'),
    ('UE', 'Unemployed'),
]

ACCOUNT_STATE = [
    ('ACTIVE', 'Active'),
    ('SUSPENDED', 'Suspended'),
    ('CLOSED', 'Closed'),
]

MONEY_REQUEST_STATUS = [
    ('OPEN', 'Open'),
    ('ACCEPTED', 'Accepted'),
    ('FULFILLED', 'Fulfilled'),
    ('CANCELLED', 'Cancelled'),
]

MONEY_REQUEST_TYPE = [
    ('INSTALLMENT', 'Installment'),
    ('MINPAY', 'Minimum Payment'),
    ('INTONLY', 'Interest Only'),
]