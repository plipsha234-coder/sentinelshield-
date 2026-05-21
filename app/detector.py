from config import SQLI_PATTERNS, XSS_PATTERNS

def detect_attack(playload):

for pattern in SQLI_PATTERNS:
if pattern.lower() in payload.lower():
return {
"status": "blocked",
"attack": "SQL injection"
}

for pattern in XSS_PATTERNS:
if pattern.lower() in payload.lower():
return {
"status": "blocked",
"attack": "XSS"
}

return {
"status": "allowed",
"attack": None
}