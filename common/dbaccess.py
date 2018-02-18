#!/usr/bin/python3
# -*- coding: utf-8 -*-

####################################
# モジュールインポート
###################################
# pip installed module section
# DBエンジン指定に必要
from sqlalchemy import create_engine
# ORMに必要
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import UniqueConstraint
# セッション作成に必要
from sqlalchemy.orm import sessionmaker

# user module section
from common import config

###################################
# ORMを定義
###################################
# ベースクラス作成
Base = declarative_base()

### マスターテーブル ###
# ユーザー一覧
class UserMaster(Base):
    __tablename__ = 'usermaster'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return "<Id='%s', Username='%s'>" % (self.id, self.name)

# クジのマスターテーブル
class KuziMaster(Base):
    __tablename__ = 'kuzimaster'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    def __repr__(self):
        return "<Id='%s', Kuziname='%s'>" % (self.id, self.name)

### トランザクションテーブル ###
# クジ引き結果一覧
class Result(Base):
    __tablename__ = 'result'

    id = Column(Integer, primary_key=True, autoincrement=True)
#    username = Column(String, unique=True)
#    kuziname = Column(String, unique=True)
    username = Column(String)
    kuziname = Column(String)
    def __repr__(self):
        return "<Id='%s', Username='%s', Kuziname='%s'>" % (self.id, self.username, self.kuziname)

#エンジン種別のパラメータを読み、エンジンを作成
if config.DB_TYPE == 'sqlite':
    engine = create_engine('sqlite:///:memory:', echo=True)
elif config.DB_TYPE == 'mysql':
    raise Exception('DB種別指定エラー:MYSQLはまだ未対応')
else:
    raise Exception('DB種別指定エラー')
# エンジン作成
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
initial = False

# 初回起動時のみ初期化処理を行う。
# 初期化の判断は、INITIALIZE変数がTRUEになっているかで決まる
if config.INITIALIZE == 'TRUE' and initial is False :
    # セッション作成
    session = Session()
    # DB初期化
    session.add_all([
            UserMaster(id=1, name='test user name1'),
            UserMaster(id=2, name='test user name2'),
            UserMaster(id=3, name='test user name3'),
            UserMaster(id=4, name='test user name4'),
            UserMaster(id=5, name='test user name5'),
            UserMaster(id=6, name='test user name6'),
            UserMaster(id=7, name='test user name7'),
            ])
    session.commit()

    session.add_all([
            KuziMaster(id=1, name='1-末吉'),
            KuziMaster(id=2, name='2-小吉'),
            KuziMaster(id=3, name='3-吉'),
            KuziMaster(id=4, name='4-中吉'),
            KuziMaster(id=5, name='5-大吉'),
            KuziMaster(id=6, name='6-御祭'),
            KuziMaster(id=7, name='7-爆発'),
            ])
    session.commit()
    session.close()
    initial = True
else:
    # TRUEでない場合は何もしない
    pass


# DB操作クラス
class DAO():
    def __init__(self):
        pass

#    def usermaster_get(self):
    def usermaster_get(self):
        # セッション作成
        session = Session()
        usermaster_list = []
        for row in session.query(UserMaster):
            usermaster_list.append({"id":row.id ,"name":row.name})
        # セッションクローズ
        session.close()
        return usermaster_list
        return usermaster_list
    
    def kuzimaster_get(self):
        # セッション作成
        session = Session()
        kuzimaster_list = []
        for row in session.query(KuziMaster):
            kuzimaster_list.append({"id":row.id ,"name":row.name})
        # セッションクローズ
        session.close()
        return kuzimaster_list
    
    def result_get(self):
        # セッション作成
        session = Session()
        resutl_list = []
        for row in session.query(Result):
            resutl_list.append({"id":row.id ,"username":row.username,"kuziname":row.kuziname})
        # セッションクローズ
        session.close()
        return resutl_list
    
    def result_insert(self, **kwargs):
        # セッション作成
        session = Session()
        kuziname = kwargs.get('kuziname','')
        username = kwargs.get('username','')
        # キーがあるかチェック
        if kuziname == '':
            print('error: kuziname dose not found')
        elif username == '':
            print('error: username dose not found')
        else:
            #session.add_all([
            #        Result(kuziname=kuziname, username=username),
            #        ])
            session.add(Result(kuziname=kuziname, username=username))
            session.commit()
        # セッションクローズ
        session.flush()
        session.close()
        return None

#dao = DAO()
#for i in dao.usermaster_get():
#    print(i)
