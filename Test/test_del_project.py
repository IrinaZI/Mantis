from model.project import Project
from random import randrange

def test_del_project(app):
    pld1 = app.project.get_project_list()
    if len(pld1) == 0:
        project = Project(name="2", description="2")
        app.project.create(project)
        pld1 = app.project.get_project_list()
    index = randrange(len(pld1))
    app.project.del_project(index)
    pld2 = app.project.get_project_list()
    assert pld1 != pld2

