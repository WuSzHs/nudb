# -*- coding: utf-8 -*-

import os, sys, re, codecs, json, requests, tools

class NuDB(object):

    def __init__(self):
        reload(sys)
        sys.setdefaultencoding("utf-8")
        
        # default host and port
        host = 'localhost'
        port = '5800'
        self.api = 'http://'+ host + ':' + port + '/nudb/'
        self.db = 'test'

    def connect(self, host, port, db):
        self.api = 'http://'+ host + ':' + port + '/nudb/'
        self.db = db
        print('API: %s, db: %s' % (self.api, self.db))

    def rput(self, data, data_type, *recBeg):
        """ data_type: json/text """
        url = self.api + 'rput'

        if data == "":
            return 'Empty data'

        if data_type == 'text' and isinstance(data, str):
            if len(recBeg) == 1:
                data = re.sub('\\\\\\\\','\\\\', data)
                opts = {
                    'db': self.db,
                    'data': data,
                    'recbeg': recBeg[0],
                    'format': data_type
                }
            else:
                return 'Wrong recBeg'
        elif data_type == 'json':
            check = tools.check_JSON(data)
            if check == 1:
                # JSON object
                opts = {
                    'db': self.db,
                    'data': json.dumps(data),
                    'format': data_type
                }
            elif check == 2:
                # JSON string
                opts = {
                    'db': self.db,
                    'data': data,
                    'format': data_type
                }
            else:
                return 'Invalid JSON format'
        else:
            return 'Wrong format'

        res = requests.post(url, opts)
        print('[rput] Response: %s' % res.status_code)
        return res.text
    
    def fput(self, filePath, data_type, *recBeg):
        """ data_type: json/text """
        url = self.api + "fput"

        fileData = {
            'file': codecs.open(filePath, 'rb', 'utf-8')
        }

        if data_type == 'text':
            if len(recBeg) == 1:
                opts = {
                    'db': self.db,
                    'recbeg': recBeg[0],
                    'format': data_type
                }
            else:
                return 'Wrong recBeg'
        elif data_type == 'json':
            opts = {
                'db': self.db,
                'format': data_type
            }
        else:
            return 'Wrong format'

        res = requests.post(url, opts, files=fileData)
        print('[fput] Response: %s' % res.status_code)
        return res.text

    def rget(self, rid):
        url = self.api + "rget"
        
        opts = {
            'db': self.db,
            'rid': rid,
            'out': 'json'
        }
        
        res = requests.get(url, opts)
        print('[rget] Response: %s' % res.status_code)
        return res.text

    def rdel(self, rid):
        url = self.api + "rdel"
        
        opts = {
            'db': self.db,
            'rid': rid,
            'out': 'json'
        }
        
        res = requests.post(url, opts)
        print('[rdel] Response: %s' % res.status_code)
        return res.text
    
    def rupdate(self, rid, data, data_type):
        """ data_type: json/text """
        url = self.api + "rupdate"
        record = ""
        
        if rid == "":
            return 'Empty rid'
        if data == "":
            return 'Empty data'

        if data_type == 'text' and isinstance(data, str):
            record = re.sub('\\\\\\\\','\\\\', data)
            opts = {
                'db': self.db,
                'getrec': 'n',
                'out': 'json',
                'rid': rid,
                'record': record
            }
            res = requests.post(url, opts)
            print('[rupdate] Response: %s' % res.status_code)
            return res.text

        elif data_type == 'json':
            """ Use rdel + rput, because rupdate of JSON format is currently not supported."""
            check = tools.check_JSON(data)
            
            if check >= 1:
                # rdel
                res = self.rdel(rid)
                obj = json.loads(res)
                
                if 'error' not in obj['result'][0].keys():
                    # delete successful -> rput
                    res = self.rput(data, data_type)
                return res
            else:
                return 'Invalid JSON format'
        else:
            return 'Wrong format'
                
    def search(self, query):
        url = self.api + "query"
        
        opts = {
            'db': self.db,
            'q': query,
            'out': 'json'
        }
        
        res = requests.get(url, opts)
        print('[search] Response: %s' % res.status_code)
        return res.text

