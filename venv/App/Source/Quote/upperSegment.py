from Layouts.QuoteActivity import upperSegment

class ConfigurationSegment(upperSegment.ConfigurationSegment):
    def __init__(self, parent):
        super(ConfigurationSegment, self).__init__(parent)


class ClientSegment(upperSegment.ClientSegment):
    def __init__(self):
        super(ClientSegment, self).__init__()


class EventSegment(upperSegment.EventSegment):
    def __init__(self):
        super(EventSegment, self).__init__()


class CodeSegment(upperSegment.CodeSegment):
    def __init__(self):
        super(CodeSegment, self).__init__()

