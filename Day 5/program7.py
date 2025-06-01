# #purpose of logging is error reporting and debugging etc.
# #logging in a file
import logging
# logging.basicConfig(level=logging.INFO,filename='log.log',filemode='w',format="%(asctime)s-%(levelname)s-%(message)s")
# logging.debug("this is debug") #this will not be saved because logging starts from info
# # logging.info("this is info")
# # logging.warning("this is warning")
# # logging.error("this is error")
# # logging.critical("this is critical")

# #loggin a variable
# var=20
# logging.info(f"value of variable is {var}")
# #logging an exception
# try:
#     1/0
# except ZeroDivisionError as e:
#     logging.error("ZeroDivisionError",exc_info=True)
#     logging.exception("using exception")

#custom logger
custom=logging.getLogger(__name__)
custom.setLevel(logging.INFO)
#adds in same file
# custom.info("This is custom logger")
#creating custom log in different file using handlers and formatters
handler=logging.FileHandler('custom.log')
formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(formatter)
custom.addHandler(handler)
custom.info("testing custom logger")