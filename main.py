import re
from datetime import datetime

lst = [
    {'due_date': None, 'due_date_reason': '', 'due_date_status': 'not_set', 'total_comments': 2, 'tags': [], 'attachments': [], 'status': 348,
     'status_extra_info': {'name': 'Отобранные кандидаты', 'color': '#70728F', 'is_closed': False}, 'assigned_to': 66,
     'assigned_to_extra_info': {'username': 'eloseva', 'full_name_display': 'Екатерина Лосева', 'photo': 'https://boards.calculate.ru/media/user/2/e/7/4/5db8064062cd4f2bd1a765c28b9a31ad06c214c1aa2682e9579d46efbfd0/avatar.80x80_q85_crop.jpg?token=ZKZahg%3Ai6teBlsjU0D3CHb3CQLb3cgTANUAfkLFcBPHuZlWtwISH9uo6VY-UdVv4fz_ST7eGhcXqAIZ8_vr0AIV4D-0Sw', 'big_photo': 'https://boards.calculate.ru/media/user/2/e/7/4/5db8064062cd4f2bd1a765c28b9a31ad06c214c1aa2682e9579d46efbfd0/avatar.300x300_q85_crop.jpg?token=ZKZahg%3A81X-QL2Wy3NP8ogda0mKC24FsedZNMza31ECDC7pD0fn4dzbJXcDXU6PP_8E1TsZFfHwtZC3X_PWkvyA2hAc-w', 'gravatar_id': 'af24d712db413d08b640f83463216f82', 'is_active': True, 'id': 66},
     'owner': 224, 'owner_extra_info': {'username': 'ikuznecova', 'full_name_display': 'Инна Кузнецова', 'photo': 'https://boards.calculate.ru/media/user/a/1/1/8/ce602c43dc7df9a5c23f6f0d0e85a6c34b01c96b69eaab9de7e490b5f533/kuznetsova.jpg.80x80_q85_crop.jpg?token=ZKZahg%3AgNDplA-t4p_PgPSpi1WndSdbon7WOXZm73j2TO2IZZwCRUg-t42-xM24LSaCxsPZTbqA9bzNRpZGZq6xr6lvug', 'big_photo': 'https://boards.calculate.ru/media/user/a/1/1/8/ce602c43dc7df9a5c23f6f0d0e85a6c34b01c96b69eaab9de7e490b5f533/kuznetsova.jpg.300x300_q85_crop.jpg?token=ZKZahg%3A9J9mtfMgA78c1HkwFeTYap4WqvjpiBPk6TCXiBN7hxAPlfRwz2JKguJwOlfNF3xj5icLb1epVa4egLLZbFAcOQ', 'gravatar_id': '4a2f04ae350841d7babecac7d3aee5b6', 'is_active': True, 'id': 224},
     'is_watcher': False, 'total_watchers': 2, 'is_voter': False, 'total_voters': 0, 'project': 54,
     'project_extra_info': {'name': 'HR: Филиал Москва', 'slug': 'hr-filial-moskva', 'logo_small_url': 'https://boards.calculate.ru/media/project/6/f/5/1/cf53d878ca0e04d85f5ba5e7904a2466348fb4c6f8b4b25157eacb1daf92/search-userpng300x300_q85_crop.png.80x80_q85_crop.png?token=ZKZahg%3A65BCs0KWuEVFMCX9Hd_xF4_6KLynzUbAhcReuL-ywdg14dN3l4PbbYPWtC2gyLse9bNs4dGzEWTdpBc97PyhUQ', 'id': 54},
     'id': 5873, 'ref': 22, 'milestone': None, 'milestone_slug': None, 'milestone_name': None, 'is_closed': False, 'points': {}, 'backlog_order': 1688559697133451,
     'sprint_order': 1688559697133530, 'kanban_order': 1688559697155019, 'created_date': '2023-07-05T12:21:37.155Z', 'modified_date': '2023-07-05T13:15:33.618Z',
     'finish_date': None,
     'subject': '06/07/2023, 11:00, Каледина Татьяна Владимировна,  (963) 971-09-94', 'client_requirement': False, 'team_requirement': False, 'generated_from_issue': None,
     'generated_from_task': None, 'from_task_ref': None, 'external_reference': None, 'tribe_gig': None, 'version': 5, 'watchers': [66, 224],
     'is_blocked': False, 'blocked_note': '', 'total_points': None, 'comment': '', 'origin_issue': None, 'origin_task': None,
     'epics': [{'id': 74, 'ref': 5, 'subject': 'Сервис-менеджер', 'color': '#51D355', 'project': {'id': 54, 'name': 'HR: Филиал Москва', 'slug': 'hr-filial-moskva'}},
               {'id': 83, 'ref': 24, 'subject': 'Собеседования в Москве', 'color': '#E44057', 'project': {'id': 24, 'name': 'Подбор персонала', 'slug': 'podbor-personala'}}],
     'epic_order': 1688564382583, 'tasks': [], 'total_attachments': 2, 'swimlane': None, 'assigned_users': [224, 66]},
    {'due_date': None, 'due_date_reason': '', 'due_date_status': 'not_set', 'total_comments': 1, 'tags': [], 'attachments': [], 'status': 348,
     'status_extra_info': {'name': 'Отобранные кандидаты', 'color': '#70728F', 'is_closed': False}, 'assigned_to': 66,
     'assigned_to_extra_info': {'username': 'eloseva', 'full_name_display': 'Екатерина Лосева', 'photo': 'https://boards.calculate.ru/media/user/2/e/7/4/5db8064062cd4f2bd1a765c28b9a31ad06c214c1aa2682e9579d46efbfd0/avatar.80x80_q85_crop.jpg?token=ZKZahg%3Ai6teBlsjU0D3CHb3CQLb3cgTANUAfkLFcBPHuZlWtwISH9uo6VY-UdVv4fz_ST7eGhcXqAIZ8_vr0AIV4D-0Sw', 'big_photo': 'https://boards.calculate.ru/media/user/2/e/7/4/5db8064062cd4f2bd1a765c28b9a31ad06c214c1aa2682e9579d46efbfd0/avatar.300x300_q85_crop.jpg?token=ZKZahg%3A81X-QL2Wy3NP8ogda0mKC24FsedZNMza31ECDC7pD0fn4dzbJXcDXU6PP_8E1TsZFfHwtZC3X_PWkvyA2hAc-w', 'gravatar_id': 'af24d712db413d08b640f83463216f82', 'is_active': True, 'id': 66}, 'owner': 224,
     'owner_extra_info': {'username': 'ikuznecova', 'full_name_display': 'Инна Кузнецова', 'photo': 'https://boards.calculate.ru/media/user/a/1/1/8/ce602c43dc7df9a5c23f6f0d0e85a6c34b01c96b69eaab9de7e490b5f533/kuznetsova.jpg.80x80_q85_crop.jpg?token=ZKZahg%3AgNDplA-t4p_PgPSpi1WndSdbon7WOXZm73j2TO2IZZwCRUg-t42-xM24LSaCxsPZTbqA9bzNRpZGZq6xr6lvug', 'big_photo': 'https://boards.calculate.ru/media/user/a/1/1/8/ce602c43dc7df9a5c23f6f0d0e85a6c34b01c96b69eaab9de7e490b5f533/kuznetsova.jpg.300x300_q85_crop.jpg?token=ZKZahg%3A9J9mtfMgA78c1HkwFeTYap4WqvjpiBPk6TCXiBN7hxAPlfRwz2JKguJwOlfNF3xj5icLb1epVa4egLLZbFAcOQ', 'gravatar_id': '4a2f04ae350841d7babecac7d3aee5b6', 'is_active': True, 'id': 224},
     'is_watcher': False, 'total_watchers': 1, 'is_voter': False, 'total_voters': 0, 'project': 54,
     'project_extra_info': {'name': 'HR: Филиал Москва', 'slug': 'hr-filial-moskva', 'logo_small_url': 'https://boards.calculate.ru/media/project/6/f/5/1/cf53d878ca0e04d85f5ba5e7904a2466348fb4c6f8b4b25157eacb1daf92/search-userpng300x300_q85_crop.png.80x80_q85_crop.png?token=ZKZahg%3A65BCs0KWuEVFMCX9Hd_xF4_6KLynzUbAhcReuL-ywdg14dN3l4PbbYPWtC2gyLse9bNs4dGzEWTdpBc97PyhUQ', 'id': 54},
     'id': 5877, 'ref': 23, 'milestone': None, 'milestone_slug': None, 'milestone_name': None, 'is_closed': False, 'points': {}, 'backlog_order': 1688561981473519,
     'sprint_order': 1688561981473595, 'kanban_order': 1688562821472751, 'created_date': '2023-07-05T12:59:41.502Z', 'modified_date': '2023-07-05T13:14:55.297Z',
     'finish_date': None, 'subject': '13:00,  10/07, Панченко Ольга, +7 (908) 131-26-28', 'client_requirement': False, 'team_requirement': False, 'generated_from_issue': None,
     'generated_from_task': None, 'from_task_ref': None, 'external_reference': None, 'tribe_gig': None, 'version': 3, 'watchers': [224], 'is_blocked': False,
     'blocked_note': '', 'total_points': None, 'comment': '', 'origin_issue': None, 'origin_task': None,
     'epics': [{'id': 74, 'ref': 5, 'subject': 'Сервис-менеджер', 'color': '#51D355', 'project': {'id': 54, 'name': 'HR: Филиал Москва', 'slug': 'hr-filial-moskva'}},
               {'id': 83, 'ref': 24, 'subject': 'Собеседования в Москве', 'color': '#E44057', 'project': {'id': 24, 'name': 'Подбор персонала', 'slug': 'podbor-personala'}}],
     'epic_order': 1688564382660, 'tasks': [], 'total_attachments': 2, 'swimlane': None, 'assigned_users': [224, 66]},
    {'due_date': None, 'due_date_reason': '', 'due_date_status': 'not_set', 'total_comments': 1, 'tags': [], 'attachments': [], 'status': 348,
     'status_extra_info': {'name': 'Отобранные кандидаты', 'color': '#70728F', 'is_closed': False}, 'assigned_to': 66,
     'assigned_to_extra_info': {'username': 'eloseva', 'full_name_display': 'Екатерина Лосева', 'photo': 'https://boards.calculate.ru/media/user/2/e/7/4/5db8064062cd4f2bd1a765c28b9a31ad06c214c1aa2682e9579d46efbfd0/avatar.80x80_q85_crop.jpg?token=ZKZahg%3Ai6teBlsjU0D3CHb3CQLb3cgTANUAfkLFcBPHuZlWtwISH9uo6VY-UdVv4fz_ST7eGhcXqAIZ8_vr0AIV4D-0Sw', 'big_photo': 'https://boards.calculate.ru/media/user/2/e/7/4/5db8064062cd4f2bd1a765c28b9a31ad06c214c1aa2682e9579d46efbfd0/avatar.300x300_q85_crop.jpg?token=ZKZahg%3A81X-QL2Wy3NP8ogda0mKC24FsedZNMza31ECDC7pD0fn4dzbJXcDXU6PP_8E1TsZFfHwtZC3X_PWkvyA2hAc-w', 'gravatar_id': 'af24d712db413d08b640f83463216f82', 'is_active': True, 'id': 66},
     'owner': 224, 'owner_extra_info': {'username': 'ikuznecova', 'full_name_display': 'Инна Кузнецова', 'photo': 'https://boards.calculate.ru/media/user/a/1/1/8/ce602c43dc7df9a5c23f6f0d0e85a6c34b01c96b69eaab9de7e490b5f533/kuznetsova.jpg.80x80_q85_crop.jpg?token=ZKZahg%3AgNDplA-t4p_PgPSpi1WndSdbon7WOXZm73j2TO2IZZwCRUg-t42-xM24LSaCxsPZTbqA9bzNRpZGZq6xr6lvug', 'big_photo': 'https://boards.calculate.ru/media/user/a/1/1/8/ce602c43dc7df9a5c23f6f0d0e85a6c34b01c96b69eaab9de7e490b5f533/kuznetsova.jpg.300x300_q85_crop.jpg?token=ZKZahg%3A9J9mtfMgA78c1HkwFeTYap4WqvjpiBPk6TCXiBN7hxAPlfRwz2JKguJwOlfNF3xj5icLb1epVa4egLLZbFAcOQ', 'gravatar_id': '4a2f04ae350841d7babecac7d3aee5b6', 'is_active': True, 'id': 224},
     'is_watcher': False, 'total_watchers': 1, 'is_voter': False, 'total_voters': 0, 'project': 54,
     'project_extra_info': {'name': 'HR: Филиал Москва', 'slug': 'hr-filial-moskva', 'logo_small_url': 'https://boards.calculate.ru/media/project/6/f/5/1/cf53d878ca0e04d85f5ba5e7904a2466348fb4c6f8b4b25157eacb1daf92/search-userpng300x300_q85_crop.png.80x80_q85_crop.png?token=ZKZahg%3A65BCs0KWuEVFMCX9Hd_xF4_6KLynzUbAhcReuL-ywdg14dN3l4PbbYPWtC2gyLse9bNs4dGzEWTdpBc97PyhUQ', 'id': 54},
     'id': 5878, 'ref': 24, 'milestone': None, 'milestone_slug': None, 'milestone_name': None, 'is_closed': False, 'points': {}, 'backlog_order': 1688562821449130,
     'sprint_order': 1688562821449207, 'kanban_order': 1688562821472750, 'created_date': '2023-07-05T13:13:41.472Z', 'modified_date': '2023-07-05T13:21:06.415Z',
     'finish_date': None, 'subject': '12:00,  06/07/2023, Позднякова Анна Викторовна,  +7 (916) 515-27-11', 'client_requirement': False, 'team_requirement': False,
     'generated_from_issue': None, 'generated_from_task': None, 'from_task_ref': None, 'external_reference': None, 'tribe_gig': None, 'version': 4, 'watchers': [224],
     'is_blocked': False, 'blocked_note': '', 'total_points': None, 'comment': '', 'origin_issue': None, 'origin_task': None,
     'epics': [{'id': 74, 'ref': 5, 'subject': 'Сервис-менеджер', 'color': '#51D355', 'project': {'id': 54, 'name': 'HR: Филиал Москва', 'slug': 'hr-filial-moskva'}},
               {'id': 83, 'ref': 24, 'subject': 'Собеседования в Москве', 'color': '#E44057', 'project': {'id': 24, 'name': 'Подбор персонала', 'slug': 'podbor-personala'}}],
     'epic_order': 1688564382584, 'tasks': [], 'total_attachments': 2, 'swimlane': None, 'assigned_users': [224, 66]}
]


