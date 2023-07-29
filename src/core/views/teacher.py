from flask import Blueprint, render_template, request, redirect, jsonify
import pandas as pd
from ..models import Subject
from .. import db
import json

TeacherViews = Blueprint("TeacherViews", __name__)


@TeacherViews.route("/")
def home():
    return "<H1>This a Teacher Homepage</H1>"


@TeacherViews.route("/upload", methods=['POST'])
def upload():
    sem = request.form.get('Sem')
    batch = request.form.get('Batch')
    file = request.files['file']

    return render_template("/teacher/teacher_upload.html")


@TeacherViews.route("/filter_by")
def filter_by():
    return "<H1>This a Teacher filter_by page</H1>"


@TeacherViews.route("/addsub", methods=['POST', 'GET'])
def addsub():
    if request.method == 'POST':
        sem = request.form.get('Sem')
        subCode = request.form.get('subcode')

        subject_entry = Subject(Sem=sem, SubCode=subCode)
        db.session.add(subject_entry)
        db.session.commit()

        return redirect("/teacher/addsub")

    subject_list = Subject.query.all()
    print(type(subject_list))

    return render_template("teacher/teacher_add_subject.html", subject_list=subject_list)
