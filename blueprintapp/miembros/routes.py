from flask import request,render_template,redirect,url_for,Blueprint

from blueprintapp.app import db
from blueprintapp.miembros.models import Miembro

bp_miembro=Blueprint('bp_miembro',__name__,template_folder='templates')

@bp_miembro.route("/")
def index():
    miembros=Miembro.query.all()
    return render_template('miembro/index.html',miembros=miembros)
@bp_miembro.route("/create",methods=['GET','POST'])
def create():
    if request.method=='GET':
        return render_template('miembro/create.html')
    elif request.method=='POST':
        nombre=request.form.get('nombre')
        email=request.form.get('email')
        miembro=Miembro(nombre=nombre,email=email)
        db.session.add(miembro)
        db.session.commit()
        return redirect(url_for('bp_miembro.index'))
        