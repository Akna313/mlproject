#This is common dont change
#use sys library to control different parts of the python runtime  environment
import sys
import logging

def error_message_details(error,error_detail:sys):#inside sys
    _,_,exc_tb=error_detail.exc_info()#we need only last information which is about error among 3 information we get
    file_name=exc_tb_frame.f_code.co_filename # get file name
    error_message="Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,ecx_tb.tb_lineno,str(error))

    return error_message

    #[{0}] is a place holder / how error message should look like inside file with custom exception

    #whenever errpr raises call function
    class CustomException(Exception):
        def __init__(self,error_message,error_detail:sys):#constructor inside sys
            super().__init__(error_message)#inheriting from Exception
            self.error_message=error_message_details(error_message,error_detail=error_detail)#override init method

        def __str__(self):
            return self.error_message#print error message

#To check everything working properly
# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divde by zero error")
#         raise CustomException(e,sys)
        
    


