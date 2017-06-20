
import os
import glob

# if __name__ == '__main__':
#     run("\linux2win\negotiate", )


def linux2win():

    dictionary = 'linux2win/negotiate'
    errorfiles = []
    
    if not os.path.isdir(dictionary):
        print('input dictionary is not a dir')
        return False

    for file in glob.glob(os.path.join(dictionary, '*.log')):
        try:
            print(file, end='\n')
            f = open(file, 'r')
            result = f.read()
            result = result.replace('\n', '\r\n')
            f.close()
            w = open(file, 'w')
            w.write(result)
            w.close()
        except IOError:
            print('error files', file)
            errorfiles.append(file)

    print('transmit completed, %d file(s) missed.' % len(errorfiles))

linux2win()
