# -*- coding: utf-8 -*-
"""
Text #302 from OpenCorpora.
"""
from __future__ import absolute_import, unicode_literals

PARSE_RESULTS = [ # word, opencorpora, aot/pymorphy
    ('Трудности', 'СУЩ,неод,жр,ед,рд', 'С,жр,ед,рд'),
    ('перевода', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('Депутаты', 'СУЩ,од,мр,мн,им', 'С,мр,мн,им'),
    ('Приморья', 'СУЩ,неод,ср,ед,рд', 'С,ср,ед,рд'),
    ('попросили', 'ГЛ,сов,перех,мн,прош,изъяв', 'Г,дст,прш,мн'),
    ('приблизить', 'ИНФ,сов,перех', 'ИНФИНИТИВ,дст'),
    ('их', 'ПРИЛ,0,мест-п,мр,ед,им', 'МС-П,0,од,но,ед,им,мр'), # aot tags were fixed
    ('к', 'ПР', 'ПРЕДЛ'),
    ('Москве', 'СУЩ,неод,жр,sg,гео,ед,дт', 'С,жр,ед,дт'),
    ('на', 'ПР', 'ПРЕДЛ'),
    ('один', 'ПРИЛ,мест-п,мр,ед,им', 'МС-П,мр,ед,им,од,но'),
    ('час', 'СУЩ,неод,мр,ед,им', 'С,мр,ед,им'),
    #(',', 'PNCT', ''),
    ('однако', 'МЕЖД', 'МЕЖД'),
    ('население', 'СУЩ,неод,ср,ед,им', 'С,ср,ед,им'),
    ('региона', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('против', 'ПР', 'ПРЕДЛ'),
    #('.', 'PNCT', ''),
    ('Следуя', 'ДЕЕПР,несов,неперех,наст', 'ДЕЕПРИЧАСТИЕ,дст,нст'),
    ('предложению', 'СУЩ,неод,ср,ед,дт', 'С,ср,ед,дт'),
    ('Дмитрия', 'СУЩ,од,мр,имя,ед,рд', 'С,мр,имя,ед,рд'),
    ('Медведева', 'СУЩ,од,мр,sg,фам,ед,рд', 'С,мр,ед,рд'),
    #(',', 'PNCT', ''),
    ('депутаты', 'СУЩ,од,мр,мн,им', 'С,мр,мн,им'),
    ('Законодательного', 'ПРИЛ,мр,ед,рд', 'П,мр,ед,рд,од,но'),
    ('собрания', 'СУЩ,неод,ср,ед,рд', 'С,ср,ед,рд'),
    ('Приморского', 'СУЩ,неод,мр,sg,гео,ед,рд', 'С,мр,ед,рд'),
    ('края', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('приняли', 'ГЛ,сов,перех,мн,прош,изъяв', 'Г,дст,прш,мн'),
    ('обращение', 'СУЩ,неод,ср,ед,им', 'С,ср,ед,им'),
    ('к', 'ПР', 'ПРЕДЛ'),
    ('премьеру', 'СУЩ,од,мр,ед,дт', 'С,мр,ед,дт'),
    ('РФ', 'СУЩ,неод,жр,sg,0,аббр,гео,ед,им', 'С,жр,ед,аббр,0'),
    ('о', 'ПР', 'ПРЕДЛ'),
    ('переходе', 'СУЩ,неод,мр,ед,пр', 'С,мр,ед,пр'),
    ('из', 'ПР', 'ПРЕДЛ'),
    ('седьмого', 'ПРИЛ,числ-п,мр,ед,рд', 'ЧИСЛ-П,мр,ед,рд,од,но'),
    ('в', 'ПР', 'ПРЕДЛ'),
    ('шестой', 'СУЩ,неод,жр,ед,рд', 'С,жр,ед,рд'),
    ('часовой', 'СУЩ,од,мр,ед,им', 'С,мр,ед,им'),
    ('пояс', 'СУЩ,неод,мр,ед,им', 'С,мр,ед,им'),
    #('.', 'PNCT', ''),
    ('Смена', 'СУЩ,неод,жр,ед,им', 'С,жр,ед,им'),
    ('часового', 'СУЩ,од,мр,ед,рд', 'С,мр,ед,рд'),
    ('пояса', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('обеспечила', 'ГЛ,сов,перех,жр,ед,прош,изъяв', 'Г,дст,прш,жр,ед'),
    ('бы', 'ЧАСТ', 'ЧАСТ'),
    ('краю', 'СУЩ,неод,мр,ед,дт', 'С,мр,ед,дт'),
    #('шестичасовую', 'UNKN', 'П,жр,ед,вн,од,но'),
    ('разницу', 'СУЩ,неод,жр,ед,вн', 'С,жр,ед,вн'),
    ('во', 'ПР', 'ПРЕДЛ'),
    #('времени', 'ГЛ,несов,неперех,ед,повел,выкл', 'С,ср,ед,рд'),
    ('со', 'ПР', 'ПРЕДЛ'),
    ('столицей', 'СУЩ,неод,жр,ед,тв', 'С,жр,ед,тв'),
    #(',', 'PNCT', ''),
    ('сообщает', 'ГЛ,несов,перех,ед,3л,наст,изъяв', 'Г,дст,нст,3л,ед'),
    ('NEWSru.com', 'UNKN', ''),
    #('.', 'PNCT', ''),
    ('Такой', 'ПРИЛ,мест-п,мр,ед,им', 'МС-П,мр,ед,им,од,но'),
    ('переход', 'СУЩ,неод,мр,ед,им', 'С,мр,ед,им'),
    #(',', 'PNCT', ''),
    ('считает', 'ГЛ,несов,перех,ед,3л,наст,изъяв', 'Г,дст,нст,3л,ед'),
    ('вице-губернатор', 'СУЩ,од,мр,ед,им', 'С,мр,ед,им'),
    ('Приморья', 'СУЩ,неод,ср,ед,рд', 'С,ср,ед,рд'),
    ('Александр', 'СУЩ,од,мр,имя,ед,им', 'С,мр,имя,ед,им'),
    #('Шемелев', 'UNKN', 'С,ср,мн,рд'),
    #(',', 'PNCT', ''),
    ('повысит', 'ГЛ,сов,перех,ед,3л,буд,изъяв', 'Г,дст,буд,3л,ед'),
    ('оперативность', 'СУЩ,неод,жр,ед,им', 'С,жр,ед,им'),
    ('взаимодействия', 'СУЩ,неод,ср,ед,рд', 'С,ср,ед,рд'),
    ('государственных', 'ПРИЛ,мн,рд', 'П,мн,рд,од,но'),
    ('органов', 'СУЩ,неод,мр,мн,рд', 'С,мр,мн,рд'),
    ('и', 'СОЮЗ', 'СОЮЗ'),
    ('организаций', 'СУЩ,неод,жр,мн,рд', 'С,жр,мн,рд'),
    #(',', 'PNCT', ''),
    ('а', 'СОЮЗ', 'СОЮЗ'),
    ('также', 'СОЮЗ', 'СОЮЗ'),
    ('краевых', 'ПРИЛ,мн,рд', 'П,мн,рд,од,но'),
    ('органов', 'СУЩ,неод,мр,мн,рд', 'С,мр,мн,рд'),
    ('власти', 'СУЩ,неод,жр,ед,рд', 'С,жр,ед,рд'),
    ('с', 'ПР', 'ПРЕДЛ'),
    ('Москвой', 'СУЩ,неод,жр,sg,гео,ед,тв', 'С,жр,ед,тв'),
    #('.', 'PNCT', ''),
    ('Предложение', 'СУЩ,неод,ср,ед,им', 'С,ср,ед,им'),
    ('поддержали', 'ГЛ,сов,перех,мн,прош,изъяв', 'Г,дст,прш,мн'),
    ('26', 'UNKN', ''),
    ('депутатов', 'СУЩ,од,мр,мн,рд', 'С,мр,мн,рд'),
    ('из', 'ПР', 'ПРЕДЛ'),
    ('30', 'UNKN', ''),
    #('.', 'PNCT', ''),
    ('Накануне', 'ПР', 'ПРЕДЛ'),
    ('губернатор', 'СУЩ,од,мр,ед,им', 'С,мр,ед,им'),
    ('Приморья', 'СУЩ,неод,ср,ед,рд', 'С,ср,ед,рд'),
    ('Сергей', 'СУЩ,од,мр,имя,ед,им', 'С,мр,имя,ед,им'),
    ('Дарькин', 'СУЩ,од,мр,sg,фам,ед,им', 'С,мр,ед,им'),
    ('заявил', 'ГЛ,сов,перех,мр,ед,прош,изъяв', 'Г,дст,прш,мр,ед'),
    ('на', 'ПР', 'ПРЕДЛ'),
    ('пресс-конференции', 'СУЩ,неод,жр,ед,рд', 'С,жр,ед,рд'),
    #(',', 'PNCT', ''),
    ('что', 'СОЮЗ', 'СОЮЗ'),
    ('смену', 'СУЩ,неод,жр,ед,вн', 'С,жр,ед,вн'),
    ('пояса', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('поддерживают', 'ГЛ,несов,перех,мн,3л,наст,изъяв', 'Г,дст,нст,3л,мн'),
    ('и', 'СОЮЗ', 'СОЮЗ'),
    ('жители', 'СУЩ,од,мр,мн,им', 'С,мр,мн,им'),
    ('края', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    #('.', 'PNCT', ''),
    ('При', 'ГЛ,несов,перех,ед,повел,выкл', 'Г,дст,пвл,2л,ед'),
    ('этом', 'МС,ср,ед,пр', 'МС,ср,ед,пр'),
    ('глава', 'СУЩ,од,мр,ед,им', 'С,мр,ед,им'),
    ('края', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('сослался', 'ГЛ,сов,неперех,мр,ед,прош,изъяв', 'Г,дст,прш,мр,ед'),
    ('на', 'ПР', 'ПРЕДЛ'),
    ('результаты', 'СУЩ,неод,мр,мн,им', 'С,мр,мн,им'),
    ('опросов', 'СУЩ,неод,мр,мн,рд', 'С,мр,мн,рд'),
    #('.', 'PNCT', ''),
    ('Между', 'ПР', 'ПРЕДЛ'),
    ('тем', 'СОЮЗ', 'СОЮЗ'),
    #(',', 'PNCT', ''),
    ('лидер', 'СУЩ,од,мр,ед,им', 'С,мр,ед,им'),
    ('фракции', 'СУЩ,неод,жр,ед,рд', 'С,жр,ед,рд'),
    ('КПРФ', 'СУЩ,неод,жр,sg,0,аббр,орг,ед,им', 'С,жр,ед,аббр,0'),
    ('Владимир', 'СУЩ,од,мр,имя,ед,им', 'С,мр,имя,ед,им'),
    ('Беспалов', 'СУЩ,од,мр,sg,фам,ед,им', 'С,мр,ед,им'),
    ('опроверг', 'ГЛ,сов,перех,мр,ед,прош,изъяв', 'Г,дст,прш,мр,ед'),
    ('эту', 'ПРИЛ,мест-п,жр,ед,вн', 'МС-П,жр,ед,вн,од,но'),
    ('информацию', 'СУЩ,неод,жр,ед,вн', 'С,жр,ед,вн'),
    #('.', 'PNCT', ''),
    ('Он', 'МС,мр,3л,ед,им', 'МС,3л,мр,ед,им'),
    ('заявил', 'ГЛ,сов,перех,мр,ед,прош,изъяв', 'Г,дст,прш,мр,ед'),
    #(',', 'PNCT', ''),
    ('что', 'СОЮЗ', 'СОЮЗ'),
    ('избиратели', 'СУЩ,од,мр,мн,им', 'С,мр,мн,им'),
    ('на', 'ПР', 'ПРЕДЛ'),
    ('встречах', 'СУЩ,неод,жр,мн,пр', 'С,жр,мн,пр'),
    ('с', 'ПР', 'ПРЕДЛ'),
    ('коммунистами', 'СУЩ,од,мр,мн,тв', 'С,мр,мн,тв'),
    ('высказывались', 'ГЛ,несов,неперех,мн,прош,изъяв', 'Г,дст,прш,мн'),
    ('против', 'ПР', 'ПРЕДЛ'),
    ('смены', 'СУЩ,неод,жр,ед,рд', 'С,жр,ед,рд'),
    ('часового', 'СУЩ,од,мр,ед,рд', 'С,мр,ед,рд'),
    ('пояса', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    #('.', 'PNCT', ''),
    ('«', 'UNKN', ''),
    ('Сегодня', 'Н', 'Н'),
    ('утром', 'СУЩ,неод,ср,ед,тв', 'С,ср,ед,тв'),
    ('у', 'ПР', 'ПРЕДЛ'),
    ('входа', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('в', 'ПР', 'ПРЕДЛ'),
    ('здание', 'СУЩ,неод,ср,ед,им', 'С,ср,ед,им'),
    ('Законодательного', 'ПРИЛ,мр,ед,рд', 'П,мр,ед,рд,од,но'),
    ('собрания', 'СУЩ,неод,ср,ед,рд', 'С,ср,ед,рд'),
    ('мы', 'МС,1л,мн,им', 'МС,1л,мн,им'),
    ('провели', 'ГЛ,сов,перех,мн,прош,изъяв', 'Г,дст,прш,мн'),
    ('встречу', 'ГЛ,сов,перех,ед,1л,буд,изъяв', 'Г,дст,буд,1л,ед'),
    #(',', 'PNCT', ''),
    ('на', 'ПР', 'ПРЕДЛ'),
    ('ней', 'МС,жр,3л,ед,рд,разг,*предл', 'МС,3л,жр,ед,рд'),
    ('присутствовали', 'ГЛ,несов,неперех,мн,прош,изъяв', 'Г,дст,прш,мн'),
    ('наши', 'ПРИЛ,мест-п,мн,им', 'МС-П,мн,им,од,но'),
    ('четыре', 'ЧИСЛ,им', 'ЧИСЛ,им'),
    ('депутата', 'СУЩ,од,мр,ед,рд', 'С,мр,ед,рд'),
    ('и', 'СОЮЗ', 'СОЮЗ'),
    ('их', 'ПРИЛ,0,мест-п,мр,ед,им', 'МС-П,0,од,но,ед,им,мр'), # aot tags were fixed
    ('помощники', 'СУЩ,од,мр,мн,им', 'С,мр,мн,им'),
    #('.', 'PNCT', ''),
    ('Мы', 'МС,1л,мн,им', 'МС,1л,мн,им'),
    ('пообщались', 'ГЛ,сов,неперех,мн,прош,изъяв', 'Г,дст,прш,мн'),
    ('с', 'ПР', 'ПРЕДЛ'),
    ('населением', 'СУЩ,неод,ср,ед,тв', 'С,ср,ед,тв'),
    ('—', 'UNKN', ''),
    ('мнение', 'СУЩ,неод,ср,ед,им', 'С,ср,ед,им'),
    ('однозначное', 'ПРИЛ,ср,ед,им', 'П,ср,ед,им,од,но'),
    #(',', 'PNCT', ''),
    ('мы', 'МС,1л,мн,им', 'МС,1л,мн,им'),
    ('получили', 'ГЛ,сов,перех,мн,прош,изъяв', 'Г,дст,прш,мн'),
    ('наказы', 'СУЩ,неод,мр,мн,им', 'С,мр,мн,им'),
    ('от', 'ПР', 'ПРЕДЛ'),
    ('избирателей', 'СУЩ,од,мр,мн,рд', 'С,мр,мн,рд'),
    ('голосовать', 'ИНФ,несов,перех', 'ИНФИНИТИВ,дст'),
    ('против', 'ПР', 'ПРЕДЛ'),
    ('обращения', 'СУЩ,неод,ср,ед,рд', 'С,ср,ед,рд'),
    ('к', 'ПР', 'ПРЕДЛ'),
    ('председателю', 'СУЩ,од,мр,ед,дт', 'С,мр,ед,дт'),
    ('правительства', 'СУЩ,неод,ср,ед,рд', 'С,ср,ед,рд'),
    ('РФ', 'СУЩ,неод,жр,sg,0,аббр,гео,ед,им', 'С,жр,ед,аббр,0'),
    ('о', 'ПР', 'ПРЕДЛ'),
    ('сокращении', 'СУЩ,неод,ср,ед,пр', 'С,ср,ед,пр'),
    ('разницы', 'СУЩ,неод,жр,ед,рд', 'С,жр,ед,рд'),
    ('с', 'ПР', 'ПРЕДЛ'),
    ('Москвой', 'СУЩ,неод,жр,sg,гео,ед,тв', 'С,жр,ед,тв'),
    ('»', 'UNKN', ''),
    #(',', 'PNCT', ''),
    ('—', 'UNKN', ''),
    ('рассказал', 'ГЛ,сов,перех,мр,ед,прош,изъяв', 'Г,дст,прш,мр,ед'),
    ('Беспалов', 'СУЩ,од,мр,sg,фам,ед,им', 'С,мр,ед,им'),
    #('.', 'PNCT', ''),
    ('Напомним', 'ГЛ,сов,перех,мн,1л,буд,изъяв', 'Г,дст,буд,1л,мн'),
    #(',', 'PNCT', ''),
    ('28', 'UNKN', ''),
    ('марта', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('2010', 'UNKN', ''),
    ('года', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('Камчатский', 'ПРИЛ,мр,ед,им', 'П,мр,ед,им,од,но'),
    ('край', 'СУЩ,неод,мр,ед,им', 'С,мр,ед,им'),
    ('и', 'СОЮЗ', 'СОЮЗ'),
    ('Чукотский', 'ПРИЛ,мр,ед,им', 'П,мр,ед,им,од,но'),
    ('автономный', 'ПРИЛ,кач,мр,ед,им', 'П,мр,ед,им,од,но'),
    ('округ', 'Н', 'Н'),
    ('перешли', 'ГЛ,сов,перех,мн,прош,изъяв', 'Г,дст,прш,мн'),
    ('на', 'ПР', 'ПРЕДЛ'),
    ('магаданское', 'ПРИЛ,ср,ед,им', 'П,ср,ед,им,од,но'),
    ('время', 'СУЩ,неод,ср,ед,им', 'С,ср,ед,им'),
    #('.', 'PNCT', ''),
    ('Таким', 'ПРИЛ,мест-п,мр,ед,тв', 'МС-П,мр,ед,тв,од,но'),
    ('образом', 'СУЩ,неод,мр,ед,тв', 'С,мр,ед,тв'),
    #(',', 'PNCT', ''),
    ('разница', 'СУЩ,неод,жр,ед,им', 'С,жр,ед,им'),
    ('во', 'ПР', 'ПРЕДЛ'),
    #('времени', 'ГЛ,несов,неперех,ед,повел,выкл', 'С,ср,ед,рд'),
    ('с', 'ПР', 'ПРЕДЛ'),
    ('Москвой', 'СУЩ,неод,жр,sg,гео,ед,тв', 'С,жр,ед,тв'),
    ('для', 'ДЕЕПР,несов,перех,наст', 'ДЕЕПРИЧАСТИЕ,дст,нст'),
    ('этих', 'ПРИЛ,мест-п,мн,рд', 'МС-П,мн,рд,од,но'),
    ('регионов', 'СУЩ,неод,мр,мн,рд', 'С,мр,мн,рд'),
    ('уменьшилась', 'ГЛ,сов,неперех,жр,ед,прош,изъяв', 'Г,дст,прш,жр,ед'),
    ('с', 'ПР', 'ПРЕДЛ'),
    ('десяти', 'ЧИСЛ,рд', 'ЧИСЛ,рд'),
    ('до', 'ПР', 'ПРЕДЛ'),
    ('восьми', 'ЧИСЛ,рд', 'ЧИСЛ,рд'),
    ('часов', 'СУЩ,неод,мр,мн,рд', 'С,мр,мн,рд'),
    #(',', 'PNCT', ''),
    ('а', 'СОЮЗ', 'СОЮЗ'),
    ('разница', 'СУЩ,неод,жр,ед,им', 'С,жр,ед,им'),
    ('с', 'ПР', 'ПРЕДЛ'),
    ('Владивостоком', 'СУЩ,неод,мр,гео,ед,тв', 'С,мр,ед,тв'),
    ('и', 'СОЮЗ', 'СОЮЗ'),
    ('Хабаровском', 'СУЩ,неод,мр,гео,ед,тв', 'С,мр,ед,тв'),
    ('—', 'UNKN', ''),
    ('с', 'ПР', 'ПРЕДЛ'),
    ('двух', 'ЧИСЛ,мр,рд', 'ЧИСЛ,мр,рд'),
    ('часов', 'СУЩ,неод,мр,мн,рд', 'С,мр,мн,рд'),
    ('до', 'ПР', 'ПРЕДЛ'),
    ('одного', 'ПРИЛ,мест-п,мр,ед,рд', 'МС-П,мр,ед,рд,од,но'),
    #('.', 'PNCT', ''),
    ('В', 'ПР', 'ПРЕДЛ'),
    ('результате', 'СУЩ,неод,мр,ед,пр', 'С,мр,ед,пр'),
    ('в', 'ПР', 'ПРЕДЛ'),
    ('Дальневосточном', 'ПРИЛ,мр,ед,пр', 'П,мр,ед,пр,од,но'),
    ('федеральном', 'ПРИЛ,мр,ед,пр', 'П,мр,ед,пр,од,но'),
    ('округе', 'СУЩ,неод,мр,ед,пр', 'С,мр,ед,пр'),
    ('осталось', 'ГЛ,сов,неперех,ср,ед,прош,изъяв', 'Г,дст,прш,ср,ед'),
    ('три', 'ГЛ,несов,перех,ед,повел,выкл', 'Г,дст,пвл,2л,ед'),
    ('часовых', 'СУЩ,од,мр,мн,рд', 'С,мр,мн,рд'),
    ('пояса', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    #('.', 'PNCT', ''),
    ('По', 'ПР', 'ПРЕДЛ'),
    ('мнению', 'СУЩ,неод,ср,ед,дт', 'С,ср,ед,дт'),
    ('полпреда', 'СУЩ,од,мр,ед,рд', 'С,мр,ед,рд'),
    ('президента', 'СУЩ,од,мр,ед,рд', 'С,мр,ед,рд'),
    ('РФ', 'СУЩ,неод,жр,sg,0,аббр,гео,ед,им', 'С,жр,ед,аббр,0'),
    ('в', 'ПР', 'ПРЕДЛ'),
    ('округе', 'СУЩ,неод,мр,ед,пр', 'С,мр,ед,пр'),
    ('Виктора', 'СУЩ,од,мр,имя,ед,рд', 'С,мр,имя,ед,рд'),
    ('Ишаева', 'СУЩ,од,мр,sg,фам,ед,рд', 'С,мр,ед,рд'),
    #(',', 'PNCT', ''),
    ('оптимальное', 'ПРИЛ,ср,ед,им', 'П,ср,ед,им,од,но'),
    ('число', 'СУЩ,неод,ср,ед,им', 'С,ср,ед,им'),
    ('часовых', 'СУЩ,од,мр,мн,рд', 'С,мр,мн,рд'),
    ('поясов', 'СУЩ,неод,мр,мн,рд', 'С,мр,мн,рд'),
    ('для', 'ДЕЕПР,несов,перех,наст', 'ДЕЕПРИЧАСТИЕ,дст,нст'),
    ('региона', 'СУЩ,неод,мр,ед,рд', 'С,мр,ед,рд'),
    ('—', 'UNKN', ''),
    ('два', 'ЧИСЛ,мр,им', 'ЧИСЛ,мр,им'),
    #('.', 'PNCT', ''),
]