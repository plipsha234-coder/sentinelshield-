RATE_LIMIT = 20
BLOCK_TIME = 60

SQLI_PATTERNS = [
"UNION SELECT",
"'OR'1'='1",
"__",
"DROP TABLE"
]

XSS_PATTERNS= [
"<script>",
"<javascript>",
"onerror="
]