#
# A very dirty written api libary for padlet.com
#

import requests
from requests.structures import CaseInsensitiveDict
import time
import random
from selenium import webdriver
import string


def get_info(id):
    answer = requests.get(api_url_wishes + '/' + str(id)).json()
    return answer['data']['attributes']


class Padlet():

    chars = string.ascii_letters

    api_url_reactions = "https://padlet.com/api/5/reactions"
    api_url_comments = "https://padlet.com/api/5/comments"
    api_url_wishes = "https://padlet.com/api/5/wishes"

    padlet_url = "Enter URL here"
    ids = []

    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print('[INFO] Chrome-Driver is starting...')
    driver = webdriver.Chrome()

    print('[INFO] Chrome-Driver is navigating to ' + padlet_url+'...')
    driver.get(padlet_url)

    time.sleep(7.5)

    def get_info(id):
        answer = requests.get(api_url_wishes + '/'+str(id)).json()
        return answer['data']['attributes']

    def rate_post(self, id, stars, method='grade'):
        global api_url_reactions
        global chars

        randStr = ''.join(random.choice(chars) for _ in range(20))

        headers = CaseInsensitiveDict()
        headers["Host"] = "padlet.com"
        headers["Connection"] = "close"
        headers["Content-Length"] = "55"
        headers["sec-ch-ua"] = "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\""
        headers["Authorization"] = "Bearer 8511fef0b505facb23032079340b9e7ce0eba665fe7caaf7d0bcdc3c9f9b3cf4"
        headers["X-CSRF-Token"] = "NAQljysgljUhx4p80rrf01fmihHeYJDQtYr8Kd2bKGZpV6MurX++sFZ4tn3uWmQVK58rT1otlGHucFVtbYcTHB=="
        headers["sec-ch-ua-mobile"] = "?0"
        headers["X-UID"] = "161581338102908370354226330361"
        headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "*/*"
        headers["Origin"] = "https://padlet.com"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Sec-Fetch-Mode"] = "same-origin"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Referer"] = "https://padlet.com/AntjeKunze/client"
        headers["Accept-Encoding"] = "gzip, deflate"
        headers["Accept-Language"] = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
        headers[
            "Cookie"] = "__cfduid=ddea24a15193c41fe5d15a9d1edc933221615813135; ww_d=83df2504ebf7256a7dc00970cb75c49c; ww_s=bf927f2dc510746909d4060e0cdab6e7; ww_dpr=1; ww_tz=Europe/Berlin; __asc=f38c528017835f7d3ddf08fbc55; __auc=f38c528017835f7d3ddf08fbc55; _ga=GA1.1.1600942286.1615813137; __cf_bm=7554e10708939d6c4d62b0b4a7471a4d276e1db8-1615813137-1800-AcB1YtCp6Gg2qXGLES38g3AwWBsgKR7wUyg/BsETovYszde/jIzT2MZr56j1s1gPSloH4Ma+1vQ/kbdN3XTL6uOXPOvQ1e3tq/rlBq07Zg35TrqhlZUVUlgkI2wHgE8PHQDzMdOYt3qvq2DtFHDdORmARwRabab3SPYw8MJFoeg3azPYbGUh85+Ki/zj89WbVeiga3ZHNrmxJfAbnpmdaK0=; Indicative_e42b4377-7049-4dec-9c6c-2b2ae32d79d4=\"%7B%22defaultUniqueID%22%3A%22758d2da9-0d23-441e-fc74-4425b2633add%22%2C%22uniqueID%22%3A%221081236182%22%2C%22lastSessionTime%22%3A1615813381299%7D\"; ww_p=WkJjVHMrNDB5UmlRbG9ybzhHdFNHQUZSZl" + randStr + "hkUHhPcTlxdlYvbFVPRHZlSlkwakFpTlNDZkxad05XSWU0NEl5dTNiOG40cC9CTHYxUUx3RklOdTdRQXIySVVzYkFoTG1hajFEQUNGeldTWVJzbk1QNTlaWFRXTmhYMEl3cDUxSExVeVJUWUtLdnNrZisxNktqS05zZmVZa1ZacUxZNkhrMm1TMHprYWtwSG13ZUtDVklSU0kxZDYrYTBpTXl6ejB0bXo4ZHZyQT09LS1OWnZzcTRjdHZ2MjdMbmxHVmdkdnRRPT0%3D--563cbd1b534993ebdbabfee10f38544eff67fcb5; _ga_4M6WGE55N0=GS1.1.1615813137.1.1.1615813382.0"

        data = '{"wish_id":' + str(id) + ',"value":' + \
            str(stars) + ',"reaction_type":"'+method+'"}'

        print('[INFO] Post ' + str(id) +
              ' was rated with value' + str(stars)+'.')

        return requests.post(api_url_reactions, headers=headers, data=data)

    def post_wish(self, title, content, x=50, y=50):
        global api_url_wishes

        randStr = ''.join(random.choice(chars) for _ in range(20))

        headers = CaseInsensitiveDict()
        headers["Host"] = "padlet.com"
        headers["Connection"] = "close"
        headers["Content-Length"] = "317"
        headers["sec-ch-ua"] = '"Chromium";v="89", ";Not A Brand";v="99"'
        headers["Authorization"] = "Bearer cbcd96435ed02078938e43108a42a640ffb6f99f3d0f74faaa6037c3f9bdb6f4"
        headers["X-CSRF-Token"] = "WVFRTYp5yk5lw0t+quGlaTKDkZwv5fMjTV8ozXw/gjzmPWKRNYo/dwHornY5XUx/1b2Kakj0GKLtK/+oXr3kTg=="
        headers["sec-ch-ua-mobile"] = "?0"
        headers["X-UID"] = "161606373031606196865715243463"
        headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "*/*"
        headers["Origin"] = "https://padlet.com"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Sec-Fetch-Mode"] = "same-origin"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Referer"] = "https://padlet.com/slenz8/client"
        headers["Accept-Encoding"] = "gzip, deflate"
        headers["Accept-Language"] = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
        headers[
            "Cookie"] = '__cfduid=ddf4ca9963cf1c37ab1a15da42c2568891616063730; ww_d=a14a649cdbe6ba6c918de1e71c71b3d7; ww_s=228543bacfe96539a6eaad836ce810a7; ww_dpr=1; ww_tz=Europe/Berlin; __asc=37d6de4e17844e796ccb319d812; __auc=37d6de4e17844e796ccb319d812; Indicative_e42b4377-7049-4dec-9c6c-2b2ae32d79d4="%7B%22defaultUniqueID%22%3A%22f3f808c0-11c5-420f-8057-75134ae43906%22%2C%22uniqueID%22%3A%221088618840%22%2C%22lastSessionTime%22%3A1616063731420%7D"; _ga=GA1.1.1533821134.1616063732; __cf_bm=93320c358a4df6f38d3d7097437bc75932277610-1616063732-1800-ARn2cssPl2WyQraztJxJT9lpUShv5jbOegbeoV48I8I+3uJNNoCMxZSwjU0K32+3wWOw7zs4BkBiEBppLGSNfEMsBX7dFyHGL+Cz/6zKALkcz9TXNca3abvrsYtdjQWlKWLAfGc2BjjIoja4gAFMUMyJggriHdaezGPpluXU/KSlfn3eb8uT3jtpsyL7cCR6kGjvFEixzVy+jh8sW12Kd6o=; ww_p=RUFTenBDdS9RZmQzdDVVdWRHe' + randStr + 'U5CazhHYnNYajI5V1EvQmoydXRFN09mYXdpV3BYWEt1cXRpWTN4RG9WSzJZZnp0NHRnWVY0cyttY1FKNjltTkJZT0JHQk5JWDFOSk80Y1V5SkVyOHh4K1BnaFpOZ1FFZ3FlczF4TnJmbS92bEx0T0FCczh1eW9sQTAvemNEV04yVFJpMkNNNG1GbDd4VExJOEhXSzNNTXBTVTNncUJZbVJpOU1KaXJITFMrVjU0Y0RmN3AzZz09LS1Yeksyc2d5Nm5rR2VpbE1kNzRNSk93PT0%3D--df4b953972f99465cc287fa9e0d11e2201174250; _ga_4M6WGE55N0=GS1.1.1616063732.1.1.1616063765.0'

        data = '{"cid":"c_new1","wall_id":113406895,"published":true,"author_id":1088618840,"width":200,"body":"<div>' + str(content) + '</div>","subject":"' + str(title) + '","attachment":"","sort_index":265967801344,"created_at":"2021-03-18T10:36:05.141Z","updated_at":"2021-03-18T10:36:05.141Z","top":' + str(
            y) + ',"left":' + str(x) + '}'

        print('[INFO] Post was posted at ('+str(x)+'/'+str(y)+').')
        return requests.post(api_url_wishes, headers=headers, data=data)

    def delete_post(self, id):
        randStr = ''.join(random.choice(chars) for _ in range(20))
        headers = CaseInsensitiveDict()
        headers["Host"] = "padlet.com"
        headers["Connection"] = "close"
        headers["sec-ch-ua"] = '"Chromium";v="89", ";Not A Brand";v="99"'
        headers["Authorization"] = "Bearer 051c543ec8c9ae2c86ee2f7f79961c5d09102fb683042986eddc8beb9bc304b6"
        headers["X-CSRF-Token"] = "0dYojEGeO7NkDP8iNASOSCilBDV8WP8oMUP6CJJVH9qz4zAJR52MRj2yPOXrYQCmZlK25BEIVFpB9XueOw/o5A=="
        headers["sec-ch-ua-mobile"] = "?0"
        headers["X-UID"] = "161607495684509381234190442345"
        headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        headers["Content-Type"] = "application/json; charset=utf-8"
        headers["Accept"] = "*/*"
        headers["Origin"] = "https://padlet.com"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Sec-Fetch-Mode"] = "same-origin"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Referer"] = "https://padlet.com/slenz8/client"
        headers["Accept-Encoding"] = "gzip, deflate"
        headers["Accept-Language"] = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
        headers[
            "Cookie"] = '__cfduid=d9554fd659985b04d1c5989d42052e47c1616074956; ww_d=37770f35ff72406d20059baa430ac94f; ' \
                        'ww_s=910348645d7759c223c25c13d152184b; ww_dpr=1; __asc=f621302e1784592e4dbb205eb5b; ' \
                        '__auc=f621302e1784592e4dbb205eb5b; ' \
                        'Indicative_e42b4377-7049-4dec-9c6c-2b2ae32d79d4="%7B%22defaultUniqueID%22%3A%221ee02dfe-57d6' \
                        '-4922-e610-e86de382aadc%22%2C%22uniqueID%22%3A%221089048143%22%2C%22lastSessionTime%22' \
                        '%3A1616074958146%7D"; _ga=GA1.1.246457546.1616074958; ww_tz=Europe/Berlin; ' \
                        '__cf_bm=4f9970dadd6387430708c933e4a33b090fbe9cde-1616074960-1800-AZ3gntahlrPCeFdDL/ElY0wJ7m' \
                        '/MWPPM61F2k5WERXOULBV4ZfKoWeAjjOvi46vAxe2RjOCoEurMUn3U4drisDY8EjYbihRddzki8y90wb8jOr8kAKBZAZd2rAmvSI5n7Fa5okPlBEq5G2FROIxajeefQ/hiLYzNumy/etTYSgem5NF2swhRsp/UJtfA69pnN7V5/Fo43bammp1Qv4ZNvwM=; ww_p=MHU3RFIya2tIL3NpSFp6a0tYdmw5L2dpdUl4Z1' + \
            str(randStr)+'UY1cE9ML2E3SkhYbm1MbCtlaTFlNVAwc1MwSUxuMDNvaDdzUVljUzRYelczTzdXamhRcUZhbkJreGN1anJqNzhvVSt6dXVqcTVXcFd2ZllQYUFBbDV5bXo3ekkwT0FVWEFOQmpEcXRtVEpacnhOYTNYYmZOSjUzZnAxNjRvaFlBK3labDRTUjNWb0ZtSjcvMFUxOXdKcmNXWUZUNnJWTjhJVzFrNXNyRmVMUT09LS1rdm13UUtBZlFlZVRBWDkzQkc5bEpRPT0%3D--581f9c0d6e0a441644b1cd96159c91a99abb0dfd; _ga_4M6WGE55N0=GS1.1.1616074958.1.1.1616075003.0 '

        print('[INFO] Post ' + str(id) + ' was deleted.')
        return requests.delete(api_url_wishes + '/' + str(id), headers=headers)

    def post_comment(self, id, author, comment):
        randStr = ''.join(random.choice(chars) for _ in range(20))
        randId = ''.join(random.choice('0123456789') for _ in range(13))
        url = "https://padlet.com/api/5/comments"

        headers = CaseInsensitiveDict()
        headers["Host"] = "padlet.com"
        headers["Connection"] = "close"
        headers["Content-Length"] = "598"
        headers["sec-ch-ua"] = "\";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\""
        headers["Authorization"] = "Bearer 1bdd2e948f7e0c500bbd2c7f7db0b1048749a2db076cdfdd5323d48a98ebe186"
        headers["X-CSRF-Token"] = "eGuvVgZbS2sRpRt+QdXpJtvP6nkOQdq9seMXFRXn0ePumfuPWusTWsLXtoOoXyF3fyjquVFSIeww3AY89dHG2A=="
        headers["sec-ch-ua-mobile"] = "?0"
        headers["X-UID"] = "1615855728250013045040648918071"
        headers[
            "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "*/*"
        headers["Origin"] = "https://padlet.com"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Sec-Fetch-Mode"] = "same-origin"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Referer"] = "https://padlet.com/AntjeKunze/client"
        headers["Accept-Encoding"] = "gzip, deflate"
        headers["Accept-Language"] = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
        headers["Cookie"] = '__cfduid=d013b0a9f1cdde62955f96dc82c3799e41615855727; ww_d=41560e629f28d3bfdd6f7f771f31fe77; ' \
                            'ww_s=4f27d440a53d8c72120584d472adad1e; ww_dpr=1; ww_tz=Europe/Berlin; ' \
                            '__asc=1485afbe1783881baadb955504a; __auc=1485afbe1783881baadb955504a; ' \
                            'Indicative_e42b4377-7049-4dec-9c6c-2b2ae32d79d4="%7B%22defaultUniqueID%22%3A%22e007c852-9417' \
                            '-4ada-e5e7-5cd678cbe497%22%2C%22uniqueID%22%3A%221082728005%22%2C%22lastSessionTime%22' \
                            '%3A1615855729335%7D"; _ga=GA1.1.582660526.1615855730; ' \
                            '__cf_bm=88b056b3609c6eafba791a2dc82097b830a82cc1-1615855730-1800' \
                            '-AasYleNntbjh8MCHmmVH7JpadsA5YHR/sP+kxpWkcWjvfbpLzLe3Owp+yuVHNA5i1plepYmUOPoI14EVHuIl' \
                            '/hz2EB6e7bROCfjXtgoAsXhCc1tNL5sv8LuUkL5I/F5FjtfRLmI4k2X4npsGNgSEzsfu6mY984s24fSdJIWgoxKN' \
                            '+O6PKPq0dtp62REdwK1Ys4LPQ8o42jcBbe5HEgicI5I=; ' \
                            'ww_p=RWQwMzRHZktRY3dpTWZIVEViSnF5SnFIV2lyZmJn' + randStr + 'RHFKcmVNTlBRLytNc0JYcFdJYWpTdTBka2NRWGQ3ZTVUdDEyaDFiemFqalNObmJJa3d3OXVvQkJjaG5IeDNBN1dJM0lWbHk0a3Budk9xYWZPVUZDQjlMcUxkSUxycTZ6RjFaai9KYUU5YWpzeC91eDVEa2tpeFFkdHpDZXc2WW5nbi93VG1YeWRtK2dOSVZVcUxjZmlwQUJkck5hWjQ4R01NcUpHdzRzUT09LS1aMnJCa1NjUEE2cWZ3QjhZb1pyRDRBPT0%3D--3e63d667564262635684248254a76e7a8119f296; _ga_4M6WGE55N0=GS1.1.1615855729.1.0.1615855731.0 '

        data = '{"id":"new_' + randId + '","wish_id":' + str(
            id) + ',"body":"' + comment + '","user":{"id":1082728006,"name":"","short_name":"' + author + '","username":null,"identities":null,"avatar":"https://padlet.net/avatars/alien1.png","lang":"de","status":null,"role":null,"email":null,"is_teacher":null,"bio":null,"tenant_id":1,"created_at":"2021-03-16T00:48:47.699Z","updated_at":"2021-03-16T00:48:47.699Z","registered_at":null,"paying":false,"quota":{"walls_used":0,"walls_limit":0,"can_make":false,"advertized_max_upload_megabytes":25,"max_upload_megabytes":30},"tenant_type":"native"},"user_id":1082728005}'

        print('[INFO] Post ' + str(id) + ' was commented.')
        return requests.post(url, headers=headers, data=data)

    def move_post(self, id, x_cord, y_cord):

        randStr = ''.join(random.choice(chars) for _ in range(20))

        headers = CaseInsensitiveDict()
        headers["Host"] = "padlet.com"
        headers["Connection"] = "close"
        headers["Content-Length"] = "696"
        headers["sec-ch-ua"] = '"Chromium";v="89", ";Not A Brand";v="99"'
        headers["Authorization"] = "Bearer 051c543ec8c9ae2c86ee2f7f79961c5d09102fb683042986eddc8beb9bc304b6"
        headers["X-CSRF-Token"] = "0dYojEGeO7NkDP8iNASOSCilBDV8WP8oMUP6CJJVH9qz4zAJR52MRj2yPOXrYQCmZlK25BEIVFpB9XueOw/o5A=="
        headers["sec-ch-ua-mobile"] = "?0"
        headers["X-UID"] = "161607495684509381234190442345"
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "*/*"
        headers["Origin"] = "https://padlet.com"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Sec-Fetch-Mode"] = "same-origin"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Referer"] = "https://padlet.com/slenz8/client"
        headers["Accept-Encoding"] = "gzip, deflate"
        headers["Accept-Language"] = "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"
        headers["Cookie"] = '__cfduid=d9554fd659985b04d1c5989d42052e47c1616074956; ww_d=37770f35ff72406d20059baa430ac94f; ww_s=910348645d7759c223c25c13d152184b; ww_dpr=1; __asc=f621302e1784592e4dbb205eb5b; __auc=f621302e1784592e4dbb205eb5b; Indicative_e42b4377-7049-4dec-9c6c-2b2ae32d79d4="%7B%22defaultUniqueID%22%3A%221ee02dfe-57d6-4922-e610-e86de382aadc%22%2C%22uniqueID%22%3A%221089048143%22%2C%22lastSessionTime%22%3A1616074958146%7D"; _ga=GA1.1.246457546.1616074958; ww_tz=Europe/Berlin; __cf_bm=4f9970dadd6387430708c933e4a33b090fbe9cde-1616074960-1800-AZ3gntahlrPCeFdDL/ElY0wJ7m/MWPPM61F2k5WERXOULBV4ZfKoWeAjjOvi46vAxe2RjOCoEurMUn3U4drisDY8EjYbihRddzki8y90wb8jOr8kAKBZAZd2rAmvSI5n7Fa5okPlBEq5G2FROIxajeefQ/hiLYzNumy/etTYSgem5NF2swhRsp/UJtfA69pnN7V5/Fo43bammp1Qv4ZNvwM=; _ga_4M6WGE55N0=GS1.1.1616074958.1.1.1616075003.0; ww_p=VHJsOXZnV0dRMVdNaG10VEZTSVd0' + \
            randStr+'d3NWYndTb1hqNVpDbDFuVnVYUDA0bnVhRkt3ZjhTZ3VGZ3d5RWcyZmNzTHZ4cHFlRFNLeHg1ZkQwT0hqQU96dDVoT1RzbnRUQ20xMmFpeE9JcWwxemdFSUh5NFBoTW8ycGNmb0tTYkNhYUVaejA5YTAzSmlyNDRWSFlFMHF6b2Z1WENpclVldEwyS0dPN01UTUtEQ1k5Y2U2VkFuSlZoa2ZmR2RvMVhmaWZLQzBLckErQT09LS0zMnRrVEVUQTRhb1VhQmo4Q3RRMnZnPT0%3D--6e3d4726539ba1a48b43b3f9370f73f0bbe12052'

        resp = get_info(1320069022)
        resp['top'] = x_cord
        resp['left'] = x_cord
        resp = str(resp).replace(': ', ':').replace(', ', ',').replace(
            'True', 'true').replace('False', 'false').replace('None', 'null').replace("'", '"')

        print('[INFO] Moved post to ('+str(x_cord)+'/'+str(y_cord)+').')
        return requests.put(api_url_wishes + '/' + str(id), headers=headers, data=str(resp))

    def get_rating(self, id):
        return \
            float(driver.find_element_by_xpath(
                '//*[@id="wish-' + str(id) + '"]/div/div[1]/section/div[1]/div/div').get_attribute(
                "title").split(" ")[2])

    def get_rating_amount(self, id):
        global driver

        return int(
            driver.find_element_by_xpath('//*[@id="wish-' + str(id) + '"]/div/div[1]/section/div[1]/div/div/span[2]').text)

        # //*[@id="wish-1307481739"]/div/div[1]/section/div[1]/div/div/span[2]

    def get_all_ids(self):
        global ids
        for wish in driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div[2]/div"):
            ids.append(int(str(wish.get_attribute("id")).split("-")[1]))
        return ids

    def number_to_id(self, number):
        global ids

        return ids[number - 1]
