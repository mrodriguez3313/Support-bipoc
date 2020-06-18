from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)
states_a = ["California", "Texas", "Minnesota"]
states_array = sorted(states_a)

@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html', states=states_array), 404
