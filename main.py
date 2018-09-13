import npyscreen


class MainWidgetTUI(npyscreen.Form):

    def activate(self):
        self.edit()
        self.parentApp.setNextForm(None)

    def create(self):
        self.serviceX = self.add(npyscreen.TitleText, name="Service X", value="[OK]", editable=False)


class MonitoringTUI(npyscreen.NPSAppManaged):

    def onStart(self):
        self.addForm("MAIN", MainWidgetTUI, name="Monitoring TUI")


if __name__ == "__main__":
    npyscreen.wrapper(MonitoringTUI().run())
