#!/usr/bin/python3
# -*- coding: utf-8 -*-


# DBエンジン指定のため
from sqlalchemy import create_engine
# ORMに必要なインポート
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import UniqueConstraint
# セッション作成に必要
from sqlalchemy.orm import sessionmaker




# DBをSQLITEのメモリに。SQLの表示を有効
engine = create_engine('sqlite:///:memory:', echo=True)
###################
# ORMを定義
###################
### マスターテーブル ###
# ユーザー一覧
Base = declarative_base()
class UserMaster(Base):
    __tablename__ = 'usermaster'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return "<Id='%s', Username='%s'>" % (self.id, self.name)

class Kuzi(Base):
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
    name = Column(String, unique=True)
    def __repr__(self):
        return "<Id='%s', Kuziname='%s'>" % (self.id, self.name)


# 定義した内容でDBを作成
Base.metadata.create_all(engine)

# テスト実行
# マッピングオブジェクト作成
user = UserMaster(id=1, name='test user name')
# セッション作成
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
# インサート
session.add(user)
session.commit()

# クエリ
for row in session.query(UserMaster):
    print(row.id, row.name)



