# Collection request to pay POST 

subscription_key = '47d15957a260416889b69c6b882c87c4'
x_reference_id = ''

def request_to_pay():
    import requests
    import json

    url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"

    payload = json.dumps({
    "amount": "90",
    "currency": "EUR",
    "externalId": "012356",
    "payer": {
    "partyIdType": "MSISDN",
    "partyId": "0969620939"
    },
    "payerMessage": "pay for school",
    "payeeNote": "payer note"
    })
    headers = {
        'X-Reference-Id': x_reference_id,
        'Ocp-Apim-Subscription-Key': subscription_key,
        'X-Target-Environment': 'sandbox',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjZmN2FlMzQ0LTJkY2EtNGU3Zi05ZDAxLTM1YzhlNTNhNDJkYiIsImV4cGlyZXMiOiIyMDIxLTA5LTE0VDE1OjU4OjMxLjIxOSIsInNlc3Npb25JZCI6IjI0ZTc0NDg2LTlmZjEtNDcyNS05YzUxLTI2MzU3Njg2ZWI1NSJ9.CsH4Lu9ko2WbxlWOGO5giTilZ22lDd0K8Mck0v2JVd1WkdYC7Kc0f43jObMvjX96Gg1x7zcGHPM80AemlUthizmAqdkcmZvOq7L6iKJO8HRZiMSDaJptuelE2funFbog5UT3M1K9kQqJNhbSzhCIKozt4iHWgw1JPdz4AmNIH6bwq3muvZ63iX20TkhUrN-dJK5vIu24wTLxRgTJaTDlheNn0MGs5fY7ykz-STOY2wKSvsVDSp0jOWH7aglj5ZTt3ACaGC3lVhS6KgDI9_dHhdqDl_WXHuZVFJXuPeIvXwZYnX6zaT8nlXg7SFBp_yn32JChLCZJdqjnAgKXFEfW8A',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, timeout=60)

    print("Request to pay:",response.text)


# Get X-reference-Id
def get_uuid():
    import requests
    global x_reference_id

    url = "https://www.uuidgenerator.net/api/version4"

    payload={}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjZmN2FlMzQ0LTJkY2EtNGU3Zi05ZDAxLTM1YzhlNTNhNDJkYiIsImV4cGlyZXMiOiIyMDIxLTA5LTE0VDE1OjU4OjMxLjIxOSIsInNlc3Npb25JZCI6IjI0ZTc0NDg2LTlmZjEtNDcyNS05YzUxLTI2MzU3Njg2ZWI1NSJ9.CsH4Lu9ko2WbxlWOGO5giTilZ22lDd0K8Mck0v2JVd1WkdYC7Kc0f43jObMvjX96Gg1x7zcGHPM80AemlUthizmAqdkcmZvOq7L6iKJO8HRZiMSDaJptuelE2funFbog5UT3M1K9kQqJNhbSzhCIKozt4iHWgw1JPdz4AmNIH6bwq3muvZ63iX20TkhUrN-dJK5vIu24wTLxRgTJaTDlheNn0MGs5fY7ykz-STOY2wKSvsVDSp0jOWH7aglj5ZTt3ACaGC3lVhS6KgDI9_dHhdqDl_WXHuZVFJXuPeIvXwZYnX6zaT8nlXg7SFBp_yn32JChLCZJdqjnAgKXFEfW8A'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=60)

    x_reference_id = response.text
    print("X-reference-ID:",response.text)

get_uuid()
request_to_pay()