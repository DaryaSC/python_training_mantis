from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_projects_list(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

        def new_projects_list(element):
            return Project(name=element['name'], id=element['id'], description=element['description'])

        try:
            soap_list = client.service.mc_projects_get_user_accessible(username, password)
            projects_list = list(map(new_projects_list, soap_list))
            return projects_list
        except WebFault:
            return False

