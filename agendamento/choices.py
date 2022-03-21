import datetime

HORA_CHOICES = (
        (datetime.time(13, 00, 00), "13h:00m ~ 13h:12m"),
        (datetime.time(13, 12, 00), "13h:12m ~ 13h:24m"),
        (datetime.time(13, 24, 00), "13h:24m ~ 13h:36m"),
        (datetime.time(13, 36, 00), "13h:36m ~ 13h:48m"),
        (datetime.time(13, 48, 00), "13h:48m ~ 14h:00m"),
        (datetime.time(14, 00, 00), "14h:00m ~ 14h:12m"),
        (datetime.time(14, 12, 00), "14h:12m ~ 14h:24m"),
        (datetime.time(14, 24, 00), "14h:24m ~ 14h:36m"),
        (datetime.time(14, 36, 00), "14h:36m ~ 14h:48m"),
        (datetime.time(14, 48, 00), "14h:48m ~ 15h:00m"),
        (datetime.time(15, 00, 00), "15h:00m ~ 15h:12m"),
        (datetime.time(15, 12, 00), "15h:12m ~ 15h:24m"),
        (datetime.time(15, 24, 00), "15h:24m ~ 15h:36m"),
        (datetime.time(15, 36, 00), "15h:36m ~ 15h:48m"),
        (datetime.time(15, 48, 00), "15h:48m ~ 16h:00m"),
        (datetime.time(16, 00, 00), "16h:00m ~ 16h:12m"),
        (datetime.time(16, 12, 00), "16h:12m ~ 16h:24m"),
        (datetime.time(16, 24, 00), "16h:24m ~ 16h:36m"),
        (datetime.time(16, 36, 00), "16h:36m ~ 16h:48m"),
        (datetime.time(16, 48, 00), "16h:48m ~ 17h:00m"),
    )