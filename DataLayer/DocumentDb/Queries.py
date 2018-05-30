import DataLayer.DocumentDb.DocumentDbContextualHttpConnectionManager
import flask.globals
import HttpContext.ActiveRequest

def GetConfigDocument():
    session = DataLayer.DocumentDb.DocumentDbContextualHttpConnectionManager.GetDbSession()
    db_id = 'CETest'
    db_query = "select * from r where r.id = '{0}'".format(db_id)
    db = list(session.QueryDatabases(db_query))[0]
    db_link = db['_self']
    coll_id = 'Config'
    coll_query = "select * from r where r.id = '{0}'".format(coll_id)
    coll = list(session.QueryCollections(db_link, coll_query))[0]
    coll_link = coll['_self']
    docs = session.ReadDocuments(coll_link)
    DataLayer.DocumentDb.DocumentDbContextualHttpConnectionManager.GetDbSessionFake()
    w = HttpContext.ActiveRequest.GetCurrentContext().etag
    return list(docs)


def get_alert():
    session = DataLayer.DocumentDb.DocumentDbContextualHttpConnectionManager.GetDbSession()
    db_id = 'Alerts'
    db_query = "select * from r where r.id = '{0}'".format(db_id)
    db = list(session.QueryDatabases(db_query))[0]
    db_link = db['_self']
    coll_id = 'Entries'
    coll_query = "select * from r where r.id = '{0}'".format(coll_id)
    coll = list(session.QueryCollections(db_link, coll_query))[0]
    coll_link = coll['_self']
    docs = session.ReadDocuments(coll_link)
    return list(docs)
