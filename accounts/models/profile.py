from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
    ("male", "男性"),
    ("female", "女性"),
    ("another", "その他"),
)

PREFECTURES_CHOICES = (
    ("01", "北海道"),("02", "青森"),("03", "岩手"),("04", "宮城"),("05", "秋田"),
    ("06", "山形"),("07", "福島"),("08", "茨城"),("09", "栃木"),("10", "群馬"),
    ("11", "埼玉"),("12", "千葉"),("13", "東京"),("14", "神奈川"),("15", "新潟"),
    ("16", "富山"),("17", "石川"),("18", "福井"),("19", "山梨"),("20", "長野"),
    ("21", "岐阜"),("22", "静岡"),("23", "愛知"),("24", "三重"),("25", "滋賀"),
    ("26", "京都"),("27", "大阪"),("28", "兵庫"),("29", "奈良"),("30", "和歌山"),
    ("31", "鳥取"),("32", "島根"),("33", "岡山"),("34", "広島"),("35", "山口"),
    ("36", "徳島"),("37", "香川"),("38", "愛媛"),("39", "高知"),("40", "福岡"),
    ("41", "佐賀"),("42", "長崎"),("43", "熊本"),("44", "大分"),("45", "宮崎"),
    ("46", "鹿児島"),("47", "沖縄"),
)


INDUSTRY_CHOICES = (
    ("01", "農林水産業"),
    ("02", "鉱業"),
    ("03", "建設業"),
    ("04", "製造業"),
    ("05", "電気・ガス・熱供給・水道業"),
    ("06", "運輸業"),
    ("07", "通信業"),
    ("08", "卸売・小売業・飲食店"),
    ("09", "金融・保険業"),
    ("10", "不動産業"),
    ("11", "弁護士・税理士・医師等専門サービス業"),
    ("12", "その他サービス業"),
    ("13", "公務"),
    ("14", "主婦"),
    ("15", "学生"),
    ("16", "その他"),
)


OCCUPATIONS_CHOICES = (
    ("01", "自営者"),
    ("02", "会社・団体役員"),
    ("03", "管理職"),
    ("04", "一般事務職"),
    ("05", "専門職"),
    ("06", "教職・研究職"),
    ("07", "技能・作業職"),
    ("08", "販売職"),
    ("09", "無職"),
    ("10", "その他"),
)



class Profile(models.Model):

    gendar   = models.CharField("性別",
                                max_length=100,
                                choices=GENDER_CHOICES,
                                blank=True)
    birthday = models.DateField("生年月日",
                                max_length=100)
    industry        = models.CharField("従事している産業",
                                        max_length=100,
                                        choices=INDUSTRY_CHOICES,
                                        blank=True)
    occupation      = models.CharField("職種",
                                        max_length=100,
                                        choices=OCCUPATIONS_CHOICES,
                                        blank=True)
    prefecture     = models.CharField(max_length=100,
                                choices=PREFECTURES_CHOICES,
                                blank=True)

    user   = models.OneToOneField(User)
 
#    def __str__(self):
#        return self.name
