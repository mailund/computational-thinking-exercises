from datetime import datetime

class Log(object):
    def __init__(self, log = None):
        self.log = log or []

    def add_entry(self, entry):
        now = datetime.now()
        self.log.append("{}: {}".format(now, entry))

    def print_entries(self):
        for entry in self.log:
            print(entry)

    def clear_log(self):
        self.log = []

    def __repr__(self):
        return "Log({})".format(self.log)


log = Log()
log.add_entry("foo")
log.add_entry("bar")
log.add_entry("baz")
log.print_entries()

print(repr(log))
\
