from configparser import ConfigParser

file = 'bank.ini'


class ConfigTest(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = ConfigParser()
        self.config.read(file_path)

    def print_msg(self):
        print(self.config.sections())
        print(self.config['account'])
        print(list(self.config['account']))
        print(self.config['account']['pin'])

    def update_configFile(self):
        self.config.add_section('bank')
        self.config.set(section='bank', option='branch', value='hsbc')
        with open(self.file_path, 'w') as f:
            self.config.write(f)


myConfig = ConfigTest(file)
myConfig.print_msg()
# myConfig.update_configFile()
myConfig.print_msg()
