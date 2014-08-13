
from sys        import argv, stdin
from os.path    import exists, join, isfile
from os.path import join,exists,basename
from os         import system

from tabs  import format_doc, format_tabs
from wiki  import convert_html
from files import read_input, read_text, read_file, write_file, do_command, list_files,list_dirs
from app.settings import BASE_DIR

DOC_DIR =  BASE_DIR+'user_doc'

#-----------------------------------------------------------------------------
# Add ins


# Create links for each item in the folder
def app_links(files):
    return [ ' * [[%s][%s]]'%(x,title_text(x)) for x in files   if len(x)>0 ]

# Return the directory list
def directory_list(d):
    dirs = [ basename(f) for f in list_dirs(d) ]
    return  '\n'.join(app_links(dirs))


# Return the directory list
def item_list(d):
    dirs = [ basename(f) for f in list_files(d) if not f.startswith('.') and not f.startswith('Index') ]
    return  '\n'.join(app_links(dirs))


# Add a list of directory entries
def include_dirs(text,d):
    return [ l if not '[[DIRS]]' in l else directory_list(d)   for l in text ]
            

# Add a list of directory entries
def include_items(text,d):
    return [ l if not '[[ITEMS]]' in l else item_list(d)   for l in text ]
            

# Create wiki text for the index page
def index_text(doc):
    d = join(DOC_DIR,doc)
    text = read_index(join(d,'.index')).split('\n')
    text = include_dirs(text,d)
    #print 'include ',d
    text = include_items(text,d)
    text.append('')
    return '\n'.join(text)

#-----------------------------------------------------------------------------
# Docs

# Convert a url to a directory
def doc_path(doc):
    return DOC_DIR+'/'+doc


# Either format the doc or return the redirect page
def doc_redirect (url):
    doc = doc_path(url)
    if exists(doc):
        if isfile(doc):  # Is a file
            return
        else:   # Is a directory
            index = join(doc,'Index')
            if exists(index):
                return url+'/Index'
            else:
                return url+'/Index/missing'
    else:
        return url+'/missing' 


# Format the text of a doc as HTML
def doc_format(doc=None):
    if not doc:
        text = stdin.read()
    else:
        if exists(doc_path(doc)):
            text = read_text(doc_path(doc))
        else:
            text = 'No doc found\n\nPATH = '+doc_path(doc)
    return format_tabs(text)


# Show the formatted document for the file
def doc_show(doc):
    return format_doc(doc_path(doc))
    

# Put the document text in storage
def doc_put(doc):
    write_file(doc_path(doc), read_input())


# Get the document text from storage
def doc_get(doc):
    print read_text(doc_path(doc))

