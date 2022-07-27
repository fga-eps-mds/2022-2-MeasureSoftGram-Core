from marshmallow import Schema, fields


class MeasureSchema(Schema):
    """
    {
        "key": "passed_tests",
        "parameters": {
            "tests": 10,
            "test_errors": 3,
            "test_failures": 1
        }
    }
    """
    key = fields.Str(required=True)
    parameters = fields.Dict(required=True)


class CalculateMeasureSchema(Schema):
    """
    {
        "measures": [
            {
                "key": "passed_tests",
                "parameters": {
                    "tests": 10,
                    "test_errors": 3,
                    "test_failures": 1
                }
            },
            {
                "key": "test_builds",
                "parameters": {
                    "param1": 8,
                    "param2": 19,
                    "parma3": 4
                }
            }
        ]
    }
    """
    measures = fields.List(fields.Nested(MeasureSchema), required=True)


class PassedTestsSchema(Schema):
    tests = fields.Float(required=True)
    test_errors = fields.Float(required=True)
    test_failures = fields.Float(required=True)


class TestBuildsSchema(Schema):
    test_execution_time = fields.Float(required=True)


class TestCoverageSchema(Schema):
    coverage = fields.Float(required=True)


class NonComplexFileDensitySchema(Schema):
    complexity = fields.Float(required=True)
    functions = fields.Float(required=True)


class CommentedFileDensitySchema(Schema):
    comment_lines_density = fields.Float(required=True)


class DuplicationAbsenceSchema(Schema):
    duplicated_lines_density = fields.Float(required=True)