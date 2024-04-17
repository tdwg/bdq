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

# bdq and ffdq are not yet approved placeholders
NAMESPACES = {
    'http://rs.tdwg.org/bdq/bdq/' : 'bdq',
    'http://rs.tdwg.org/bdq/ffdq/' : 'ffdq',
    'http://rs.tdwg.org/dwc/iri/' : 'dwciri',
    'http://rs.tdwg.org/dwc/terms/' : 'dwc',
    'http://purl.org/dc/elements/1.1/' : 'dc',
    'http://purl.org/dc/terms/' : 'dcterms'}
