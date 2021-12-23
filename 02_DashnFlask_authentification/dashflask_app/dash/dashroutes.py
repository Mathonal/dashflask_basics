"""Routes for parent Flask app."""
from flask import Blueprint, render_template, request
from flask import current_app as app
from flask_login import login_required, current_user

from .utils_dashboard import getHashDashURL

dashr = Blueprint('dashr', __name__,
        template_folder='templates',
        static_folder='static')

from .genericDash import dashboard1,dashboard2
# GENERIC DASHBOARDS (can access from everywhere : demonstration purpose)
@dashr.route('/app1')
#@login_required
def app1_template():
    return render_template('dashboard_page.html', dash_url = dashboard1.url_base)
@dashr.route('/app2')
#@login_required
def app2_template():
    return render_template('app1.html', dash_url = dashboard2.url_base)

# PERSONNALISED DASHBOARD with AUTHENTIFICATION
@dashr.route('/mydash/', methods=['POST'])
@login_required
def mydashboard():
    """ 
        generate url from currentuser name and dashboardname 
        to access the private dashoard
    """
    # Get wanted dashboard name via button value
    buttonval = request.form.get('dashbutton')
    url = '/privatedash/'+getHashDashURL(current_user.name+buttonval)+'/'
    return render_template('dashboard_page.html',
        dash_url = url)
