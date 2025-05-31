# Handle multiple exceptions in a single block.
# def Handle_exceptions(a,b):
#     try:
#         result=a/b 
#     except ZeroDivisionError:
#         return 'wrong value'
#     except TypeError:
#         return 'only numeric values'
#     else:
#         return result
# print(Handle_exceptions('10',20))

#handling multiple exceptions using same except block
def Handle_exceptions(a,b):
    try:
        result=a/b 
    except (ZeroDivisionError,TypeError) as e:
        if isinstance(e,ZeroDivisionError):
            return 'please dont give zero'
        if isinstance(e,TypeError) :
            return 'please only numeric values'
    else:
        return result
print(Handle_exceptions(7,'4'))