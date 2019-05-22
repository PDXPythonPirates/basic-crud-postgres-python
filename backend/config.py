from configparser import ConfigParser
 
 
def config(filename='backend\setting.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # get section for postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file.')
 
    return db

def skconfig(filename='backend\setting.ini', section='flask'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section for flask
    skey = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            skey[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return skey 
    