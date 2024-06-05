#!/usr/bin/env python3
"""
Authentication module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    This class is a template for all authentication system we will implement.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method returns True if the path is not in the list
        of strings excluded_paths.
        """
        if path is None or excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        This method will be implemented later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method will be implemented later
        """
        return None
