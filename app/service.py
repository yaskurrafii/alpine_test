"""
service.py

All of the function that we need to call in main.py should put it in here
"""

from .model import Payload


def changing_payload(list_1, list_2):
    """
    list_1 : list
    list_2 : list

    flow :
    1. Make all of the sentence or string inside list must be in upper letter
    2. pairing all of the thing inside list by the index of every list
    3. Put it together of pairing result using join() function
    """
    changed_1 = [x.upper() for x in list_1]
    changed_2 = [x.upper() for x in list_2]
    pairing = [val for pair in zip(changed_1, changed_2) for val in pair]
    return ",".join(pairing)


def extract(session, data):
    """
    extracting payload and checking if the data exist or not
    if the data exist it will return the data that has an output column in it
    if not it will make an expected output value to put it into output column
    and create data to database

    session : DB Session
    data : payload of request
    """
    cache_payload = (
        session.query(Payload)
        .filter(Payload.list_1 == str(data.list_1), Payload.list_2 == str(data.list_2))
        .first()
    )

    if cache_payload:
        return cache_payload

    output = changing_payload(data.list_1, data.list_2)

    new_data = Payload(list_1=str(data.list_1), list_2=str(data.list_2), output=output)
    session.add(new_data)
    session.commit()
    session.refresh(new_data)

    return new_data
