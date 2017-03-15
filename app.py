import vk_api
import photo_cycle as pc
import json

def main():


    with open('config.json') as json_data_file:
          config = dict(json.load(json_data_file))
    

    _login = config['login']
    _password = config['pass']
    _my_id = '80314023'

    vk_session = vk_api.VkApi(login=_login, password = _password)

    vk_session.authorization()
    vk= vk_session.get_api()
    pc.start(vk)

if __name__==("__main__"):
    main()