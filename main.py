import npyscreen
import yaml
import requests
from requests import RequestException

with open("config.yml", 'r') as stream:
    try:
        yml_content = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)


class MainWidgetTUI(npyscreen.ActionForm):

    def activate(self):
        self.edit()
        self.parentApp.setNextForm(None)

    def while_waiting(self):
        for service in yml_content['services']:
            current_service = self.SERVICES.get(service['name'])
            try:
                resp = requests.get(service['url'])
                if resp.status_code == 200:
                    current_service.value = '[OK]'
            except RequestException as e:
                current_service.value = '[FAILED]'
            current_service.display()

    def create(self):
        self.SERVICES = {}
        for service in yml_content['services']:
            self.SERVICES.update({service['name']: self.add(npyscreen.TitleText, name=service['name'], value="Not started", editable=False)})


class MonitoringTUI(npyscreen.NPSAppManaged):

    def onStart(self):
        self.keypress_timeout_default = 10
        self.addForm("MAIN", MainWidgetTUI, name="Monitoring TUI")


if __name__ == "__main__":
    npyscreen.wrapper(MonitoringTUI().run())
