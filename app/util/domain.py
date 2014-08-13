
from datetime   import datetime
from os         import system
from os.path    import isfile, exists,join
from re         import compile, IGNORECASE, DOTALL

from wiki  import *
from tabs  import format_tabs, format_doc
from files import read_input, read_text, write_file, is_writable
from app.settings import DOC_DIR


# Read the domain mapping from a file
def domain_map():
    map = {}
    for d in open(join(DOC_DIR, doc)


# Either format the doc or return the redirect page
def doc_redirect (url):
    doc = map_doc_path(url)
    if exists(doc):
        if not isfile(doc):
            index = join(doc,'Index')
            if exists(index):
                return redirect_path(url) + '/Index'
            else:
                return redirect_path(url) + '/Index/missing'
    else:
        return redirect_path(url) + '/missing' 


# Either format the doc or return the redirect page
def show_domain_doc(url):
    doc = map_doc_path(url)
    if exists(doc) and isfile(doc):
        text = read_text(doc)
        return format_tabs(text)


# Put the document text in storage
def put_domain_doc(doc):
    write_file(map_doc_path(doc), read_input())


# Get the document text from storage
def get_domain_doc(doc):
    if not doc_redirect(doc):
        print read_text(map_doc_path(doc))
    else:
        print "redirect:%s/missing" % doc_redirect(doc)


#  Formatter to add tabs to the HTML formatting
def print_tab_doc(filename):
    print format_doc(filename)

