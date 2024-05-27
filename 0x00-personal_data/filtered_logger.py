#!/usr/bin/env python3
"""
This module for task "Regex-ing"
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    This function returns the log message obfuscated.
    Args:
        fields: a list of strings representing all fields to obfuscate.
        redaction: a string representing by what the field will be obfuscated.
        message: a string representing the log line.
        separator: a string representing by which character is separating all
        fields in the log line (message).
    """
    data_list = re.split(separator, message)
    for i in range(len(data_list)):
        if re.split('=', data_list[i])[0] in fields:
            data_list[i] = re.sub('(?<==).*', redaction, data_list[i])
    return ";".join(data_list)
