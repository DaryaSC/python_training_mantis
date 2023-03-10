import random
from model.project import Project


def test_delete_some_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name="test", description="test"))
    old_projects = app.soap.get_projects_list("administrator", "root")
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.soap.get_projects_list("administrator", "root")
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
