# This code defines a custom exception class called `CustomException` that inherits from the built-in `Exception` class. It also includes a function called `error_message_detail` that takes an error and its details as input and returns a formatted error message with the filename, line number, and error message.


import logging
import sys  # used to manipulate the different types of Python runtime environment


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = (
        error_detail.exc_info()
    )  # returns a tuple of three values that represent the type, value, and traceback of the exception
    file_name = (
        exc_tb.tb_frame.f_code.co_filename
    )  # accesses the filename where the exception occurred
    line_number = (
        exc_tb.tb_lineno
    )  # accesses the line number where the exception occurred
    error_message = f"Error occurred in python script: {file_name} at line number: {line_number} with error message: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message
