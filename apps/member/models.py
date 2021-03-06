# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..association.models import *

from django.contrib.auth.models import User

class Country(models.Model):
	AD = 'Andorra'
	AE = 'United Arab Emirates'
	AF = 'Afghanistan'
	AG = 'Antigua & Barbuda'
	AI = 'Anguilla'
	AL = 'Albania'
	AM = 'Armenia'
	AN = 'Netherlands Antilles'
	AO = 'Angola'
	AQ = 'Antarctica'
	AR = 'Argentina'
	AS = 'American Samoa'
	AT = 'Austria'
	AU = 'Australia'
	AW = 'Aruba'
	AZ = 'Azerbaijan'
	BA = 'Bosnia and Herzegovina'
	BB = 'Barbados'
	BD = 'Bangladesh'
	BE = 'Belgium'
	BF = 'Burkina Faso'
	BG = 'Bulgaria'
	BH = 'Bahrain'
	BI = 'Burundi'
	BJ = 'Benin'
	BM = 'Bermuda'
	BN = 'Brunei Darussalam'
	BO = 'Bolivia'
	BR = 'Brazil'
	BS = 'Bahama'
	BT = 'Bhutan'
	BV = 'Bouvet Island'
	BW = 'Botswana'
	BY = 'Belarus'
	BZ = 'Belize'
	CA = 'Canada'
	CC = 'Cocos (Keeling) Islands'
	CF = 'Central African Republic'
	CG = 'Congo'
	CH = 'Switzerland'
	CI = 'Ivory Coast'
	CK = 'Cook Iislands'
	CL = 'Chile'
	CM = 'Cameroon'
	CN = 'China'
	CO = 'Colombia'
	CR = 'Costa Rica'
	CU = 'Cuba'
	CV = 'Cape Verde'
	CX = 'Christmas Island'
	CY = 'Cyprus'
	CZ = 'Czech Republic'
	DE = 'Germany'
	DJ = 'Djibouti'
	DK = 'Denmark'
	DM = 'Dominica'
	DO = 'Dominican Republic'
	DR = 'Democratic Republic of Congo'
	DZ = 'Algeria'
	EC = 'Ecuador'
	EE = 'Estonia'
	EG = 'Egypt'
	EH = 'Western Sahara'
	ER = 'Eritrea'
	ES = 'Spain'
	ET = 'Ethiopia'
	FI = 'Finland'
	FJ = 'Fiji'
	FK = 'Falkland Islands (Malvinas)'
	FM = 'Micronesia'
	FO = 'Faroe Islands'
	FR = 'France'
	FX = 'France, Metropolitan'
	GA = 'Gabon'
	GB = 'United Kingdom (Great Britain)'
	GD = 'Grenada'
	GE = 'Georgia'
	GF = 'French Guiana'
	GH = 'Ghana'
	GI = 'Gibraltar'
	GL = 'Greenland'
	GM = 'Gambia'
	GN = 'Guinea'
	GP = 'Guadeloupe'
	GQ = 'Equatorial Guinea'
	GR = 'Greece'
	GS = 'South Georgia and the South Sandwich Islands'
	GT = 'Guatemala'
	GU = 'Guam'
	GW = 'Guinea-Bissau'
	GY = 'Guyana'
	HK = 'Hong Kong'
	HM = 'Heard & McDonald Islands'
	HN = 'Honduras'
	HR = 'Croatia'
	HT = 'Haiti'
	HU = 'Hungary'
	ID = 'Indonesia'
	IE = 'Ireland'
	IL = 'Israel'
	IN = 'India'
	IO = 'British Indian Ocean Territory'
	IQ = 'Iraq'
	IR = 'Islamic Republic of Iran'
	IS = 'Iceland'
	IT = 'Italy'
	JM = 'Jamaica'
	JO = 'Jordan'
	JP = 'Japan'
	KE = 'Kenya'
	KG = 'Kyrgyzstan'
	KH = 'Cambodia'
	KI = 'Kiribati'
	KM = 'Comoros'
	KN = 'St. Kitts and Nevis'
	KP = 'Korea, Democratic People Republic of'
	KR = 'Korea, Republic of'
	KW = 'Kuwait'
	KY = 'Cayman Islands'
	KZ = 'Kazakhstan'
	LA = 'Lao People Democratic Republic'
	LB = 'Lebanon'
	LC = 'Saint Lucia'
	LI = 'Liechtenstein'
	LK = 'Sri Lanka'
	LR = 'Liberia'
	LS = 'Lesotho'
	LT = 'Lithuania'
	LU = 'Luxembourg'
	LV = 'Latvia'
	LY = 'Libyan Arab Jamahiriya'
	MA = 'Morocco'
	MC = 'Monaco'
	MD = 'Moldova, Republic of'
	MG = 'Madagascar'
	MH = 'Marshall Islands'
	ML = 'Mali'
	MN = 'Mongolia'
	MM = 'Myanmar'
	MO = 'Macau'
	MP = 'Northern Mariana Islands'
	MQ = 'Martinique'
	MR = 'Mauritania'
	MS = 'Monserrat'
	MT = 'Malta'
	MU = 'Mauritius'
	MV = 'Maldives'
	MW = 'Malawi'
	MX = 'Mexico'
	MY = 'Malaysia'
	MZ = 'Mozambique'
	NA = 'Namibia'
	NC = 'New Caledonia'
	NE = 'Niger'
	NF = 'Norfolk Island'
	NG = 'Nigeria'
	NI = 'Nicaragua'
	NL = 'Netherlands'
	NO = 'Norway'
	NP = 'Nepal'
	NR = 'Nauru'
	NU = 'Niue'
	NZ = 'New Zealand'
	OM = 'Oman'
	PA = 'Panama'
	PE = 'Peru'
	PF = 'French Polynesia'
	PG = 'Papua New Guinea'
	PH = 'Philippines'
	PK = 'Pakistan'
	PL = 'Poland'
	PM = 'St. Pierre & Miquelon'
	PN = 'Pitcairn'
	PR = 'Puerto Rico'
	PT = 'Portugal'
	PW = 'Palau'
	PY = 'Paraguay'
	QA = 'Qatar'
	RE = 'Reunion'
	RO = 'Romania'
	RU = 'Russian Federation'
	RW = 'Rwanda'
	SA = 'Saudi Arabia'
	SB = 'Solomon Islands'
	SC = 'Seychelles'
	SD = 'Sudan'
	SE = 'Sweden'
	SG = 'Singapore'
	SH = 'St. Helena'
	SI = 'Slovenia'
	SJ = 'Svalbard & Jan Mayen Islands'
	SK = 'Slovakia'
	SL = 'Sierra Leone'
	SM = 'San Marino'
	SN = 'Senegal'
	SO = 'Somalia'
	SR = 'Suriname'
	ST = 'Sao Tome & Principe'
	SV = 'El Salvador'
	SY = 'Syrian Arab Republic'
	SZ = 'Swaziland'
	TC = 'Turks & Caicos Islands'
	TD = 'Chad'
	TF = 'French Southern Territories'
	TG = 'Togo'
	TH = 'Thailand'
	TJ = 'Tajikistan'
	TK = 'Tokelau'
	TM = 'Turkmenistan'
	TN = 'Tunisia'
	TO = 'Tonga'
	TP = 'East Timor'
	TR = 'Turkey'
	TT = 'Trinidad & Tobago'
	TV = 'Tuvalu'
	TW = 'Taiwan, Province of China'
	TZ = 'Tanzania, United Republic of'
	UA = 'Ukraine'
	UG = 'Uganda'
	UM = 'United States Minor Outlying Islands'
	US = 'United States of America'
	UY = 'Uruguay'
	UZ = 'Uzbekistan'
	VA = 'Vatican City State (Holy See)'
	VC = 'St. Vincent & the Grenadines'
	VE = 'Venezuela'
	VG = 'British Virgin Islands'
	VI = 'United States Virgin Islands'
	VN = 'Viet Nam'
	VU = 'Vanuatu'
	WF = 'Wallis & Futuna Islands'
	WS = 'Samoa'
	YE = 'Yemen'
	YT = 'Mayotte'
	YU = 'Yugoslavia'
	ZA = 'South Africa'
	ZM = 'Zambia'
	ZW = 'Zimbabwe'
	country_choices = (
		(AD, 'Andorra'),
		(AE, 'United Arab Emirates'),
		(AF, 'Afghanistan'),
		(AG, 'Antigua & Barbuda'),
		(AI, 'Anguilla'),
		(AL, 'Albania'),
		(AM, 'Armenia'),
		(AN, 'Netherlands Antilles'),
		(AO, 'Angola'),
		(AQ, 'Antarctica'),
		(AR, 'Argentina'),
		(AS, 'American Samoa'),
		(AT, 'Austria'),
		(AU, 'Australia'),
		(AW, 'Aruba'),
		(AZ, 'Azerbaijan'),
		(BA, 'Bosnia and Herzegovina'),
		(BB, 'Barbados'),
		(BD, 'Bangladesh'),
		(BE, 'Belgium'),
		(BF, 'Burkina Faso'),
		(BG, 'Bulgaria'),
		(BH, 'Bahrain'),
		(BI, 'Burundi'),
		(BJ, 'Benin'),
		(BM, 'Bermuda'),
		(BN, 'Brunei Darussalam'),
		(BO, 'Bolivia'),
		(BR, 'Brazil'),
		(BS, 'Bahama'),
		(BT, 'Bhutan'),
		(BV, 'Bouvet Island'),
		(BW, 'Botswana'),
		(BY, 'Belarus'),
		(BZ, 'Belize'),
		(CA, 'Canada'),
		(CC, 'Cocos (Keeling) Islands'),
		(CF, 'Central African Republic'),
		(CG, 'Congo'),
		(CH, 'Switzerland'),
		(CI, 'Ivory Coast'),
		(CK, 'Cook Iislands'),
		(CL, 'Chile'),
		(CM, 'Cameroon'),
		(CN, 'China'),
		(CO, 'Colombia'),
		(CR, 'Costa Rica'),
		(CU, 'Cuba'),
		(CV, 'Cape Verde'),
		(CX, 'Christmas Island'),
		(CY, 'Cyprus'),
		(CZ, 'Czech Republic'),
		(DE, 'Germany'),
		(DJ, 'Djibouti'),
		(DK, 'Denmark'),
		(DM, 'Dominica'),
		(DO, 'Dominican Republic'),
		(DR, 'Democratic Republic of Congo'),
		(DZ, 'Algeria'),
		(EC, 'Ecuador'),
		(EE, 'Estonia'),
		(EG, 'Egypt'),
		(EH, 'Western Sahara'),
		(ER, 'Eritrea'),
		(ES, 'Spain'),
		(ET, 'Ethiopia'),
		(FI, 'Finland'),
		(FJ, 'Fiji'),
		(FK, 'Falkland Islands (Malvinas)'),
		(FM, 'Micronesia'),
		(FO, 'Faroe Islands'),
		(FR, 'France'),
		(FX, 'France, Metropolitan'),
		(GA, 'Gabon'),
		(GB, 'United Kingdom (Great Britain)'),
		(GD, 'Grenada'),
		(GE, 'Georgia'),
		(GF, 'French Guiana'),
		(GH, 'Ghana'),
		(GI, 'Gibraltar'),
		(GL, 'Greenland'),
		(GM, 'Gambia'),
		(GN, 'Guinea'),
		(GP, 'Guadeloupe'),
		(GQ, 'Equatorial Guinea'),
		(GR, 'Greece'),
		(GS, 'South Georgia and the South Sandwich Islands'),
		(GT, 'Guatemala'),
		(GU, 'Guam'),
		(GW, 'Guinea-Bissau'),
		(GY, 'Guyana'),
		(HK, 'Hong Kong'),
		(HM, 'Heard & McDonald Islands'),
		(HN, 'Honduras'),
		(HR, 'Croatia'),
		(HT, 'Haiti'),
		(HU, 'Hungary'),
		(ID, 'Indonesia'),
		(IE, 'Ireland'),
		(IL, 'Israel'),
		(IN, 'India'),
		(IO, 'British Indian Ocean Territory'),
		(IQ, 'Iraq'),
		(IR, 'Islamic Republic of Iran'),
		(IS, 'Iceland'),
		(IT, 'Italy'),
		(JM, 'Jamaica'),
		(JO, 'Jordan'),
		(JP, 'Japan'),
		(KE, 'Kenya'),
		(KG, 'Kyrgyzstan'),
		(KH, 'Cambodia'),
		(KI, 'Kiribati'),
		(KM, 'Comoros'),
		(KN, 'St. Kitts and Nevis'),
		(KP, 'Korea, Democratic People Republic of'),
		(KR, 'Korea, Republic of'),
		(KW, 'Kuwait'),
		(KY, 'Cayman Islands'),
		(KZ, 'Kazakhstan'),
		(LA, 'Lao People Democratic Republic'),
		(LB, 'Lebanon'),
		(LC, 'Saint Lucia'),
		(LI, 'Liechtenstein'),
		(LK, 'Sri Lanka'),
		(LR, 'Liberia'),
		(LS, 'Lesotho'),
		(LT, 'Lithuania'),
		(LU, 'Luxembourg'),
		(LV, 'Latvia'),
		(LY, 'Libyan Arab Jamahiriya'),
		(MA, 'Morocco'),
		(MC, 'Monaco'),
		(MD, 'Moldova, Republic of'),
		(MG, 'Madagascar'),
		(MH, 'Marshall Islands'),
		(ML, 'Mali'),
		(MN, 'Mongolia'),
		(MM, 'Myanmar'),
		(MO, 'Macau'),
		(MP, 'Northern Mariana Islands'),
		(MQ, 'Martinique'),
		(MR, 'Mauritania'),
		(MS, 'Monserrat'),
		(MT, 'Malta'),
		(MU, 'Mauritius'),
		(MV, 'Maldives'),
		(MW, 'Malawi'),
		(MX, 'Mexico'),
		(MY, 'Malaysia'),
		(MZ, 'Mozambique'),
		(NA, 'Namibia'),
		(NC, 'New Caledonia'),
		(NE, 'Niger'),
		(NF, 'Norfolk Island'),
		(NG, 'Nigeria'),
		(NI, 'Nicaragua'),
		(NL, 'Netherlands'),
		(NO, 'Norway'),
		(NP, 'Nepal'),
		(NR, 'Nauru'),
		(NU, 'Niue'),
		(NZ, 'New Zealand'),
		(OM, 'Oman'),
		(PA, 'Panama'),
		(PE, 'Peru'),
		(PF, 'French Polynesia'),
		(PG, 'Papua New Guinea'),
		(PH, 'Philippines'),
		(PK, 'Pakistan'),
		(PL, 'Poland'),
		(PM, 'St. Pierre & Miquelon'),
		(PN, 'Pitcairn'),
		(PR, 'Puerto Rico'),
		(PT, 'Portugal'),
		(PW, 'Palau'),
		(PY, 'Paraguay'),
		(QA, 'Qatar'),
		(RE, 'Reunion'),
		(RO, 'Romania'),
		(RU, 'Russian Federation'),
		(RW, 'Rwanda'),
		(SA, 'Saudi Arabia'),
		(SB, 'Solomon Islands'),
		(SC, 'Seychelles'),
		(SD, 'Sudan'),
		(SE, 'Sweden'),
		(SG, 'Singapore'),
		(SH, 'St. Helena'),
		(SI, 'Slovenia'),
		(SJ, 'Svalbard & Jan Mayen Islands'),
		(SK, 'Slovakia'),
		(SL, 'Sierra Leone'),
		(SM, 'San Marino'),
		(SN, 'Senegal'),
		(SO, 'Somalia'),
		(SR, 'Suriname'),
		(ST, 'Sao Tome & Principe'),
		(SV, 'El Salvador'),
		(SY, 'Syrian Arab Republic'),
		(SZ, 'Swaziland'),
		(TC, 'Turks & Caicos Islands'),
		(TD, 'Chad'),
		(TF, 'French Southern Territories'),
		(TG, 'Togo'),
		(TH, 'Thailand'),
		(TJ, 'Tajikistan'),
		(TK, 'Tokelau'),
		(TM, 'Turkmenistan'),
		(TN, 'Tunisia'),
		(TO, 'Tonga'),
		(TP, 'East Timor'),
		(TR, 'Turkey'),
		(TT, 'Trinidad & Tobago'),
		(TV, 'Tuvalu'),
		(TW, 'Taiwan, Province of China'),
		(TZ, 'Tanzania, United Republic of'),
		(UA, 'Ukraine'),
		(UG, 'Uganda'),
		(UM, 'United States Minor Outlying Islands'),
		(US, 'United States of America'),
		(UY, 'Uruguay'),
		(UZ, 'Uzbekistan'),
		(VA, 'Vatican City State (Holy See)'),
		(VC, 'St. Vincent & the Grenadines'),
		(VE, 'Venezuela'),
		(VG, 'British Virgin Islands'),
		(VI, 'United States Virgin Islands'),
		(VN, 'Viet Nam'),
		(VU, 'Vanuatu'),
		(WF, 'Wallis & Futuna Islands'),
		(WS, 'Samoa'),
		(YE, 'Yemen'),
		(YT, 'Mayotte'),
		(YU, 'Yugoslavia'),
		(ZA, 'South Africa'),
		(ZM, 'Zambia'),
		(ZW, 'Zimbabwe'),
		)
	country = models.CharField(max_length=100, choices=country_choices, default=IN)
	def __str__(self):
		return self.country

