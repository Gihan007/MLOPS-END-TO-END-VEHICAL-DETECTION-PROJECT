# from src.logger import logging

# logging.debug("Thois is debug message")
# logging.info("This is an info messaege")
# logging.warning("this is from Warning Messaeg")
# logging.error("This is eror mesage")
# logging.critical("this is critical messaeg")


#--------------------------------------- DEMO for Exception File ------------------------------------

# below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

#---------------------------------------AFTER CREATEING ENTIRE PIPELINE---------------------------

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()