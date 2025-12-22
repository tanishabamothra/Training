cache=[]
def get_data(key):
    for k, v in cache:
        if k == key:
            return v
    return None
