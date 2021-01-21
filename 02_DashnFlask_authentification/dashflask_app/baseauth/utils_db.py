from .models import User,UserDashboard

def find_dashboardlist(user,verbose=False):
    """
        look in UserDashboard database and 
        gets all dashboards associated to input user
    """
    dlist = UserDashboard.query.filter(
        UserDashboard.name == user.name).all()
    
    # debug/dev feature
    if verbose : 
        print('dashboards in UserDashboard for {} : {}'
        .format(user.name,len(dlist)))
        for elem in dlist : print(elem.dashref)
    
    return dlist