class State(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=100)
	state = models.ForeignKey(State, default='', null=True)
	def __str__(self):
		return self.name

class Education(models.Model):
	university = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	course = models.CharField(max_length=100)
	starting_year = models.DateField(auto_now=True)
	finishing_year = models.DateField(auto_now=True)
	univ_country = models.ForeignKey(Country, related_name='univ_country')
	univ_state = models.ForeignKey(State, related_name='univ_state')
	univ_city = models.ForeignKey(City, related_name='univ_city')
	def __str__(self):
		return self.university
class Profile(models.Model):
	user = models.OneToOneField(User)
	dob = models.DateField(auto_now=False, auto_now_add=False)
	f = 'female'
	m = 'male'
	gender_choices = (
		(f,'Female'),
		(m,'Male'),
		)
	gender = models.CharField(max_length=6, choices=gender_choices, default=f)
	nationality = models.ForeignKey(Country, related_name='nationality')
	current_country = models.ForeignKey(Country, related_name='curent_country')
	user_state = models.ForeignKey(State, related_name='user_state')
	user_city =  models.ForeignKey(City, related_name='user_city')
	address = models.TextField(max_length=255)
	education = models.ForeignKey(Education, related_name='education')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	association = models.ForeignKey('association.Association', on_delete=models.CASCADE, null=True, blank=True)
	email_confirmed = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username
