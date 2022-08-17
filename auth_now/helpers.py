from .models import *



def add_user_id_n_save(request, data, unique=None):
    try:
        user = UserIdentity.objects.filter(username=request.user)
        if len(user) > 0:
            user_id = user[0]
            if (unique is True and data.Meta.model.objects.filter(user_fk=user_id, **data.cleaned_data).exists()): #buggy test with economic activity bool
                return False
            else:
                temp = data.save(commit=False)
                temp.user_fk = user_id
                temp.save()
                return True
    except Exception as e:
        logging.info(f"ERROR: Profile must be created first {e}")
        return False


def get_user(request,):
    user = None
    user_set = UserIdentity.objects.filter(username=request.user)
    if len(user_set) > 0:
        user = user_set[0]
    return user


def check_mutable(queryset, **data):
    _mutable = queryset._mutable
    queryset._mutable = True
    for key, value in data.items():
        queryset[key] = value
    queryset._mutable = _mutable
    return queryset
    
    
def remove_key_from_queryset(query_dict, key):
    _mutable = query_dict._mutable
    query_dict._mutable = True
    query_dict.pop(key)
    query_dict._mutable = _mutable
    return query_dict


def querydict_to_dict(query_dict):
    val = dict((key,value) for key, value in query_dict.items())
    return val


def list_sub_list(lst, n):
    newl = []
    start_index = 0
    end_index = n
    if len(lst)>n:
        floor_division = len(lst)//n
        modulo = len(lst)%n
        for ad in range(floor_division):
            newl.append(lst[start_index:end_index])
            start_index = end_index
            end_index += n
        if modulo:
            newl.append(lst[end_index-n:])
    else:
        newl.append(lst)
    return newl