import datetime


class TimeLog:
    def __init__(self, log_path):
        self.log_path = log_path

    def __enter__(self):
        self.time_start = datetime.datetime.utcnow()
        self.log = open(self.log_path, 'a', encoding='utf-8')
        self.log.write(f'Начало работы программы: {datetime.datetime.utcnow()}\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.log.write('Finished with error', str(exc_val))
        self.log.write(f'Программа завершила работу в {datetime.datetime.utcnow()}\n')
        self.log.write(f'Общее время работы программы: {datetime.datetime.utcnow() - self.time_start}\n')
        self.log.close()
