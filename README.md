# insteonstatus

Convert Insteon Hub status into JSON

This code snippet was used as part of a suite and is not intended to be used standalone.

# Basic Usage

```
# clear buffer
curl -s -u ${USER}:${PASS} -X POST http://${HOST}:${PORT}/sx.xml?${DEVICE}=1900 2>&1 > /dev/null
sleep 1

# send status
URL=http://${HOST}:${PORT}/3?0262${DEVICE}0F1900=I=3
curl -s -u ${USER}:${PASS} -X POST ${URL} 2>/dev/null
sleep 1

# read buffer
curl -s -u ${USER}:${PASS} -X POST http://${HOST}:${PORT}/buffstatus.xml 2>/dev/null | ./status.py
```
