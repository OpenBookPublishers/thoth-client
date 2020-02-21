#!/usr/bin/env python3
"""GraphQL client for Thoth"""

__version__ = "0.1.0"
__author__ = "Javier Arias <javi@openbookpublishers.com>"
__copyright__ = "Copyright (c) 2020 Open Book Publishers"
__license__ = "Apache 2.0"

from .client import ThothClient
from .errors import ThothError
from .mutation import ThothMutation

__all__ = ["ThothClient", "ThothMutation", "ThothError"]