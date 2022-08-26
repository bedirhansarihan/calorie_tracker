import typing

import  requests
import pprint

def _requester(food_name, page_number):
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjYwNzdBNzkyMERFNDM1NDQ5QkUxNEEwNTI5QkZFNjQxNUEzOTZFRjgiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJZSGVua2cza05VU2I0VW9GS2JfbVFWbzVidmcifQ.eyJuYmYiOjE2NjE0Mzc2NzYsImV4cCI6MTY2MTUyNDA3NiwiaXNzIjoiaHR0cHM6Ly9vYXV0aC5mYXRzZWNyZXQuY29tIiwiYXVkIjoiYmFzaWMiLCJjbGllbnRfaWQiOiJhZDZkMDdlNGJhY2I0Y2M4OTM0M2MzZGMwY2Q3Y2NlNCIsInNjb3BlIjpbImJhc2ljIl19.P7IXWTp5p_xPCE1ekdmF99F4g1nW4OQgw4RUuzIAdUtkUEXi8BaM8k4vUywPakFhSOTDigdC71D3UxU327ce2vX2fgiVQ9_7JxqntWcz9A8hlTLMyI8lCdYHe13Eg3ufBT1cTJMKPWvEGyXE6p5UzAvfaZxdTRJsGF5bfTLXPtZ-pNk_5hu9VzXU3Ne4UTSSboipLZ3f2WtCbmEQdmKtYm89y-CYI2k1eVRKQMtnv6X-kYpERE467AIzBMKszVHfrcUzMG8ipfvX5OtPbrQIosPZ0E17WkuqQp7R71lZC38S2nzHpyZhXwOxCykdnMYoyXdG9zDw6bzhTGU596p4usz44-14lRo_xAed4RrOBGBDE0otA1ASN1MLXaOamtGJCDeBJSHcvUklbSsx_hkoQe8MRzd4leeCi_gBXqeHhDBrWh4Ds9i0pa7l6sIQGkerA3GiZkkQmqsQjk6rK7u8WjGlHhtz6OE3T3GXnQwWhZNOo7h0uiv1D4EhRB41xJIigTjXK_rbuQ98eg7qCj5S4ewDS2xd6g3wZNNmJ3NYtSSVDB80HpLT3cGqAzRRE6mAbUW86dowYttDtQ9KdDbjXaCD0XeGXTktFZoKvVZ8s4DfYxyR4Pfy-L0mVvxsKaezpJ2wP80_Wyp7i36F_WyTdyN9tIo8LcQC6Jo0F5CKdMk',
        'Content-Type': 'application/json',
        'language': 'TR'
    }
    params = {

        'method': 'foods.search',
        'search_expression': food_name,
        'format': 'json',
        'max_results': 50,
        'page_number': page_number

    }
    try:
        r = requests.post('https://platform.fatsecret.com/rest/server.api', params=params, headers=headers)
        info_response: list = r.json()['foods']['food']
        return  info_response
    except:

        return None

def food_search(food_name, page_number):

    food_data: typing.List[tuple] = list()

    for i in range(page_number):
        info_response = _requester(food_name, i)

        if info_response is not None:

            for food in info_response:
                tuple_data: tuple = food_desc_splitter(food)

                if tuple_data is not None:

                    food_data.append(tuple_data + (tuple_data[0],))


    return food_data
def food_desc_splitter(f: dict):

    food_name = f['food_name']
    nutrition_facts = f['food_description']

    splitted_nutrition_facts = nutrition_facts.split()

    if splitted_nutrition_facts[1][-1] == 'g':

        amount = splitted_nutrition_facts[1][:-1]
    else:
        return

    calories = splitted_nutrition_facts[4][:-4]
    fat = splitted_nutrition_facts[7][:-1]
    carbs = splitted_nutrition_facts[10][:-1]
    protein = splitted_nutrition_facts[13][:-1]


    return (food_name, amount, carbs, protein, fat, calories)



