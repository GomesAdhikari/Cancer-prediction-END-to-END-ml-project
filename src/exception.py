import sys


class CustomException(Exception):
    def __init__(self,exception : Exception,error_detail:sys):
        super().__init__(exception)
        self.exception = exception
        self.error_detail = error_detail
        self.error = ''
        self.error_message()

    def error_message(self):
        _,_,traceback = self.error_detail.exc_info()
        file_name = traceback.tb_frame.f_code.co_filename
        error_message = f'Error occured in Python Script [{file_name}] line [{traceback.tb_lineno}] line number Error message [{str(self.exception)}]'
        self.error = error_message

    def __str__(self):
        return self.error

