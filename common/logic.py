#!/usr/bin/python3
# -*- coding: utf-8 -*-

# installed module section
import random
# user module section
from common import config
from common.dbaccess import DAO

class DataManage():
    def __init__(self):
        pass 
        self.dao = DAO()

    def omikuzi_get(self, **kwargs):
        username = kwargs.get('username','')
        draw_kuzi_dict = {}
        omikuzi_index = random.randrange(1,7)
        if username == '':
            print('usernameの指定がありません')
        else:
            for i in self.dao.usermaster_get():
                if i['name']== username:
                    for j in self.dao.kuzimaster_get():
                        if j['id'] == omikuzi_index:
                            draw_kuzi = j['name']
                            draw_kuzi_dict.update({'username':i['name'], 'kuzi':j['name']}) 
                            self.dao.result_insert(username=i['name'],kuziname=j['name'])
                            print('test')
    
        return draw_kuzi_dict
    

if __name__ == '__main__':
    dm = DataManage()
    dm.omikuzi_get(username='test user name1')
    dao = DAO()
    for i in dao.result_get():
        print(i)

