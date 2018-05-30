import pydocumentdb.document_client as document_client
import HttpContext.ActiveRequest



class documentDbConnectionDetails:
    documentdburi = ""
    documentdkey = ""
    dbname = ""
    collectionname = ""


# Gets a contextual db session which is being held under a HTTP context.
def GetDbSession() -> document_client.DocumentClient:
    """
    Gets an active session to the db
    """
    if not hasattr(HttpContext.ActiveRequest.GetCurrentContext(), "dbSession"):
        HttpContext.ActiveRequest.GetCurrentContext().dbSession = document_client.DocumentClient \
            (documentDbConnectionDetails.documentdburi, {'masterKey': documentDbConnectionDetails.documentdkey})

        return HttpContext.ActiveRequest.GetCurrentContext().dbSession

    else:
        return HttpContext.ActiveRequest.GetCurrentContext().dbSession


def GetDbSessionFake(k, y) ->list:
    """
    this is doing docs

    :param k:
    :type k: int
    :param y:
    :type y: document_client.DocumentClient
    :return: list of document_client.DocumentClient
    :rtype: tuple of (dict, dict)
    """
    return k + y
