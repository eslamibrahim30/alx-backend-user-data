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
        This method will be implemented later
        """
        return False

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
