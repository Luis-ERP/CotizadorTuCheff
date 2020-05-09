from Layouts.mainActivity import MainActivity, AuthenticationDialogActivity


class Main(MainActivity):
    def __init__(self):
        super().__init__()


class AuthenticationDialog(AuthenticationDialogActivity):
    def __init__(self, parent):
        super(AuthenticationDialog, self).__init__(parent)

        ##initial window
        self.changeToSuccesWindow()

