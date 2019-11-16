# -*- coding: utf-8 -*-
# @Author: Halloweenwx
# @Date:   2019-11-14 20:03:45
# @Last Modified by:   Halloweenwx
# @Last Modified time: 2019-11-14 20:06:49
import requests

cookies = {
    'dotmatics.elementalKey': 'SLsLWlMhrHnTjDerSrlG',
    'CUSTOMER': 'Beijing University of Posts and Telecommunications',
    'E_GROUP_NAME': 'Beijing University of Posts and Telecommunications',
    'SID': '6A1wQZxeRZ2F9w4hAYT',
    '_abck': '3F028728304E00E815AC4E937A67BBC8~0~YAAQ6IpodRqZV09uAQAA4Ly+aAI9TUcdJez7VMMccHU1I2rEsbz6NyyW2vpS2VGw5s+inBff5i1+gcKziLZDhdJGpw3/GpeiKku17p3486bMadgFMpJ6oJT+tl73/Nx6ir7lImklImXmMON+9kCFXUwbz96VO6yXMmoi+1JYuNHItdi+MKyvBV669ImPNVZa+STdZxeDn5VaR4I1/d0WV9G+T5fs/xhSKodB+0grfDKlNo32p+OCiTocnXHgd4isVLjNt7LfXYLiP2uE9Ic9nKc7ybbKQAB0sxn57h7NXT3+wtZt0LBXZY6CmMBuKbHUYHrNTDpappqdxDoHrCo9~-1~-1~-1',
    'bm_sz': '8A8539EF773703DBFF7AA89F37B7A1BA~YAAQ6IpodWO/V09uAQAAXqv/aAVgFgUKFO/z7FIqUa9q39mRIDWnVpmJXtr0aXOkvvgTiVEiH9JhUMe0ia99/jhertSg4Ql+tULECnf1h86HmqGXCTwbSWKraRhh3bmcopkRgWDtujVpgxMinhIbvnmum/5zokVip8ErgEBuR48eswEPTW2nOGI1KMQwV1Olj8bW8Io/Jd0=',
    '_sp_id.630e': '1747125a-1bd4-4815-81cc-2e1cc744c829.1573267830.6.1573732765.1573719868.ed5e9b1b-0172-420d-ae59-e08137fc4397',
    '_sp_ses.630e': '*',
    'JSESSIONID': 'B1B4E7133A3C1E0628958FF0D91B6280',
    'ak_bmsc': 'BEACEA989C49AC3646387533EBEF3E7C6875B547D44600009E41CD5D5986895E~pl9cPVOjZ0FBPZTtVpLHHhZexSMI2pO8+x3D4pL6BLqRhaMjrSW1aw39iXQ792aVF+m3Qs4eMP0Tv2cO6P+Mlkg6zmzk1W42QQLG4U43MPpCBk6HQZfvJLJFU2oVKiCZ7Eu3PIXdvPmRjqsv7GrllXvcUrxqZs3NTnnni4YGsbwRtd6Y2r49NninDXJCRZ2M+/eA+ZFJ0toybCrgLTajKW3ZFk89BryNNqs9/+Nn11a3WA71Yej15zE+AUr0fiocJ3',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Referer': 'https://apps.webofknowledge.com/UA_GeneralSearch_input.do?product=UA&search_mode=GeneralSearch&SID=6A1wQZxeRZ2F9w4hAYT&preferencesSaved=',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh-CN;q=0.7,zh;q=0.6,ja;q=0.5',
}

params = (
    ('product', 'UA'),
    ('search_mode', 'GeneralSearch'),
    ('SID', '6A1wQZxeRZ2F9w4hAYT'),
    ('preferencesSaved', ''),
)

response = requests.get('https://apps.webofknowledge.com/UA_GeneralSearch_input.do', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://apps.webofknowledge.com/UA_GeneralSearch_input.do?product=UA&search_mode=GeneralSearch&SID=6A1wQZxeRZ2F9w4hAYT&preferencesSaved=', headers=headers, cookies=cookies)
