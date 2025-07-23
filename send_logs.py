import logstash
import logging
import socket

host = 'localhost'

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.TCPLogstashHandler(host, 5002, version=1))

test_logger.info('This is a Python log test message', extra={
    'user': 'renuka',
    'port': 41568,
    'level': 'INFO',
    'timestamp': 'Jul 23, 2025 14:45:00'
})
