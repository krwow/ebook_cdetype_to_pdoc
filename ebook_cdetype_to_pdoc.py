from mobi_header import MobiHeader
import os


ebook_extensions = ['.mobi', '.azw3']

def change_cdetype_to_pdoc(extensions=ebook_extensions):
    # Get location of this script.
    path = os.path.realpath(os.path.dirname(__file__))

    # Get list of all files and folders in the location of script.
    try:
        files_list = os.listdir(path)
    except FileNotFoundError:
        os.mkdir(path)
        files_list = os.listdir(path)

    for file_name in files_list:
        # Getting a file extension part from the whole file name.
        file_extension = os.path.splitext(file_name)[1]

        if file_extension in extensions:
            path_and_file = os.path.join(path, file_name)
            print('-> E-book filename:', file_name)

            try:
                item = MobiHeader(path_and_file)
                current_cdetype_val = item.get_exth_value_by_id(501)
                print('Current cdetype value:', current_cdetype_val)

                if current_cdetype_val == 'PDOC':
                    print('No need to change cdetype value.')
                elif (current_cdetype_val != 'PDOC' and
                        current_cdetype_val != None):
                    item.change_exth_metadata(501, 'PDOC')
                    item.to_file()
                    new_cdetype_val = item.get_exth_value_by_id(501)
                    print('New cdetype value:', new_cdetype_val)
                elif current_cdetype_val == None:
                    print('No cdetype field found in this file.')
            except UnicodeDecodeError as exception_error:
                print(('Encoding error. Cannot access metadata. Value of '
                      'cdetype will remain unchanged.'))


if __name__ == '__main__':
    change_cdetype_to_pdoc()