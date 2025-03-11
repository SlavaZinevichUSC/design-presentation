class OutputInterface:
    def __init__(self):
        pass

    def show(self, message):
        pass

class OutputScreen(OutputInterface):
    def __init__(self):
        OutputInterface.__init__(self)

    def show(self, message):
        print(message)

class OutputScreenExclaim(OutputInterface):
    def __init__(self):
        OutputInterface.__init__(self)

    def show(self, message):
        print(message + '!')

class Logger:
    def __init__(self):
        self.buffer = []
        self.lock = False

    def log(self, message):
        def sleep(seconds):
            pass
        while self.lock:
            sleep(1)

        #acquire lock
        self.lock = True
        #perform operation
        self.buffer.append(message)
        #release lock
        self.lock = False

    def flush(self):
        #write out to memory
        for message in self.buffer:
            print(message)
        self.buffer = []
        pass
