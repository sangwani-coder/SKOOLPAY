from functools import wraps

from werkzeug.utils import send_file

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from . import momo_api as momo

bp = Blueprint('payment', __name__, url_prefix='/user')

@bp.route('/payment', methods=('GET', 'POST'))
def payment():
    if request.method == "GET":
        return render_template('parent/pay.html', session='user')
    momo.get_uuid()

    amount = request.form.get('amount')
    partyid = request.form.get('partyid')

    status = momo.request_to_pay(amount, partyid)

    if status == 202:
        momo.get_transaction_status()
        flash("PAYMENT SUCCESSFUL")
        return redirect("/")
    else:
        print(status)
        flash("PAYMENT FAILED")
        return redirect("/")

    

    
    