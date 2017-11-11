from model.project import Project


def test_add_project(app):
    project = Project(name="1", description="1")
    pla1 = app.soap.get_project_list("administrator", "root")
    app.project.create(project)
    pla2 = app.soap.get_project_list("administrator", "root")
    assert pla1 != pla2
