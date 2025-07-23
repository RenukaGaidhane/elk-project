import logging
import logstash
import time

host = 'localhost'
port = 5002

logger = logging.getLogger('python-logstash')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler(host, port, version=1))

# Simulate log entries
for i in range(5):
    logger.info('Python app log - login success', extra={
        'user': 'renuka',
        'port': 41658 + i,
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S'),
        'level': 'INFO'
    })
    time.sleep(1)
