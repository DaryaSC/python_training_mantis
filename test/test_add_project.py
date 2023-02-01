from model.project import Project
import string
import random


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    old_projects = app.soap.get_projects_list("administrator", "root")
    project = Project(name=random_string(10), description=random_string(20))
    app.project.create(project)
    new_projects = app.soap.get_projects_list("administrator", "root")
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
