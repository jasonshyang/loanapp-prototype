from random import randint

def get_risk_score():
    '''
    mock function to get risk score
    '''
    return randint(0,1000)

def get_risk_level(risk_score):
    if risk_score < 0:
        raise ValueError('INVALID RISK SCORE - Risk score must be a positive integer')
    elif risk_score > 600:
        return 'low'
    elif risk_score > 300:
        return 'medium'
    else:
        return 'high'