import os 
import sys

class housing_exception(Exception):

    def __init__(self, error_message: Exception) -> str:
        super().__init__(error_message)
        self.error_message=housing_exception.get_detailed_error_message(error_message=error_message,
                                                                        error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        """
        error_message:Exception object
        error_detail:object of sys module 
        """
        _,_,exec_tb=error_detail.exc_info()
        line_number=exec_tb.tb_frame.f_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename

        error_message=f"Error occured in scrip: [{file_name}] at line number :[{line_number}] error message:[{error_message}"
        return error_message

    
    def __str__(self) -> str: #whenever u want to print the output of any class what information should be displayed is given by this function
        return self.error_message

    
    def __repr__(self) -> str:
        return housing_exception.__name__.str()