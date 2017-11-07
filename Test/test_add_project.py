from model.project import Project


def test_add_project(app):
    project = Project(name="1", description="1")
    pla1=app.project.get_project_list()
    app.project.create(project)
    pla2 = app.project.get_project_list()
    assert pla1 != pla2
