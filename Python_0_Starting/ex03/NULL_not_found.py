def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    
    if obj_type == type(None) and object == None:
        print(f"Nothing: {object} {obj_type}")
    elif obj_type == type(float("NaN")):
        print(f"Cheese: {object} {obj_type}")
    elif obj_type == type(0) and object == 0:
        print(f"Zero: {object} {obj_type}")
    elif obj_type == type('') and object == '':
        print(f"Empty: {object} {obj_type}")
    elif obj_type == type(False):
        print(f"Fake: {object} {obj_type}")
    else :
        print("Type not Found")
        return 1
    return 0