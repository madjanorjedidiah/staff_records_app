from .models import *



def add_user_id_n_save(request, data, unique=None):
    try:
        user = UserBioInfo.objects.filter(user_fk=request.user)
        if len(user) > 0:
            user_id = user[0]
            if (unique is True and data.Meta.model.objects.filter(user_fk=user_id, **data.cleaned_data).exists()): #buggy test with economic activity bool
                return False
            else:
                temp = data.save(commit=False)
                temp.assembly_id = assembly_id
                temp.save()
                return True
    except Exception as e:
        #logging.info(f"ERROR: Profile must be created first {e}")
        return False


def get_user(request,):
    user = None
    user_set = UserBioInfo.objects.filter(user_fk=request.user)
    if len(assembly_set) > 0:
        user = user_set[0]
    return user