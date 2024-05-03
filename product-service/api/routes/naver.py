import requests
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse

client_id = 'eeCAwoPqKjNHz7WqddzW'
client_secret = ''
redirect_url = 'http://127.0.0.1:8000/callback/naver'
state = 'RAMDOM_STATE'

router = APIRouter()


@router.get('/login/naver')
async def login_naver():
    api_url = f'https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_url}&state={state}'
    html_content = f"<a href='{api_url}'><img height='50' src='http://static.nid.naver.com/oauth/small_g_in.PNG'/></a>"
    return HTMLResponse(content=html_content, status_code=200)


@router.get('/callback/naver')
async def callback_naver(req: Request):
    code = req.query_params.get('code')
    print('code - ', code)

    req_url = f'https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_url}&code={code}&state={state}'
    request_token = requests.get(req_url)
    json_token = request_token.json()
    print('token info - ', json_token)

    access_token = json_token.get('access_token')
    profile_url = f'https://openapi.naver.com/v1/nid/me'
    headers = {'Authorization': f'Bearer {access_token}'}

    request_profile = requests.get(profile_url, headers=headers)
    json_profile = request_profile.json()
    print('profile info - ', json_profile)

    return 'Done'








