#
# Contributors: S. Van Hoey, John Wieczorek, Paul J. Morris
# Modified from https://github.com/tdwg/dwc/blob/master/build/build.py
# 
# Build script for TDWG BDQ (Biodiversity Data Quality) artifacts
#
__version__ = '2024-04-17T-21:00'
import io
import os
import re
import csv
import sys
import codecs

from urllib import request
from jinja2 import FileSystemLoader, Environment

# bdq and bdqffdq are not yet approved placeholders
NAMESPACES = {
    'https://rs.tdwg.org/bdq/terms/' : 'bdq',
    'https://rs.tdwg.org/bdq/ffdq/' : 'bdqffdq',
    'https://www.w3.org/TR/annotation-vocab/' : 'oa',
    'http://www.w3.org/2002/07/owl#' : 'owl',
    'https://rs.tdwg.org/dwc/iri/' : 'dwciri',
    'https://rs.tdwg.org/dwc/terms/' : 'dwc',
    'https://purl.org/dc/elements/1.1/' : 'dc',
    'https://purl.org/dc/terms/' : 'dcterms'}
