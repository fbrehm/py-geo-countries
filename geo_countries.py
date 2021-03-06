#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2015 by Frank Brehm, Berlin
@summary: 2-letter, 3-letter, and numerical codes for countries.
"""

# Standard modules
import warnings

__author__ = 'Frank Brehm <frank@brehm-online.com>'
__copyright__ = '(C) 2015 by Frank Brehm, Berlin'
__contact__ = 'frank@brehm-online.com'
__version__ = '0.2.0'
__license__ = 'LGPLv3+'

# Global variables

CNT_I_CODE2 = 0
CNT_I_CODE3 = 1
CNT_I_NUMCODE = 2
CNT_I_COUNTRY = 3
CNT_I_FLAG = 4

CNT_F_REGULAR = 0x01
CNT_F_OLD = 0x02
CNT_F_REGION = 0x04
CNT_F_ANY = CNT_F_REGULAR | CNT_F_OLD | CNT_F_REGION

_country = []
_two_letter = {}
_three_letter = {}
_numeric = {}


# =============================================================================
class Country(object):
    """
    Class for data of a country.
    """

    # -------------------------------------------------------------------------
    def __init__(
        self, name, two_letter=None, three_letter=None,
            numcode=None, flag=CNT_F_REGULAR):

        self._name = name.strip()
        self._two_letter = two_letter
        self._three_letter = three_letter
        self._numcode = None
        if numcode is not None:
            self._numcode = int(numcode)
        self._flag = flag

    # -------------------------------------------------------------------------
    @property
    def name(self):
        """The literal country name in English language"""
        return self._name

    # -------------------------------------------------------------------------
    @property
    def two_letter(self):
        """The 2-letter code of the country."""
        return self._two_letter

    # -------------------------------------------------------------------------
    @property
    def three_letter(self):
        """The 3-letter code of the country."""
        return self._three_letter

    # -------------------------------------------------------------------------
    @property
    def numcode(self):
        """The numeric code of the country."""
        return self._numcode

    # -------------------------------------------------------------------------
    @property
    def flag(self):
        """A flag describing the type of country."""
        return self._flag


# =============================================================================
def country(key, flags=CNT_F_ANY):

    if flag not in (CNT_F_REGULAR, CNT_F_OLD, CNT_F_REGION, CNT_F_ANY):
        raise ValueError("Invalid flags %r for a country.", flags)

    index = None

    # Pseudo-loop to find the country index
    while True:

        # key is an integer value - search in _numeric
        if isinstance(key, int):
            if key in _numeric:
                index = _numeric[key]
            break

        # key is a string with a numeric content
        try:
            int_key = int(key)
            if int_key in _numeric:
                index = _numeric[int_key]
            break
        except ValueError:
            pass

        str_key = str(key).strip().lower()

        if str_key in _two_letter:
            index = _two_letter[str_key]
            break

        if str_key in _three_letter:
            index = _three_letter[str_key]

        # At the end break the pseudo-loop
        break

    if index is None:
        return None

    c = _country[index]
    result_flag = flags & c.flag
    if not result_flag:
        return None

    return c


# =============================================================================
_cdata = (
    ('AF', 'AFG',   4, 'Afghanistan'),
    ('AL', 'ALB',   8, 'Albania'),
    ('DZ', 'DZA',  12, 'Algeria'),
    ('AS', 'ASM',  16, 'American Samoa'),
    ('AD', 'AND',  20, 'Andorra'),
    ('AO', 'AGO',  24, 'Angola'),
    ('AI', 'AIA', 660, 'Anguilla'),
    ('AQ', None, None, 'Antarctica'),
    ('AG', 'ATG',  28, 'Antigua and Barbuda'),
    (None, None,  896, 'Areas not elsewhere specified'),
    (None, None,  898, 'Areas not specified'),
    ('AR', 'ARG',  32, 'Argentina'),
    ('AM', 'ARM',  51, 'Armenia'),
    ('AW', 'ABW', 533, 'Aruba'),
    ('AU', 'AUS',  36, 'Australia'),
    ('AT', 'AUT',  40, 'Austria'),
    ('AZ', 'AZE',  31, 'Azerbaijan'),
    ('BS', 'BHS',  44, 'Bahamas'),
    ('BH', 'BHR',  48, 'Bahrain'),
    ('BD', 'BGD',  50, 'Bangladesh'),
    ('BB', 'BRB',  52, 'Barbados'),
    ('BY', 'BLR', 112, 'Belarus'),
    ('BE', 'BEL',  56, 'Belgium'),
    ('BZ', 'BLZ',  84, 'Belize'),
    ('BJ', 'BEN', 204, 'Benin'),
    ('BM', 'BMU',  60, 'Bermuda'),
    ('BT', 'BTN',  64, 'Bhutan'),
    ('BO', 'BOL',  68, 'Bolivia'),
    ('BA', 'BIH',  70, 'Bosnia and Herzegovina'),
    ('BW', 'BWA',  72, 'Botswana'),
    ('BV', None, None, 'Bouvet Island'),
    ('BR', 'BRA',  76, 'Brazil'),
    ('IO', None, None, 'British Indian Ocean Territory'),
    ('VG', 'VGB',  92, 'British Virgin Islands'),
    ('BN', 'BRN',  96, 'Brunei Darussalam'),
    ('BG', 'BGR', 100, 'Bulgaria'),
    ('BF', 'BFA', 854, 'Burkina Faso'),
    ('BI', 'BDI', 108, 'Burundi'),
    ('KH', 'KHM', 116, 'Cambodia'),
    ('CM', 'CMR', 120, 'Cameroon'),
    ('CA', 'CAN', 124, 'Canada'),
    ('CV', 'CPV', 132, 'Cape Verde'),
    ('KY', 'CYM', 136, 'Cayman Islands'),
    ('CF', 'CAF', 140, 'Central African Republic'),
    ('TD', 'TCD', 148, 'Chad'),
    (None, None,  830, 'Channel Islands'),
    ('CL', 'CHL', 152, 'Chile'),
    ('CN', 'CHN', 156, 'China'),
    ('CX', None, None, 'Christmas Island'),
    ('CC', None, None, 'Cocos (keeling) Islands'),
    ('CO', 'COL', 170, 'Colombia'),
    ('KM', 'COM', 174, 'Comoros'),
    ('CG', 'COG', 178, 'Congo'),
    ('CK', 'COK', 184, 'Cook Islands'),
    ('CR', 'CRI', 188, 'Costa Rica'),
    ('CI', 'CIV', 384, 'Côte d\'Ivoire'),
    ('HR', 'HRV', 191, 'Croatia'),
    ('CU', 'CUB', 192, 'Cuba'),
    ('CY', 'CYP', 196, 'Cyprus'),
    ('CZ', 'CZE', 203, 'Czech Republic'),
    ('KP', 'PRK', 408, 'Democratic People\'s Republic of Korea'),
    ('CD', 'COD', 180, 'Democratic Republic of the Congo'),
    ('DK', 'DNK', 208, 'Denmark'),
    ('DJ', 'DJI', 262, 'Djibouti'),
    ('DM', 'DMA', 212, 'Dominica'),
    ('DO', 'DOM', 214, 'Dominican Republic'),
    ('TP', 'TMP', 626, 'East Timor'),
    ('EC', 'ECU', 218, 'Ecuador'),
    ('EG', 'EGY', 818, 'Egypt'),
    ('SV', 'SLV', 222, 'El Salvador'),
    ('GQ', 'GNQ', 226, 'Equatorial Guinea'),
    ('ER', 'ERI', 232, 'Eritrea'),
    ('EE', 'EST', 233, 'Estonia'),
    ('ET', 'ETH', 231, 'Ethiopia'),
    ('FO', 'FRO', 234, 'Faeroe Islands'),
    ('FK', 'FLK', 238, 'Falkland Islands (Malvinas)'),
    ('FM', 'FSM', 583, 'Micronesia, Federated States of'),
    ('FJ', 'FJI', 242, 'Fiji'),
    ('FI', 'FIN', 246, 'Finland'),
    ('MK', 'MKD', 807, 'The former Yugoslav Republic of Macedonia'),
    ('FR', 'FRA', 250, 'France'),
    ('GF', 'GUF', 254, 'French Guiana'),
    ('PF', 'PYF', 258, 'French Polynesia'),
    ('TF', None, None, 'French Southern Territories'),
    ('GA', 'GAB', 266, 'Gabon'),
    ('GM', 'GMB', 270, 'Gambia'),
    ('GE', 'GEO', 268, 'Georgia'),
    ('DE', 'DEU', 276, 'Germany'),
    ('GH', 'GHA', 288, 'Ghana'),
    ('GI', 'GIB', 292, 'Gibraltar'),
    ('GR', 'GRC', 300, 'Greece'),
    ('GL', 'GRL', 304, 'Greenland'),
    ('GD', 'GRD', 308, 'Grenada'),
    ('GP', 'GLP', 312, 'Guadeloupe'),
    ('GU', 'GUM', 316, 'Guam'),
    ('GT', 'GTM', 320, 'Guatemala'),
    ('GN', 'GIN', 324, 'Guinea'),
    ('GW', 'GNB', 624, 'Guinea-Bissau'),
    ('GY', 'GUY', 328, 'Guyana'),
    ('HT', 'HTI', 332, 'Haiti'),
    ('HM', None, None, 'Heard Island And Mcdonald Islands'),
    ('VA', 'VAT', 336, 'Holy See'),
    ('HN', 'HND', 340, 'Honduras'),
    ('HK', 'HKG', 344, 'Hong Kong Special Administrative Region of China'),
    ('HU', 'HUN', 348, 'Hungary'),
    ('IS', 'ISL', 352, 'Iceland'),
    ('IN', 'IND', 356, 'India'),
    ('ID', 'IDN', 360, 'Indonesia'),
    ('IR', 'IRN', 364, 'Iran (Islamic Republic of)'),
    ('IQ', 'IRQ', 368, 'Iraq'),
    ('IE', 'IRL', 372, 'Ireland'),
    (None, 'IMY', 833, 'Isle of Man'),
    ('IL', 'ISR', 376, 'Israel'),
    ('IT', 'ITA', 380, 'Italy'),
    ('JM', 'JAM', 388, 'Jamaica'),
    ('JP', 'JPN', 392, 'Japan'),
    ('JO', 'JOR', 400, 'Jordan'),
    ('KZ', 'KAZ', 398, 'Kazakhstan'),
    ('KE', 'KEN', 404, 'Kenya'),
    ('KI', 'KIR', 296, 'Kiribati'),
    ('KW', 'KWT', 414, 'Kuwait'),
    ('KG', 'KGZ', 417, 'Kyrgyzstan'),
    ('LA', 'LAO', 418, 'Lao People\'s Democratic Republic'),
    ('LV', 'LVA', 428, 'Latvia'),
    ('LB', 'LBN', 422, 'Lebanon'),
    ('LS', 'LSO', 426, 'Lesotho'),
    ('LR', 'LBR', 430, 'Liberia'),
    ('LY', 'LBY', 434, 'Libyan Arab Jamahiriya'),
    ('LI', 'LIE', 438, 'Liechtenstein'),
    ('LT', 'LTU', 440, 'Lithuania'),
    ('LU', 'LUX', 442, 'Luxembourg'),
    ('MO', 'MAC', 446, 'Macau'),
    ('MG', 'MDG', 450, 'Madagascar'),
    ('MW', 'MWI', 454, 'Malawi'),
    ('MY', 'MYS', 458, 'Malaysia'),
    ('MV', 'MDV', 462, 'Maldives'),
    ('ML', 'MLI', 466, 'Mali'),
    ('MT', 'MLT', 470, 'Malta'),
    ('MH', 'MHL', 584, 'Marshall Islands'),
    ('MQ', 'MTQ', 474, 'Martinique'),
    ('MR', 'MRT', 478, 'Mauritania'),
    ('MU', 'MUS', 480, 'Mauritius'),
    ('YT', None, None, 'Mayotte'),
    ('MX', 'MEX', 484, 'Mexico'),
    ('MC', 'MCO', 492, 'Monaco'),
    ('MN', 'MNG', 496, 'Mongolia'),
    ('MS', 'MSR', 500, 'Montserrat'),
    ('MA', 'MAR', 504, 'Morocco'),
    ('MZ', 'MOZ', 508, 'Mozambique'),
    ('MM', 'MMR', 104, 'Myanmar'),
    ('NA', 'NAM', 516, 'Namibia'),
    ('NR', 'NRU', 520, 'Nauru'),
    ('NP', 'NPL', 524, 'Nepal'),
    ('NL', 'NLD', 528, 'Netherlands'),
    ('AN', 'ANT', 530, 'Netherlands Antilles'),
    ('NC', 'NCL', 540, 'New Caledonia'),
    ('NZ', 'NZL', 554, 'New Zealand'),
    ('NI', 'NIC', 558, 'Nicaragua'),
    ('NE', 'NER', 562, 'Niger'),
    ('NG', 'NGA', 566, 'Nigeria'),
    ('NU', 'NIU', 570, 'Niue'),
    ('NF', 'NFK', 574, 'Norfolk Island'),
    ('MP', 'MNP', 580, 'Northern Mariana Islands'),
    ('NO', 'NOR', 578, 'Norway'),
    (None, 'PSE', 275, 'Occupied Palestinian Territory'),
    ('OM', 'OMN', 512, 'Oman'),
    ('PK', 'PAK', 586, 'Pakistan'),
    ('PW', 'PLW', 585, 'Palau'),
    ('PA', 'PAN', 591, 'Panama'),
    ('PG', 'PNG', 598, 'Papua New Guinea'),
    ('PY', 'PRY', 600, 'Paraguay'),
    ('PE', 'PER', 604, 'Peru'),
    ('PH', 'PHL', 608, 'Philippines'),
    ('PN', 'PCN', 612, 'Pitcairn'),
    ('PL', 'POL', 616, 'Poland'),
    ('PT', 'PRT', 620, 'Portugal'),
    ('PR', 'PRI', 630, 'Puerto Rico'),
    ('QA', 'QAT', 634, 'Qatar'),
    ('KR', 'KOR', 410, 'Republic of Korea'),
    ('MD', 'MDA', 498, 'Republic of Moldova'),
    ('RO', 'ROM', 642, 'Romania'),
    ('RE', 'REU', 638, 'Réunion'),
    ('RU', 'RUS', 643, 'Russian Federation'),
    ('RW', 'RWA', 646, 'Rwanda'),
    ('SH', 'SHN', 654, 'Saint Helena'),
    ('KN', 'KNA', 659, 'Saint Kitts and Nevis'),
    ('LC', 'LCA', 662, 'Saint Lucia'),
    ('PM', 'SPM', 666, 'Saint Pierre and Miquelon'),
    ('VC', 'VCT', 670, 'Saint Vincent and the Grenadines'),
    ('WS', 'WSM', 882, 'Samoa'),
    ('SM', 'SMR', 674, 'San Marino'),
    ('ST', 'STP', 678, 'Sao Tome and Principe'),
    ('SA', 'SAU', 682, 'Saudi Arabia'),
    ('SN', 'SEN', 686, 'Senegal'),
    ('SC', 'SYC', 690, 'Seychelles'),
    ('SL', 'SLE', 694, 'Sierra Leone'),
    ('SG', 'SGP', 702, 'Singapore'),
    ('SK', 'SVK', 703, 'Slovakia'),
    ('SI', 'SVN', 705, 'Slovenia'),
    ('SB', 'SLB',  90, 'Solomon Islands'),
    ('SO', 'SOM', 706, 'Somalia'),
    ('ZA', 'ZAF', 710, 'South Africa'),
    ('GS', None, None, 'South Georgia And The South Sandwich Islands'),
    ('ES', 'ESP', 724, 'Spain'),
    ('LK', 'LKA', 144, 'Sri Lanka'),
    ('SD', 'SDN', 736, 'Sudan'),
    ('SR', 'SUR', 740, 'Suriname'),
    ('SJ', 'SJM', 744, 'Svalbard and Jan Mayen Islands'),
    ('SZ', 'SWZ', 748, 'Swaziland'),
    ('SE', 'SWE', 752, 'Sweden'),
    ('CH', 'CHE', 756, 'Switzerland'),
    ('SY', 'SYR', 760, 'Syrian Arab Republic'),
    ('TW', 'TWN', 158, 'Taiwan Province of China'),
    ('TJ', 'TJK', 762, 'Tajikistan'),
    ('TH', 'THA', 764, 'Thailand'),
    ('TG', 'TGO', 768, 'Togo'),
    ('TK', 'TKL', 772, 'Tokelau'),
    ('TO', 'TON', 776, 'Tonga'),
    ('TT', 'TTO', 780, 'Trinidad and Tobago'),
    ('TN', 'TUN', 788, 'Tunisia'),
    ('TR', 'TUR', 792, 'Turkey'),
    ('TM', 'TKM', 795, 'Turkmenistan'),
    ('TC', 'TCA', 796, 'Turks and Caicos Islands'),
    ('TV', 'TUV', 798, 'Tuvalu'),
    ('UG', 'UGA', 800, 'Uganda'),
    ('UA', 'UKR', 804, 'Ukraine'),
    ('AE', 'ARE', 784, 'United Arab Emirates'),
    ('GB', 'GBR', 826, 'United Kingdom'),
    ('TZ', 'TZA', 834, 'United Republic of Tanzania'),
    ('US', 'USA', 840, 'United States'),
    ('UM', None, None, 'United States Minor Outlying Islands'),
    ('VI', 'VIR', 850, 'United States Virgin Islands'),
    ('UY', 'URY', 858, 'Uruguay'),
    ('UZ', 'UZB', 860, 'Uzbekistan'),
    ('VU', 'VUT', 548, 'Vanuatu'),
    ('VE', 'VEN', 862, 'Venezuela'),
    ('VN', 'VNM', 704, 'Viet Nam'),
    ('WF', 'WLF', 876, 'Wallis and Futuna Islands'),
    ('EH', 'ESH', 732, 'Western Sahara'),
    ('YE', 'YEM', 887, 'Yemen'),
    ('YU', 'YUG', 891, 'Yugoslavia'),
    ('ZM', 'ZMB', 894, 'Zambia'),
    ('ZW', 'ZWE', 716, 'Zimbabwe'),
    (None, None,  810, 'Union of Soviet Socialist Republics',      CNT_F_OLD),
    (None, None,  532, 'Netherlands Antilles',                     CNT_F_OLD),
    (None, None,  890, 'Socialist Federal Republic of Yugoslavia', CNT_F_OLD),
    (None, None,  200, 'Czechoslovakia',                           CNT_F_OLD),
    (None, None,  278, 'German Democratic Republic',               CNT_F_OLD),
    (None, None,  280, 'Federal Republic of Germany',              CNT_F_OLD),
    (None, None,  582, 'Pacific Islands (Trust Territory)',        CNT_F_OLD),
    (None, None,  720, 'Democratic Yemen',                         CNT_F_OLD),
    (None, None,  886, 'Yemen',                                    CNT_F_OLD),
    (None, None,  230, 'Ethiopia',                                 CNT_F_OLD),
    (None, None,  104, 'Burma',                                    CNT_F_OLD),
    (None, None,  116, 'Democratic Kampuchea',                     CNT_F_OLD),
    (None, None,  180, 'Zaire',                                    CNT_F_OLD),
    (None, None,  384, 'Ivory Coast',                              CNT_F_OLD),
    (None, None,  854, 'Upper Volta',                              CNT_F_OLD),
    (None, None,    2, 'Africa',                          CNT_F_REGION),
    (None, None,   14, 'Eastern Africa',                  CNT_F_REGION),
    (None, None,   17, 'Middle Africa',                   CNT_F_REGION),
    (None, None,   15, 'Northern Africa',                 CNT_F_REGION),
    (None, None,   18, 'Southern Africa',                 CNT_F_REGION),
    (None, None,   11, 'Western Africa',                  CNT_F_REGION),
    (None, None,   19, 'Americas',                        CNT_F_REGION),
    (None, None,  419, 'Latin America and the Caribbean', CNT_F_REGION),
    (None, None,   29, 'Caribbean',                       CNT_F_REGION),
    (None, None,   13, 'Central America',                 CNT_F_REGION),
    (None, None,    5, 'South America',                   CNT_F_REGION),
    (None, None,   21, 'Northern America',                CNT_F_REGION),
    (None, None,  142, 'Asia',                            CNT_F_REGION),
    (None, None,   30, 'Eastern Asia',                    CNT_F_REGION),
    (None, None,   62, 'South-central Asia',              CNT_F_REGION),
    (None, None,   35, 'South-eastern Asia',              CNT_F_REGION),
    (None, None,  145, 'Western Asia',                    CNT_F_REGION),
    (None, None,  150, 'Europe',                          CNT_F_REGION),
    (None, None,  151, 'Eastern Europe',                  CNT_F_REGION),
    (None, None,  154, 'Northern Europe',                 CNT_F_REGION),
    (None, None,   39, 'Southern Europe',                 CNT_F_REGION),
    (None, None,  155, 'Western Europe',                  CNT_F_REGION),
    (None, None,    9, 'Oceania',                         CNT_F_REGION),
    (None, None,   53, 'Australia and New Zealand',       CNT_F_REGION),
    (None, None,   54, 'Melanesia',                       CNT_F_REGION),
    (None, None,   55, 'Micronesia-Polynesia',            CNT_F_REGION),
    (None, None,   57, 'Micronesia',                      CNT_F_REGION),
    (None, None,   61, 'Polynesia',                       CNT_F_REGION),
)

for data in _cdata:
    flag = CNT_F_REGULAR
    if len(data) > 4:
        flag = data[4]
    c = Country(data[3], data[0], data[1], data[2], flag)
    _country.append(c)
    index = len(_country) - 1

    if c.two_letter:
        key = c.two_letter.lower()
        if key in _two_letter:
            warnings.warn((
                "Two letter code %r already exists." % (key)), RuntimeWarning)
        else:
            _two_letter[key] = index

    if c.three_letter:
        key = c.three_letter.lower()
        if key in _three_letter:
            warnings.warn((
                "Three letter code %r already exists." % (key)), RuntimeWarning)
        else:
            _three_letter[key] = index

    if c.numcode is not None:
        if c.numcode in _numeric:
            warnings.warn((
                "Numeric code %r already exists." % (c.numcode)), RuntimeWarning)
        else:
            _numeric[c.numcode] = index


# =============================================================================

if __name__ == "__main__":

    pass

# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
