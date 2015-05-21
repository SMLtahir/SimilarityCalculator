import json
import os


class ConfigBase:
    def __init__(self):
        json_conf = open('config/config.json')
        self.conf = json.load(json_conf)
        json_conf.close()

        if os.path.exists('config/config.test.json'):
            json_test_conf = open('config/config.test.json')
            conf_test = json.load(json_test_conf)
            self.conf.update(conf_test)
            json_test_conf.close()

        if os.path.exists('config/config.local.json'):
            json_loc_conf = open('config/config.local.json')
            conf_local = json.load(json_loc_conf)
            self.conf.update(conf_local)
            json_loc_conf.close()