# diwo
# =======================================
from klibee.logger import Logger


# third-party
# =======================================
import csv


# function
# =======================================
def export_list_of_dictionaries(self, filepath, items, verbose = True):

    # make folders if necessary
    self.make_folders(filepath)

    # go
    fieldnames = items[0].keys()

    with open(filepath, 'w', encoding='UTF8', newline='\n') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(items)

    # log
    if (verbose):
        Logger.success("File {} successfully exported with {} rows.".format(filepath, len(items)))
