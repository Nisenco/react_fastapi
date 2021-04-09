def make_response(status=200, message=u"成功", **kwargs):
    data = {"status": status, "msg": message, 'data': ''}
    data.update(kwargs)
    return data
