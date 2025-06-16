from jsonschema import validate


{
  "type": "object",
  "required": ["token", "expires", "status", "result"],
  "properties": {
    "token": {
      "type": "string"
    },
    "expires": {
      "type": "string",
      "format": "date-time"
    },
    "status": {
      "type": "string",
      "enum": ["Success"]
    },
    "result": {
      "type": "string"
    }
  }
}


{
  "type": "object",
  "required": ["code", "message"],
  "properties": {
    "code": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  }
}