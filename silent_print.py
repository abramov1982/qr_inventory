# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

import subprocess
import sys

# ref: https://geonet.esri.com/thread/59446
# ref: https://helpx.adobe.com/jp/acrobat/kb/510705.html


def main(path_to_acrobat, pdffile, printer_name):
    # acroread = r'C:\Program Files (x86)\Adobe\Reader 11.0\Reader\AcroRd32.exe'
    # '"%s"'is to wrap double quotes around paths
    # as subprocess will use list2cmdline internally if we pass it a list
    # which escapes double quotes and Adobe Reader doesn't like that

    cmd = f'{path_to_acrobat} /N /T {pdffile} {printer_name}'

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    exit_code = proc.wait()



if __name__ == '__main__':
    pdffile = sys.argv[1]
    printer_name = sys.argv[2]
    main(pdffile, printer_name)