from entities.status import Status


class Todo:
    def __init__(self, text):
        self.text = text
        self.status = Status.NEW

    def toggle_status(self):
        if self.status == Status.NEW:
            self.status = Status.DONE
        else:
            self.status = Status.NEW