def get_titles():
    subj_list = []
    for i in lst:
        subj_list.append(i['subject'])
    return subj_list


def get_date_and_time():
    data = [
        '06/07/2023, 11:00, Каледина Татьяна Владимировна, (963) 971-09-94',
        '13:00, 10/07, Панченко Ольга, +7 (908) 131-26-28',
        '12:00, 06/07/2023, Позднякова Анна Викторовна, +7 (916) 515-27-11',
        'Петров Тимофей Васильевич, +7 (981) 002-51-58',
        '09/06, 01:00, Пронин Илья, +7 (900) 000-00-09',
        '09/07, Дроздова Мария, +7 (900) 000-00-10',
    ]
    date_regex = r'\d{2}/\d{2}/\d{4}/|\d{2}/\d{2}'
    time_regex = r'\d{2}:\d{2}'
    dict_date_and_time = dict()
    for index, item in enumerate(data):
        date_match = re.search(date_regex, item)
        time_match = re.search(time_regex, item)

        if time_match:
            time = time_match.group()
        else:
            time = None

        if date_match:
            date = date_match.group()
        else:
            date = None

        dict_date_and_time[index] = f"{f'{date}/2023' if date else 'None'}, {time if time else 'None'}"
    return dict_date_and_time


print(get_date_and_time())


def sorted_list_with_us_id_epic_82():
    time_data = get_date_and_time()
    _filter_list = []
    _lst = []
    __keys = list()

    for k, v in time_data.items():
        if v == 'None, None':
            _filter_list.insert(0, k)
        elif 'None' in v:
            _filter_list.append(k)
        else:
            date_string = v.replace('/', '.')
            _lst.append((k, date_string))

    sorted_lst = sorted(_lst, key=lambda x: datetime.strptime(x[1], '%d.%m.%Y, %H:%M'))
    __keys = [x[0] for x in sorted_lst]
    _filter_list.extend(__keys)

    return _filter_list


print(sorted_list_with_us_id_epic_82())