def verfuDataUser (name, email, password):
    if len(name) < 5:
        return False
    elif len(password) < 7:
        return False
    elif not ('@' in email):
        return False
    elif len(email) < 5:
        return False
    else:
        return True