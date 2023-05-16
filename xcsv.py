'''extract csv data'''
import logging as log
import csv
from locale import getpreferredencoding

def cxs(f):
    '''extract csv data'''
    d = []
    log.info('< %s', f)
    n = 0
    with open(
        f,
        encoding=getpreferredencoding(),
        newline='') as csvfile:

        for n, row in enumerate(csv.reader(csvfile, delimiter=";")):
            d.append(row)

    log.info('# %d CSV rows read (excluding header)', n)
    return d
