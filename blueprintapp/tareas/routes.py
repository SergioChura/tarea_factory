from flask import request,render_template,redirect,url_for,Blueprint

from blueprintapp.app import db
from blueprintapp.tareas.models import Tarea

bp_tarea=Blueprint('bp_tarea',__name__,template_folder='templates')

@bp_tarea.route("/")
def index():
    tareas=Tarea.query.all()
    return render_template('tareas/index.html',tareas=tareas)
    
@bp_tarea.route("/create",methods=['GET','POST'])
def create():
    if request.method=='GET':
        return render_template('tareas/create.html')
    elif request.method=='POST':
        descripcion=request.form.get('descripcion')
        completado=True if 'completardo' in request.form.keys() else False
        tarea=Tarea(descripcion=descripcion,completado=completado)
        db.session.add(tarea)
        db.session.commit()
        return redirect(url_for('bp_tarea.index'))
