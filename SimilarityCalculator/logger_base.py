import sys
import logging


class LoggerBase:
    def __init__(self, module_name):

        try:
            self.logger = logging.getLogger('| TagNav |')
            self.logger.setLevel(logging.DEBUG)

            # create file handler for logging
            fh = logging.FileHandler('logs/' + module_name + '.log')
            fh.setLevel(logging.INFO)

            # create console handler with a higher log level
            ch = logging.StreamHandler()
            ch.setLevel(logging.WARNING)

            # create formatter and add it to the handlers
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # add the handlers to the logger
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
        except IOError, e:
            print 'There was an error logging data into the log file. ' \
                  'Please check the log files or the logger_base module in debug mode to see where the error may be.'
            sys.exit()
