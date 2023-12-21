import os

bot_responses = {
    "hello": ["Привет, путник!", "Здравствуйте!", "Приветствую!", "Добрый день!", "Здорова!", "Хай",
              "Хеллоу(да-да я из Англии)", "Привет, шеф!"],
    "how_are_you": ["Хорошо, спасибо!", "Все отлично!", "Дела хороши!", "Прогрессирую!",
                    "Все в порядке, спасибо за интерес.", "Лучше всех!",
                    "Все замечательно!", "Стабильно и хорошо.", "Дела идут вверх!", "Все просто прекрасно!"],
    'do_work': ['Ничего!', 'Жду пока мне кто-то напишет!', 'Нахожусь в режиме ожидания!', 'Учу питон!', 'Общаюсь с вами!'],
    "jokes": ["Почему программисты на Python всегда улыбаются? Потому что у них код работает!",
              "Что делает питон после того, как закончит изучать Python? Он начинает писать свой собственный код!",
              "Почему питоны из Python такие общительные? Потому что им всегда есть что сказать!",
              "Что произойдет, если питон начнет изучать Python? Он станет самым умным питоном в мире!"],
    "anecdote": "Заходят как-то программисты на Python, C# и C++ в бар. \n"
                "Программист на Python говорит: -Мне бокал пива.  Выпил, оплатил, ушел.\n"
                "Программист на C#: Здравствуйте налейте мне, пожалуйста, пенного хмельного пива в стеклянную тару, "
                "в простонародии называемую бокалом. Минут 30 сидел, пил, оплатил, со всеми в баре попрощался и ушел.\n"
                "А программист на C++ часа три не мог открыть рот.",
    "buy": ["До свидания!", "Удачи, путник!", "До скорой встречи!", "Возвращайтесь, если что!",
            "Да пребудет с вами сила", "Ещё увидимся!"]
}

main_character = {
    'name': 'Артем',
    'age': 26,
    'skills': ['Стрельба', 'Крафт', 'Вождение дрезины'],
    'wife': {
        'name': 'Аня',
        'age': 27,
        'about_ann': 'супруга Артема.\n'
                     'Аня считается лучшим снайпером среди рейнджеров-спартанцев, так что можно не волноваться за тыл,'
                     ' когда она занимается прикрытием. Анна славится своим несгибаемым духом, но она по-прежнему верит'
                     ' в доброту, примирение и прощение, поэтому будет призывать найти мирное решение, '
                     'если это возможно.',
        'photo': os.path.join(os.getcwd(), "photo", "ann.jpg")
    },
    'about_me': 'Я рейнджер ордена "SPARTA".\nВ возрасте 4-х лет я пережил мировую ядерную войну, укрывшись в '
                'московском метрополитенене. После войны, моим домом стала станция метро ВДНХ. '
                'Всю свою жизнь я мечтал выбраться на поверхность.',
    'photos': [os.path.join(os.getcwd(), "photo", "artem.jpeg"), os.path.join(os.getcwd(), "photo", "artem2.jpg")]
}

message_templates = {
    'hello_ms': ['привет', 'ку', 'hi', 'hello', 'приветик', 'хай', 'хелло'],
    'hay_ms': ['как дела', 'как дела?', 'кд', 'how are you?', 'как ты?', 'как ты'],
    'do_work_ms': ['что делаешь?', 'что делаешь', 'что нового?', 'что нового', 'чд', 'занят?', 'занят',
                   'чем занимаешься', 'чем занят?', 'чем занимаешься?', 'чем занят'],
    'jokes_ms': ['шутка', 'расскажи шутку', 'шутку', 'можно шутку', 'требую шутку', 'пошути', 'можно шутку?'],
    'anecdote_ms': ['расскажи анекдот', 'анекдот', 'расскажи анедкдот', 'можно анекдот?', 'трубую анекдот', 'занешь анекдот?'],
    'buy_ms': ['пока', 'бывай', 'до встречи', 'увидимся', 'buy', 'бай', 'досвидания', 'бай', 'гудбай', 'goodbuy'],
    'help_ms': ['помоги', 'помощь', 'help', 'хелп', 'нужна помощь', 'нужна помощь', 'помоги пожалуйста']
}