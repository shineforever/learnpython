#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import os
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
print(BASEDIR)

from HomeworkCheck.conf import mylogging
from core import main
#
#
# if __name__ == "__main__":
# 	main()
