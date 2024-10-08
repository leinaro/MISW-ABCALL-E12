from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class SecurityAnswerSchema(Schema):
    verification_id = fields.Str(required=True)
    answer = fields.Str(required=True)


class VerificationSchema(Schema):
    verification_id = fields.Str(dump_only=True)
    agent_id = fields.Str(required=True)
    security_question = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)


class AgentCreationSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))
    role = fields.Str(required=True, validate=validate.OneOf(["agent", "admin"]))
    identification = fields.Str(required=True)
    phone = fields.Str(required=True)
    address = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    zip_code = fields.Str(required=True)
    country = fields.Str(required=True)


class IncidentCreationSchema(Schema):
    agent_id = fields.Str(required=True)
    description = fields.Str(required=True, validate=validate.Length(min=1))
    date = fields.Date(required=True)


class AdminActionSchema(Schema):
    agent_id = fields.Str(required=True)