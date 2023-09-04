from pymongo import MongoClient


def getDbHandle(db_name:str, host:str, port:int = 27107, username:str|None =None, password:str|None=None)->tuple(dict, MongoClient):
    """
    get a handle to a mongo database with the given name and credentials

    Args:
        db_name (str): database name
        host (str): host name or ip address
        port (int): port number
        username (str | None, optional):  username.  Defaults to None.
        password (str | None, optional): password. Defaults to None.

    Returns:
        _type_: _description_
    """    

    
    
    params = { 'host': host, 'port': int(port), 'username': username, 'password': password }
    # drop the params that are None
    params = { k: v for k, v in params.items() if v is not None }



    client = MongoClient(**params)
    db_handle = client[db_name]
    return db_handle, client
