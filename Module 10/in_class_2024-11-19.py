from logging import *
# # handle multiple exceptions
# repeat = True

# while repeat:
#     try:
#         number = int(input("Enter an Integer: "))  
#         print(f"you entered the number {number}")
#         repeat = False
#     except ValueError:
#         print("You entered an invalid integer")
#         print("Please try again")

# # handle multiple exceptions
# try:
#     filename = input("enter file name:")
#     movies = []
#     with open(filename) as file:
#         for line in file:
#             line = line.replace("\n","")
#             movies.append(line)
#     print(movies)
# except FileNotFoundError:
#     print(f"Could not find the {filename} file")
# except OSError:
#     print("File Found, but error reading file")
# except UnicodeDecodeError:
#     print("File type is not accepted, file must end in .csv")
# except Exception:
#     print("Unresolvable Error Occured")

# # treating exception as an object
# try:
#     filename = input("enter file name:")
#     movies = []
#     with open(filename) as file:
#         for line in file:
#             line = line.replace("\n","")
#             movies.append(line)
#     print(movies)
# except FileNotFoundError as e:
#     print(f"Could not find the {filename} file")
#     print(f"Full error message: {e}")
# finally:
#     file.close()

try:
    number = int(input("Enter a number greater than 10: "))
    if number <= 10:
        raise OSError("OS Test Error") 
    print(f"You entered the number {number}")
except OSError as e:
    print("successfully handled OS Error")
    print(e)
except Exception as e2:
    log.exception(e2)
    raise e2