import requests

headers = {
    'Authorization': 'Bearer FPO6ZW3QKJIOC6BCO4KXT5EQCTZTX4UF',
}

requests.get('https://api.wit.ai/message?v=20160412&q=show%20me%20the%20departures%20board%20for%20victoria', headers=headers)