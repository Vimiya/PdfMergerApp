import logging as lg
lg.basicConfig(filename='app_logs.log', level=lg.DEBUG,
               format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')


def writelogs(username, msglevel, msg):
    logger1=lg.getLogger(username)
    if msglevel == 'DEBUG' or msglevel == 'debug':
        logger1.debug(msg)
    if msglevel == 'INFO' or msglevel == 'info':
        logger1.info(msg)
    if msglevel == 'WARNING' or msglevel == 'warning':
        logger1.warning(msg)
    if msglevel == 'ERROR' or msglevel == 'error':
        logger1.error(msg)
    if msglevel == 'CRITICAL' or msglevel == 'critical':
        logger1.critical(msg)
    if msglevel == 'EXCEPTION' or msglevel == 'exception':
        logger1.exception(msg)


def getpath(pathname):
    """
    This function will return the list of files and directories in the given path
    to the calling module
    """
    writelogs('getpath', 'info', 'Entered into getpath')
    try:

        path = pathname
        lst_dir = fetchlist(path)
        return lst_dir
    except Exception as e:
        writelogs('getpath','error','Error occurred while listing files and directories')
        writelogs('getpath','exception',e)
    else:
        writelogs('getpath','info','Getting the list of files and directories is successful')


def fetchlist(path1):
    """
    This function will find the list of files and directories in the given path
    """
    writelogs('fetchlist', 'info', 'Entered into getlist')
    try:
        import os
        lst = os.walk(top=str(path1))
        l1 = []

        for i in list(lst):
            l1.append('Directory Path: '+i[0])
            l1.append("Files: ")
            l1.append(i[2])
            l1.append("Folders:")
            l1.append(i[1])
            l1.append("........................")
        return l1
    except Exception as e:
        writelogs('fetchlist', 'error', 'Error occurred while listing files and directories')
        writelogs('fetchlist', 'exception', e)


def fetchfile(file_path):
    """
    This function will help you to filter only pdf file from a directory
    """
    writelogs('fetchfile','info','Entered into fetchfile')
    try:

        import os
        a = os.walk(file_path)
        l = []
        dir_lst = list(a)

        import re
        pattern = re.compile(r"\.pdf$")
        import PyPDF2 as pdf
        import os
        from os import path

        f_writer = pdf.PdfFileWriter()

        for lst in dir_lst:
            if type(lst) == tuple:
                for dirct in lst:
                    if type(dirct) == list:
                        for file in dirct:
                            matches = pattern.finditer(file)
                            for match in matches:
                                l.append(file)
                                f1 = open(path.join(lst[0], file), 'rb')

                                f1_read = pdf.PdfFileReader(f1)

                                for page_no in range(f1_read.numPages):
                                    f1_pages = f1_read.getPage(page_no)
                                    f_writer.addPage(f1_pages)

        fnew = open("Mergedfile.pdf", 'wb')
        f_writer.write(fnew)
        filename = path.join(os.getcwd(), 'Mergedfile.pdf')

        return l, filename

    except Exception as e:
        writelogs('fetchfile', 'error', 'Error occurred while fetching .pdf files')
        writelogs('fetchfile', 'exception', e)
    else:
        writelogs('fetchfile', 'info', 'Fetching .pdf files is successful')

