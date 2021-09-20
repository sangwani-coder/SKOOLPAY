# Collection request to pay POST 

from re import X


subscription_key = '47d15957a260416889b69c6b882c87c4'
x_reference_id = ''


'''request payment from a consumer (payer)'''
def request_to_pay(amount, partyid):
    import requests
    import json

    url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"

    payload = json.dumps({
    "amount": amount,
    "currency": "EUR",
    "externalId": "012356",
    "payer": {
    "partyIdType": "MSISDN",
    "partyId": partyid
    },
    "payerMessage": "pay for school",
    "payeeNote": "payer note"
    })
    headers = {
        'X-Reference-Id': x_reference_id,
        'Ocp-Apim-Subscription-Key': subscription_key,
        'X-Target-Environment': 'sandbox',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjZmN2FlMzQ0LTJkY2EtNGU3Zi05ZDAxLTM1YzhlNTNhNDJkYiIsImV4cGlyZXMiOiIyMDIxLTA5LTIwVDEwOjE1OjM5LjM4MiIsInNlc3Npb25JZCI6IjU5OWMyOWRjLWEzZGUtNDM2OC05OGEzLTA2YWY2M2RjOTQ4OCJ9.H3x8sAb13C8Hsvqb1ay4dGA2TzINS1HD7Jid_DUWgfVkCHmSsnoFo7mhxMQjHzShwb2G8PegzOi_-Be_jI3PjElvIJ4ww_HBJQVLN2CWSXdq-rCBAaRqKBnVWj2ZSjx9abisdhc7VoAE-0em85mYXUTWlmf5iT1geKH9lQHI45sClnM-3PWVtxui_dSclghjqrhnczOujafI_yZS3uPOyuqRttw6yRnhjbQWPQjpTBGsQzLIDuCTWEhtLNAqYswkXBNF3W09YZ3l9zVAT67QPK_D16lGNFHimVKfX_F5h9hbsVTkGvhaEkx4z2uxTiEjWhYX8xRaau1iy_YQPSm5pw',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, timeout=60)

    status = response.status_code

    return status

# Get X-reference-Id
def get_uuid():
    import requests
    global x_reference_id

    url = "https://www.uuidgenerator.net/api/version4"

    payload={}
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjZmN2FlMzQ0LTJkY2EtNGU3Zi05ZDAxLTM1YzhlNTNhNDJkYiIsImV4cGlyZXMiOiIyMDIxLTA5LTIwVDEwOjE1OjM5LjM4MiIsInNlc3Npb25JZCI6IjU5OWMyOWRjLWEzZGUtNDM2OC05OGEzLTA2YWY2M2RjOTQ4OCJ9.H3x8sAb13C8Hsvqb1ay4dGA2TzINS1HD7Jid_DUWgfVkCHmSsnoFo7mhxMQjHzShwb2G8PegzOi_-Be_jI3PjElvIJ4ww_HBJQVLN2CWSXdq-rCBAaRqKBnVWj2ZSjx9abisdhc7VoAE-0em85mYXUTWlmf5iT1geKH9lQHI45sClnM-3PWVtxui_dSclghjqrhnczOujafI_yZS3uPOyuqRttw6yRnhjbQWPQjpTBGsQzLIDuCTWEhtLNAqYswkXBNF3W09YZ3l9zVAT67QPK_D16lGNFHimVKfX_F5h9hbsVTkGvhaEkx4z2uxTiEjWhYX8xRaau1iy_YQPSm5pw'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=60)

    x_reference_id = response.text

def get_transaction_status():
    import requests
    url = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay/{x_reference_id}".format(x_reference_id=x_reference_id)
    payload={}
    headers = {
        'X-Target-Environment': 'sandbox',
        'Ocp-Apim-Subscription-Key':  subscription_key,
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjZmN2FlMzQ0LTJkY2EtNGU3Zi05ZDAxLTM1YzhlNTNhNDJkYiIsImV4cGlyZXMiOiIyMDIxLTA5LTIwVDEwOjE1OjM5LjM4MiIsInNlc3Npb25JZCI6IjU5OWMyOWRjLWEzZGUtNDM2OC05OGEzLTA2YWY2M2RjOTQ4OCJ9.H3x8sAb13C8Hsvqb1ay4dGA2TzINS1HD7Jid_DUWgfVkCHmSsnoFo7mhxMQjHzShwb2G8PegzOi_-Be_jI3PjElvIJ4ww_HBJQVLN2CWSXdq-rCBAaRqKBnVWj2ZSjx9abisdhc7VoAE-0em85mYXUTWlmf5iT1geKH9lQHI45sClnM-3PWVtxui_dSclghjqrhnczOujafI_yZS3uPOyuqRttw6yRnhjbQWPQjpTBGsQzLIDuCTWEhtLNAqYswkXBNF3W09YZ3l9zVAT67QPK_D16lGNFHimVKfX_F5h9hbsVTkGvhaEkx4z2uxTiEjWhYX8xRaau1iy_YQPSm5pw'
    }

    response = requests.request("GET", url, headers=headers, data=payload, timeout=60)

    status = response.status_code
    print("transaction status:", response.text)
    return status

# get_uuid()
# request_to_pay()
# get_transaction_status()