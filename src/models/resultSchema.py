from marshmallow import Schema, fields


class ResultSchema(Schema):
    id = fields.Int()
    download = fields.Float()
    upload = fields.Float()
    ping = fields.Float()
    timestamp = fields.DateTime()
