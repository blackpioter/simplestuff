def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError

    if len(sports) > 5:
        raise ValueError

    dct = {'name': name, 'age': age}

    if len(sports):
        dct['sports'] = sorted(sports)

    if len(awards):
        dct['awards'] = awards
    return dct
