import vk_api
import moi_base as vb
vk_session = vk_api.VkApi(token = 'token')

from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            vk_session = vk_api.VkApi(token = 'token')
            vk = vk_session.get_api()
            dt=vk.users.get(user_ids=event.user_id,fields='bdate')[0]['bdate']
            mas=[int(i) for i in dt.split('.')]
            year= 2019-mas[2]
            if year<30:
                text=vb.start(event.text,True)
            else:
                text=vb.start(event.text,False)
            print(vk.wall.post(owner_id=-186293891 ,message=text))
