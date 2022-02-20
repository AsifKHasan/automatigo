'''
    get_part_of_text is for getting an initial portion of a (supposedly) long text for search in a drop down
    it first tries to take out the leading portion upto a ','
    if there is no ',' in the text, it tries to take out the leading portion upto a SPACE
    if the text does not even have a SPACE, the full text is returned
'''
def get_part_of_text(text):
    s = text.split(',')
    if len(s) == 0:
        s = text.split(' ')
        if len(s) == 0:
            return text
        else:
            return s[0]
    else:
        return s[0]

def convert_to_degree(minutes):
    mnt = int(minutes)
    mnt = mnt * 6
    if mnt == 0:
        mnt = 360
    return mnt

def is_method(obj, name):
    return callable(getattr(obj, name, None))

def method_by_name(obj, name):
    return getattr(obj, name)